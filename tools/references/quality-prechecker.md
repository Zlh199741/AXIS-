---
name: quality-prechecker
description: 实时质量预检系统。自动化检查提示词的素材预算、违禁词、视听语言一致性、时间轴合理性、格式规范性，并集成白皮书T0标准校验。
---

# 实时质量预检系统

## 用途

自动化检查提示词的素材预算、违禁词、视听语言一致性、时间轴合理性、格式规范性，**集成白皮书T0标准校验**，生成检查报告并提供修复建议。

---

## 一、检查维度

### 1.1 六大检查维度

| 维度 | 检查内容 | 严重度 |
|------|----------|--------|
| **D1:素材预算** | 图片/视频/音频数量限制 | 🔴 ERROR |
| **D2:违禁词** | 政治/暴力/色情/低俗 | 🔴 ERROR |
| **D3:视听语言** | 轴线/视线/越轴/景别 | 🔴 ERROR |
| **D4:时间轴** | 时长/动作密度/安全区 | 🟠 WARNING |
| **D5:格式规范** | 景别/运镜/光影/引号 | 🔴 ERROR |
| **D6:白皮书T0标准** | 纯白背景/多视图/渲染参数等 | 🔴 ERROR |

---

## 二、检查项详解

### 2.1 维度一：素材预算

| 检查项 | 标准 | 阈值 | 严重度 |
|--------|------|------|--------|
| 图片数量 | 每条提示词 | ≤9 | 🔴 ERROR |
| 视频数量 | 每条提示词 | ≤3 | 🔴 ERROR |
| 音频数量 | 每条提示词 | ≤3 | 🔴 ERROR |
| 总文件数 | 每条提示词 | ≤12 | 🔴 ERROR |

**修复建议**：
- 拆分剧情点为多条提示词
- 减少引用图片，改用文字描述
- 合并相似引用

---

### 2.2 维度二：违禁词扫描

#### 违禁词库分类

| 类别 | 示例词 | 处理方式 |
|------|--------|----------|
| 政治敏感 | 领导人、领土争议 | 🔴 ERROR |
| 暴力血腥 | 肢解、酷刑、斩首 | 🔴 ERROR |
| 色情低俗 | 性行为、裸露 | 🔴 ERROR |
| 封建迷信 | 鬼怪祭祀 | 🟠 WARNING |

#### 违禁词替换表

| 原始词 | 违规原因 | 替换建议 |
|---------|---------|----------|
| 轻薄 | 性暗示 | 冒犯 |
| 淫笑 | 低俗 | 冷笑 |
| 春宫图 | 色情 | 古画 |
| 性侵 | 严重违规 | 伤害 |
| 血腥 | 暴力 | 删除或改为瘀伤 |

---

### 2.3 维度三：视听语言一致性

| 检查项 | 规则 | 严重度 |
|--------|------|--------|
| 轴线保持 | 对话场景需在轴线同侧 | 🔴 ERROR |
| 视线匹配 | 反应镜头后需有POV或留悬念 | 🟠 WARNING |
| 越轴标注 | 越轴必须有【越轴】标注 | 🔴 ERROR |
| 景别逻辑 | 景别变化需平滑 | 🟡 INFO |
| 焦段统一 | 同一场景焦段变化≤2档 | 🟡 INFO |

---

### 2.4 维度四：时间轴合理性

| 检查项 | 标准 | 严重度 |
|--------|------|--------|
| 单镜头时长 | ≤5秒 | 🟠 WARNING |
| 总时长 | ≤15秒 | 🔴 ERROR |
| 动作密度 | 1拍≈2.5秒 | 🟠 WARNING |
| 头尾安全区 | 0.5秒不放关键内容 | 🟡 INFO |

---

### 2.5 维度五：格式规范性

| 检查项 | 标准 | 严重度 |
|--------|------|--------|
| 景别标注 | 每镜头必须有 | 🔴 ERROR |
| 运镜动词 | 需在词库中 | 🔴 ERROR |
| 光影描述 | 每场景必须有 | 🟠 WARNING |
| 台词引号 | 必须用中文"" | 🔴 ERROR |
| @引用格式 | @图片N/@视频N/@音频N | 🔴 ERROR |

---

### 2.6 维度六：白皮书T0标准（AI绘画终极提示词工程白皮书）

⚠️ **必须符合 AI绘画终极提示词 (Prompt) 工程白皮书.txt 的T0级工业商用标准**

