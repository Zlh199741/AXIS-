# AXIS 全流程指令合集
> ⚠️ 本文件于 2026-04-22 因误删操作重建。

---

## 快速指令索引

| 指令 | 说明 |
|------|------|
| `~full [小说名]` | 路径一：从原著全流程启动 |
| `~brainworm [点子]` | 路径二：从创意点子全流程启动 |
| `~start ep01` | 路径三：从导演分析直接启动 |
| `~outline` | 生成集纲（必须先确认集数） |
| `~script ep01` | 生成剧本 |
| `~director ep01` | 执行导演分析 |
| `~style ep01` | 执行视觉风格选择 |
| `~art ep01` | 执行服化道设计 |
| `~storyboard ep01` | 执行分镜编写（三平台） |
| `~check ep01` | 运行全量校验 |
| `~status ep01` | 查看集数进度状态 |

---

## 阶段指令详解

### ~full [小说名]
```
执行路径一：
1. 将小说放入 novel/ 目录
2. 初始化 .agent-state.json 和 .stage-gate.json
3. 运行小说分析（融合模块）
4. 依次执行：集纲 → 剧本 → 导演分析 → 视觉风格 → 服化道 → 分镜
```

### ~outline（集纲生成）
```
🔴 执行前必须询问用户：本章计划生成几集？
加载 Agents：short-drama-architect
必须加载：short-drama-architect-skill + genre-adaptive-skill
产出：assets/outline/ch{XX}-outline.md
校验：short-drama-architect-review-skill + compliance-review-skill
```

### ~script ep01（剧本生成）
```
加载 Agents：short-drama-scriptwriter
必须加载：short-drama-scriptwriter-skill
前置：assets/outline/{chapter}-outline.md
产出：assets/novel/{chapter}-script.md
强制校验（顺序执行）：
  python3 tools/validators/plot-fidelity-checker.py <ep> --chapter <ch>
  python3 tools/validators/novel-dialogue-fidelity-checker.py <ep> --chapter <ch>
```

### ~director ep01（导演分析）
```
加载 Agents：director
必须加载（缺一不可）：
  - skills/director-skill/SKILL.md
  - skills/character-interaction-design-skill/SKILL.md
  - skills/film-lighting-technique-skill/SKILL.md
  - resources/unified-audiovisual-language-library.md（分段：1-400 + 401-642行）
产出：outputs/ep01/01-director-analysis.md
原文溯源铁律：必须完整读取 novel/ 原著文件
```

### ~style ep01（视觉风格选择）
```
加载 Agents：director（visual-style-selector 角色）
必须加载：visual-style-selector-skill
产出：assets/visual-style-guide.md
校验：python3 tools/validators/cross-file-consistency-checker.py <ep>
```

### ~art ep01（服化道设计）
```
加载 Agents：art-designer
必须加载（缺一不可）：
  - skills/aesthetic-vision-skill/SKILL.md（五问法）
  - skills/art-design-skill/SKILL.md（分段读取，共1188行）
  - skills/scene-concept-design-skill/SKILL.md
  - skills/prop-concept-design-skill/SKILL.md
产出：assets/prompts/character-prompts.md + scene-prompts.md + props-prompts.md
      assets/character-bible.md（步骤5.5，≤600 tokens）
强制校验（顺序执行）：
  python3 tools/validators/t0-validator.py --batch --dir assets/prompts/
  python3 tools/validators/cross-file-consistency-checker.py <ep>
  python3 tools/generators/context-snapshot-generator.py <ep>
```

### ~storyboard ep01（分镜编写）
```
加载 Agents：storyboard-artist
入口门禁（必须先执行时长预测）：
  sovereign-duration-predictor-skill STEP 1-4
  时长覆盖率 ≥ 90% 才允许开始编写

必须加载（缺一不可）：
  - skills/seedance-storyboard-skill/SKILL.md
  - skills/sovereign-duration-predictor-skill/SKILL.md
  - resources/unified-audiovisual-language-library.md
  - resources/advanced-seedance-guide.md
  - tools/references/cross-platform-converter.md
  - tools/references/spatial-continuity-checker.md
  - tools/references/ai-generation-predictor.md
  - assets/character-bible.md
  - assets/visual-style-guide.md

产出（当前仅 Seedance 2.0）：
  outputs/ep01/02-seedance-prompts.md
  ~~outputs/ep01/02-kling-prompts.md~~ ⏸️ 暂停
  ~~outputs/ep01/02-kling-3.0-prompts.md~~ ⏸️ 暂停
  outputs/ep01/03-text-storyboard.md

出口校验（顺序执行）：
  python3 tools/validators/beat-density-checker.py <ep>
  python3 tools/validators/stage-output-validator.py <ep> storyboard
  python3 tools/validators/cross-file-consistency-checker.py <ep>
  python3 tools/generators/context-snapshot-generator.py <ep>
  python3 tools/validators/novel-fidelity-checker.py <ep>
  python3 tools/management/episode-progress-reporter.py <ep>
```

