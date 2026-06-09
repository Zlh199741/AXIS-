#!/usr/bin/env python3
"""
原文忠实度校验工具单元测试 (novel-fidelity-checker.py)
覆盖：角色名提取 / 外观描写提取 / 产物解析 / 忠实度比对
"""

import unittest
import sys
import importlib.util
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

TOOLS_DIR = Path(__file__).parent.parent.parent / "tools" / "validators"


def _load_module(name, filepath):
    spec = importlib.util.spec_from_file_location(name, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


nfc = _load_module("novel_fidelity_checker", TOOLS_DIR / "novel-fidelity-checker.py")


# ============================================================
# 角色名提取
# ============================================================

class TestIsPlausibleName(unittest.TestCase):
    """名字候选过滤"""

    def test_valid_names(self):
        for name in ["洛小阳", "江辰", "崔云秀", "萧炎"]:
            with self.subTest(name=name):
                self.assertTrue(nfc.is_plausible_name(name))

    def test_rejects_short(self):
        self.assertFalse(nfc.is_plausible_name("我"))

    def test_rejects_empty(self):
        self.assertFalse(nfc.is_plausible_name(""))

    def test_rejects_bad_start(self):
        for name in ["不知道", "这个人", "那家伙"]:
            with self.subTest(name=name):
                self.assertFalse(nfc.is_plausible_name(name))

    def test_rejects_dash(self):
        self.assertFalse(nfc.is_plausible_name("洛—小"))

    def test_rejects_repeated_char(self):
        self.assertFalse(nfc.is_plausible_name("哈哈"))


class TestExtractCharacterNames(unittest.TestCase):
    """从小说文本提取角色名"""

    def test_extract_from_dialogue_tags(self):
        text = (
            '\u201c你好啊。\u201d洛小阳说。\n'
            '\u201c再见。\u201d洛小阳说。\n'
            '\u201c来这里。\u201d洛小阳说道。\n'
            '\u201c不行。\u201d江辰说道。\n'
            '\u201c可以。\u201d江辰说。\n'
            '\u201c好的。\u201d江辰说。\n'
        )
        names = nfc.extract_character_names_from_novel(text)
        self.assertIn("洛小阳", names)
        self.assertIn("江辰", names)

    def test_ignores_low_frequency(self):
        text = '"你好。"路人甲说。\n只出现一次。\n'
        names = nfc.extract_character_names_from_novel(text)
        self.assertNotIn("路人甲", names)

    def test_stopwords_filtered(self):
        text = (
            '"废话。"不可能说。\n'
            '"废话。"不可能说。\n'
            '"废话。"不可能说。\n'
        )
        names = nfc.extract_character_names_from_novel(text)
        self.assertNotIn("不可能", names)


class TestExtractCharacterDescriptions(unittest.TestCase):
    """角色外观/性格描写提取"""

    def test_extract_appearance(self):
        text = "洛小阳长得高大魁梧，一双金色的眼睛闪着寒光。洛小阳穿着一件黑色铠甲。洛小阳性格冷漠。"
        char_names = {"洛小阳": {"洛小阳"}}
        profiles = nfc.extract_character_descriptions(text, char_names)
        self.assertIn("洛小阳", profiles)
        p = profiles["洛小阳"]
        self.assertTrue(len(p.appearance_keywords) > 0)

    def test_extract_personality(self):
        text = "洛小阳性格冷漠，从不与人交流。"
        char_names = {"洛小阳": {"洛小阳"}}
        profiles = nfc.extract_character_descriptions(text, char_names)
        p = profiles["洛小阳"]
        self.assertTrue(len(p.personality_keywords) > 0)

    def test_no_description_returns_empty(self):
        text = "洛小阳走进了房间。"
        char_names = {"洛小阳": {"洛小阳"}}
        profiles = nfc.extract_character_descriptions(text, char_names)
        p = profiles["洛小阳"]
        self.assertEqual(len(p.appearance_keywords), 0)


# ============================================================
# 产物解析器
# ============================================================

class TestParseDirectorCharacters(unittest.TestCase):
    """导演分析人物清单解析"""

    def test_parse_list_format(self):
        content = """
## 人物清单
1. 洛小阳（男主角）—— 二十岁少年
2. 江辰（配角）—— 古代公子

## 场景清单
"""
        chars = nfc.parse_director_characters(content)
        self.assertIn("洛小阳", chars)
        self.assertIn("江辰", chars)

    def test_parse_table_format(self):
        content = """
## 人物清单
| 角色名 | 年龄 | 描述 |
|--------|------|------|
| 洛小阳 | 20   | 男主角 |
| 崔云秀 | 18   | 女主角 |

## 场景清单
"""
        chars = nfc.parse_director_characters(content)
        self.assertIn("洛小阳", chars)
        self.assertIn("崔云秀", chars)

    def test_empty_content(self):
        chars = nfc.parse_director_characters("")
        self.assertEqual(len(chars), 0)


class TestParseCharacterPrompts(unittest.TestCase):
    """角色提示词解析"""

    def test_parse_ep_label_format(self):
        content = """
## [ep01][character][新增] 洛小阳
A版本：一位二十岁古代少年，身高180cm
B版本：young male warrior, tall, muscular
"""
        chars = nfc.parse_character_prompts(content)
        self.assertIn("洛小阳", chars)

    def test_parse_numbered_format(self):
        content = """
## 1. 洛小阳（男主角）
A版本提示词内容
## 2. 江辰（配角）
B版本提示词内容
"""
        chars = nfc.parse_character_prompts(content)
        self.assertIn("洛小阳", chars)
        self.assertIn("江辰", chars)


if __name__ == "__main__":
    unittest.main()
