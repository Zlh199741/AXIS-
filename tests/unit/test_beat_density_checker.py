#!/usr/bin/env python3
"""
节拍密度校验器（beat-density-checker.py）单元测试

覆盖解析引擎纯函数：
- extract_p_blocks：从 markdown 提取 P 块，规范化 p_id（含拆分后缀 a/b/c）
- extract_declared_duration：提取声明时长（支持 建议/加粗/中文秒/约 等写法）
"""

import unittest
import importlib.util
from pathlib import Path

_project_root = Path(__file__).parent.parent.parent
_spec = importlib.util.spec_from_file_location(
    "beat_density_checker",
    _project_root / "tools" / "validators" / "beat-density-checker.py",
)
bdc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bdc)


class TestExtractPBlocks(unittest.TestCase):
    def test_two_blocks_with_normalized_id(self):
        content = "## P1 | 开场\n内容A\n## P2 | 高潮\n内容B"
        blocks = bdc.extract_p_blocks(content)
        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0][0], "P01")
        self.assertEqual(blocks[1][0], "P02")

    def test_title_extracted(self):
        blocks = bdc.extract_p_blocks("### P01 | 开场镜头\n正文")
        self.assertEqual(blocks[0][1], "开场镜头")

    def test_split_suffix_id(self):
        blocks = bdc.extract_p_blocks("### P01a | 拆分块\n正文")
        self.assertEqual(blocks[0][0], "P01-a")

    def test_no_blocks(self):
        self.assertEqual(bdc.extract_p_blocks("没有任何 P 块的普通文本"), [])


class TestExtractDeclaredDuration(unittest.TestCase):
    def test_duration_suggest(self):
        self.assertEqual(bdc.extract_declared_duration("时长建议：8s"), 8)

    def test_duration_bold(self):
        self.assertEqual(bdc.extract_declared_duration("**时长**：20s"), 20)

    def test_duration_chinese_unit(self):
        self.assertEqual(bdc.extract_declared_duration("时长：12秒"), 12)

    def test_duration_approx(self):
        self.assertEqual(bdc.extract_declared_duration("时长：约15s"), 15)

    def test_no_duration(self):
        self.assertIsNone(bdc.extract_declared_duration("这里没有时长信息"))


class TestBubbleContext(unittest.TestCase):
    """_is_bubble_context：识别气泡/浮叠/广播等非口型语境"""

    def test_bubble_keyword_true(self):
        self.assertTrue(bdc._is_bubble_context("气泡弹出一行字"))

    def test_broadcast_true(self):
        self.assertTrue(bdc._is_bubble_context("系统广播响起"))

    def test_non_bubble_false(self):
        self.assertFalse(bdc._is_bubble_context("镜头推进至中景"))


class TestSystemOrUiText(unittest.TestCase):
    """_is_system_or_ui_text：识别系统消息/卡片/章节标题（非角色对白）"""

    def test_system_ding_true(self):
        self.assertTrue(bdc._is_system_or_ui_text("叮！系统提示"))

    def test_field_label_true(self):
        self.assertTrue(bdc._is_system_or_ui_text("名称：万界群"))

    def test_dialogue_false(self):
        self.assertFalse(bdc._is_system_or_ui_text("你好世界，我来了"))


if __name__ == "__main__":
    unittest.main()
