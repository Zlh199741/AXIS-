#!/usr/bin/env python3
"""
原著台词忠实度校验器（novel-dialogue-fidelity-checker.py）单元测试

覆盖纯函数：
- normalize_quotes / normalize_text：引号与标点归一化
- similarity：相似度（含「逐字子串视为 exact」规则）
- get_threshold：按台词长度动态阈值
- extract_novel_dialogues / extract_script_dialogues：原著与剧本台词提取
- _is_whitelisted / match_all：比对状态机（exact / original / not_found）
- gather_all_novel_dialogues：--all-chapters 跨章节聚合（含文件系统）

设计原则：用模块自身常量构造输入，避免硬编码导致脆裂。
"""

import unittest
import importlib.util
import tempfile
from pathlib import Path

# 文件名含连字符，按项目约定用 importlib 从路径加载
_project_root = Path(__file__).parent.parent.parent
_spec = importlib.util.spec_from_file_location(
    "novel_dialogue_fidelity_checker",
    _project_root / "tools" / "validators" / "novel-dialogue-fidelity-checker.py",
)
ndf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ndf)


class TestNormalizeQuotes(unittest.TestCase):
    def test_curly_double_quotes(self):
        self.assertEqual(ndf.normalize_quotes("\u201c\u4f60\u597d\u201d"), '"\u4f60\u597d"')

    def test_corner_brackets(self):
        self.assertEqual(ndf.normalize_quotes("\u300c\u4f60\u597d\u300d"), '"\u4f60\u597d"')

    def test_plain_text_unchanged(self):
        self.assertEqual(ndf.normalize_quotes("\u666e\u901a\u6587\u672c"), "\u666e\u901a\u6587\u672c")


class TestNormalizeText(unittest.TestCase):
    def test_strip_punctuation_and_space(self):
        self.assertEqual(ndf.normalize_text("\u4f60\u597d\uff0c\u4e16\u754c\uff01"), "\u4f60\u597d\u4e16\u754c")

    def test_strip_quotes_and_brackets(self):
        self.assertEqual(ndf.normalize_text('"\u4f60\u597d"\uff08\u4e16\u754c\uff09'), "\u4f60\u597d\u4e16\u754c")


class TestSimilarity(unittest.TestCase):
    def test_identical_returns_one(self):
        self.assertEqual(ndf.similarity("\u4f60\u597d\u4e16\u754c", "\u4f60\u597d\u4e16\u754c"), 1.0)

    def test_substring_quote_counts_as_exact(self):
        # 提示词是原著的逐字片段（>=4 字且更短）→ 视为 1.0
        self.assertEqual(
            ndf.similarity("\u6c38\u8fdc\u4e0d\u4f1a\u80cc\u53db", "\u6211\u8981\u4e00\u4e2a\u6c38\u8fdc\u4e0d\u4f1a\u80cc\u53db\u6211\u7684\u73a9\u5177"),
            1.0,
        )

    def test_unrelated_low_similarity(self):
        self.assertLess(ndf.similarity("\u4f60\u597d\u4e16\u754c", "\u5b8c\u5168\u65e0\u5173\u7684\u53e6\u4e00\u53e5\u8bdd"), 0.85)

    def test_empty_returns_zero(self):
        self.assertEqual(ndf.similarity("\uff0c\uff01", "\u4f60\u597d"), 0.0)


class TestGetThreshold(unittest.TestCase):
    def test_very_short(self):
        self.assertEqual(ndf.get_threshold("\u662f\u7684"), 0.60)

    def test_short(self):
        self.assertEqual(ndf.get_threshold("\u4f60\u597d\u4e16\u754c"), 0.75)

    def test_normal(self):
        self.assertEqual(ndf.get_threshold("\u4f60\u597d\u4e16\u754c\u4e00\u4e8c\u4e09"), ndf.CLOSE_MATCH_THRESHOLD)


class TestExtractNovelDialogues(unittest.TestCase):
    def test_standalone_quote_line(self):
        ds = ndf.extract_novel_dialogues('"\u4f60\u597d\u4e16\u754c\u670b\u53cb"')
        self.assertTrue(any(d.text == "\u4f60\u597d\u4e16\u754c\u670b\u53cb" for d in ds))

    def test_speaker_verb_quote(self):
        ds = ndf.extract_novel_dialogues('\u53f6\u950b\u9053\uff0c"\u4f60\u597d\u4e16\u754c"')
        self.assertTrue(any(d.text == "\u4f60\u597d\u4e16\u754c" for d in ds))

    def test_chat_colon_format(self):
        ds = ndf.extract_novel_dialogues("\u6797\u98de\uff1a\u4f60\u597d\u4e16\u754c\u5440")
        self.assertTrue(any(d.text == "\u4f60\u597d\u4e16\u754c\u5440" and d.speaker == "\u6797\u98de" for d in ds))


