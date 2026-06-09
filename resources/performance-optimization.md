# 性能优化指南

> 本指南提供提示词长度优化、素材引用效率、生成失败重试策略、成本控制和批量生成优化等指导
>
> ⚠️ **注意**：本指南中引用的部分 Python 脚本（如 `batch-generator.py`、`batch-replace.py`、`cost-tracker.py`、`performance-monitor.py`、`retry-generator.py`、`prompt-optimizer.py`）为**计划实现的工具**，代码块中的内容为使用示例和伪代码参考。当前已实现的工具请查看 `tools/` 目录。

---

## 一、提示词长度优化

### 1.1 长度标准

| 平台 | 推荐长度 | 最大长度 | 备注 |
|------|----------|----------|------|
| Seedance | 500-1000字 | 1000字 | 过长会影响理解 |
| Kling 2.6 | 200-400字 | 800字 | 简洁为主 |
| Kling 3.0 | 150-300字 | 600字 | 智能分镜需要简洁 |

### 1.2 精简技巧

**保留要素**：
- 核心动作描述 ✓
- 关键场景要素 ✓
- 镜头变化 ✓
- 情绪基调 ✓

**可省略**：
- 重复的修饰词 ✗
- 过于详细的背景 ✗
- 冗长的心理描写 ✗
- 过多的形容词 ✗

### 1.3 精简示例

**优化前（328字）**：
```markdown
一个穿着深蓝色长袍的年轻男子站在古老的书院门口，他的脸上带着一种沉稳而又自信的表情，眼神中透露着一种历经沧桑的智慧的光芒，头发束成发髻，用一根古朴的玉簪固定，身后背着
一把长剑，剑鞘上刻着精美的花纹，整个人看起来就像是从古代画卷中走出来的侠客一般
```

**优化后（156字）**：
```markdown
蓝袍男子立于书院门口，面容沉稳自信，眼神深邃，历经沧桑。发束玉簪，背负长剑，剑鞘雕花。如古卷侠客。
```

### 1.4 自动精简工具

```bash
# 使用命令行工具精简
python tools/prompt-optimizer.py --input prompt.txt --output optimized.txt --level aggressive
```

---

## 二、素材引用效率

### 2.1 引用原则

| 原则 | 说明 |
|------|------|
| 必要才引用 | 只引用对生成关键的素材 |
| 避免重复 | 同一素材不要多次引用 |
| 引用精准 | 明确引用用途 |
| 数量控制 | 严格遵守平台限制 |

### 2.2 引用数量限制

| 平台 | 图片 | 视频 | 音频 | 总计 |
|------|------|------|------|------|
| Seedance | ≤9 | ≤3 | ≤3 | ≤12 |
| Kling 2.6 | ≤1 | - | 内置 | 1 |
| Kling 3.0 | ≤1 | - | 内置 | 1 |

### 2.3 优化策略

**问题：引用过多**
```markdown
# 问题：引用了12张图片
@图片1 @图片2 @图片3 @图片4 ... (太多)
```

**解决方案：减少引用**
```markdown
# 优化：只引用必要的3张
@图片1（角色A外形）
@图片2（场景整体氛围）
@图片3（关键道具）
```

### 2.4 引用映射表优化

```markdown
| 引用编号 | 素材来源 | 用途 | 优先级 |
|---------|---------|------|--------|
| @图片1 | character-prompts.md - 江辰 | 角色外形 | 必选 |
| @图片2 | scene-prompts.md - 书院门口 | 场景参考 | 必选 |
| @图片3 | scene-prompts.md - 教室 | 备用场景 | 可选 |
```

---

## 三、生成失败重试策略

### 3.1 失败类型与解决方案

| 失败类型 | 表现 | 解决方案 |
|----------|------|----------|
| 动作不自然 | 肢体扭曲、面部变形 | 减少动作复杂度、使用特写 |
| 场景崩坏 | 背景模糊、物体融合 | 简化场景、使用参考图 |
| 风格不符 | 与要求风格不符 | 明确风格关键词、增加描述 |
| 角色不像 | 与参考图差异大 | 重新生成参考图、明确主体参考 |
| 光影异常 | 过度曝光、阴影错误 | 简化光影描述、指定光源 |

### 3.2 重试参数调整

**第一次重试**：
```markdown
# 保持原有提示词，直接重试
```

**第二次重试**：
```markdown
# 简化关键描述，减少复杂元素
原：动作华丽的太极拳法
改：太极拳法
```

**第三次重试**：
```markdown
# 改变镜头角度/景别
原：正面特写
改：侧面特写
```

**第四次重试**：
```markdown
# 彻底简化
原：蓝袍男子在书院门口施展太极拳，动作行云流水，衣袂飘飘
改：男子站立
```

### 3.3 批量重试脚本

