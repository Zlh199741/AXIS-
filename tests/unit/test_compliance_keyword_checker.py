#!/usr/bin/env python3
"""
合规关键词校验器（compliance-keyword-checker.py）单元测试

覆盖纯逻辑函数：
- build_keyword_index：词库 dict → 扁平索引（含绝对禁止/替换词/按词长降序）
- is_whitelisted：上下文白名单 + 行级正则白名单
- deduplicate_hits：同行同词去重
- scan_file：逐行扫描（含分隔线/空行跳过、不存在文件兜底）
"""

import unittest
import tempfile
import importlib.util
from pathlib import Path

_project_root = Path(__file__).parent.parent.parent
_spec = importlib.util.spec_from_file_location(
    "compliance_keyword_checker",
    _project_root / "tools" / "validators" / "compliance-keyword-checker.py",
)
ckc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ckc)


class TestBuildKeywordIndex(unittest.TestCase):
    def test_absolute_ban_entry(self):
        idx = ckc.build_keyword_index({"absolute_ban": {"words": ["禁词"]}})
        self.assertEqual(len(idx), 1)
        e = idx[0]
        self.assertEqual(e["word"], "禁词")
        self.assertEqual(e["category"], "绝对禁止")
        self.assertEqual(e["severity"], "🔴")
        self.assertTrue(e["is_absolute_ban"])

    def test_replacement_entry(self):
        idx = ckc.build_keyword_index({
            "blood_violence": {"_severity": "🟡", "replacements": {"砍": "击"}}
        })
        self.assertEqual(len(idx), 1)
        self.assertEqual(idx[0]["word"], "砍")
        self.assertEqual(idx[0]["replacement"], "击")
        self.assertFalse(idx[0]["is_absolute_ban"])

    def test_sorted_by_length_desc(self):
        idx = ckc.build_keyword_index({"absolute_ban": {"words": ["甲", "甲乙丙", "甲乙"]}})
        lengths = [len(e["word"]) for e in idx]
        self.assertEqual(lengths, sorted(lengths, reverse=True))

    def test_empty_dictionary(self):
        self.assertEqual(ckc.build_keyword_index({}), [])


class TestIsWhitelisted(unittest.TestCase):
    def test_context_pattern_match(self):
        wl = {"context_patterns": [{"word": "杀", "allowed_contexts": ["杀青"]}]}
        self.assertTrue(ckc.is_whitelisted("杀", "今天电影杀青了", wl))

    def test_context_pattern_no_match(self):
        wl = {"context_patterns": [{"word": "杀", "allowed_contexts": ["杀青"]}]}
        self.assertFalse(ckc.is_whitelisted("杀", "他杀了人", wl))

    def test_line_pattern_wildcard(self):
        wl = {"line_pattern_whitelist": [{"words": ["*"], "pattern": r"^#"}]}
        self.assertTrue(ckc.is_whitelisted("任意词", "# 这是标题", wl))

    def test_empty_whitelist(self):
        self.assertFalse(ckc.is_whitelisted("词", "任意行", {}))


class TestDeduplicateHits(unittest.TestCase):
    def test_dedup_same_line_same_word(self):
        hits = [
            {"line_num": 1, "word": "a"},
            {"line_num": 1, "word": "a"},
            {"line_num": 2, "word": "a"},
        ]
        self.assertEqual(len(ckc.deduplicate_hits(hits)), 2)

    def test_keeps_distinct_words(self):
        hits = [{"line_num": 1, "word": "a"}, {"line_num": 1, "word": "b"}]
        self.assertEqual(len(ckc.deduplicate_hits(hits)), 2)

    def test_empty(self):
        self.assertEqual(ckc.deduplicate_hits([]), [])


class TestScanFile(unittest.TestCase):
    def _write(self, text):
        f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        f.write(text)
        f.close()
        return Path(f.name)

    def test_hit_detected_with_line_number(self):
        idx = ckc.build_keyword_index({"absolute_ban": {"words": ["禁词"]}})
        p = self._write("第一行正常\n第二行有禁词在此\n")
        try:
            hits = ckc.scan_file(p, idx)
        finally:
            p.unlink()
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["line_num"], 2)
        self.assertEqual(hits[0]["word"], "禁词")

    def test_skips_separator_and_blank(self):
        idx = ckc.build_keyword_index({"absolute_ban": {"words": ["禁词"]}})
        p = self._write("---\n\n禁词")
        try:
            hits = ckc.scan_file(p, idx)
        finally:
            p.unlink()
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["line_num"], 3)

    def test_nonexistent_file_returns_empty(self):
        idx = ckc.build_keyword_index({"absolute_ban": {"words": ["x"]}})
        self.assertEqual(ckc.scan_file(Path("/no/such/file.md"), idx), [])


if __name__ == "__main__":
    unittest.main()