---

## 校验工具全集

### 强制校验（任何情况不可跳过）

```bash
# 1. Seedance 节拍密度（分镜后立即执行）
python3 tools/validators/beat-density-checker.py ep01
# exit 0 = PASS，exit 1 = 有 critical P块 → 必须拆分重写

# 2. 剧情忠实度（剧本生成后立即执行）
python3 tools/validators/plot-fidelity-checker.py ep01 --chapter ch01
# exit 0 = 覆盖率100%，exit 1 = 不足 → 必须重新生成剧本

# 3. 台词忠实度（剧本生成后）
python3 tools/validators/novel-dialogue-fidelity-checker.py ep01 --chapter ch01
# 全部完全一致或白名单豁免才算 PASS

# 4. T0 服化道校验（服化道设计后）
python3 tools/validators/t0-validator.py --batch --dir assets/prompts/
# 全部 100/100 才算 PASS

# 5. 产物结构校验（每阶段后）
python3 tools/validators/stage-output-validator.py ep01 <阶段名>
# 如：python3 tools/validators/stage-output-validator.py ep01 storyboard

# 6. 跨文件一致性（视觉风格/服化道/分镜后）
python3 tools/validators/cross-file-consistency-checker.py ep01
```

### 生成类工具

```bash
# 上下文快照（每阶段完成后更新）
python3 tools/generators/context-snapshot-generator.py ep01

# 30秒预告片
python3 tools/generators/trailer-generator.py ep01

# 跨平台转换（Seedance → Kling 2.6 + Kling 3.0）
python3 tools/generators/cross-platform-converter.py \
  --input outputs/ep01/02-seedance-prompts.md \
  --target all --output-dir outputs/ep01

# 时长预测
python3 tools/generators/duration-predictor.py ep01
```

### 进度管理工具

```bash
# 更新子步骤状态
python3 tools/management/stage-step-updater.py ep01 导演分析 生成 completed
python3 tools/management/stage-step-updater.py ep01 导演分析 --complete-stage
python3 tools/management/stage-step-updater.py ep01 导演分析 --status

# 集数进度报告
python3 tools/management/episode-progress-reporter.py ep01

# 下一步操作指引
python3 tools/management/next-step-prompter.py ep01 导演分析

# 引擎入口检查
python engine_cli.py --mode check-snapshot --ep ep01
python engine_cli.py --mode status --ep ep01
```

---

## 状态文件操作规范

### .agent-state.json
```json
{
  "activeChapter": "ch01",
  "activeEpisode": "ep01",
  "projectName": "项目名称",
  "novelFile": "novel/001-第1章.txt",
  "novelDir": "novel/",
  "workflowPath": "路径一",
  "visualStyle": "写实CG融合 × ...",
  "totalChapters": 3,
  "chapters": {
    "ch01": {
      "title": "第1章标题",
      "status": "completed",
      "episodeCount": 3,
      "episodes": ["ep01", "ep02", "ep03"]
    }
  },
  "episodes": {
    "ep01": {
      "title": "第1集：标题",
      "status": "in-progress",
      "currentStage": "导演分析",
      "stageHistory": ["导演分析-completed"],
      "outputDir": "outputs/ep01",
      "characterPrompts": "assets/prompts/character-prompts.md",
      "scenePrompts": "assets/prompts/scene-prompts.md"
    }
  }
}
```

### .stage-gate.json episodeProgress 初始化
```python
# 新增集数时执行：
python3 tools/management/stage-step-updater.py ep01 导演分析 --status
```

---

## 🔴 铁律清单（所有阶段通用）

1. **python3 -c 绝对禁用**：必须写入 .py 文件再调用
2. **跳过校验 = 产出作废**：任何自动化校验都不能跳过
3. **业务审核 + 合规审核必须人工确认**：AI 不得自行标记
4. **全文校验不抽查**：plot-fidelity-checker 必须全集覆盖
5. **exit 1 必须重生成**：不允许忽略或手动修补绕过
6. **beat-density-checker 0 个 critical 才能交付**
7. **平台输出**：当前仅 Seedance 2.0（Kling 2.6/3.0 暂停启用）
8. **context-snapshot 每阶段更新**：check-snapshot 失败禁止进入下一阶段
9. **删除文件必须走 /delete-files 工作流**：列清单 + 用户确认 + 验证
10. **子步骤立即同步**：完成即调用 stage-step-updater，禁止事后补录
11. **🔴 CHANGELOG 强制同步**：任何对 AXIS 系统规则文件（agents/skills/CLAUDE.md/流程文档）的新增/修改/删减，必须同步更新 `CHANGELOG.md`，记录具体变更内容，否则视同操作未完成
