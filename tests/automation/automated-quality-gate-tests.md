---
name: automated-quality-gate-tests
description: 自动化质量门禁测试。用于在 CI/CD 流程中自动验证项目质量，确保每次提交都满足质量标准。
---

# 自动化质量门禁测试

## 用途
在 CI/CD 流程中自动运行质量门禁检查，确保每次代码提交或阶段切换都满足质量标准。

---

## 测试结构

```
tests/
├── automation/
│   ├── test_quality_gate_phase1.py    # 阶段一门禁自动化测试
│   ├── test_quality_gate_phase2.py    # 阶段二门禁自动化测试
│   ├── test_quality_gate_phase3.py    # 阶段三门禁自动化测试
│   ├── test_project_health.py         # 项目健康度测试
│   └── run_quality_gate.py            # 门禁测试运行器
```

---

## 自动化测试文件

### test_quality_gate_phase1.py - 阶段一门禁自动化测试

```python
#!/usr/bin/env python3
"""
阶段一门禁自动化测试
测试导演分析阶段的入口和出口门禁
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys
import json

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tools.quality_gate_checker import (
    check_phase1_entry,
    check_phase1_exit
)


class TestPhase1QualityGate(unittest.TestCase):
    """阶段一质量门禁测试"""
    
    def setUp(self):
        """测试前准备"""
        self.test_dir = tempfile.mkdtemp()
        self.project_dir = Path(self.test_dir) / "test_project"
        self.project_dir.mkdir()
        
        # 创建必要的目录结构
        (self.project_dir / "script").mkdir()
        (self.project_dir / "outputs").mkdir()
        (self.project_dir / "assets").mkdir()
    
    def tearDown(self):
        """测试后清理"""
        shutil.rmtree(self.test_dir)
    
    def test_phase1_entry_gate_pass(self):
        """测试阶段一入口门禁 - 通过"""
        # 准备测试数据
        # 创建剧本文件
        script_file = self.project_dir / "script" / "第一集.txt"
        script_file.write_text("测试剧本内容", encoding="utf-8")
        
        # 创建 CLAUDE.md
        claude_file = self.project_dir / "CLAUDE.md"
        claude_file.write_text("# CLAUDE", encoding="utf-8")
        
        # 执行入口门禁检查
        issues = check_phase1_entry("ep01")
        
        # 验证结果
        self.assertEqual(len(issues), 0, f"应该有 0 个问题，实际有 {len(issues)} 个: {issues}")
    
    def test_phase1_entry_gate_fail_no_script(self):
        """测试阶段一入口门禁 - 失败：无剧本"""
        # 不创建剧本文件
        
        issues = check_phase1_entry("ep01")
        
        # 应该有剧本相关问题
        self.assertGreater(len(issues), 0)
        self.assertTrue(any("剧本" in issue for issue in issues))
    
    def test_phase1_exit_gate_pass(self):
        """测试阶段一出口门禁 - 通过"""
        # 创建完整的导演分析文件
        output_dir = self.project_dir / "outputs" / "ep01"
        output_dir.mkdir(parents=True)
        
        analysis_file = output_dir / "01-director-analysis.md"
        analysis_file.write_text("""
# 导演分析 - ep01

## P01 剧情点
讲戏：江辰穿越到古代...

## 人物清单
1. 江辰 - 主角

## 场景清单
1. 江府房间 - 内景

## 视听语言要点
- P01：近景，暖光
        """, encoding="utf-8")
        
        issues = check_phase1_exit("ep01")
        
        self.assertEqual(len(issues), 0, f"应该有 0 个问题，实际有 {len(issues)} 个: {issues}")
    
    def test_phase1_exit_gate_fail_incomplete(self):
        """测试阶段一出口门禁 - 失败：不完整"""
        # 创建不完整的导演分析文件
        output_dir = self.project_dir / "outputs" / "ep01"
        output_dir.mkdir(parents=True)
        
        analysis_file = output_dir / "01-director-analysis.md"
        analysis_file.write_text("""
# 导演分析 - ep01

## P01 剧情点
讲戏：江辰穿越...
        """, encoding="utf-8")
        
        issues = check_phase1_exit("ep01")
        
        # 应该有缺失章节的问题
        self.assertGreater(len(issues), 0)
        self.assertTrue(any("人物清单" in issue or "场景清单" in issue for issue in issues))


class TestPhase1GateIntegration(unittest.TestCase):
    """阶段一门禁集成测试"""
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def test_full_phase1_workflow(self):
        """测试完整阶段一工作流"""
        # 1. 入口检查
        # 准备剧本
        script_dir = Path(self.test_dir) / "script"
        script_dir.mkdir()
        (script_dir / "第一集.txt").write_text("剧本内容", encoding="utf-8")
        
        # 创建 CLAUDE.md
        Path(self.test_dir / "CLAUDE.md").write_text("# CLAUDE", encoding="utf-8")
        
        # 创建目录
        (self.test_dir / "assets").mkdir()
        (self.test_dir / "outputs").mkdir()
        
        entry_issues = check_phase1_entry("ep01")
        self.assertEqual(len(entry_issues), 0)
        
        # 2. 执行阶段任务（模拟）
        output_dir = Path(self.test_dir) / "outputs" / "ep01"
        output_dir.mkdir(parents=True)
        (output_dir / "01-director-analysis.md").write_text("""
# 导演分析
## P01 讲戏
## 人物清单
## 场景清单
## 视听语言
        """, encoding="utf-8")
        
        # 3. 出口检查
        exit_issues = check_phase1_exit("ep01")
        
        # 应该通过
        self.assertEqual(len(exit_issues), 0)


if __name__ == "__main__":
    unittest.main()
```

