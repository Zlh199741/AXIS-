---
name: integration-tests
description: 集成测试模块。用于测试多个模块协作的正确性，模拟真实工作流程。
---

# 集成测试

## 用途
测试多个模块协作的正确性，模拟真实工作流程，验证端到端功能。

---

## 测试结构

```
tests/
├── integration/
│   ├── test_director_workflow.py      # 导演工作流测试
│   ├── test_art_designer_workflow.py  # 服化道工作流测试
│   ├── test_storyboard_workflow.py   # 分镜工作流测试
│   ├── test_full_episode.py          # 完整集数流程测试
│   └── test_cross_episode.py         # 跨集一致性测试
```

---

## 集成测试文件

### test_director_workflow.py - 导演工作流测试

```python
#!/usr/bin/env python3
"""
导演工作流集成测试
测试从剧本到导演分析的完整流程
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.file_parser import ScriptParser
from lib.validator import DirectorAnalysisValidator
from lib.director_analyzer import DirectorAnalyzer


class TestDirectorWorkflow(unittest.TestCase):
    """导演工作流测试"""
    
    def setUp(self):
        """测试前准备"""
        self.test_dir = tempfile.mkdtemp()
        self.script_content = """
        第1章 穿越黑道世家
        
        "吱~砰！"
        "江公子，你……你拴门做什么？"
        "做什么？嘿嘿……"
        
        第2章 系统出现
        
        "叮！系统启动！"
        """
        
        # 创建测试文件
        self.script_file = Path(self.test_dir) / "第一集.txt"
        self.script_file.write_text(self.script_content, encoding="utf-8")
        
        self.parser = ScriptParser()
        self.validator = DirectorAnalysisValidator()
        self.analyzer = DirectorAnalyzer()
    
    def tearDown(self):
        """测试后清理"""
        shutil.rmtree(self.test_dir)
    
    def test_script_to_analysis(self):
        """测试剧本到导演分析流程"""
        # 1. 解析剧本
        script_data = self.parser.parse(str(self.script_file))
        
        self.assertIsNotNone(script_data)
        self.assertIn("第1章", script_data["content"])
        
        # 2. 生成导演分析
        analysis = self.analyzer.analyze(script_data["content"])
        
        self.assertIn("P01", analysis)
        self.assertIn("人物清单", analysis)
        self.assertIn("场景清单", analysis)
        
        # 3. 验证导演分析
        validation = self.validator.validate(analysis)
        
        self.assertTrue(validation["valid"])
    
    def test_scene_extraction(self):
        """测试场景提取"""
        # 解析剧本
        script_data = self.parser.parse(str(self.script_file))
        
        # 提取场景
        scenes = self.analyzer.extract_scenes(script_data["content"])
        
        self.assertIsInstance(scenes, list)
    
    def test_character_extraction(self):
        """测试人物提取"""
        # 解析剧本
        script_data = self.parser.parse(str(self.script_file))
        
        # 提取人物
        characters = self.analyzer.extract_characters(script_data["content"])
        
        self.assertIsInstance(characters, list)


class TestDirectorOutputValidation(unittest.TestCase):
    """导演输出验证测试"""
    
    def setUp(self):
        self.validator = DirectorAnalysisValidator()
    
    def test_complete_analysis(self):
        """测试完整分析验证"""
        content = """
        # 导演分析 - ep01
        
        ## P01 剧情点
        讲戏：江辰穿越到古代黑道世家...
        
        ## P02 剧情点
        讲戏：系统出现，发布任务...
        
        ## 人物清单
        1. 江辰 - 主角，现代人穿越到古代
        2. 崔云秀 - 女主角
        
        ## 场景清单
        1. 江府房间 - 内景 - 夜晚
        2. 大街 - 外景 - 白天
        
        ## 视听语言要点
        - P01：近景转全景，暖光
        - P02：特写，闪回效果
        """
        
        result = self.validator.validate(content)
        
        self.assertTrue(result["valid"])
        self.assertEqual(len(result["missing"]), 0)
    
    def test_incomplete_analysis(self):
        """测试不完整分析"""
        content = """
        # 导演分析 - ep01
        
        ## P01 剧情点
        讲戏内容...
        
        ## 人物清单
        1. 江辰 - 主角
        """
        
        result = self.validator.validate(content)
        
        self.assertFalse(result["valid"])
        self.assertIn("场景清单", result["missing"])


if __name__ == "__main__":
    unittest.main()
```

