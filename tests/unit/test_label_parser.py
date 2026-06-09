#!/usr/bin/env python3
"""
标签解析模块单元测试
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.label_parser import LabelParser, LabelType, EpisodeLabel


class TestLabelParser(unittest.TestCase):
    """标签解析器测试"""

    def setUp(self):
        self.parser = LabelParser()

    def test_parse_character_label(self):
        """测试人物标签解析"""
        label = "[ep01][character][新增] 江辰"
        result = self.parser.parse(label)
        self.assertEqual(result.episode, "ep01")
        self.assertEqual(result.type, LabelType.CHARACTER)
        self.assertEqual(result.action, "新增")
        self.assertEqual(result.name, "江辰")

    def test_parse_scene_label(self):
        """测试场景标签解析"""
        label = "[ep02][scene][变体] 江府房间-夜"
        result = self.parser.parse(label)
        self.assertEqual(result.episode, "ep02")
        self.assertEqual(result.type, LabelType.SCENE)
        self.assertEqual(result.action, "变体")

    def test_parse_reuse_label(self):
        """测试复用标签"""
        label = "[ep03][character][复用] 江辰"
        result = self.parser.parse(label)
        self.assertEqual(result.action, "复用")

    def test_extract_episode_labels(self):
        """测试提取集数标签"""
        content = """
        ## [ep01][character][新增] 江辰
        ## [ep01][scene][新增] 江府
        ## [ep02][character][新增] 新角色
        """
        labels = self.parser.extract_all(content)
        self.assertEqual(len(labels), 3)
        ep01_labels = [l for l in labels if l.episode == "ep01"]
        self.assertEqual(len(ep01_labels), 2)

    def test_filter_by_episode(self):
        """测试按集数筛选"""
        content = """
        ## [ep01][character][新增] 江辰
        ## [ep02][character][新增] 新角色
        """
        labels = self.parser.extract_all(content)
        ep01_labels = self.parser.filter_by_episode(labels, "ep01")
        self.assertEqual(len(ep01_labels), 1)
        self.assertEqual(ep01_labels[0].name, "江辰")


class TestEpisodeLabel(unittest.TestCase):
    """集数标签测试"""

    def test_label_equality(self):
        """测试标签相等"""
        label1 = EpisodeLabel("ep01", LabelType.CHARACTER, "新增", "江辰")
        label2 = EpisodeLabel("ep01", LabelType.CHARACTER, "新增", "江辰")
        self.assertEqual(label1, label2)

    def test_label_to_string(self):
        """测试标签转字符串"""
        label = EpisodeLabel("ep01", LabelType.CHARACTER, "新增", "江辰")
        result = str(label)
        self.assertIn("ep01", result)
        self.assertIn("character", result)
        self.assertIn("江辰", result)


if __name__ == "__main__":
    unittest.main()