```python
# tools/retry-generator.py
def retry_with_backoff(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            result = generate(prompt)
            if result.success:
                return result
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            prompt = simplify_prompt(prompt)  # 简化提示词
            time.sleep(2 ** attempt)  # 指数退避
    return None
```

---

## 四、成本控制指南

### 4.1 成本构成

| 成本项 | 计算方式 | 优化策略 |
|--------|----------|----------|
| 生成次数 | 按生成次数计费 | 减少生成次数 |
| 素材数量 | 按素材使用计费 | 精简引用 |
| 重试成本 | 重试次数×单价 | 提高首次成功率 |
| 人工审核 | 按审核次数计费 | 减少返工 |

### 4.2 优化措施

**生成环节**：
1. 提示词优化 → 减少重试
2. 参考图准备 → 提高首次成功率
3. 分镜拆分 → 避免无效生成

**审核环节**：
1. 自检清单 → 减少审核轮次
2. 问题前置发现 → 降低返工率

### 4.3 成本监控

```bash
# 查看成本报告
python tools/cost-tracker.py --report
```

```
📊 成本报告
═══════════════════════════════
项目：我在恐怖副本当老师
────────────────────────────────
生成次数：36次
审核次数：12次
重试次数：8次
────────────────────────────────
预估成本：¥XXX
────────────────────────────────
优化建议：
- ep02 重试率较高(33%)，建议优化提示词
- ep03 一次性通过率100% ✓
```

---

## 五、批量生成优化

### 5.1 批量策略

**分集批量**：
```bash
# 批量生成 ep01-ep03 的 Seedance 提示词
python tools/batch-generator.py --episodes ep01,ep02,ep03 --platform seedance
```

**平台批量**：
```bash
# 一次性生成三个平台的提示词
python tools/batch-generator.py --episode ep01 --platform all
```

### 5.2 并行处理

```python
# 批量生成时使用并行处理
from concurrent.futures import ThreadPoolExecutor

def batch_generate(episodes, platforms):
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for ep in episodes:
            for platform in platforms:
                futures.append(executor.submit(generate, ep, platform))

        results = [f.result() for f in futures]
        return results
```

### 5.3 生成队列管理

```python
class GenerationQueue:
    def __init__(self, max_concurrent=3):
        self.queue = []
        self.running = 0
        self.max_concurrent = max_concurrent

    def add(self, prompt, priority=0):
        self.queue.append((priority, prompt))
        self.queue.sort(reverse=True)  # 按优先级排序

    def process(self):
        while self.queue and self.running < self.max_concurrent:
            priority, prompt = self.queue.pop(0)
            self.running += 1
            generate_async(prompt, callback=self.complete)
```

---

## 六、效率提升技巧

### 6.1 模板复用

**建立个人模板库**：
```
templates/
├──  standard-dialogue.yaml
├──  action-sequence.yaml
├──  emotional-climax.yaml
└──  cliffhanger.yaml
```

**使用方法**：
```python
# 加载模板
template = load_template("action-sequence.yaml")

# 填充内容
filled = fill_template(template, {
    "character": "江辰",
    "action": "拔剑",
    "emotion": "愤怒"
})
```

### 6.2 批量替换

```bash
# 批量替换集数
python tools/batch-replace.py --dir outputs/ep01 --from ep01 --to ep02
```

### 6.3 自动化工作流

```yaml
# .axis-workflow.yaml
workflow:
  name: "standard-episode"
  steps:
    - step: director-analysis
      tool: "director-skill"
      input: "novel/chapter-{n}.md"
      output: "outputs/ep{n}/01-director-analysis.md"

    - step: art-design
      tool: "art-design-skill"
      input: "outputs/ep{n}/01-director-analysis.md"
      output: "assets/prompts/character-prompts.md"

    - step: storyboard
      tool: "seedance-storyboard-skill"
      input: "outputs/ep{n}/01-director-analysis.md"
      output: "outputs/ep{n}/02-seedance-prompts.md"
```

---

## 七、性能指标监控

### 7.1 关键指标

| 指标 | 目标值 | 监控方式 |
|------|--------|----------|
| 首次成功率 | ≥80% | 统计生成成功次数 |
| 一次性通过率 | ≥85% | 统计审核通过次数 |
| 平均生成时间 | ≤30秒 | 记录生成耗时 |
| 成本效率 | 持续优化 | 成本追踪 |

### 7.2 监控面板

```bash
# 启动性能监控
python tools/performance-monitor.py --dashboard
```

```
📊 性能监控面板
═══════════════════════════════
首次成功率：82% ████████░░
一次性通过率：88% ████████░░
平均生成时间：25s ██████░░░░
────────────────────────────────
今日生成：36次
今日成本：¥XX
────────────────────────────────
⚡ 优化建议：
- ep02提示词可进一步精简
```

---

**版本**：1.0
**更新日期**：2026-03-15