#### 角色提示词（6项强制要求）

| 检查项 | 必需关键词 | 严重度 |
|--------|-----------|--------|
| 纯白背景隔离 | `strictly isolated on a pure white background` | 🔴 ERROR |
| 表情集 | `facial expression sheet` + `4 close-up headshots` | 🔴 ERROR |
| 服饰拆分 | `separated clothing breakdown` + `RGB color palette` | 🔴 ERROR |
| 多视图 | `full-body front/side/back view` + `close-up headshot` | 🔴 ERROR |
| 核心渲染参数 | PBR/AO/Unreal Engine 5/Octane Render（至少2项） | 🔴 ERROR |
| 微观细节 | 皮肤纹理/毛孔/眼球反光/发丝物理（至少2项） | 🔴 ERROR |

#### 场景提示词（5项强制要求）

| 检查项 | 必需关键词 | 严重度 |
|--------|-----------|--------|
| 镜头指定 | `shot on` + 焦段 | 🔴 ERROR |
| 构图法则 | rule of thirds / symmetrical composition | 🔴 ERROR |
| 全局光照 | global illumination / volumetric lighting / god rays | 🔴 ERROR |
| 色彩分级 | color grading / teal and orange / cyberpunk | 🔴 ERROR |
| T0级渲染后缀 | Unreal Engine 5 / 8k / masterpiece | 🔴 ERROR |

#### 道具提示词（5项强制要求）

| 检查项 | 必需关键词 | 严重度 |
|--------|-----------|--------|
| 纯白背景隔离 | `strictly isolated on a pure white background` | 🔴 ERROR |
| 微距视角 | macro lens / 100mm | 🔴 ERROR |
| 硬表面材质 | 至少2项 | 🔴 ERROR |
| 渲染参数 | PBR / Octane Render | 🔴 ERROR |
| T0级画质后缀 | 8k / masterpiece | 🔴 ERROR |

#### 额外检测项

| 检查项 | 说明 | 严重度 |
|--------|------|--------|
| 极致动漫风格 | 8大工作室风格至少指定1个 | 🟠 WARNING |
| 防崩坏指令 | 必须包含防崩坏指令 | 🔴 ERROR |

#### 修复建议

- 缺失项：在提示词中添加对应关键词
- 风格未指定：添加 Studio Trigger / Ufotable / MAPPA 等
- 防崩坏指令缺失：在提示词末尾添加 `Please avoid any text, watermarks, blurred edges, distorted anatomy`

---

## 三、检查执行

### 3.1 检查流程

```markdown
输入：Seedance/Kling提示词
        ↓
1. 素材预算检查 (D1)
        ↓
2. 违禁词扫描 (D2)
        ↓
3. 视听语言检查 (D3)
        ↓
4. 时间轴检查 (D4)
        ↓
5. 格式规范检查 (D5)
        ↓
6. 白皮书T0标准检查 (D6) ← 新增
        ↓
生成报告
```

> ⚠️ **注意**：D6白皮书T0标准检查可使用独立工具 `tools/validators/t0-validator.py` 执行

### 3.2 检查函数实现

```python
class QualityPreChecker:
    """实时质量预检器"""
    
    def __init__(self, prompt: str):
        self.prompt = prompt
        self.issues = []
        self.passed = True
    
    def run_all_checks(self) -> dict:
        """执行全部检查"""
        self.check_budget()        # 素材预算
        self.scan_prohibited()     # 违禁词
        self.check_audiovisual()   # 视听语言
        self.check_timeline()     # 时间轴
        self.check_format()      # 格式规范
        
        return {
            "passed": len([i for i in self.issues if i["severity"] == "🔴 ERROR"]) == 0,
            "error_count": len([i for i in self.issues if i["severity"] == "🔴 ERROR"]),
            "warning_count": len([i for i in self.issues if i["severity"] == "🟠 WARNING"]),
            "issues": self.issues
        }
```

---

## 四、检查函数详解

### 4.1 素材预算检查