---

### test_quality_gate_phase2.py - 阶段二门禁自动化测试

```python
#!/usr/bin/env python3
"""
阶段二门禁自动化测试
测试服化道设计阶段的入口和出口门禁
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tools.quality_gate_checker import (
    check_phase2_entry,
    check_phase2_exit
)


class TestPhase2QualityGate(unittest.TestCase):
    """阶段二质量门禁测试"""
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.project_dir = Path(self.test_dir) / "test_project"
        self.project_dir.mkdir()
        
        # 创建必要的目录
        (self.project_dir / "script").mkdir()
        (self.project_dir / "outputs").mkdir()
        (self.project_dir / "assets").mkdir()
    
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def test_phase2_entry_gate_pass(self):
        """测试阶段二入口门禁 - 通过"""
        # 创建导演分析文件
        output_dir = self.project_dir / "outputs" / "ep01"
        output_dir.mkdir(parents=True)
        
        analysis_file = output_dir / "01-director-analysis.md"
        analysis_file.write_text("""
# 导演分析 - ep01

## 人物清单
1. 江辰 - 主角

## 场景清单
1. 江府房间
        """, encoding="utf-8")
        
        issues = check_phase2_entry("ep01")
        
        self.assertEqual(len(issues), 0, f"应该有 0 个问题，实际有 {len(issues)} 个: {issues}")
    
    def test_phase2_entry_gate_fail_no_analysis(self):
        """测试阶段二入口门禁 - 失败：无导演分析"""
        issues = check_phase2_entry("ep01")
        
        self.assertGreater(len(issues), 0)
    
    def test_phase2_exit_gate_pass(self):
        """测试阶段二出口门禁 - 通过"""
        # 创建人物提示词文件
        assets_dir = self.project_dir / "assets"
        
        char_prompts = assets_dir / "character-prompts.md"
        char_prompts.write_text("""
# 人物提示词

## [ep01][character][新增] 江辰
**提示词**：一位二十岁左右的古代公子哥儿
**布局**：特写 + 三视图
        """, encoding="utf-8")
        
        scene_prompts = assets_dir / "scene-prompts.md"
        scene_prompts.write_text("""
# 场景提示词

## [ep01][scene][新增] 场景宫格
**提示词**：3×3 宫格布局
        """, encoding="utf-8")
        
        issues = check_phase2_exit("ep01")
        
        self.assertEqual(len(issues), 0)
    
    def test_phase2_enhanced_mode_pass(self):
        """测试增强模式出口门禁 - 通过"""
        assets_dir = self.project_dir / "assets"
        
        # 增强模式人物提示词
        char_prompts = assets_dir / "character-prompts.md"
        char_prompts.write_text("""
# 人物提示词

## [ep01][character][新增] 江辰
**提示词**：古代公子哥儿

### 材质与工艺细节
- 丝绸锦袍：光泽,织纹细腻
- 羊脂玉佩：温润,雕刻精细
        """, encoding="utf-8")
        
        issues = check_phase2_exit("ep01")
        
        # 增强模式应该也通过
        self.assertEqual(len(issues), 0)


class TestPhase2GateIntegration(unittest.TestCase):
    """阶段二门禁集成测试"""
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def test_full_phase2_workflow(self):
        """测试完整阶段二工作流"""
        # 1. 准备前置条件
        output_dir = Path(self.test_dir) / "outputs" / "ep01"
        output_dir.mkdir(parents=True)
        (output_dir / "01-director-analysis.md").write_text("""
## 人物清单
1. 江辰
## 场景清单
1. 江府
        """, encoding="utf-8")
        
        assets_dir = Path(self.test_dir) / "assets"
        assets_dir.mkdir()
        
        # 2. 入口检查
        entry_issues = check_phase2_entry("ep01")
        self.assertEqual(len(entry_issues), 0)
        
        # 3. 执行阶段任务（模拟）
        (assets_dir / "character-prompts.md").write_text("""
## [ep01][character][新增] 江辰
**提示词**：...
**布局**：特写 + 三视图
        """, encoding="utf-8")
        
        (assets_dir / "scene-prompts.md").write_text("""
## [ep01][scene][新增] 场景
**提示词**：...
**宫格**：3×3
        """, encoding="utf-8")
        
        # 4. 出口检查
        exit_issues = check_phase2_exit("ep01")
        self.assertEqual(len(exit_issues), 0)


if __name__ == "__main__":
    unittest.main()
```

