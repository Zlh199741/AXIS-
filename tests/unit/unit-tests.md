---
name: unit-tests
description: 单元测试模块。用于测试项目各核心功能模块的正确性。
---

# 单元测试

## 用途
验证项目各核心功能模块的正确性，确保代码逻辑正确。

---

## 测试结构

```
tests/
├── unit/
│   ├── test_file_parser.py      # 文件解析测试
│   ├── test_prompt_builder.py  # 提示词构建测试
│   ├── test_budget_checker.py  # 预算检查测试
│   ├── test_label_parser.py     # 标签解析测试
│   └── test_validator.py        # 验证器测试
└── run_all.py                   # 运行所有测试
```

---

## 测试文件

### test_file_parser.py - 文件解析测试

```python
#!/usr/bin/env python3
"""
文件解析模块单元测试
"""

import unittest
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.file_parser import ScriptParser, AssetParser, OutputParser


class TestScriptParser(unittest.TestCase):
    """剧本解析器测试"""
    
    def setUp(self):
        self.parser = ScriptParser()
    
    def test_parse_episode_number(self):
        """测试集数解析"""
        # 测试不同格式的文件名
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
```

---

### test_prompt_builder.py - 提示词构建测试

```python
#!/usr/bin/env python3
"""
提示词构建模块单元测试
"""

import unittest
from lib.prompt_builder import (
    SeedancePromptBuilder,
    CharacterPromptBuilder,
    ScenePromptBuilder
)


class TestSeedancePromptBuilder(unittest.TestCase):
    """Seedance 提示词构建器测试"""
    
    def setUp(self):
        self.builder = SeedancePromptBuilder()
    
    def test_build_basic_prompt(self):
        """测试基础提示词构建"""
        result = self.builder.build(
            scene="室内场景",
            action="主角坐下",
            duration=5
        )
        
        self.assertIn("室内场景", result)
        self.assertIn("主角坐下", result)
        self.assertIn("5秒", result)
    
    def test_add_camera_movement(self):
        """测试添加运镜"""
        base = "主角走进房间"
        result = self.builder.add_camera_movement(
            base,
            movement="推",
            from_point="全景",
            to_point="特写"
        )
        
        self.assertIn("推", result)
        self.assertIn("全景", result)
        self.assertIn("特写", result)
    
    def test_add_lighting(self):
        """测试添加光影"""
        base = "室内场景"
        result = self.builder.add_lighting(
            base,
            source="窗户",
            color="暖黄色",
            effect="摇曳"
        )
        
        self.assertIn("暖黄色", result)
        self.assertIn("窗户", result)
    
    def test_add_audio(self):
        """测试添加声音"""
        base = "主角走进房间"
        result = self.builder.add_audio(
            base,
            bgm="轻柔音乐",
            sfx="脚步声"
        )
        
        self.assertIn("背景音乐", result)
        self.assertIn("脚步声", result)


class TestCharacterPromptBuilder(unittest.TestCase):
    """人物提示词构建器测试"""
    
    def setUp(self):
        self.builder = CharacterPromptBuilder()
    
    def test_build_standard_layout(self):
        """测试标准布局（特写+三视图）"""
        result = self.builder.build(
            name="江辰",
            description="古代公子哥儿",
            layout="standard"
        )
        
        self.assertIn("江辰", result)
        self.assertIn("特写", result)
        self.assertIn("三视图", result)
    
    def test_build_enhanced_layout(self):
        """测试增强布局（8视图）"""
        result = self.builder.build(
            name="江辰",
            description="古代公子哥儿",
            layout="enhanced"
        )
        
        self.assertIn("江辰", result)
        self.assertIn("8视图", result)
    
    def test_add_material_details(self):
        """测试添加材质细节"""
        base = "身穿暗红色锦袍"
        materials = [
            {"name": "丝绸", "properties": "光泽,织纹细腻"},
            {"name": "金线", "properties": "拉丝,手工刺绣"}
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
            base,
            main_light="烛光",
            auxiliary="闪电",
            logic="冷暖对比"
        )
        
        self.assertIn("烛光", result)
        self.assertIn("闪电", result)


if __name__ == "__main__":
    unittest.main()
```

---

### test_budget_checker.py - 预算检查测试