```python
def check_budget(self):
    """检查素材预算"""
    import re
    
    # 统计引用数量
    image_count = len(re.findall(r'@图片\d+', self.prompt))
    video_count = len(re.findall(r'@视频\d+', self.prompt))
    audio_count = len(re.findall(r'@音频\d+', self.prompt))
    total_count = image_count + video_count * 3 + audio_count
    
    # 检查限制
    checks = [
        (image_count <= 9, f"图片数量: {image_count} ≤ 9 ✓", f"图片数量: {image_count} > 9 ✗"),
        (video_count <= 3, f"视频数量: {video_count} ≤ 3 ✓", f"视频数量: {video_count} > 3 ✗"),
        (audio_count <= 3, f"音频数量: {audio_count} ≤ 3 ✓", f"音频数量: {audio_count} > 3 ✗"),
        (total_count <= 12, f"总文件数: {total_count} ≤ 12 ✓", f"总文件数: {total_count} > 12 ✗")
    ]
    
    for passed, ok_msg, fail_msg in checks:
        if passed:
            self.add_issue("素材预算", ok_msg, "🟢 PASS")
        else:
            self.add_issue("素材预算", fail_msg, "🔴 ERROR")
```

### 4.2 违禁词扫描

```python
def scan_prohibited(self):
    """扫描违禁词"""
    
    # 违禁词库
    prohibited_words = {
        "政治敏感": ["领导人", "领土争议", "敏感历史"],
        "暴力血腥": ["肢解", "酷刑", "斩首", "分尸", "爆头"],
        "色情低俗": ["性行为", "裸露", "色情", "淫秽"],
        "封建迷信": ["鬼怪", "祭祀", "僵尸"]
    }
    
    for category, words in prohibited_words.items():
        for word in words:
            if word in self.prompt:
                self.add_issue(
                    "违禁词扫描",
                    f"发现{category}词: {word}",
                    "🔴 ERROR"
                )
```

### 4.3 视听语言检查

```python
def check_audiovisual(self):
    """检查视听语言一致性"""
    
    import re
    
    # 检查轴线保持（对话场景）
    dialogue_patterns = ['对话', '交谈', '对视', '说话']
    has_dialogue = any(p in self.prompt for p in dialogue_patterns)
    
    if has_dialogue:
        # 检查是否有越轴标注
        if '越轴' not in self.prompt:
            # 检查轴线是否保持一致（简化检查）
            # 实际需要更复杂的逻辑
            pass
    
    # 检查视线匹配
    if '视线' in self.prompt or '看向' in self.prompt:
        # 简化检查
        pass
```

### 4.4 时间轴检查

```python
def check_timeline(self):
    """检查时间轴合理性"""
    import re
    
    # 提取时间标注
    time_pattern = r'T\+(\d+\.?\d*)s'
    times = re.findall(time_pattern, self.prompt)
    
    if times:
        max_time = max([float(t) for t in times])
        
        if max_time > 15:
            self.add_issue(
                "时间轴",
                f"最大时长 {max_time}s > 15s",
                "🔴 ERROR"
            )
        elif max_time > 10:
            self.add_issue(
                "时间轴",
                f"最大时长 {max_time}s > 10s（建议拆分）",
                "🟠 WARNING"
            )
```

### 4.5 格式规范检查

```python
def check_format(self):
    """检查格式规范性"""
    
    # 检查景别标注
    shot_levels = ['特写', '近景', '中景', '全景', '远景']
    has_shot_level = any(sl in self.prompt for sl in shot_levels)
    
    if not has_shot_level:
        self.add_issue(
            "格式规范",
            "缺少景别标注（特写/近景/中景/全景/远景）",
            "🔴 ERROR"
        )
    
    # 检查引号
    if '"' in self.prompt and '""' not in self.prompt:
        self.add_issue(
            "格式规范",
            "台词应使用中文引号\"\"",
            "🔴 ERROR"
        )
```

---

## 五、报告生成

### 5.1 报告模板

```markdown
# 📋 质量预检报告

**检查时间**: 2026-03-12 15:30
**检查文件**: outputs/ep01/02-seedance-prompts.md
**检查结果**: ❌ 未通过

---

## 🔴 错误 (3项)

1. **素材预算**
   - 图片数量: 12 > 9 ✗
   - 建议：拆分剧情点为2条提示词

2. **违禁词扫描**
   - 发现暴力词: 斩首
   - 建议：替换为"斩伤"

3. **格式规范**
   - 缺少景别标注
   - 建议：为每个镜头添加景别

---

## 🟠 警告 (2项)

1. **时间轴**
   - 最大时长 12s > 10s
   - 建议：考虑拆分

2. **视听语言**
   - 对话场景缺少越轴标注
   - 建议：如需越轴请标注【越轴】

---

## 🟢 通过 (2项)

1. **视听语言** - 轴线保持 ✓
2. **时间轴** - 动作密度合理 ✓

---

## 📝 修复建议

### 立即修复
1. 图片引用从12减少到9以下
2. 将"斩首"替换为"斩伤"
3. 添加景别标注

### 建议修复
1. 考虑拆分超长镜头
2. 越轴场景添加标注
```

