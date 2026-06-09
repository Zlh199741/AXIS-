#!/usr/bin/env python3
"""
Seedance 模板校验器（seedance-template-validator.py）单元测试

覆盖解析引擎纯函数与正则常量：
- split_into_p_blocks：按 ## PXX 切块（含 P01a / P03-1 拆分后缀）
- extract_section / extract_machine_layer / extract_human_layer：分层抽取
- TIME_SEGMENT_RE / QUOTED_PAYLOAD_RE：时间段与引号载荷提取
- SEVERITY_ORDER / AUDIO_MUSIC_NEGATION_TERMS：契约常量

设计原则：只测稳定的纯函数与常量，避免依赖文件 IO 与整体判定流程。
"""

import unittest
import importlib.util
from pathlib import Path

_project_root = Path(__file__).parent.parent.parent
_spec = importlib.util.spec_from_file_location(
    "seedance_template_validator",
    _project_root / "tools" / "validators" / "seedance-template-validator.py",
)
stv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(stv)


class TestSplitIntoPBlocks(unittest.TestCase):
    def test_two_blocks(self):
        text = "## P01 \u5f00\u573a\n\u6b63\u6587A\n## P02 \u9ad8\u6f6e\n\u6b63\u6587B"
        blocks = stv.split_into_p_blocks(text)
        self.assertEqual([b[0] for b in blocks], ["P01", "P02"])

    def test_block_text_captured(self):
        text = "## P01 \u5f00\u573a\n\u6b63\u6587A\n## P02 \u9ad8\u6f6e\n\u6b63\u6587B"
        blocks = stv.split_into_p_blocks(text)
        self.assertIn("\u6b63\u6587A", blocks[0][3])
        self.assertNotIn("\u6b63\u6587B", blocks[0][3])

    def test_split_suffix_ids(self):
        self.assertEqual(stv.split_into_p_blocks("## P01a x\ny")[0][0], "P01a")
        self.assertEqual(stv.split_into_p_blocks("## P03-1 x\ny")[0][0], "P03-1")

    def test_no_blocks(self):
        self.assertEqual(stv.split_into_p_blocks("\u6ca1\u6709 P \u5757\u7684\u6587\u672c"), [])


class TestExtractSection(unittest.TestCase):
    def test_between_markers(self):
        block = "A\n\u5f00\u59cb\u6807\u8bb0\n\u5185\u5bb91\n\u505c\u6b62\u6807\u8bb0\nB"
        out = stv.extract_section(block, r"\u5f00\u59cb\u6807\u8bb0", [r"\u505c\u6b62\u6807\u8bb0"])
        self.assertIn("\u5185\u5bb91", out)
        self.assertNotIn("B", out)

    def test_no_start_returns_none(self):
        self.assertIsNone(stv.extract_section("\u65e0\u5339\u914d", r"^###\s*\U0001f3ac", [r"^###"]))


class TestLayerExtraction(unittest.TestCase):
    def test_machine_layer(self):
        block = "### \U0001f3ac Seedance \u63d0\u793a\u8bcd\n\u673a\u8bfb\u5185\u5bb9\u884c\n### \U0001f4cb \u5176\u4ed6"
        out = stv.extract_machine_layer(block)
        self.assertIsNotNone(out)
        self.assertIn("\u673a\u8bfb\u5185\u5bb9\u884c", out)

    def test_machine_layer_absent(self):
        self.assertIsNone(stv.extract_machine_layer("### \U0001f4cb \u5bfc\u6f14\u5206\u6790\n\u6587\u672c"))

    def test_human_layer(self):
        block = "### \U0001f4cb \u5bfc\u6f14\u5206\u6790\n\u5206\u6790\u5185\u5bb9\n### \U0001f3ac Seedance"
        out = stv.extract_human_layer(block)
        self.assertIsNotNone(out)
        self.assertIn("\u5206\u6790\u5185\u5bb9", out)


class TestRegexConstants(unittest.TestCase):
    def test_time_segment_re(self):
        found = stv.TIME_SEGMENT_RE.findall("0-3\u79d2 3-7\u79d2")
        self.assertIn(("0", "3"), found)
        self.assertIn(("3", "7"), found)

    def test_quoted_payload_re(self):
        found = stv.QUOTED_PAYLOAD_RE.findall('\u53f0\u8bcd\uff1a"\u4f60\u597d\u4e16\u754c"')
        self.assertIn("\u4f60\u597d\u4e16\u754c", found)


class TestContractConstants(unittest.TestCase):
    def test_severity_order(self):
        self.assertLess(stv.SEVERITY_ORDER["critical"], stv.SEVERITY_ORDER["warning"])
        self.assertLess(stv.SEVERITY_ORDER["warning"], stv.SEVERITY_ORDER["info"])

    def test_negation_terms_present(self):
        self.assertIn("\u7981\u6b62", stv.AUDIO_MUSIC_NEGATION_TERMS)
        self.assertIn("\u4e0d\u8981", stv.AUDIO_MUSIC_NEGATION_TERMS)


if __name__ == "__main__":
    unittest.main()