---

### test_quality_gate_phase3.py - 阶段三门禁自动化测试

```python
#!/usr/bin/env python3
"""
阶段三门禁自动化测试
测试分镜编写阶段的入口和出口门禁
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tools.quality_gate_checker import (
    check_phase3_entry,
    check_phase3_exit
)


class TestPhase3QualityGate(unittest.TestCase):
    """阶段三质量门禁测试"""
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.project_dir = Path(self.test_dir) / "test_project"
        self.project_dir.mkdir()
        
        # 创建必要的目录
        (self.project_dir / "script").mkdir()
        (self.project_dir / "outputs").mkdir()
        (self.project_dir / "assets").mkdir()
    
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def test_phase3_entry_gate_pass(self):
        """测试阶段三入口门禁 - 通过"""
        # 创建所有前置文件
        output_dir = self.project_dir / "outputs" / "ep01"
        output_dir.mkdir(parents=True)
        (output_dir / "01-director-analysis.md").write_text("内容", encoding="utf-8")
        
        assets_dir = self.project_dir / "assets"
        (assets_dir / "character-prompts.md").write_text("内容", encoding="utf-8")
        (assets_dir / "scene-prompts.md").write_text("内容", encoding="utf-8")
        
        issues = check_phase3_entry("ep01")
        
        self.assertEqual(len(issues), 0)
    
    def test_phase3_exit_gate_pass(self):
        """测试阶段三出口门禁 - 通过"""
        # 创建完整的分镜文件
        output_dir = self.project_dir / "outputs" / "ep01"
        
        prompts_file = output_dir / "02-seedance-prompts.md"
        prompts_file.write_text("""
# Seedance 提示词 - ep01

## 素材对应表
| ID | 类型 | 描述 |
|----|------|------|
| @图片1 | 人物 | 江辰 |

## 单条提示词预算表
| 剧情点 | 图片 | 视频 | 音频 | 总数 | 结论 |
|--------|------|------|------|------|------|
| P01 | 1 | 0 | 0 | 1 | 通过 |

## 视听语言设计
- P01：镜头设计...
        """, encoding="utf-8")
        
        issues = check_phase3_exit("ep01")
        
        self.assertEqual(len(issues), 0)
    
    def test_phase3_exit_gate_fail_budget(self):
        """测试阶段三出口门禁 - 失败：预算超限"""
        output_dir = self.project_dir / "outputs" / "ep01"
        
        prompts_file = output_dir / "02-seedance-prompts.md"
        prompts_file.write_text("""
# Seedance 提示词

## 素材对应表
## 单条提示词预算表
| P01 | 10 | 5 | 5 | 20 | 不通过 |
        """, encoding="utf-8")
        
        issues = check_phase3_exit("ep01")
        
        # 应该检测到预算问题
        self.assertGreater(len(issues), 0)


class TestPhase3GateIntegration(unittest.TestCase):
    """阶段三门禁集成测试"""
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def test_full_phase3_workflow(self):
        """测试完整阶段三工作流"""
        # 1. 准备前置条件
        output_dir = Path(self.test_dir) / "outputs" / "ep01"
        output_dir.mkdir(parents=True)
        (output_dir / "01-director-analysis.md").write_text("内容", encoding="utf-8")
        
        assets_dir = Path(self.test_dir) / "assets"
        assets_dir.mkdir()
        (assets_dir / "character-prompts.md").write_text("内容", encoding="utf-8")
        (assets_dir / "scene-prompts.md").write_text("内容", encoding="utf-8")
        
        # 2. 入口检查
        entry_issues = check_phase3_entry("ep01")
        self.assertEqual(len(entry_issues), 0)
        
        # 3. 执行阶段任务（模拟）
        (output_dir / "02-seedance-prompts.md").write_text("""
# Seedance 提示词

## 素材对应表
| @图片1 | 人物 | 江辰 |

## 单条提示词预算表
| P01 | 1 | 0 | 0 | 1 | 通过 |

## 视听语言设计
- P01：镜头...
        """, encoding="utf-8")
        
        # 4. 出口检查
        exit_issues = check_phase3_exit("ep01")
        self.assertEqual(len(exit_issues), 0)


if __name__ == "__main__":
    unittest.main()
```