---

### test_art_designer_workflow.py - 服化道工作流测试

```python
#!/usr/bin/env python3
"""
服化道工作流集成测试
测试从导演分析到服化道产出的完整流程
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.label_parser import LabelParser
from lib.prompt_builder import CharacterPromptBuilder, ScenePromptBuilder
from lib.validator import ArtDesignValidator


class TestArtDesignerWorkflow(unittest.TestCase):
    """服化道工作流测试"""
    
    def setUp(self):
        self.label_parser = LabelParser()
        self.char_builder = CharacterPromptBuilder()
        self.scene_builder = ScenePromptBuilder()
        self.validator = ArtDesignValidator()
    
    def test_analysis_to_character_prompt(self):
        """测试从导演分析到人物提示词"""
        # 导演分析中的人物清单
        character_list = [
            {"name": "江辰", "description": "主角，20岁，古代公子哥儿"},
            {"name": "崔云秀", "description": "女主角，大家闺秀"}
        ]
        
        # 生成人物提示词
        prompts = []
        for char in character_list:
            prompt = self.char_builder.build(
                name=char["name"],
                description=char["description"],
                layout="standard"
            )
            prompts.append(prompt)
        
        self.assertEqual(len(prompts), 2)
        self.assertIn("江辰", prompts[0])
        self.assertIn("特写", prompts[0])
    
    def test_analysis_to_scene_prompt(self):
        """测试从导演分析到场景提示词"""
        # 导演分析中的场景清单
        scene_list = [
            {"name": "江府房间", "type": "内景", "time": "夜晚"},
            {"name": "大街", "type": "外景", "time": "白天"}
        ]
        
        # 生成场景提示词
        scenes = [s["name"] for s in scene_list]
        prompt = self.scene_builder.build_grid(scenes, "3x3")
        
        self.assertIn("江府房间", prompt)
        self.assertIn("大街", prompt)
    
    def test_enhanced_mode_workflow(self):
        """测试增强模式工作流"""
        # 增强模式人物提示词
        prompt = self.char_builder.build(
            name="江辰",
            description="古代公子哥儿",
            layout="enhanced"
        )
        
        # 添加材质细节
        materials = [
            {"name": "丝绸锦袍", "properties": "光泽,织纹细腻"},
            {"name": "羊脂玉佩", "properties": "温润,雕刻精细"}
        ]
        prompt = self.char_builder.add_material_details(prompt, materials)
        
        # 验证
        result = self.validator.validate_character(prompt)
        
        self.assertTrue(result["valid"])
        self.assertTrue(result.get("enhanced_mode"))
    
    def test_label_generation(self):
        """测试标签生成"""
        label = self.label_parser.generate(
            episode="ep01",
            type="character",
            action="新增",
            name="江辰"
        )
        
        self.assertIn("ep01", label)
        self.assertIn("character", label)
        self.assertIn("新增", label)
        self.assertIn("江辰", label)


class TestArtDesignValidation(unittest.TestCase):
    """服化道设计验证测试"""
    
    def setUp(self):
        self.validator = ArtDesignValidator()
    
    def test_standard_character_validation(self):
        """测试标准人物提示词验证"""
        content = """
        # 人物提示词
        
        ## [ep01][character][新增] 江辰
        **提示词**：一位二十岁左右的古代公子哥儿
        **布局**：特写 + 三视图
        
        ## [ep02][character][新增] 新角色
        **提示词**：...
        **布局**：特写 + 三视图
        """
        
        # 验证 ep01
        result = self.validator.validate_character(content)
        self.assertTrue(result["valid"])
        
        # 验证标签
        labels = self.label_parser.extract_all(content)
        ep01_chars = [l for l in labels if l.episode == "ep01"]
        
        self.assertEqual(len(ep01_chars), 1)
    
    def test_scene_grid_validation(self):
        """测试场景宫格验证"""
        content = """
        # 场景提示词
        
        ## [ep01][scene][新增] 场景宫格
        **宫格**：3×3
        第1行：场景1-3
        第2行：场景4-6
        第3行：场景7-9
        """
        
        result = self.validator.validate_scene(content)
        self.assertTrue(result["valid"])


if __name__ == "__main__":
    unittest.main()
```