```python
#!/usr/bin/env python3
"""
预算检查模块单元测试
"""

import unittest
from lib.budget_checker import BudgetChecker, BudgetLimit


class TestBudgetChecker(unittest.TestCase):
    """预算检查器测试"""
    
    def setUp(self):
        self.checker = BudgetChecker()
    
    def test_check_image_references(self):
        """测试图片引用检查"""
        # 测试通过情况
        prompt = "使用 @图片1 @图片2 @图片3"
        result = self.checker.check(prompt)
        self.assertTrue(result["pass"])
        
        # 测试超限情况
        prompt = "使用 " + " ".join([f"@图片{i}" for i in range(15)])
        result = self.checker.check(prompt)
        self.assertFalse(result["pass"])
        self.assertIn("图片", result["reason"])
    
    def test_check_video_references(self):
        """测试视频引用检查"""
        # 测试通过情况
        prompt = "使用 @视频1 @视频2 @视频3"
        result = self.checker.check(prompt)
        self.assertTrue(result["pass"])
        
        # 测试超限情况
        prompt = "使用 " + " ".join([f"@视频{i}" for i in range(5)])
        result = self.checker.check(prompt)
        self.assertFalse(result["pass"])
        self.assertIn("视频", result["reason"])
    
    def test_check_audio_references(self):
        """测试音频引用检查"""
        prompt = "使用 @音频1 @音频2"
        result = self.checker.check(prompt)
        self.assertTrue(result["pass"])
    
    def test_check_total_references(self):
        """测试总引用数检查"""
        # 9 图片 + 3 视频 + 3 音频 = 15 > 12
        refs = ["@图片{}".format(i) for i in range(10)]
        refs += ["@视频{}".format(i) for i in range(4)]
        refs += ["@音频{}".format(i) for i in range(4)]
        
        prompt = "使用 " + " ".join(refs)
        result = self.checker.check(prompt)
        
        self.assertFalse(result["pass"])
    
    def test_calculate_budget(self):
        """测试预算计算"""
        prompt = "@图片1 @图片2 @视频1 @音频1"
        
        budget = self.checker.calculate_budget(prompt)
        
        self.assertEqual(budget["images"], 2)
        self.assertEqual(budget["videos"], 1)
        self.assertEqual(budget["audios"], 1)
        self.assertEqual(budget["total"], 4)


class TestBudgetLimit(unittest.TestCase):
    """预算限制测试"""
    
    def test_default_limits(self):
        """测试默认限制"""
        limits = BudgetLimit()
        
        self.assertEqual(limits.max_images, 9)
        self.assertEqual(limits.max_videos, 3)
        self.assertEqual(limits.max_audios, 3)
        self.assertEqual(limits.max_total, 12)
    
    def test_custom_limits(self):
        """测试自定义限制"""
        limits = BudgetLimit(
            max_images=5,
            max_videos=2,
            max_audios=2,
            max_total=8
        )
        
        self.assertEqual(limits.max_images, 5)
        self.assertEqual(limits.max_total, 8)


if __name__ == "__main__":
    unittest.main()
```

---

### test_label_parser.py - 标签解析测试

```python
#!/usr/bin/env python3
"""
标签解析模块单元测试
"""

import unittest
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
```

---

### test_validator.py - 验证器测试