class TestExtractScriptDialogues(unittest.TestCase):
    def test_speaker_modifier_quote(self):
        ds = ndf.extract_script_dialogues('\u5973\u513f\uff08\u6492\u5a07\uff09\uff1a"\u6211\u8981\u73a9\u5177"')
        self.assertEqual(len(ds), 1)
        self.assertEqual(ds[0].text, "\u6211\u8981\u73a9\u5177")
        self.assertEqual(ds[0].speaker, "\u5973\u513f")

    def test_scene_header_and_action_skipped(self):
        text = (
            "### \u7b2c1\u573a - \u6d4b\u8bd5\u573a\u666f\n"
            "\u25b2 \u5979\u7f13\u7f13\u8f6c\u8eab\uff0c\u770b\u5411\u7a97\u5916\n"
            '\u5973\u513f\uff1a"\u6211\u8981\u73a9\u5177"'
        )
        ds = ndf.extract_script_dialogues(text)
        self.assertEqual(len(ds), 1)
        self.assertEqual(ds[0].text, "\u6211\u8981\u73a9\u5177")
        self.assertIn("\u7b2c1\u573a", ds[0].p_id)


class TestMatchAll(unittest.TestCase):
    def test_exact_status(self):
        novel = [ndf.NovelDialogue(speaker="", text="\u4f60\u597d\u4e16\u754c\u670b\u53cb", line_no=1)]
        prompt = [ndf.PromptDialogue(speaker="", text="\u4f60\u597d\u4e16\u754c\u670b\u53cb", p_id="P01", raw="")]
        results = ndf.match_all(prompt, novel)
        self.assertEqual(results[0].status, "exact")

    def test_not_found_status(self):
        novel = [ndf.NovelDialogue(speaker="", text="\u4f60\u597d\u4e16\u754c", line_no=1)]
        prompt = [ndf.PromptDialogue(speaker="", text="\u8fd9\u662f\u5b8c\u5168\u4e0d\u5b58\u5728\u7684\u81ea\u521b\u53f0\u8bcd\u5185\u5bb9", p_id="P01", raw="")]
        results = ndf.match_all(prompt, novel)
        self.assertEqual(results[0].status, "not_found")

    def test_whitelisted_original_status(self):
        if not ndf.ORIGINAL_DIALOGUE_WHITELIST:
            self.skipTest("\u767d\u540d\u5355\u4e3a\u7a7a")
        wl_text = ndf.ORIGINAL_DIALOGUE_WHITELIST[0]
        self.assertTrue(ndf._is_whitelisted(wl_text))
        prompt = [ndf.PromptDialogue(speaker="", text=wl_text, p_id="P01", raw="")]
        results = ndf.match_all(prompt, [])
        self.assertEqual(results[0].status, "original")


class TestGatherAllNovelDialogues(unittest.TestCase):
    """--all-chapters 跨章节聚合（新增功能）"""

    def test_reads_all_txt_and_extracts(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "novel").mkdir()
            (root / "novel" / "\u7b2c1\u7ae0.txt").write_text(
                '\u53f6\u950b\u9053\uff0c"\u8de8\u7ae0\u53f0\u8bcd\u4e00"\n"\u72ec\u7acb\u53f0\u8bcd\u4e8c"',
                encoding="utf-8",
            )
            dialogues, files_read = ndf.gather_all_novel_dialogues(root)
            self.assertIn("\u7b2c1\u7ae0.txt", files_read)
            self.assertTrue(any("\u8de8\u7ae0\u53f0\u8bcd\u4e00" == x.text for x in dialogues))

    def test_missing_novel_dir_returns_empty(self):
        with tempfile.TemporaryDirectory() as d:
            dialogues, files_read = ndf.gather_all_novel_dialogues(Path(d))
            self.assertEqual(dialogues, [])
            self.assertEqual(files_read, [])

    def test_dedup_across_files(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "novel").mkdir()
            (root / "novel" / "a.txt").write_text('"\u91cd\u590d\u53f0\u8bcd\u5185\u5bb9"', encoding="utf-8")
            (root / "novel" / "b.txt").write_text('"\u91cd\u590d\u53f0\u8bcd\u5185\u5bb9"', encoding="utf-8")
            dialogues, files_read = ndf.gather_all_novel_dialogues(root)
            matches = [x for x in dialogues if x.text == "\u91cd\u590d\u53f0\u8bcd\u5185\u5bb9"]
            self.assertEqual(len(matches), 1)
            self.assertEqual(len(files_read), 2)


if __name__ == "__main__":
    unittest.main()