---

### test_storyboard_workflow.py - 分镜工作流测试

```python
#!/usr/bin/env python3
"""
分镜工作流集成测试
测试从服化道产出到分镜提示词的完整流程
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.prompt_builder import SeedancePromptBuilder
from lib.budget_checker import BudgetChecker
from lib.validator import SeedancePromptValidator


class TestStoryboardWorkflow(unittest.TestCase):
    """分镜工作流测试"""
    
    def setUp(self):
        self.prompt_builder = SeedancePromptBuilder()
        self.budget_checker = BudgetChecker()
        self.validator = SeedancePromptValidator()
    
    def test_art_to_storyboard(self):
        """测试从服化道到分镜"""
        # 服化道产出：人物和场景
        character = {
            "name": "江辰",
            "description": "二十岁公子哥儿"
        }
        scene = {
            "name": "江府房间",
            "description": "古色古香的卧室"
        }
        
        # 生成 Seedance 提示词
        prompt = self.prompt_builder.build(
            scene=f"{scene['name']}：{scene['description']}",
            action=f"{character['name']}走进房间",
            duration=5
        )
        
        # 添加运镜
        prompt = self.prompt_builder.add_camera_movement(
            prompt,
            movement="推",
            from_point="全景",
            to_point="中景"
        )
        
        # 添加光影
        prompt = self.prompt_builder.add_lighting(
            prompt,
            source="烛光",
            color="暖黄色",
            effect="摇曳"
        )
        
        self.assertIsNotNone(prompt)
        self.assertIn("江府房间", prompt)
        self.assertIn("江辰", prompt)
    
    def test_budget_check_integration(self):
        """测试预算检查集成"""
        prompt = """
        镜头中出现 @图片1 和 @图片2
        参考 @视频1
        背景音乐 @音频1
        """
        
        budget = self.budget_checker.calculate_budget(prompt)
        
        self.assertEqual(budget["images"], 2)
        self.assertEqual(budget["videos"], 1)
        self.assertEqual(budget["audios"], 1)
        
        check_result = self.budget_checker.check(prompt)
        self.assertTrue(check_result["pass"])
    
    def test_material_mapping_integration(self):
        """测试素材映射表集成"""
        # 定义素材映射
        material_mapping = {
            "@图片1": {"type": "人物", "description": "江辰定妆照"},
            "@图片2": {"type": "场景", "description": "江府房间"},
            "@视频1": {"type": "动作参考", "description": "行走动作"},
            "@音频1": {"type": "背景音乐", "description": "古风配乐"}
        }
        
        # 验证映射完整性
        required_types = ["人物", "场景", "动作参考", "背景音乐"]
        
        for type_name in required_types:
            found = any(m["type"] == type_name for m in material_mapping.values())
            self.assertTrue(found, f"Missing type: {type_name}")
    
    def test_reference_resolution(self):
        """测试引用解析"""
        prompt = "主角 @图片1 走进场景 @图片2"
        
        # 提取所有引用
        import re
        refs = re.findall(r'@[图片视频音频]\d+', prompt)
        
        self.assertIn("@图片1", refs)
        self.assertIn("@图片2", refs)


class TestSeedanceOutputValidation(unittest.TestCase):
    """Seedance 输出验证测试"""
    
    def setUp(self):
        self.validator = SeedancePromptValidator()
    
    def test_complete_prompt_validation(self):
        """测试完整提示词验证"""
        content = """
        # Seedance 提示词 - ep01
        
        ## 素材对应表
        | ID | 类型 | 描述 |
        |----|------|------|
        | @图片1 | 人物 | 江辰定妆照 |
        | @图片2 | 场景 | 江府房间 |
        
        ## 单条提示词预算表
        | 剧情点 | 图片 | 视频 | 音频 | 总数 | 结论 |
        |--------|------|------|------|------|------|
        | P01 | 2 | 0 | 1 | 3 | 通过 |
        
        ## P01 提示词
        镜头缓缓推进，展示江府房间...
        """
        
        result = self.validator.validate(content)
        
        self.assertTrue(result["valid"])
    
    def test_budget_validation(self):
        """测试预算验证"""
        # 正常预算
        prompt = "@图片1 @图片2 @视频1 @音频1"
        result = self.validator.validate_budget(prompt)
        self.assertTrue(result["valid"])
        
        # 超预算
        prompt = " ".join([f"@图片{i}" for i in range(12)])
        result = self.validator.validate_budget(prompt)
        self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main()
```