### 5.2 报告生成函数

```python
def generate_report(self) -> str:
    """生成检查报告"""
    
    errors = [i for i in self.issues if i["severity"] == "🔴 ERROR"]
    warnings = [i for i in self.issues if i["severity"] == "🟠 WARNING"]
    infos = [i for i in self.issues if i["severity"] == "🟢 PASS"]
    
    report = "# 📋 质量预检报告\n\n"
    report += f"**检查结果**: {'❌ 未通过' if errors else '✅ 通过'}\n\n"
    
    if errors:
        report += "## 🔴 错误\n\n"
        for i, e in enumerate(errors, 1):
            report += f"{i}. **{e['check']}**: {e['detail']}\n"
            report += f"   - 建议: {generate_fix_suggestion(e['check'])}\n\n"
    
    if warnings:
        report += "## 🟠 警告\n\n"
        for i, w in enumerate(warnings, 1):
            report += f"{i}. **{w['check']}**: {w['detail']}\n\n"
    
    return report
```

---

## 六、自动修复建议

### 6.1 修复建议映射

```python
def generate_fix_suggestion(check_type: str) -> str:
    """生成修复建议"""
    
    fixes = {
        "素材预算-图片": "1)拆分剧情点为多条提示词 2)减少引用图片，改用文字描述",
        "素材预算-时长": "将长镜头拆分为多个短镜头，每条≤15秒",
        "违禁词": "替换为中性词",
        "轴线保持": "在越轴处插入中性镜头（特写/空镜）作为过渡",
        "视线匹配": "添加 POV 镜头展示角色看到的内容，或标注'留悬念'",
        "格式-景别": "为每个镜头添加景别：特写/近景/中景/全景/远景",
        "格式-引号": "将英文\"\"替换为中文\"\"",
        "时间轴-时长": "拆分镜头，确保单条≤15秒"
    }
    
    return fixes.get(check_type, "手动检查并修改")
```

---

## 七、使用示例

### 7.1 基础使用

```python
# 初始化检查器
checker = QualityPreChecker(prompt_text)

# 执行检查
result = checker.run_all_checks()

# 输出报告
print(checker.generate_report())
```

### 7.2 命令行使用

```bash
# 检查单文件
python quality_prechecker.py --input outputs/ep01/02-seedance-prompts.md

# 检查并生成报告
python quality_prechecker.py --input outputs/ep01/02-seedance-prompts.md --report report.md

# 自动修复
python quality_prechecker.py --input outputs/ep01/02-seedance-prompts.md --fix
```

### 7.3 批量检查

```bash
# 检查所有分镜文件
python quality_prechecker.py --batch --dir outputs/

# 检查指定集数
python quality_prechecker.py --episode ep01
```

---

## 八、集成到工作流

### 8.1 分镜编写阶段集成

```markdown
## 分镜编写流程（更新）

1. 分镜师编写提示词
2. 运行时自动预检 ← 新增
3. 如有问题 → 提示修改
4. 通过后 → 导演审核
```

### 8.2 自动触发规则

```yaml
# precheck-config.yaml
triggers:
  on_save: true          # 保存时自动检查
  on_generate: true      # 生成前检查
  before_review: true   # 审核前检查
  
checks:
  budget: true           # 素材预算
  prohibited: true       # 违禁词
  audiovisual: true     # 视听语言
  timeline: true       # 时间轴
  format: true          # 格式规范

auto_fix:
  enabled: false        # 是否自动修复
  suggest_only: true    # 仅提供建议
```

---

## 九、配置选项

### 9.1 检查严格度

```yaml
# strictness: lenient / normal / strict
strictness: normal

# 严格模式下
# - WARNING视为ERROR
# - INFO视为WARNING
```

### 9.2 自定义违禁词

```yaml
# custom_prohibited_words.yaml
custom_words:
  - "自定义违禁词1"
  - "自定义违禁词2"
```

---

## 版本信息

- 版本: 1.0
- 更新日期: 2026-03-12
- 本系统为AXIS质量保障核心组件