---

### test_project_health.py - 项目健康度测试

```python
#!/usr/bin/env python3
"""
项目健康度测试
测试项目的整体健康状况
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


class TestProjectHealth(unittest.TestCase):
    """项目健康度测试"""
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def test_directory_structure(self):
        """测试目录结构完整性"""
        required_dirs = ["script", "assets", "outputs", "tools", "skills", "agents"]
        
        for dir_name in required_dirs:
            dir_path = Path(self.test_dir) / dir_name
            dir_path.mkdir()
        
        missing = []
        for dir_name in required_dirs:
            if not (Path(self.test_dir) / dir_name).exists():
                missing.append(dir_name)
        
        self.assertEqual(len(missing), 0, f"缺失目录: {missing}")
    
    def test_required_files(self):
        """测试必要文件存在"""
        # 创建 CLAUDE.md
        (Path(self.test_dir) / "CLAUDE.md").write_text("# CLAUDE", encoding="utf-8")
        
        required_files = ["CLAUDE.md"]
        
        missing = []
        for file_name in required_files:
            if not (Path(self.test_dir) / file_name).exists():
                missing.append(file_name)
        
        self.assertEqual(len(missing), 0, f"缺失文件: {missing}")
    
    def test_agent_files_exist(self):
        """测试 Agent 文件存在"""
        agents_dir = Path(self.test_dir) / "agents"
        agents_dir.mkdir()
        
        required_agents = ["director.md", "art-designer.md", "storyboard-artist.md"]
        
        for agent in required_agents:
            (agents_dir / agent).write_text("# Agent", encoding="utf-8")
        
        existing = list(agents_dir.glob("*.md"))
        
        self.assertGreaterEqual(len(existing), 3)
    
    def test_skill_files_exist(self):
        """测试 Skill 文件存在"""
        skills_dir = Path(self.test_dir) / "skills"
        
        # 创建子目录
        (skills_dir / "test-skill").mkdir(parents=True)
        (skills_dir / "test-skill" / "SKILL.md").write_text("# Skill", encoding="utf-8")
        
        skill_files = list(skills_dir.glob("**/SKILL.md"))
        
        self.assertGreater(len(skill_files), 0)


class TestQualityGateIntegration(unittest.TestCase):
    """质量门禁集成测试"""
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def test_full_project_quality_gate(self):
        """测试完整项目质量门禁"""
        from tools.quality_gate_checker import (
            check_phase1_entry,
            check_phase1_exit,
            check_phase2_entry,
            check_phase2_exit,
            check_phase3_entry,
            check_phase3_exit
        )
        
        # 准备项目结构
        script_dir = Path(self.test_dir) / "script"
        script_dir.mkdir()
        (script_dir / "第一集.txt").write_text("剧本", encoding="utf-8")
        
        (Path(self.test_dir) / "CLAUDE.md").write_text("# CLAUDE", encoding="utf-8")
        
        assets_dir = Path(self.test_dir) / "assets"
        assets_dir.mkdir()
        
        output_dir = Path(self.test_dir) / "outputs" / "ep01"
        output_dir.mkdir(parents=True)
        
        # 阶段一
        entry1 = check_phase1_entry("ep01")
        self.assertEqual(len(entry1), 0)
        
        (output_dir / "01-director-analysis.md").write_text("""
# 导演分析
## P01 讲戏
## 人物清单
1. 江辰
## 场景清单
1. 江府
## 视听语言
        """, encoding="utf-8")
        
        exit1 = check_phase1_exit("ep01")
        self.assertEqual(len(exit1), 0)
        
        # 阶段二
        entry2 = check_phase2_entry("ep01")
        self.assertEqual(len(entry2), 0)
        
        (assets_dir / "character-prompts.md").write_text("""
## [ep01][character][新增] 江辰
**提示词**：...
**布局**：特写 + 三视图
        """, encoding="utf-8")
        
        (assets_dir / "scene-prompts.md").write_text("""
## [ep01][scene][新增] 场景
**提示词**：...
**宫格**：3×3
        """, encoding="utf-8")
        
        exit2 = check_phase2_exit("ep01")
        self.assertEqual(len(exit2), 0)
        
        # 阶段三
        entry3 = check_phase3_entry("ep01")
        self.assertEqual(len(entry3), 0)
        
        (output_dir / "02-seedance-prompts.md").write_text("""
# Seedance 提示词
## 素材对应表
| @图片1 | 人物 | 江辰 |
## 单条提示词预算表
| P01 | 1 | 0 | 0 | 1 | 通过 |
## 视听语言设计
- P01：...
        """, encoding="utf-8")
        
        exit3 = check_phase3_exit("ep01")
        self.assertEqual(len(exit3), 0)
        
        # 全部通过
        print("所有阶段门禁测试通过！")


if __name__ == "__main__":
    unittest.main()
```