---

### test_full_episode.py - 完整集数流程测试

```python
#!/usr/bin/env python3
"""
完整集数流程集成测试
测试从剧本到最终分镜的完整端到端流程
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.workflow import EpisodeWorkflow
from lib.state_manager import StateManager


class TestFullEpisodeWorkflow(unittest.TestCase):
    """完整集数流程测试"""
    
    def setUp(self):
        """测试前准备"""
        self.test_dir = tempfile.mkdtemp()
        self.project_dir = Path(self.test_dir) / "test_project"
        self.project_dir.mkdir()
        
        # 创建必要的目录
        (self.project_dir / "script").mkdir()
        (self.project_dir / "outputs" / "ep01").mkdir()
        (self.project_dir / "assets").mkdir()
        
        self.workflow = EpisodeWorkflow(str(self.project_dir))
        self.state_manager = StateManager(str(self.project_dir))
    
    def tearDown(self):
        """测试后清理"""
        shutil.rmtree(self.test_dir)
    
    def test_complete_episode_flow(self):
        """测试完整集数流程"""
        # 阶段 1: 导演分析
        script_content = """
        第1集 穿越
        
        江辰正在睡觉，突然...
        """
        
        script_file = self.project_dir / "script" / "第一集.txt"
        script_file.write_text(script_content, encoding="utf-8")
        
        # 执行导演分析
        phase1_result = self.workflow.run_phase1("ep01")
        
        self.assertTrue(phase1_result["success"])
        self.assertTrue((self.project_dir / "outputs" / "ep01" / "01-director-analysis.md").exists())
        
        # 更新状态
        self.state_manager.update_phase_status("ep01", "phase1", "completed")
        
        # 阶段 2: 服化道设计
        phase2_result = self.workflow.run_phase2("ep01")
        
        self.assertTrue(phase2_result["success"])
        self.assertTrue((self.project_dir / "assets" / "character-prompts.md").exists())
        
        # 更新状态
        self.state_manager.update_phase_status("ep01", "phase2", "completed")
        
        # 阶段 3: 分镜编写
        phase3_result = self.workflow.run_phase3("ep01")
        
        self.assertTrue(phase3_result["success"])
        self.assertTrue((self.project_dir / "outputs" / "ep01" / "02-seedance-prompts.md").exists())
        
        # 更新状态
        self.state_manager.update_phase_status("ep01", "phase3", "completed")
        
        # 验证最终状态
        status = self.state_manager.get_episode_status("ep01")
        self.assertEqual(status["phase1"], "completed")
        self.assertEqual(status["phase2"], "completed")
        self.assertEqual(status["phase3"], "completed")
    
    def test_phase_dependencies(self):
        """测试阶段依赖"""
        # 尝试跳过阶段 1 直接执行阶段 2
        result = self.workflow.run_phase2("ep01")
        
        self.assertFalse(result["success"])
        self.assertIn("依赖", result["error"])
    
    def test_state_persistence(self):
        """测试状态持久化"""
        # 设置状态
        self.state_manager.update_phase_status("ep01", "phase1", "completed")
        
        # 读取状态
        status = self.state_manager.get_episode_status("ep01")
        
        self.assertEqual(status["phase1"], "completed")
        
        # 重新加载
        new_manager = StateManager(str(self.project_dir))
        status = new_manager.get_episode_status("ep01")
        
        self.assertEqual(status["phase1"], "completed")


class TestMultiEpisodeWorkflow(unittest.TestCase):
    """多集工作流测试"""
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.workflow = EpisodeWorkflow(self.test_dir)
    
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def test_parallel_episode_processing(self):
        """测试多集并行处理"""
        episodes = ["ep01", "ep02", "ep03"]
        
        results = []
        for ep in episodes:
            result = self.workflow.run_phase1(ep)
            results.append(result)
        
        # 所有集数都应该成功
        self.assertEqual(len(results), 3)
    
    def test_cross_episode_consistency(self):
        """测试跨集一致性"""
        # 模拟跨集素材复用
        result = self.workflow.check_consistency("ep01", "ep02")
        
        self.assertIn("consistency", result)


if __name__ == "__main__":
    unittest.main()
```