```python
#!/usr/bin/env python3
"""
验证器模块单元测试
"""

import unittest
from lib.validator import (
    DirectorAnalysisValidator,
    ArtDesignValidator,
    SeedancePromptValidator
)


class TestDirectorAnalysisValidator(unittest.TestCase):
    """导演分析验证器测试"""
    
    def setUp(self):
        self.validator = DirectorAnalysisValidator()
    
    def test_validate_complete_analysis(self):
        """测试完整分析验证"""
        content = """
        # 导演分析
        
        ## P01 剧情点
        讲戏内容...
        
        ## 人物清单
        1. 江辰 - 主角
        
        ## 场景清单
        1. 江府房间 - 内景
        
        ## 视听语言要点
        镜头：近景
        光影：暖光
        """
        
        result = self.validator.validate(content)
        self.assertTrue(result["valid"])
    
    def test_validate_missing_sections(self):
        """测试缺失章节验证"""
        content = """
        # 导演分析
        
        ## P01 剧情点
        讲戏内容...
        """
        
        result = self.validator.validate(content)
        self.assertFalse(result["valid"])
        self.assertIn("人物清单", result["missing"])
    
    def test_validate_empty_points(self):
        """测试空剧情点验证"""
        content = """
        # 导演分析
        
        ## 人物清单
        1. 江辰
        
        ## 场景清单
        1. 江府
        """
        
        result = self.validator.validate(content)
        self.assertFalse(result["valid"])


class TestArtDesignValidator(unittest.TestCase):
    """服化道设计验证器测试"""
    
    def setUp(self):
        self.validator = ArtDesignValidator()
    
    def test_validate_character_prompt(self):
        """测试人物提示词验证"""
        content = """
        # 人物提示词
        
        ## [ep01][character][新增] 江辰
        **提示词**：一位二十岁左右的古代公子哥儿
        **布局**：特写 + 三视图
        """
        
        result = self.validator.validate_character(content)
        self.assertTrue(result["valid"])
    
    def test_validate_character_missing_layout(self):
        """测试人物提示词缺失布局"""
        content = """
        # 人物提示词
        
        ## [ep01][character][新增] 江辰
        **提示词**：一位二十岁左右的古代公子哥儿
        """
        
        result = self.validator.validate_character(content)
        self.assertFalse(result["valid"])
    
    def test_validate_scene_prompt(self):
        """测试场景提示词验证"""
        content = """
        # 场景提示词
        
        ## [ep01][scene][新增] 江府房间
        **提示词**：古色古香的卧室
        **宫格**：3×3
        """
        
        result = self.validator.validate_scene(content)
        self.assertTrue(result["valid"])
    
    def test_validate_enhanced_mode(self):
        """测试增强模式验证"""
        content = """
        # 人物提示词
        
        ## [ep01][character][新增] 江辰
        **提示词**：...
        
        ### 材质与工艺细节
        - 丝绸
        - 金线
        """
        
        result = self.validator.validate_character(content)
        self.assertTrue(result["valid"])
        self.assertTrue(result.get("enhanced_mode"))


class TestSeedancePromptValidator(unittest.TestCase):
    """Seedance 提示词验证器测试"""
    
    def setUp(self):
        self.validator = SeedancePromptValidator()
    
    def test_validate_complete_prompt(self):
        """测试完整提示词验证"""
        content = """
        # Seedance 提示词
        
        ## 素材对应表
        | ID | 类型 | 描述 |
        |----|------|------|
        | @图片1 | 人物 | 江辰 |
        
        ## P01 提示词
        镜头缓缓推进...
        """
        
        result = self.validator.validate(content)
        self.assertTrue(result["valid"])
    
    def test_validate_missing_mapping(self):
        """测试缺失素材映射表"""
        content = """
        # Seedance 提示词
        
        ## P01 提示词
        镜头缓缓推进...
        """
        
        result = self.validator.validate(content)
        self.assertFalse(result["valid"])
        self.assertIn("素材对应表", result["missing"])
    
    def test_validate_reference_consistency(self):
        """测试引用一致性"""
        content = """
        # Seedance 提示词
        
        ## 素材对应表
        | ID | 类型 | 描述 |
        |----|------|------|
        | @图片1 | 人物 | 江辰 |
        
        ## P01 提示词
        镜头中出现 @图片1
        """
        
        result = self.validator.validate_references(content)
        self.assertTrue(result["consistent"])
    
    def test_validate_budget(self):
        """测试预算验证"""
        content = """
        ## P01 提示词
        """ + " @图片1" * 10
        
        result = self.validator.validate_budget(content)
        self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main()
```

---

## 运行测试

### 运行所有单元测试
```bash
python -m pytest tests/unit/ -v
```

### 运行特定测试
```bash
python -m pytest tests/unit/test_budget_checker.py -v
```

### 生成测试报告
```bash
python -m pytest tests/unit/ --html=report.html --self-contained-html
```

---

## 测试覆盖率目标

| 模块 | 目标覆盖率 |
|------|-----------|
| file_parser | 80% |
| prompt_builder | 85% |
| budget_checker | 90% |
| label_parser | 85% |
| validator | 80% |

---

## 持续集成

在 `.github/workflows/test.yml` 中配置自动化测试：

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        pip install pytest
        pip install -r requirements.txt
    - name: Run tests
      run: python -m pytest tests/unit/ -v
    - name: Upload coverage
      uses: codecov/codecov-action@v2
```

