#!/usr/bin/env python3
"""
提示词构建模块单元测试
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.prompt_builder import SeedancePromptBuilder, CharacterPromptBuilder, ScenePromptBuilder


class TestSeedancePromptBuilder(unittest.TestCase):
    """Seedance 提示词构建器测试"""

    def setUp(self):
        self.builder = SeedancePromptBuilder()

    def test_build_basic_prompt(self):
        """测试基础提示词构建"""
        result = self.builder.build(scene="室内场景", action="主角坐下", duration=5)
        self.assertIn("室内场景", result)
        self.assertIn("主角坐下", result)
        self.assertIn("5秒", result)

    def test_add_camera_movement(self):
        """测试添加运镜"""
        base = "主角走进房间"
        result = self.builder.add_camera_movement(base, movement="推", from_point="全景", to_point="特写")
        self.assertIn("推", result)
        self.assertIn("全景", result)
        self.assertIn("特写", result)

    def test_add_lighting(self):
        """测试添加光影"""
        base = "室内场景"
        result = self.builder.add_lighting(base, source="窗户", color="暖黄色", effect="摇曳")
        self.assertIn("暖黄色", result)
        self.assertIn("窗户", result)

    def test_add_audio(self):
        """测试添加声音"""
        base = "主角走进房间"
        result = self.builder.add_audio(base, bgm="轻柔音乐", sfx="脚步声")
        self.assertIn("背景音乐", result)
        self.assertIn("脚步声", result)


class TestCharacterPromptBuilder(unittest.TestCase):
    """人物提示词构建器测试"""

    def setUp(self):
        self.builder = CharacterPromptBuilder()

    def test_build_standard_layout(self):
        """测试标准布局（特写+三视图）"""
        result = self.builder.build(name="江辰", description="古代公子哥儿", layout="standard")
        self.assertIn("江辰", result)
        self.assertIn("特写", result)
        self.assertIn("三视图", result)

    def test_build_enhanced_layout(self):
        """测试增强布局（8视图）"""
        result = self.builder.build(name="江辰", description="古代公子哥儿", layout="enhanced")
        self.assertIn("江辰", result)
        self.assertIn("8视图", result)

    def test_add_material_details(self):
        """测试添加材质细节"""
        base = "身穿暗红色锦袍"
        materials = [
            {"name": "丝绸", "properties": "光泽,织纹细腻"},
            {"name": "金线", "properties": "拉丝,手工刺绣"},
        ]
        result = self.builder.add_material_details(base, materials)
        self.assertIn("丝绸", result)
        self.assertIn("金线", result)


class TestScenePromptBuilder(unittest.TestCase):
    """场景提示词构建器测试"""

    def setUp(self):
        self.builder = ScenePromptBuilder()

    def test_build_grid_3x3(self):
        """测试 3x3 宫格构建"""
        scenes = ["场景1", "场景2", "场景3", "场景4", "场景5",
                  "场景6", "场景7", "场景8", "场景9"]
        result = self.builder.build_grid(scenes, "3x3")
        self.assertIn("3×3", result)
        self.assertIn("场景1", result)

    def test_build_grid_3x4(self):
        """测试 3x4 宫格构建"""
        scenes = ["场景" + str(i) for i in range(12)]
        result = self.builder.build_grid(scenes, "3x4")
        self.assertIn("3×4", result)

    def test_add_lighting_specification(self):
        """测试添加光影规范"""
        base = "古色古香的卧室"
        result = self.builder.add_lighting_specification(
            base, main_light="烛光", auxiliary="闪电", logic="冷暖对比"
        )
        self.assertIn("烛光", result)
        self.assertIn("闪电", result)


if __name__ == "__main__":
    unittest.main()