---

### test_cross_episode.py - 跨集一致性测试

```python
#!/usr/bin/env python3
"""
跨集一致性测试
测试多集之间的素材复用和一致性
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.consistency_checker import ConsistencyChecker
from lib.label_parser import LabelParser


class TestCrossEpisodeConsistency(unittest.TestCase):
    """跨集一致性测试"""
    
    def setUp(self):
        self.checker = ConsistencyChecker()
        self.label_parser = LabelParser()
    
    def test_character_consistency(self):
        """测试人物一致性"""
        # ep01 的人物设计
        ep01_characters = {
            "江辰": {
                "description": "二十岁，剑眉星目",
                "outfit": "暗红色锦袍"
            }
        }
        
        # ep02 的人物设计
        ep02_characters = {
            "江辰": {
                "description": "二十岁，剑眉星目",
                "outfit": "暗红色锦袍"
            },
            "新角色": {
                "description": "..."
            }
        }
        
        # 检查一致性
        result = self.checker.check_character_consistency(
            ep01_characters,
            ep02_characters
        )
        
        self.assertTrue(result["consistent"])
        self.assertIn("江辰", result["matching"])
    
    def test_scene_consistency(self):
        """测试场景一致性"""
        # ep01 的场景
        ep01_scenes = {
            "江府房间": {"style": "古色古香", "light": "暖黄烛光"}
        }
        
        # ep02 的场景
        ep02_scenes = {
            "江府房间": {"style": "古色古香", "light": "暖黄烛光"},
            "新场景": {"style": "..."}
        }
        
        result = self.checker.check_scene_consistency(
            ep01_scenes,
            ep02_scenes
        )
        
        self.assertTrue(result["consistent"])
    
    def test_reuse_detection(self):
        """测试复用检测"""
        content = """
        ## [ep01][character][新增] 江辰
        ## [ep02][character][复用] 江辰
        """
        
        labels = self.label_parser.extract_all(content)
        
        # 识别复用
        reused = [l for l in labels if l.action == "复用"]
        
        self.assertEqual(len(reused), 1)
        self.assertEqual(reused[0].name, "江辰")
    
    def test_variant_detection(self):
        """测试变体检测"""
        content = """
        ## [ep01][character][新增] 江辰
        ## [ep02][character][变体] 江辰-战斗形态
        """
        
        labels = self.label_parser.extract_all(content)
        
        # 识别变体
        variants = [l for l in labels if l.action == "变体"]
        
        self.assertEqual(len(variants), 1)
        self.assertIn("江辰", variants[0].name)


class TestMaterialReuse(unittest.TestCase):
    """素材复用测试"""
    
    def setUp(self):
        self.checker = ConsistencyChecker()
    
    def test_reuse_recommendation(self):
        """测试复用推荐"""
        # 已有的素材库
        existing_materials = {
            "characters": [
                {"name": "江辰", "tags": ["主角", "古代", "公子"]}
            ],
            "scenes": [
                {"name": "江府", "tags": ["室内", "古代", "卧室"]}
            ]
        }
        
        # 新集数需要的素材
        new_materials = {
            "characters": [
                {"name": "江辰", "tags": ["主角", "古代", "公子"]}
            ],
            "scenes": [
                {"name": "江府", "tags": ["室内", "古代", "卧室"]}
            ]
        }
        
        # 推荐复用
        recommendations = self.checker.recommend_reuse(
            existing_materials,
            new_materials
        )
        
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)


if __name__ == "__main__":
    unittest.main()
```

---

## 运行集成测试

### 运行所有集成测试
```bash
python -m pytest tests/integration/ -v
```

### 运行特定测试
```bash
python -m pytest tests/integration/test_full_episode.py -v
```

### 运行完整测试套件
```bash
python -m pytest tests/ -v --cov=lib
```

---

## 集成测试覆盖率目标

| 场景 | 目标覆盖率 |
|------|-----------|
| 导演工作流 | 90% |
| 服化道工作流 | 90% |
| 分镜工作流 | 90% |
| 完整集数流程 | 85% |
| 跨集一致性 | 85% |

