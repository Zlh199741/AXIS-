#!/usr/bin/env python3
"""
T0 标准校验器（t0-validator.py）单元测试

覆盖 T0Validator 的核心可测行为：
- 关键词存在性检测（passed_items / missing_items）
- 防崩坏（anti-corruption）检测
- 返回结构契约（passed/score/passed_items/missing_items/anti_corruption）
- 未知类型处理
- 辅助函数 clean_text / heading_level

设计原则：用模块自身的 RULES / ANTI_CORRUPTION_KEYWORDS 常量构造输入，
避免硬编码关键词导致测试随规则微调而脆裂。
"""

import unittest
import importlib.util
from pathlib import Path

# t0-validator.py 含连字符，无法直接 import，按项目约定用 importlib 从路径加载
_project_root = Path(__file__).parent.parent.parent
_spec = importlib.util.spec_from_file_location(
    "t0_validator",
    _project_root / "tools" / "validators" / "t0-validator.py",
)
t0 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(t0)


class TestReturnContract(unittest.TestCase):
    """返回结构契约测试"""

    def setUp(self):
        self.v = t0.T0Validator()

    def test_return_has_all_keys(self):
        result = self.v.validate_prompt("任意内容", "character")
        for key in ("passed", "score", "passed_items", "missing_items", "anti_corruption"):
            self.assertIn(key, result)

    def test_return_field_types(self):
        result = self.v.validate_prompt("任意内容", "character")
        self.assertIsInstance(result["passed"], bool)
        self.assertIsInstance(result["score"], int)
        self.assertIsInstance(result["passed_items"], list)
        self.assertIsInstance(result["missing_items"], list)
        self.assertIsInstance(result["anti_corruption"], bool)

    def test_score_within_range(self):
        result = self.v.validate_prompt("任意内容", "character")
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 100)

    def test_unknown_type_returns_error(self):
        result = self.v.validate_prompt("xxx", "not_a_real_type")
        self.assertFalse(result["passed"])
        self.assertIn("error", result)


class TestKeywordDetection(unittest.TestCase):
    """关键词存在性检测（T0 校验本质是关键词匹配）"""

    def setUp(self):
        self.v = t0.T0Validator()

    def test_required_keyword_present_marks_passed(self):
        """文本含某必需规则的关键词 → 该规则名出现在 passed_items"""
        rule = t0.RULES["character"]["1_background"]
        keyword = rule["keywords"][0]
        result = self.v.validate_prompt(f"角色设定 {keyword}", "character")
        self.assertIn(rule["name"], result["passed_items"])

    def test_required_keyword_absent_marks_missing(self):
        """文本不含任何关键词 → 必需规则名出现在 missing_items"""
        result = self.v.validate_prompt("一段没有任何 T0 关键词的普通中文描述", "character")
        self.assertIn(t0.RULES["character"]["1_background"]["name"], result["missing_items"])

    def test_props_without_keywords_fails(self):
        result = self.v.validate_prompt("一件普通的道具", "props")
        self.assertFalse(result["passed"])
        self.assertGreater(len(result["missing_items"]), 0)

    def test_scene_without_fields_fails(self):
        result = self.v.validate_prompt("## [ep01][scene] 测试场景\n一些不完整的描述", "scene")
        self.assertFalse(result["passed"])


class TestAntiCorruption(unittest.TestCase):
    """防崩坏（negative prompt）检测"""

    def setUp(self):
        self.v = t0.T0Validator()

    def test_anti_corruption_detected(self):
        keyword = t0.ANTI_CORRUPTION_KEYWORDS[0]
        result = self.v.validate_prompt(f"内容 {keyword}", "character")
        self.assertTrue(result["anti_corruption"])

    def test_anti_corruption_absent_adds_missing(self):
        result = self.v.validate_prompt("没有任何防崩坏负面约束的内容", "character")
        self.assertFalse(result["anti_corruption"])
        self.assertIn("防崩坏指令 (Negative Prompt)", result["missing_items"])


class TestCleanText(unittest.TestCase):
    """clean_text：去除 markdown 干扰符并归一化"""

    def setUp(self):
        self.v = t0.T0Validator()

    def test_removes_markdown_symbols(self):
        self.assertEqual(self.v.clean_text("**Bold** `code`"), "bold code")

    def test_collapses_whitespace_and_lowercases(self):
        self.assertEqual(self.v.clean_text("  AAA\n\n  BBB  "), "aaa bbb")


class TestHeadingLevel(unittest.TestCase):
    """heading_level：识别 2-6 级 markdown 标题"""

    def setUp(self):
        self.v = t0.T0Validator()

    def test_h2_and_h4(self):
        self.assertEqual(self.v.heading_level("## 标题"), 2)
        self.assertEqual(self.v.heading_level("#### 标题"), 4)

    def test_non_heading_returns_none(self):
        self.assertIsNone(self.v.heading_level("普通文本"))

    def test_h1_not_matched(self):
        # 正则为 #{2,6}，一级标题不计入
        self.assertIsNone(self.v.heading_level("# 一级标题"))


if __name__ == "__main__":
    unittest.main()
