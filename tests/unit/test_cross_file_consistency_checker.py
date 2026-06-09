#!/usr/bin/env python3
"""
跨文件一致性校验器（cross-file-consistency-checker.py）单元测试

覆盖纯函数：
- extract_p_ids：按出现顺序提取 P 块 ID（含拆分后缀）
- _extract_scene_from_section：场景字段提取（排除 场景锚点/类型/切换，标题兜底）
- check_c08_spatial_anchor_continuity：GSA 空间锚点存在性（空/缺失/合规三分支）
- Issue：数据结构契约

设计原则：用最小可控输入触发明确分支，断言 severity/check_id 等稳定契约字段。
"""

import unittest
import importlib.util
from pathlib import Path

_project_root = Path(__file__).parent.parent.parent
_spec = importlib.util.spec_from_file_location(
    "cross_file_consistency_checker",
    _project_root / "tools" / "validators" / "cross-file-consistency-checker.py",
)
cfc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cfc)


class TestExtractPIds(unittest.TestCase):
    def test_order_and_levels(self):
        content = "## P01 \u4e00\n\u6587\n### P02 \u4e8c\n## P03-1 \u4e09"
        self.assertEqual(cfc.extract_p_ids(content), ["P01", "P02", "P03-1"])

    def test_split_letter_suffix(self):
        self.assertEqual(cfc.extract_p_ids("## P01a x"), ["P01a"])

    def test_none(self):
        self.assertEqual(cfc.extract_p_ids("\u6ca1\u6709 P \u5757"), [])


class TestExtractSceneFromSection(unittest.TestCase):
    def test_pure_scene_field(self):
        self.assertEqual(
            cfc._extract_scene_from_section("**\u573a\u666f**\uff1a\u6668\u5149\u5ead\u9662\n\u5176\u4ed6"),
            "\u6668\u5149\u5ead\u9662",
        )

    def test_scene_anchor_excluded(self):
        # 「场景锚点：」不应被当作场景字段
        self.assertIsNone(cfc._extract_scene_from_section("\u573a\u666f\u9526\u70b9\uff1a\u67d0\u4e9b\u63cf\u8ff0"))

    def test_title_fallback(self):
        self.assertEqual(
            cfc._extract_scene_from_section("## P01 | \u53e4\u98ce\u8857\u5e02 | \u65e5\u95f4"),
            "\u53e4\u98ce\u8857\u5e02",
        )


class TestCheckC08(unittest.TestCase):
    def test_empty_content_info(self):
        issues = cfc.check_c08_spatial_anchor_continuity("")
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "info")
        self.assertEqual(issues[0].check_id, "C08")

    def test_missing_gsa_critical(self):
        content = (
            "## P01 | \u573a\u666fA\n"
            "### \U0001f3ac Seedance \u63d0\u793a\u8bcd\n"
            "\u8fd9\u91cc\u6ca1\u6709\u7a7a\u95f4\u9526\u70b9\u884c\n"
        )
        issues = cfc.check_c08_spatial_anchor_continuity(content)
        self.assertTrue(any(i.severity == "critical" and "\u7f3a\u5c11" in i.description for i in issues))

    def test_valid_gsa_no_missing_critical(self):
        content = (
            "## P01 | \u573a\u666fA\n"
            "### \U0001f3ac Seedance \u63d0\u793a\u8bcd\n"
            "[Global Spatial Anchor: \u89d2\u8272\u4f4d\u4e8e\u753b\u9762\u5de6\u4fa7\uff0c\u95e8\u534a\u5f00\uff0c\u76f8\u8ddd\u4e09\u6b65]\n"
            "\u753b\u9762\u63cf\u8ff0\n"
        )
        issues = cfc.check_c08_spatial_anchor_continuity(content)
        self.assertFalse(any(i.severity == "critical" and "\u7f3a\u5c11" in i.description for i in issues))


class TestIssueDataclass(unittest.TestCase):
    def test_fields(self):
        issue = cfc.Issue(
            check_id="C01", severity="warning", location="f.md",
            description="d", expected="e", actual="a", suggestion="s",
        )
        self.assertEqual(issue.check_id, "C01")
        self.assertEqual(issue.severity, "warning")


if __name__ == "__main__":
    unittest.main()