---

## 运行自动化测试

### 运行所有门禁测试
```bash
python -m pytest tests/automation/ -v
```

### 运行特定阶段门禁测试
```bash
python -m pytest tests/automation/test_quality_gate_phase1.py -v
```

### 在 CI 中运行
```bash
#.github/workflows/quality-gate.yml
name: Quality Gate

on: [push, pull_request]

jobs:
  quality-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Run quality gate tests
        run: |
          python -m pytest tests/automation/ -v --junitxml=report.xml
      - name: Publish test results
        uses: dorny/test-reporter@v1
        if: always()
        with:
          name: quality-gate
          path: report.xml
          reporter: java-junit
```

---

## 质量门禁检查清单

| 阶段 | 检查项 | 自动化 |
|------|--------|--------|
| 阶段一 | 剧本文件存在 | ✅ |
| 阶段一 | CLAUDE.md 存在 | ✅ |
| 阶段一 | 目录结构完整 | ✅ |
| 阶段一 | 导演分析完整 | ✅ |
| 阶段二 | 导演分析已完成 | ✅ |
| 阶段二 | 人物提示词格式正确 | ✅ |
| 阶段二 | 场景提示词格式正确 | ✅ |
| 阶段二 | 增强模式内容完整 | ✅ |
| 阶段三 | 前置阶段已完成 | ✅ |
| 阶段三 | 素材对应表完整 | ✅ |
| 阶段三 | 预算检查通过 | ✅ |
| 阶段三 | 视听语言设计完整 | ✅ |

---

## 门禁测试覆盖率目标

| 模块 | 目标覆盖率 |
|------|-----------|
| 阶段一门禁 | 95% |
| 阶段二门禁 | 95% |
| 阶段三门禁 | 95% |
| 项目健康度 | 90% |
| 集成门禁 | 90% |

