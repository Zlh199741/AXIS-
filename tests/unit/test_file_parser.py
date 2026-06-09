#!/usr/bin/env python3
"""
文件解析模块单元测试
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.file_parser import ScriptParser, AssetParser, OutputParser


class TestScriptParser(unittest.TestCase):
    """剧本解析器测试"""

    def setUp(self):
        self.parser = ScriptParser()

    def test_parse_episode_number(self):
        """测试集数解析"""
        test_cases = [
            ("第一集.txt", "ep01"),
            ("ep01-剧本.md", "ep01"),
            ("script_ep02.md", "ep02"),
            ("第10集.txt", "ep10"),
        ]
        for filename, expected in test_cases:
            with self.subTest(filename=filename):
                result = self.parser.extract_episode_number(filename)
                self.assertEqual(result, expected)

    def test_parse_scene_markers(self):
        """测试场景标记解析"""
        content = """
        P01 场景：江府房间
        P02 场景：大街上
        P03 场景：牢房
        """
        scenes = self.parser.extract_scenes(content)
        self.assertEqual(len(scenes), 3)
        self.assertIn("江府房间", scenes)

    def test_parse_character_list(self):
        """测试人物列表解析"""
        content = """
        ## 人物清单
        1. 江辰 - 主角
        2. 崔云秀 - 女主角
        3. 系统 - 设定
        """
        characters = self.parser.extract_characters(content)
        self.assertEqual(len(characters), 3)
        self.assertEqual(characters[0]["name"], "江辰")


class TestAssetParser(unittest.TestCase):
    """资产解析器测试"""

    def setUp(self):
        self.parser = AssetParser()

    def test_parse_character_prompts(self):
        """测试人物提示词解析"""
        content = """
        # 人物提示词
        ## [ep01][character][新增] 江辰
        **提示词**：一位二十岁左右的古代公子哥儿...
        """
        prompts = self.parser.parse_character_prompts(content)
        self.assertIn("ep01", prompts)
        self.assertIn("江辰", prompts["ep01"])

    def test_parse_scene_prompts(self):
        """测试场景提示词解析"""
        content = """
        # 场景提示词
        ## [ep01][scene][新增] 江府房间
        **提示词**：古色古香的卧室...
        """
        prompts = self.parser.parse_scene_prompts(content)
        self.assertIn("ep01", prompts)
        self.assertIn("江府房间", prompts["ep01"])


class TestOutputParser(unittest.TestCase):
    """输出解析器测试"""

    def setUp(self):
        self.parser = OutputParser()

    def test_parse_seedance_prompts(self):
        """测试 Seedance 提示词解析"""
        content = """
        ## P01 提示词
        镜头缓缓推进...
        """
        prompts = self.parser.parse_seedance_prompts(content)
        self.assertIn("P01", prompts)

    def test_parse_material_mapping(self):
        """测试素材映射表解析"""
        content = """
        ## 素材对应表
        | ID | 类型 | 描述 |
        |----|------|------|
        | @图片1 | 人物 | 江辰定妆照 |
        """
        mapping = self.parser.parse_material_mapping(content)
        self.assertIn("@图片1", mapping)


if __name__ == "__main__":
    unittest.main()
