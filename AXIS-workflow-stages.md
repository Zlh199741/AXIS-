# AXIS 工作流各阶段详细说明
> ⚠️ 本文件于 2026-04-22 因误删操作重建。

---

## 工作流路径总览

| 路径 | 入口指令 | 适用场景 |
|------|---------|---------|
| **路径一** | `~full [小说名]` | 从原著小说开始全流程制作 |
| **路径二** | `~brainworm [点子]` | 从创意点子开始全流程制作 |
| **路径三** | `~start ep01` | 已有剧本/角色，直接从导演分析开始 |

---

## 阶段一：小说分析（路径一专属）

**调度**：融合模块 chuanban-chaishu-skills（小说分析无独立 agent 文件，由融合模块承担）  
**触发条件**：`novel/` 目录下有原著 .txt 文件

### 产出物
```
assets/novel-analysis/{书名}/
├── 拆分/              每章节独立 .md 文件（按章编号）
├── 概括/              分组概括（每3章一组）
├── ABC爽点分析.md     爽点提取与分类
├── 事件线追踪.md      关键事件时间线
├── 人物关系分析.md    角色关系图谱
├── 人物和设定/        人物地位yaml + 角色设定
├── 全书概括.md        全书主线摘要
├── 剧本结构诊断报告.md 三段式结构分析
├── 合规审核报告.md    内容合规初审
└── 融合分析报告.yaml  综合分析汇总
```

### 质量门禁
- 章节识别率 ≥ 90%
- B 完整度合格率 ≥ 80%
- 合规审核 PASS

---

## 阶段二：脑洞生成（路径二专属）

**调度 Agent**：brainworm-generator  
**触发条件**：用户提供创意点子（< 200字）

### 产出物
```
brainworm/{项目名}/
├── 世界观扩展.md
├── 人设卡片.md
├── 核心梗.md
├── 故事卡.md
└── 集数规划.md
```

### 质量门禁
- brainworm-generator-review-skill 业务审核 PASS
- 合规审核 PASS

---

## 阶段三：道具与金手指提取（可选）

**调度 Agent**：art-designer（由制片人调度）  
**前置条件**：novel/ 目录有小说文件或用户直接输入

### 产出物
`assets/prompts/props-prompts.md`（道具 + 金手指两类条目）

### 每条道具必须包含
1. 原文描述
2. 视觉特征
3. 功能设定
4. 英文绘画提示词

### 质量门禁
- 道具条目 ≥ 3条
- 五问法声明全部填写（Q1-Q5，禁止空白模板占位符）
- costume-prop-character-design-review-skill PASS

---

## 阶段四：集纲生成

**调度 Agent**：short-drama-architect  
**必须加载**：short-drama-architect-skill + genre-adaptive-skill

### 产出物
`assets/outline/ch{XX}-outline.md`

### 每集集纲必须包含
- 情绪循环3步（3-10-60 结构）
- 精彩台词（≥3句）
- 卡点钩子（极限卡点收尾）

### 三段式结构
- 蓄能期（1/3集数）
- 加压期（1/3集数）
- 升级期（1/3集数）

### 质量门禁
- short-drama-architect-review-skill 业务审核 PASS
- 合规审核 PASS
- 🔴 动态集数确认（执行前必须询问用户本章集数）

---

## 阶段五：剧本生成

**调度 Agent**：short-drama-scriptwriter  
**必须加载**：short-drama-scriptwriter-skill  
**前置文件**：`assets/outline/{chapter}-outline.md`

### 产出物
`assets/novel/{chapter}-script.md`

### 格式规范
- 每集 2–4 个核心场次
- 场次标头 + 出场人物 + @人名条标签
- 绝对视觉化剥离（无心理描写，全部外化为 `▲` 前缀动作）
- 专业影视标签：`▲动作白描` / `▲特写` / `【切镜】` / `"音效"` / `▲黑屏`
- 极限卡点收尾（截断在最高潮前 0.5秒 + `▲黑屏`）

### 🔴 强制校验（必须顺序执行）
```bash
python3 tools/validators/plot-fidelity-checker.py <ep> --chapter <ch>
# → 覆盖率 100% → exit 0 才能继续
python3 tools/validators/novel-dialogue-fidelity-checker.py <ep> --chapter <ch>
# → 全部通过才能继续
```

---

## 阶段六：导演分析

**调度 Agent**：director  
**必须加载**：
- 🔴 resources/director-thinking-layer.md（**第一优先·道层**：导演工作法三尺度＝2A整集骨架+2B每场八问+2C镜头组接；先于视听技术，缺层判不合格）
- skills/novel-dialogue-extractor-skill/SKILL.md（🔴 前置步骤·对话提取）
- skills/director-skill/SKILL.md
- skills/character-interaction-design-skill/SKILL.md
- skills/film-lighting-technique-skill/SKILL.md
- resources/unified-audiovisual-language-library.md（术层·分段读取：第1-400行 + 第401-642行；🔴 它是"怎么拍"，非"演什么"）
- assets/character-bible.md（角色外观快照，若已存在）
- assets/visual-style-guide.md（视觉风格快照，若已存在）

### 🔴 前置步骤：原文对话提取（导演讲戏前必须完成）
1. 加载 novel-dialogue-extractor-skill，对本集涉及的小说章节执行逐句对话扫描
2. 产出物：`outputs/ep{XX}/00-dialogue-extraction.md`（结构化对话清单）
3. 导演讲戏时从清单中引用台词，确保台词零丢失
4. 覆盖率 < 100% → 阻断后续步骤

### 产出物
- `outputs/ep{XX}/00-dialogue-extraction.md`（对话提取清单）
- `outputs/ep{XX}/01-director-analysis.md`（导演分析）

### 必须包含的5大模块
1. **剧情梗概**（100字以内）
2. **3秒钩子设计**（开场抓人设计）
3. **10秒叙事结构**（节奏节拍分析）
4. **1分钟情绪地图**（情绪弧线）
5. **卡点设计**（收尾钩子）

### 每个 P 块必须包含
- 叙事功能标签
- 情绪钩子设计块（4项：情绪标签/触发事件/表现手法/钩子类型）
- 人物清单（含原文描写摘录、视觉标签、素材状态）
- 场景清单（含场景特征、素材状态）

### 原文溯源铁律
- 必须完整读取原始小说文件
- 每个角色逐一搜索外观/性格/能力原文描写
- 人物清单中每个角色必须包含：①原文外观描写摘录 ②性格特征 ③特殊能力/标记

---

## 阶段七：视觉风格选择

**调度 Agent**：director（visual-style-selector 角色）  
**必须加载**：visual-style-selector-skill

### 产出物
`assets/visual-style-guide.md`

### 必须包含
- 风格名称 + 子风格
- 色彩基调（主色/辅色/强调色 + 色温）
- 全局风格前缀（Seedance/Kling 双语版本）
- 混搭风格兼容性检查（若有）

### 🔴 强制校验
```bash
python3 tools/validators/cross-file-consistency-checker.py <ep>
```

---

## 阶段八：服化道设计

**调度 Agent**：art-designer  
**必须加载**（缺一不可）：
- skills/aesthetic-vision-skill/SKILL.md（五问法模板/体型矩阵/入镜规范/第7维度评分）
- skills/art-design-skill/SKILL.md（约330行·模块化精简后完整读取；详规在 references/ 按需读取）
- skills/scene-concept-design-skill/SKILL.md（含路由C·场景设定板：单图六区块 / 两视图同源 / 白灰底，模板 templates/scene-design-board-template.md，校验 tools/validators/scene-board-validator.py）
- skills/prop-concept-design-skill/SKILL.md
- skills/character-interaction-design-skill/SKILL.md
- skills/film-lighting-technique-skill/SKILL.md

**🔴 角色唯一标准·全部角色必出（2026-05-31 起电影级角色提案板取代三栏式工业资产）**：
- skills/cinematic-character-pitch-board-skill/SKILL.md（电影级角色提案板技能·横版16:9中性灰六区块）
- skills/cinematic-character-pitch-board-review-skill/SKILL.md（提案板配对审核技能）

> 🔴 2026-05-31 起：电影级角色提案板为**唯一角色标准**，取代三栏式工业资产。所有角色输出提案板（主角/重要配角出完整六区块；次要/一次性配角/群演出精简提案板：区块A主视觉+B转面+F色板）。同一角色各区块必须共享同一基底人物（五官/比例/发型/服装/配饰严格一致），由 pitch-board-review × art-direction-review 核对。三栏式已彻底废除（模板删除、校验器不再接受三栏式）；存量三栏式文件需回炉重生成为提案板。

### 产出物
```
assets/prompts/
├── character-prompts.md    角色提示词（电影级角色提案板·16:9六区块）
├── scene-prompts.md        场景提示词
└── props-prompts.md        道具/金手指提示词
assets/character-bible.md   角色外观快照（步骤5.5生成，≤600 tokens）
```

### 电影级角色提案板强制要素（8项·2026-05-31 唯一标准）
1. 横版大画幅 16:9
2. 中性灰提案板背景（#BEC1C4~#C7CACD，非纯白/纯黑/无场景元素）
3. 六区块版面（顶部细条 + 区块A主视觉/B全身5视图转面/C头部6视图/D情绪肖像/E服装拆解/F色板）
4. 区块A 85mm全身立像 + 金色身高刻度尺
5. HSB 色板（≥4色含 #HEX，区块F）
6. 区块E 服装配件拆解（4-6张100mm微距）
7. 同一基底人物（A/B/C/D 五官/发型/服装/配饰严格一致）
8. 核心渲染参数（PBR/AO/SSS/UE5/Octane 至少2项）

### 五问法声明（每个设计必须填写 Q1-Q5）
- Q1：这个角色/场景/道具最本质的视觉冲击点是什么？
- Q2：在 AI 生成语境下，这个视觉冲击点用什么具体词汇表达？
- Q3：有哪些常见的错误生成方向需要规避？
- Q4：这个设计在不同场景/光线条件下的变体是什么？
- Q5：如何用 HSB 色值锁定最关键的色彩？

### 🔴 强制校验（顺序执行）
```bash
python3 tools/validators/t0-validator.py --batch --dir assets/prompts/
python3 tools/validators/cross-file-consistency-checker.py <ep>
python3 tools/generators/context-snapshot-generator.py <ep>
```

### 🔴 提案板校验（2026-05-31 起电影级角色提案板为唯一角色标准·全部角色必出，故本校验必须运行）
```bash
python3 tools/validators/pitch-board-validator.py --auto
```
> 说明：`--auto` 仅在确无角色提案板文件时软跳过；正常流程下角色资产必为提案板，校验必须通过。

---

## 阶段九：分镜编写

**调度 Agent**：storyboard-artist  
**必须加载**（缺一不可）：
- skills/seedance-storyboard-skill/SKILL.md（T0工业级标准）
- skills/sovereign-duration-predictor-skill/SKILL.md（🔴 时长预测，分镜前必须执行）
- skills/film-lighting-technique-skill/SKILL.md
- resources/unified-audiovisual-language-library.md
- resources/advanced-seedance-guide.md
- tools/references/cross-platform-converter.md（三平台转换器）
- tools/references/camera-movement-master.md
- tools/references/spatial-continuity-checker.md
- tools/references/ai-generation-predictor.md
- 🔴 Seedance 2.0 情绪-微表情-语气增强模块.md（情绪/对白/演技镜头必做：RHYTHM CURVE、微表情递进链、台词语气参数化、小蔡6字段）
- 🔴 Seedance_2.0_核心技能速查手册_6层堆栈_6字段_台词_微表情递进链(1).md（6层堆栈结构 + 6字段分镜格式 + 台词发声方式 + 微表情递进链速查）
- 🔴 Seedance_2.0_情绪与语气提示词写法手册.md（情绪与语气统一写法：微表情嵌「主体动作/表情」字段、语气嵌台词`{}`前动作描写）
- 🔴 Seedance_2.0_微表情物理描述素材库_100组(1).md（100组微表情物理化词库：用面部肌肉物理指令替代抽象情绪词）
- assets/character-bible.md
- assets/visual-style-guide.md

### 🔴 入口门禁（分镜前强制）
1. **时长预测报告**（sovereign-duration-predictor-skill STEP 1-4）
   - 原始节拍数量
   - 预测基础时长 vs 目标时长（≥ 90% 才允许开始）
   - 缺口分析和补充建议
2. 加载 storyboard-generation-cheatsheet.md（Phase A 生成速查表）
3. 动作戏场景：combat-enhanced-module.md（提前加载）

### 产出物
```
outputs/ep{XX}/
├── 02-seedance-prompts.md      Seedance 2.0 提示词（主力）
├── 02-kling-prompts.md         Kling 2.6 提示词（全局待用·不启用）
├── 02-kling-3.0-prompts.md     Kling 3.0 提示词（全局待用·不启用）
└── 03-text-storyboard.md       文字分镜
```

### 编写中强制检查项（每条 P 块）
> 🔴 2026-06-07 方向B（修订）：**翻译审计 / 密度校验两张表不再写进提示词文件**；
> **🎭 台词审计保留**——它是「非配音台词」（屏幕文字等）的唯一逐字留存处，关乎源剧本忠实度。
> 翻译/密度的权威校验已脚本化、确定性、零 AI 自评：
> 翻译零残留→`seedance-template-validator`（直接扫机读层禁用术语）；
> 节拍密度→`beat-density-checker`。
> 台词逐字仍由 `seedance-template-validator`（读来源剧本逐字比对）+`dialogue-sync-checker` 把关。
> 翻译/密度两表若仍保留则照常被校验（向后兼容），但不再是必需项。
- 情感熵三子项**独立逐行**核查（①环境熵增 ②时间弹性→特写拆解 ③通感模拟）
- 动作戏打点：每个打点必须有**显式特写切镜组**
- 空间坐标锚点（每条 P 强制）
- T+时间轴（0.5秒精度）
- 视线对焦（每条 P 强制）

### Seedance P-Block 机读层结构
```
### [时间段]（[镜头描述]）
[画面描述，含角色/环境/动作]

#### 机读层
- **对白层**：[时间] @角色："台词" | 气泡/口型/画外音
- **配乐层**：[时间] [音乐描述]
- **音效层**：[时间] [音效描述]
```

### 🔴 出口门禁（分镜后强制校验）

**推荐：一键 Skill 合规审计（9-B/9-C 脚本化，省 token，自动跑齐本阶段全部校验器并出 9-C 报告表）**
```bash
python3 tools/validators/skill-compliance-auditor.py <ep> storyboard --md
# → exit 1 即未通过；表格逐项列出每个校验器结果，模型无需再手工生成审计表
```

**或逐项执行（等价的底层校验器清单）**
```bash
python3 tools/validators/beat-density-checker.py <ep>
# → exit 1（有 critical P 块） → 必须拆分或重写后重跑

python3 tools/validators/stage-output-validator.py <ep> storyboard
python3 tools/validators/seedance-template-validator.py outputs/<ep>/02-seedance-prompts.md
python3 tools/validators/machine-layer-timing-checker.py outputs/<ep>/02-seedance-prompts.md
python3 tools/validators/dialogue-sync-checker.py <ep>
# → 同集 seedance/kling 平行产物间台词逐字一致；D01漂移/D02丢失=critical
python3 tools/validators/cross-file-consistency-checker.py <ep>
python3 tools/generators/context-snapshot-generator.py <ep>
python3 tools/validators/novel-fidelity-checker.py <ep>
```

### P-Block 拆分规范
当 `beat-density-checker` 报告 ≥ 200% critical：
1. 将超载 P 块拆分为 Pa + Pb（或 Pa + Pb + Pc）
2. 每个子块保持叙事完整性
3. 更新提示词文件头部的预算表、P 块列表、总时长
4. 重跑 beat-density-checker 直到 0 个 critical

### 对白密度计算参数
| 类型 | 字速 | 前锚 | 后留白 |
|------|------|------|-------|
| 口型对白 💬 | 0.40s/字 | 0.80s | 0.80s |
| 气泡/电话/画外音 🫧 | 0.20s/字 | 0.00s | 0.30s |
| 系统消息/卡片 | 0.15s/字 | 0.00s | 0.20s |
| 反应镜头 | 1.50s/个 | — | — |
| critical 阈值 | ≥ 200% | | |

---

## 阶段十：全剧收尾（最后一集完成后触发）

**触发条件**：`episode-progress-reporter.py` 输出「全系列所有集数均已完成」

### 收尾动作（必须逐项完成）
1. 确认待生成集数列表为空
2. 新建交付文件夹：`{项目名}-交付包/`
3. 运行 `python3 tools/management/build-delivery-package.py`（如已存在）
4. ZIP 压缩备份
5. 删除工作区输出文件（可选，按用户要求）

### 交付包必包含
- `outputs/ep01/` ~ `outputs/epXX/`（全部集数产物）
- `assets/novel-analysis/`（小说分析）
- `assets/outline/`（集纲）
- `assets/prompts/`（提示词库）
- `assets/character-bible.md` + `assets/visual-style-guide.md`
- `README.md`（项目说明）

---

## 🔴 全局禁令

1. **禁止 `python3 -c "..."` 内联脚本**（会冻结界面）
2. **禁止跳过任何校验步骤**
3. **禁止 AI 自行标记业务审核/合规审核为 PASS**（需人工确认）
4. **禁止在工具未运行的情况下将步骤标记为 completed**
5. **删除文件前必须执行 `/delete-files` 工作流**（逐目录扫描 + 用户确认）

---

## 阶段十一：集间交接（每集分镜完成后执行）

**触发条件**：当前集数 `分镜编写` 阶段全部通过（Seedance + 文字分镜产物 + 全量校验 PASS；Kling 全局待用）

### 集间交接清单（必须逐项完成）

**A. 本集收尾**
- [ ] `episode-progress-reporter.py <ep>` 输出本集进度报告
- [ ] `context-snapshot-generator.py <ep>` 更新上下文快照（最终状态）
- [ ] `stage-step-updater.py <ep> 分镜编写 --complete-stage` 标记完成
- [ ] `stage-step-updater.py <ep> 集间交接 --complete-stage`

**B. 下一集预备（ep02+）**
- [ ] 在 `.stage-gate.json` 的 `episodeProgress` 中新增下一集条目
- [ ] 在 `.agent-state.json` 的 `episodes` 中新增下一集空槽位，更新 `activeEpisode`
- [ ] 确认 `assets/prompts/` 中本集新增角色/场景/道具已标记 `[epNN][...][新增]`
- [ ] 确认下一集可复用的素材已标记 `[epNN][...][复用]`
- [ ] 生成下一集导演分析所需的上下文交接摘要（含：本集结尾钩子 + 待解悬念 + 角色状态）

**C. 跨集一致性巡检（ep02+）**
```bash
python3 tools/validators/cross-episode-consistency-checker.py
```
- 检查角色外观/道具材质/色值跨集是否一致
- 存在不一致项 → 必须修正后重跑，PASS 后才允许进入下一集

**D. 通知用户**
```
✅ ep{XX} 集间交接完成
   下一步：~start ep{XX+1}
   待解悬念：[列出本集末尾未解的悬念]
   下一集入口：python engine_cli.py --mode check-snapshot --ep ep{XX+1}
```

---

## 铁律级 Skill 强制调用 Must-Call Checklist

> � **单一权威来源（Single Source of Truth）**：本节是 AXIS 全系统逐阶段 Skill 强制加载清单的**唯一权威定义**。
> `CLAUDE.md` 子规则 9 不再复制本清单，只指向此处；如需增删任一阶段的 Skill，**只修改本节**，避免双份维护漂移。
>
> �🔴 每个阶段开始前必须逐一加载以下 Skill 并输出「📋 Skill 加载确认」。  
> 缺漏任何一个 ✅ 标记的 Skill → **立即中止** → 补充加载后重新执行。  
> 每项必须**逐项打勾输出**，不允许概括性声明"已加载"。

### 导演分析阶段
```
✅ resources/director-thinking-layer.md（🔴 第一优先·道层：导演工作法三尺度＝2A整集骨架+2B每场八问+2C镜头组接，先于视听技术）
✅ skills/director-skill/SKILL.md（导演执行主技能）
✅ skills/character-interaction-design-skill/SKILL.md（角色互动设计）
✅ skills/film-lighting-technique-skill/SKILL.md（电影质感光源技巧）
✅ resources/unified-audiovisual-language-library.md（视听执行术层；🔴 非导演思维本身）
   — 分段读取：第1-400行 ✅ + 第401-642行 ✅（微表情标签库必须覆盖）
⬜ skills/visual-language-logic/SKILL.md（可选：视觉语法与剪辑思维）
⬜ skills/plot-psyche-double-helix-skill/SKILL.md（可选：情节-心因双螺旋）
⬜ skills/script-structure-diagnosis-skill/SKILL.md（可选：剧本结构诊断）
--- 审核 ---
✅ skills/script-analysis-review-skill/SKILL.md（业务审核）
✅ skills/character-interaction-design-review-skill/SKILL.md（角色互动设计审核）
✅ skills/film-lighting-technique-review-skill/SKILL.md（电影光影技巧审核）
⬜ skills/plot-psyche-double-helix-review-skill/SKILL.md（可选：情节-心因双螺旋审核）
⬜ skills/script-structure-diagnosis-review-skill/SKILL.md（可选：剧本结构诊断审核）
⬜ skills/visual-language-logic-review-skill/SKILL.md（可选：视觉语法与剪辑审核）
✅ skills/compliance-review-skill/SKILL.md（合规审核）
```

### 集纲生成阶段
```
✅ skills/short-drama-architect-skill/SKILL.md（集纲架构师主技能）
✅ skills/genre-adaptive-skill/SKILL.md（类型适配技能）
⬜ skills/story-card-bridge/SKILL.md（脑洞来源时必须：故事卡桥接）
--- 审核 ---
✅ skills/short-drama-architect-review-skill/SKILL.md（业务审核）
✅ skills/genre-adaptive-review-skill/SKILL.md（类型适配结果审核）
⬜ skills/story-card-bridge-review-skill/SKILL.md（脑洞来源时必须：故事卡桥接审核）
✅ skills/compliance-review-skill/SKILL.md（合规审核）
```

### 剧本生成阶段
```
✅ skills/short-drama-scriptwriter-skill/SKILL.md（剧本转化主技能）
--- 审核 ---
✅ skills/short-drama-scriptwriter-review-skill/SKILL.md（业务审核）
⬜ skills/script-structure-diagnosis-review-skill/SKILL.md（可选：剧本结构诊断审核）
✅ skills/compliance-review-skill/SKILL.md（合规审核）
```

### 服化道设计阶段
```
✅ skills/art-design-skill/SKILL.md（服化道设计主技能）
   — 分段读取：第1-400行 ✅ + 第401-800行 ✅ + 第801-1188行 ✅
✅ skills/aesthetic-vision-skill/SKILL.md（五问法/体型矩阵/入镜规范/第7维度评分）
✅ skills/character-interaction-design-skill/SKILL.md（角色互动设计）
✅ skills/film-lighting-technique-skill/SKILL.md（电影质感光源技巧）
✅ skills/scene-concept-design-skill/SKILL.md（场景概念设计）
✅ skills/prop-concept-design-skill/SKILL.md（道具概念设计）
⬜ skills/costume-prop-character-design-skill/SKILL.md（可选：角色服化道与道具设计补充技能）
✅ skills/cinematic-character-pitch-board-skill/SKILL.md（🔴 全部角色必出·唯一角色标准：主角/重要配角完整六区块，次要/一次性/群演出精简提案板）
--- 审核 ---
✅ skills/art-direction-review-skill/SKILL.md（工业级融合版业务审核）
✅ skills/costume-prop-character-design-review-skill/SKILL.md（服化道角色道具设计审核）
✅ skills/cinematic-character-pitch-board-review-skill/SKILL.md（🔴 全部角色必出·唯一角色标准：电影级角色提案板审核）
✅ skills/character-interaction-design-review-skill/SKILL.md（角色互动设计审核）
✅ skills/film-lighting-technique-review-skill/SKILL.md（电影光影技巧审核）
✅ skills/compliance-review-skill/SKILL.md（合规审核）
--- 自动化校验 ---
✅ python3 tools/validators/t0-validator.py --batch --dir assets/prompts/
```

### 分镜编写阶段（🔴 所有 ✅ 项绝对不可跳过）
```
✅ resources/director-thinking-layer.md（🔴🔴 道层·导演工作法三尺度；机读层每条P必须承接对应P的①戏核/④转折/⑧表演与调度，并衔接2C组接）
✅ outputs/<集数>/01-director-analysis.md（🔴 戏核来源；若为空壳则禁止生成，回退导演阶段补"道"）
✅ skills/seedance-storyboard-skill/SKILL.md（T0工业级分镜主技能）
✅ skills/seedance-storyboard-skill/combat-enhanced-module.md（动作导演增强模块）
✅ skills/sovereign-duration-predictor-skill/SKILL.md（🔴 T0+++ 影视时长预测）
✅ skills/film-lighting-technique-skill/SKILL.md（电影质感光源技巧）
✅ tools/references/camera-movement-master.md（完整运镜工具箱）
✅ tools/references/cross-platform-converter.md（🔴 跨平台转换器）
✅ tools/references/quality-prechecker.md（实时质量预检系统）
✅ tools/references/style-preset-library.md（风格预设模板库）
✅ tools/references/emotion-quantization-system.md（情感量化与BGM同步系统）
✅ tools/references/multimodal-dynamic-fusion.md（多模态动态融合系统）
✅ tools/references/spatial-continuity-checker.md（🔴 全局空间锚点连续性检查）
✅ tools/references/ai-generation-predictor.md（🔴 AI视频生成效果预测）
✅ resources/unified-audiovisual-language-library.md（视听语言术层；🔴 先读「第零层」真实理论根基；"29条"为风格化速查非工业标准）
✅ resources/advanced-seedance-guide.md（高级 Seedance 2.0 指南）
✅ Seedance 2.0 情绪-微表情-语气增强模块.md（🔴 表演层增强：RHYTHM CURVE、微表情递进、台词语气参数化、小蔡6字段）
✅ Seedance_2.0_核心技能速查手册_6层堆栈_6字段_台词_微表情递进链(1).md（🔴 6层堆栈结构 + 6字段分镜格式 + 台词发声方式 + 微表情递进链速查）
✅ Seedance_2.0_情绪与语气提示词写法手册.md（🔴 情绪与语气统一写法：微表情嵌「主体动作/表情」、语气嵌台词`{}`前动作描写）
✅ Seedance_2.0_微表情物理描述素材库_100组(1).md（🔴 100组微表情物理化词库：面部肌肉物理指令替代抽象情绪词）
--- 审核（按平台逐一执行） ---
✅ skills/seedance-prompt-review-skill/SKILL.md（Seedance 业务审核）
⬜ skills/kling-prompt-review-skill/SKILL.md（Kling 2.6 业务审核 — 全局待用·不启用）
⬜ skills/kling-3.0-prompt-review-skill/SKILL.md（Kling 3.0 业务审核 — 全局待用·不启用）
✅ skills/sovereign-duration-predictor-review-skill/SKILL.md（🔴 时长校验审核）
⬜ skills/visual-language-logic-review-skill/SKILL.md（可选：视觉语法与剪辑审核）
✅ skills/compliance-review-skill/SKILL.md（合规审核）
```

### 脑洞生成阶段
```
✅ skills/brainworm-generator-skill/SKILL.md（脑洞生成主技能）
--- 审核 ---
✅ skills/brainworm-generator-review-skill/SKILL.md（业务审核）
⬜ skills/story-card-bridge-review-skill/SKILL.md（脑洞→集纲桥接审核，来源为脑洞时必须）
✅ skills/compliance-review-skill/SKILL.md（合规审核）
```

### 道具提取阶段
```
✅ skills/prop-concept-design-skill/SKILL.md（道具概念设计主技能）
✅ skills/costume-prop-character-design-skill/SKILL.md（角色服化道与道具设计）
--- 审核 ---
✅ skills/costume-prop-character-design-review-skill/SKILL.md（业务审核）
✅ skills/compliance-review-skill/SKILL.md（合规审核）
```

---

## 子规则 9-A：Skill 内容强制全文读取（🔴🔴🔴 最高铁律 — 不允许任何跳过）

> **核心原则：引用/调用任何 Skill 文件时，必须强制识别该文件内容的所有文字信息，一字不漏。不允许跳过、不允许抽样、不允许依赖记忆。**

### 强制读取三步规范

**第一步：确认文件总行数**
- 使用 `view_file` 读取 Skill 文件时，**先确认 `full_length` 总行数**
- 文件 ≤ 1000 行 → 一次性完整读取（不传 offset/limit）
- 文件 > 1000 行 → **必须分段读取，直至覆盖全部行**：
  ```
  第1次：view_file（offset=1, limit=500）
  第2次：view_file（offset=501, limit=500）
  第3次：view_file（offset=1001, limit=500）
  … 直到 offset + limit ≥ full_length
  ```

**第二步：逐段扫描所有文字内容**
- 每段读取后，**必须逐条提取该段内的强制要求、格式模板、评分标准、禁止项**
- 特别注意：Skill 文件中标注「强制」「🔴」「铁律」「禁止」「必须」的条款，**每一条都必须在后续产物中有对应体现**
- 禁止"扫一眼"——每一行都必须被理解和记录

**第三步：输出完整加载确认（强制格式）**
```
📋 Skill 加载确认（全文强制读取）：
✅ [全文已读] skills/xxx-skill/SKILL.md
   — 总行数：N 行 | 已读取：N 行（100%）
   — 强制要素清单：
     1. [要求1，原文位置：第X行]
     2. [要求2，原文位置：第X行]
     3. [禁止项1，原文位置：第X行]
     …（所有 🔴/强制/铁律 条款全部列出）
```

### 严禁行为（触发即产物作废，重新执行）

| 违规行为 | 后果 |
|---------|------|
| 仅在 Checklist 打勾但未实际读取文件 | 立即中止 → 产物作废 → 从头重新执行 |
| 凭记忆或推测声明"已加载" | 同上 |
| 只读取文件开头部分（覆盖率 < 100%）即停止 | 同上 |
| 超过 1000 行文件未分段读取 | 同上 |
| 加载确认中未列出所有 🔴/强制/铁律 条款 | 同上 |
| 产物中遗漏了 Skill 定义的强制字段 | 同上 |

### 常用大型 Skill 分段读取备忘

| Skill 文件 | 已知行数 | 分段方案 |
|-----------|---------|---------|
| `art-design-skill/SKILL.md` | 1188行 | 第1-400行 + 第401-800行 + 第801-1188行（3次） |
| `resources/unified-audiovisual-language-library.md` | ~642行 | 第1-400行 + 第401-642行（2次） |
| 其他 > 1000 行文件 | 运行时确认 | 每次500行，循环直至全文 |

---

## 子规则 9-B：输出后 Skill 合规审计（🔴 绝对铁律）

- 每个阶段生成完成后、进入审核前，必须执行 **Skill 合规审计**
- 审计方式：逐一对照每个已加载 Skill 中定义的强制输出要求，检查产物是否完整满足
- **审计四维度**：
  1. **格式合规**：输出格式是否符合 Skill 定义的模板/结构
  2. **内容完整**：Skill 要求的所有必须字段是否全部出现在产物中
  3. **规则遵循**：Skill 定义的禁止项是否全部未违反
  4. **工具调用**：Skill 要求调用的脚本/工具是否全部执行
- 审计发现缺失项 → 立即补充修复 → 重新审计 → 全部通过后才允许进入审核阶段

### 🔴 脚本化执行（强制优先，省 token）
本审计的四维度已脚本化，**不再由模型手工逐项打勾生成报告表**。每个阶段产出后运行：
```bash
python3 tools/validators/skill-compliance-auditor.py <ep> <阶段> --md
# 阶段：outline / script / director / style / design / storyboard
# 它会自动跑齐该阶段 workflow 规定的全部底层校验器（stage-output / t0 /
# pitch-board / beat-density / dialogue-sync / cross-file-consistency 等），
# 覆盖审计四维度（尤其「工具调用」维度），并直接渲染成 9-C 标准报告表。
# exit 1 即未通过 → 修复后重审，不得进入下一阶段。
```
模型只需阅读脚本输出的报告表，无需再消耗 token 通读产物全文自检格式/结构/工具调用。

### 🔴 一条龙编排（推荐入口，审计→放行→下一步全自动）
若希望"跑审计 + 通过即出下一步指令"一步到位，用编排器（零模型 token、不改状态文件）：
```bash
python3 tools/management/stage-pipeline.py <ep> <阶段key> [--path 路径一|路径二|路径三]
# 阶段key：outline / script / director / style / design / storyboard
# 行为：① 调 skill-compliance-auditor 跑齐该阶段全部校验器（9-C 报告）
#       ② 全 PASS → 自动调 next-step-prompter 输出下一步完整执行指令
#       ③ 有 FAIL → 中止并列出需修复项，不放行（fail-closed，exit 1）
```
模型仅需在"创作生成"与"审美/语义判断"两点介入，规则校验、放行判定、下一步指令派发全部脚本完成。

---

## 子规则 9-C：Skill 合规审计报告模板（强制使用）

```
📊 Skill 合规审计报告
阶段：[当前阶段名称]
产物文件：[输出文件路径]

| Skill 文件 | 核心要求 | 是否满足 | 证据/位置 |
|-----------|---------|---------|----------|
| skills/xxx/SKILL.md | [要求1] | ✅/❌ | [产物中的具体位置] |
| skills/yyy/SKILL.md | [要求1] | ✅/❌ | [产物中的具体位置] |
| ...       | ...     | ...     | ...      |

审计结论：✅ 全部通过 / ❌ 存在 N 项缺失（需修复后重审）
```

> 🔴 本报告表**应由 `skill-compliance-auditor.py --md` 自动生成**（见 9-B 脚本化执行），
> 而非手工填写。脚本输出的表头为「维度 / 对应 Skill / 工具 / 结果 / critical / 说明」，
> 与本模板等价并更精确（含每项 critical 计数与失败摘要）。

---

## 两步审核工作流

**流程**：`agent 生成 → 写入文件 → director 两步审核`

### 第一步：业务审核
加载阶段专属审核 Skill，按评分表输出结构化审核报告：

| 阶段 | 业务审核 Skill | 审核重点 |
|------|-------------|---------|
| 集纲生成 | short-drama-architect-review-skill | 3-10-60情绪循环、三段式结构、卡点设计 |
| 剧本生成 | short-drama-scriptwriter-review-skill | 绝对视觉化、场次划分、专业标签规范 |
| 导演分析 | script-analysis-review-skill | 叙事结构、讲戏质量、剧情完整性、视听语言逻辑 |
| 服化道设计 | art-direction-review-skill | 五大设计铁律、核心记忆点、形状语言、T0合规评分（第7维度≥12分） |
| Seedance 分镜 | seedance-prompt-review-skill | Seedance 2.0 规范、运镜/节奏合理性、叙事连贯性 |
| Kling 2.6 分镜 | kling-prompt-review-skill | Kling 2.6 规范、音画协同、音频设计、时长选择 **（全局待用·不启用）** |
| Kling 3.0 分镜 | kling-3.0-prompt-review-skill | 智能分镜、主体参考、15秒超长生成规范 **（全局待用·不启用）** |

### 第二步：合规审核
- 加载 `skills/compliance-review-skill/SKILL.md`
- 检查内容：真人限制、版权IP、政治敏感、色情/暴力尺度、平台红线

### 汇总反馈规则
- 两步全 PASS → 进入下一阶段
- 任一 FAIL → **合并所有修改意见** → agent 一次性修改 → 覆盖写入 → director 重新两步审核 → 循环直到全 PASS
- **目的**：agent 一次拿到所有问题（业务 + 合规），避免反复修改

### 审核输出协议（强制）
- 业务审核必须严格使用对应审核 Skill 的评分表 + PASS/FAIL 模板输出
- 合规审核必须严格使用 compliance-review-skill 的 PASS/FAIL 模板输出
- 不允许使用"简要说明通过原因"替代评分表
- 最终汇总必须包含：业务结论、合规结论、是否进入下一阶段

---

## Resumable Subagents 机制

**目的**：确保每个 subagent 的上下文连续，避免重复理解和丢失信息。

### .agent-state.json 标准结构
> 🔴 agentId 直接挂在 `episodes.<集数>` 顶层（与「调用规则」`episodes.<集数>.<agent-name>` 一致），**不使用 `agents` 嵌套层**。
```json
{
  "activeEpisode": "ep01",
  "projectName": "项目名",
  "workflowPath": "路径一",
  "visualStyle": "风格名称（中文 / English）",
  "episodes": {
    "ep01": {
      "director": "<agentId>",
      "art-designer": "<agentId>",
      "storyboard-artist": "<agentId>",
      "currentStage": "导演分析-completed",
      "stageHistory": ["导演分析-completed"]
    },
    "ep02": {
      "director": "",
      "art-designer": "",
      "storyboard-artist": "",
      "currentStage": "",
      "stageHistory": []
    }
  }
}
```

### stageHistory / currentStage 标准枚举（🔴 强制统一）
> 统一格式：`<阶段中文名>-<状态英文>`；状态后缀只用 `completed` / `inherited` / `in-progress`（**禁止 complete 无 d、禁止中英混搭一个枚举两种写法**）。

| 阶段 | 标准取值 |
|------|---------|
| 导演分析 | `导演分析-completed` |
| 视觉风格选择 | `视觉风格选择-completed`（首集）/ `视觉风格选择-inherited`（ep02+ 继承）|
| 服化道设计 | `服化道设计-completed` |
| 分镜编写 | `分镜编写-completed` |
| 集间交接 | `集间交接-completed` |

### 调用规则
> 🔴 agentId 口径（与 CLAUDE.md「Resumable Subagents 机制」一致，单一权威）：
> agentId **只在当前运行会话内有效，不跨会话/重启持久化**；`episodes.<集数>.<agent-name>` 三字段
> 仅作**会话内可选缓存，默认留空、为空是正常状态**，跨会话不读它。
> **跨会话 / 跨集 / 回改的连续性靠「上下文快照」**（`python3 tools/generators/context-snapshot-generator.py <ep>`），
> 而非 agentId 持久化。真正的阶段进度真值是 `currentStage / stageHistory`。

- **同一集内首次调用 subagent**：正常调用；runtime 返回的会话内 agentId 可选缓存到 `episodes.<集数>.<agent-name>`（不必写盘，跨会话无效）
- **同一集内后续调用同一 subagent**：用会话内 agentId → `Resume agent <agentId> and ...`
- **跨集 / 跨会话 / 回改**：不依赖 agentId；先加载目标集上下文快照还原硬约束，再以全新会话执行
- **跨集时**：不清空旧集记录，仅创建新集空槽位并更新 `activeEpisode`

### 旧结构迁移（若检测到旧结构）
若 `.agent-state.json` 顶层仅有 `director/art-designer/storyboard-artist` 三个键（旧格式），自动迁移为新结构：
1. `activeEpisode` 设为当前处理集数
2. 将旧键值写入 `episodes.<activeEpisode>.<agent-name>`
3. 旧结构字段迁移后不再写入

---

## 跨集继承与 assets 本集标记规范

### assets 素材标记格式（强制）
```
角色文件：## [epNN][character][新增|变体|复用] 角色名
场景文件：## [epNN][scene][新增|变体|复用] 场景名
道具文件：## [epNN][props][新增|变体|复用] 道具名
```

- **新增**：本集首次出现的角色/场景/道具
- **变体**：已有素材的外观/状态变化（如受伤、换装）
- **复用**：直接继承前集素材，无变化（可只记录索引，不重复全文）

### ep02+ 跨集继承规则
- **视觉风格**：ep02+ 跳过视觉风格选择阶段，直接继承 ep01 的 `assets/visual-style-guide.md`
- **角色一致性**：每集导演分析时必须读取 `assets/character-bible.md` 确保角色外观不漂移
- **道具一致性**：`cross-episode-consistency-checker.py` 每集分镜完成后必须运行
- **钩子交接**：每集结尾钩子必须在下一集集间交接摘要中明确标注

---

## 项目状态检测与路由

**初始化时自动检测项目进度，路由到对应阶段**：

### 单集进度判断逻辑
| 文件状态 | 路由到 |
|---------|-------|
| `outputs/ep01/` 不存在或为空 | 导演分析阶段 |
| 有 `01-director-analysis.md`，assets/ 中无本集标签（ep01新增）| 服化道设计阶段 |
| assets/ 中有本集标签，无 `02-seedance-prompts.md` | 分镜编写阶段 |
| 有 Seedance + 文字分镜 | 该集已完成（Kling 全局待用·不启用） |

### 项目进度报告格式
```
📊 项目进度检测

小说文件（novel/ 目录）：[文件列表]
当前集数：ep01
当前阶段：[阶段名称]
Agent 状态：[已恢复 / 全新会话]

下一步：[具体操作指令]
```

### 集数识别规范
- 标准格式：`epNN`（NN 为两位数字，如 ep01、ep02）
- 兼容输入：`ep1` / `EP01` / `Ep02`（统一归一化为 ep01/ep02）
- 识别正则：`(?i)\bep\s*0*([1-9]\d?)\b`
- 排序规则：按数值升序（ep2 < ep10）

---

## 各阶段详细执行流程

> 以下为每个阶段的完整分步执行规范，必须严格按步骤执行，不允许跳过任何步骤。

---

### 小说分析阶段 — 完整执行流程（路径一专属）

收到 `~analyze [小说文本]` 或 `~full [小说文本]` 触发路径一时：

**第一步：确定输入源**
1. 用户直接输入小说文本 → 使用用户输入
2. 未输入 → 扫描 `novel/` 目录，读取所有 .txt 文件（支持两种格式）：
   - 单一文件：`novel/novel.txt`
   - 多集分章：`第一集.txt ~ 第N集.txt`（按文件名自然排序合并）
3. `novel/` 无 txt 文件 → 提示用户上传小说文件

**第二步：调用 融合模块（chuanban-chaishu-skills）执行小说分析**
1. 必须参考 `融合模块/chuanban-chaishu-skills/` 下的相关 Skill
2. 执行分析流程（按顺序）：
   - **拆分**：识别章节结构，逐章拆分为独立 .md 文件
   - **概括**：每3章一组生成内容概括
   - **人物**：提取人物关系图谱（角色地位/关系/能力）
   - **事件线**：提取关键事件时间线
   - **ABC爽点分析**：按 A（外部冲突）/B（内部成长）/C（浪漫/情感）分类提取爽点
3. 生成完成后写入：`assets/novel-analysis/{书名}/`

**第三步：输出结构规范**
```
assets/novel-analysis/{书名}/
├── 拆分/              每章节独立 .md 文件（001_第1章.md …）
├── 概括/              分组概括（组1_第1-3章_概括.md …）
├── ABC爽点分析_ch1-X.md
├── 事件线追踪_ch1-X.md
├── 人物关系分析_ch1-X.md
├── 人物和设定/        角色地位.yaml + 关系图谱.yaml
├── 全书概括.md
├── 剧本结构诊断报告_ch1-X.md
├── 合规审核报告_ch1-X.md
└── 融合分析报告.yaml  综合汇总（供集纲生成读取）
```

**第四步：质量门禁**
- 章节识别率 ≥ 90%
- B完整度合格率 ≥ 80%
- 合规审核报告 PASS（无🔴必须修改项）

**第五步：与集纲生成衔接**
```
✅ 小说分析已完成！已保存至：assets/novel-analysis/{书名}/
包含：{N}章节拆分 + 分组概括 + 人物关系 + 事件线 + ABC爽点 + 剧本结构诊断 + 合规审核
→ 输入 ~outline 进入集纲生成阶段（将读取融合分析报告.yaml作为输入）
```

**注**：`~analyze` 仅执行小说分析，不进入视频制作；`~analyze-full` = 小说分析 + 完整视频制作流程。

---

### 视觉风格选择阶段 — 完整执行流程

**触发条件**：导演分析完成后（首集必须执行；ep02+ 直接继承 ep01，跳过本阶段）

收到 `~style` 或由 `~full`/`~start` 自动触发：

**第一步：向用户询问视觉风格（首集必做）**

```
🎨 请选择视觉风格与目标媒介

Q1：视觉风格（从预设选择或自由描述）：

【极致动漫美学（推荐短剧）】
- 扳机社/赛博张力：Studio Trigger style, hyper-dynamic angle, high-contrast neon
- 飞碟社/极致光污染：Ufotable style, hyper-realistic CGI VFX, massive glowing particles
- 顶级韩漫/暗黑大男主：Korean Webtoon style, Solo Leveling, dark shadowy aura
- 90年代复古/蒸汽波：90s retro anime, VHS filter, muted pastel, CRT scanlines
- MAPPA/混沌暴力美学：MAPPA style, cinematic fisheye, sketchy line art, gritty texture
- 京阿尼/极致微观光影：Kyoto Animation, photographic lighting, hyper-detailed sparkling eyes
- 吉卜力/治愈系手绘：Studio Ghibli, hand-painted watercolor, soft sunlight
- 新海诚/极致环境壁纸：Makoto Shinkai, breathtaking twilight, gorgeous lens flare

【通用风格】
- 真人写实：Photorealistic style, cinema-grade lighting
- 国漫：Chinese anime style, elegant brush strokes
- 日漫：Japanese anime style, vibrant colors
- 3D CG/皮克斯：3D CGI Pixar style, clean geometry
- 迪士尼：Disney style, whimsical, colorful

【色彩分级】
- 青橙色调 / 赛博朋克 / 柯达胶片 等

也可自由描述风格（如：吉卜力水彩质感，色彩饱和度偏低，线条柔和，胶片颗粒感...）

Q2：目标媒介（电影 | 短剧 | 漫剧 | MV | 广告）
```

用户确认后才能进入第二步，禁止跳过。

**第二步：调用 visual-style-selector 生成**
1. 必须参考 `skills/visual-style-selector-skill/SKILL.md`
2. 检查 agentId → Resume 或新建，记录 agentId
3. 传入用户确认的视觉风格 + 目标媒介
4. 生成完成后写入 `assets/visual-style-guide.md`

**第三步：视觉风格规范文档内容（强制包含）**
```
assets/visual-style-guide.md 必须包含：

**主风格**：[风格名称]
**子风格**：[子风格名称]
**目标媒介**：[媒介类型]

**色彩基调**：
- 主色调：[颜色+色值]
- 辅助色：[颜色+色值]
- 强调色：[颜色+色值]
- 色温：夜间[X]K / 日间[X]K / 特殊场景[X]K

**全局风格前缀**（Seedance版本）：
[纯英文，可直接前置到每条Seedance提示词]

**全局风格前缀**（Kling版本）：
[纯英文，Kling格式]

**场景光影规范**：[每类场景的光源/色温/光比规范]
**禁止事项**：[与风格不符的视觉元素]
```

**第四步：两步审核**
1. 第一步业务审核：`Resume director agent and 使用 visual-style-selector-review-skill 审核`
2. 第二步合规审核：`Resume director agent and 使用 compliance-review-skill 审核`
3. 全 PASS → 下一步；任一 FAIL → 修改 → 重审

**第五步：强制校验**
```bash
python3 tools/validators/cross-file-consistency-checker.py <ep>
```

**第六步：通知用户**
```
✅ 视觉风格规范已生成！已通过审核
已保存至：assets/visual-style-guide.md
风格：[风格名称] | 媒介：[媒介类型]
→ 输入 ~design 进入服化道设计
```

**ep02+ 跨集继承规则**：
- ep02+ 直接读取 `assets/visual-style-guide.md` 继承视觉风格
- **不重新执行本阶段**
- 每集服化道设计时需注明"继承自 ep01"

---

### 脑洞生成阶段 — 完整执行流程

收到 `~brainworm` 或 `~brainworm [点子]` 指令后：

**第一步：点子解析**
分析用户输入的原始点子，提取：
- 核心题材类型（豪门/玄幻/都市/系统/甜宠/虐恋等30+种）
- 核心冲突元素
- 预期受众定位

**第二步：调用 brainworm-generator 生成**
1. 必须参考 `skills/brainworm-generator-skill/SKILL.md`（脑洞生成主技能）
2. 必须参考 `skills/brainworm-generator-review-skill/SKILL.md`（业务审核）
3. 必须参考 `skills/compliance-review-skill/SKILL.md`（合规审核）
4. 检查 `.agent-state.json` 是否有 `brainworm-generator` 的 agentId
5. 如有：`Resume agent <agentId> and 生成脑洞扩展`
6. 如无：`Use brainworm-generator agent to 生成`，并记录返回的 agentId
7. 生成完成后，按项目名创建目录写入 `brainworm/{项目名}/`

**第三步：脑洞输出内容规范**

```
**世界观扩展**（时代背景 + 核心规则 + 势力分布）

**核心梗**（核心卖点×3 + 情绪钩子×3（3秒/10秒/1分钟）+ 卡点设计）

**人设卡片**：
- 主角人设（身份+标签+视觉特征+人物弧光+金手指）
- 反派人设（身份+特征+压迫点+结局设计）
- 配角人设（身份+特征+功能定位）

**故事卡**：
- 主线故事卡（核心冲突+目标+障碍+转折）
- 支线故事卡（功能+与主线关系）

**集数规划**：
- 动态集数三段式分布（按本章内容规划集数；示例10集：蓄能期1-3 / 加压期4-7 / 升级期8-10，按总集数 1/3 均分）
```

**第四步：与集纲生成的衔接**
脑洞生成完成后，可直接进入集纲生成阶段：
- `~outline`：读取 `brainworm/{项目名}/` 下的文件生成集纲

**第五步：通知用户**
```
✅ 脑洞扩展已完成！
已保存至：brainworm/{项目名}/
包含内容：世界观扩展.md / 人设卡片.md / 核心梗.md / 故事卡.md / 集数规划.md
如有修改意见可以直接提出，没有的话 → 输入 ~outline 进入集纲生成阶段
```

---

### 道具与金手指提取阶段 — 完整执行流程

收到 `~prop` 或 `~prop [小说文本]` 指令后：

**第一步：确定输入源**
1. 用户直接输入小说文本 → 使用用户输入
2. 未输入 → 扫描 `novel/` 目录，读取所有 .txt 文件
3. `novel/` 无 txt 文件：提示用户上传小说文件

**第二步：调用 art-designer 生成**（道具与金手指提取由 art-designer 承担）
1. 必须参考 `skills/prop-concept-design-skill/SKILL.md`
2. 必须参考 `skills/costume-prop-character-design-review-skill/SKILL.md`（业务审核）
3. 必须参考 `skills/compliance-review-skill/SKILL.md`（合规审核）
4. 检查 agentId → Resume 或新建 agent，记录返回的 agentId
5. 生成完成后，写入 `assets/prompts/props-prompts.md`

**第三步：提取输出格式规范**

```
道具提取：
📦 道具：{道具名称}
- 原文描述：{提炼原文中关于该道具的描述}
- 视觉特征：外观、颜色、材质、光效
- 功能设定：{该道具在小说中的作用}
- 🎨 绘画提示词：{英文 Prompt}

金手指提取：
🌟 金手指/系统：{系统名称}
- 核心机制：{一句话总结核心功能}
- 展现形式：{视网膜全息面板/脑海声音/异化器官等}
- 🎨 视觉提示词：{英文 Prompt}
- 📝 系统设定Prompt：{可直接喂给大模型的 Prompt}
```

**第四步：通知用户**
```
✅ 道具与金手指提取完成！
已保存至：assets/prompts/props-prompts.md
包含：X个道具提取 + X个金手指提取（含英文绘画提示词 + 系统设定Prompt）
→ 输入 ~outline 进入集纲生成阶段
```

---

### 集纲生成阶段 — 完整执行流程

**3-10-60 情绪循环算法（本阶段强制遵循）**

| 节点 | 要求 |
|------|------|
| **前3秒钩子** | 极致视觉奇观/肢体冲突/反常态画面，瞬间抓眼球 |
| **前10秒叙事** | 快速交代人物关系、核心矛盾、解释前3秒起因 |
| **1分钟爽点** | 完整情绪释放（反派被打脸/误会解开/武力镇压） |
| **卡点钩子** | 截断在最高潮前0.5秒，绝不提供完整闭环 |

收到 `~outline` 指令后：

**第一步：确定输入源**
1. 用户直接输入小说文本 → 使用用户输入
2. 未输入 → 扫描 `novel/` 目录（支持单一文件 `novel.txt` 或多集分章 `第一集.txt~第N集.txt`）
3. 🔴 **必须向用户确认本章计划生成几集**（不允许默认使用固定集数）

**第二步：调用 short-drama-architect 生成**
1. 传入爆款短剧核心算法指导（3-10-60情绪循环 + 绝对视觉化原则）
2. 必须参考 `skills/short-drama-architect-skill/SKILL.md`
3. 必须参考 `skills/genre-adaptive-skill/SKILL.md`（类型适配，根据小说类型自动适配叙事模板）
4. 如来源是脑洞扩展：必须参考 `skills/story-card-bridge/SKILL.md`（故事卡桥接）
5. 检查 agentId → Resume 或新建，记录 agentId
6. 生成完成后，写入 `assets/outline/{chXX}-outline.md`

**第三步：集纲每集输出格式（强制）**
```
第X集：[四字高能词]
故事梗概：（对应小说第X-X章）[一句话概括]
情绪循环：
  【前3秒钩子】[最具冲击力的起幅画面]
  【前10秒叙事】[人物关系与矛盾背景]
  【1分钟爽点】[核心冲突爆发与爽点落地]
精彩台词：[角色]："[极具张力的一句话]"
卡点钩子：[悬念设置]
```

**第四步：通知用户**
```
✅ 集纲已完成！已保存至：assets/outline/{chXX}-outline.md
包含：三段式情绪周期规划（蓄能期/加压期/升级期）+ 每集3-10-60标准集纲 + 终极卡点设计
→ 输入 ~script 进入剧本生成阶段
```

---

### 剧本生成阶段 — 完整执行流程

**绝对视觉化剥离原则（去心理化铁律，本阶段强制遵循）**
- ❌ 禁止：心理描写、内心独白、抽象情感描述
- ✅ 强制：所有心理活动外化为具体肢体动作、微表情或破坏性物理交互
- 示例：
  - ❌ 禁止写："他感到极其愤怒"
  - ✅ 必须写："▲他眼眶猩红，猛地一拳砸塌实木桌子"

收到 `~script` 指令后：

**第一步：检查前置文件**
检查 `assets/outline/{chapter}-outline.md` 是否存在，不存在则提示先完成集纲生成。

**第二步：调用 short-drama-scriptwriter 生成**
1. 传入绝对视觉化剥离原则指导
2. 必须参考 `skills/short-drama-scriptwriter-skill/SKILL.md`
3. 必须参考 `skills/short-drama-scriptwriter-review-skill/SKILL.md`（业务审核）
4. 必须参考 `skills/compliance-review-skill/SKILL.md`（合规审核）
5. 检查 agentId → Resume 或新建，记录 agentId
6. 生成完成后，写入 `assets/novel/{chapter}-script.md`

**第三步：专业影视标签规范（强制）**
| 标签 | 用途 |
|------|------|
| `▲ [动作描述]` | 动作白描标记 |
| `▲特写：[画面描述]` | 特写镜头标记 |
| `【切镜】` | 场景转换标记 |
| `"砰——"一声巨响` | 音效标注（双引号包裹） |
| `▲黑屏。` | 黑屏截断（卡点收尾） |

**第四步：场次划分要求**
```
[场次编号] [日/夜] [内/外] [具体场景名称]
人物：[角色A]、[角色B]
【人名条：姓名｜身份】
▲[动作白描]
角色A："[台词]"
```

**第五步：强制校验（顺序执行，不可跳过）**
```bash
python3 tools/validators/plot-fidelity-checker.py <ep> --chapter <ch>
# 覆盖率 < 100% → exit 1 → 必须重新生成剧本

python3 tools/validators/novel-dialogue-fidelity-checker.py <ep> --chapter <ch>
# 任何"改动"或"未找到" → 必须修正后重跑
```

**第六步：通知用户**
```
✅ 短剧剧本初稿已完成！已保存至：assets/novel/{chapter}-script.md
包含：每集2-4个核心场次 + 绝对视觉化白描 + 专业影视标签 + 极限卡点收尾
→ 输入 ~start 进入导演分析阶段
```

---

### 导演分析阶段 — 完整执行流程

**爆款短剧逻辑融合（自动执行）**

| 设计点 | 要求 |
|--------|------|
| 黄金3秒钩子 | 每个剧情点开篇必须有强视觉冲击或悬念（极致视觉奇观/肢体冲突/反常态画面） |
| 前10秒叙事 | 快速展示钩子引发的后果和人物应激反应 |
| 情绪高潮点 | 剧情点中段推向情绪高潮（反派被打脸/武力镇压/绝地反击） |
| 卡点钩子 | 结尾停留在危机/悬念边缘，截断在最高潮前0.5秒 |
| 标签化人设 | 人物外观需有视觉反差标签 |
| 绝对客观视角 | 只记录摄像机能拍到的，禁止内心独白 |

**视听语言层次（自动融合）**
- **基础级（5条）**：轴线原则/屏幕方向/30度原则/视线匹配、动接动/静接动冲击、光影叙事/色温对立、焦段心理隐喻、J-Cut/L-Cut/声画对位
- **进阶级（好莱坞T0 9大维度）**：物理动力学、构图与权力、神经劫持、语义与深度、生物本能、情感熵、意志延伸、神格化、非人境

收到 `~start` 或 `~start <集数>` 指令后：

**第一步：收集基本信息（首集必做）**
向用户询问：
```
Q1：视觉风格（从预设选择或自由描述）
预设选项：扳机社赛博张力 / 飞碟社极致光污染 / 顶级韩漫暗黑大男主 /
MAPPA混沌暴力美学 / 京阿尼极致微观光影 / 吉卜力治愈系手绘 /
新海诚极致环境壁纸 / 真人写实 / 国漫 / 日漫 / 3D CG皮克斯 / 迪士尼 /
90年代复古蒸汽波 等，也可自由描述

Q2：目标媒介（电影 | 短剧 | 漫剧 | MV | 广告）
```

**第二步：确定目标集数**
1. 用户指定集数（如 `~start ep01`）→ 使用指定集数
2. 未指定 → 使用项目状态检测确定的当前集数

**第三步：调用 director 执行分析**
1. 检查 `.agent-state.json` 是否有 `director` 的 agentId
2. 如有：`Resume agent <agentId> and 分析剧本（指定集数，传入项目配置）`
3. 如无：`Use director agent to 分析剧本`，记录返回的 agentId
4. 生成完成后，写入 `outputs/<集数>/01-director-analysis.md`

**第四步：导演两步自审**
1. 第一步业务审核：`Resume director agent and 使用 script-analysis-review-skill 审核 01-director-analysis.md`
2. 第二步合规审核：`Resume director agent and 使用 compliance-review-skill 审核 01-director-analysis.md`
3. 汇总两轮反馈：
   - 全 PASS → 进入下一步
   - 任一 FAIL → 合并修改意见 → Resume director 修改 → 覆盖写入 → 回到第四步重审

**第五步：通知用户**
```
✅ 导演分析已完成！已通过业务审核和合规审核
已保存至：outputs/<集数>/01-director-analysis.md
人物清单：[列出人物名]
场景清单：[列出场景名]
如有修改意见可以直接提出，没有的话 → 输入 ~design 进入服化道设计
```

---

### 服化道设计阶段 — 完整执行流程

**Nano Banana Pro 单版本输出规范（强制 · 唯一版本）**

> 🔴 当前服化道提示词**只输出 Nano Banana Pro 一个版本（中文段 + 英文段分离）**；B版本（MJ纯英文）已暂停启用。

| 版本 | 用途 | 格式 |
|------|------|------|
| **Nano Banana Pro** | Nano Banana Pro、即梦等支持中英文混合输入的工具 | 中文段 + 英文段两段分离输出 |
| ~~B版本 MJ纯英文~~ | ~~Midjourney、DALL-E~~ | ⏸️ 暂停启用 |

每个角色/场景/道具必须输出 Nano Banana Pro 中英分离版本（🔴 中英分离＝通用提示词格式；**角色**的两段正文须描述「电影级角色提案板」六区块、非泛化单图，见阶段八「电影级角色提案板强制要素」）：
```
### Nano Banana Pro（中英文）

**【中文描述段】**
[纯中文一整段，不夹杂英文术语，自然语言叙事]

**【英文描述段】**
[纯英文一整段，不换行，包含所有技术关键词和渲染参数]
```

**工业级角色设计方法论（五大设计铁律）**
1. **辨识度铁律**：所有设计必须有且仅有1个核心记忆点，单点极致
2. **可信度铁律**：幻想设计必须基于「功能→结构→造型」逻辑推导
3. **情绪优先铁律**：所有造型语言最终服务于角色的情绪与叙事表达
4. **落地适配铁律**：设计必须匹配应用场景（短剧/动画/游戏）
5. **技术实现铁律**：考虑 PBR 材质、拓扑约束、绑定需求的可实现性

**形状语言设计系统**
| 形状 | 情感语义 |
|------|---------|
| 圆形 | 友好、柔软、可爱（圆润线条） |
| 方形 | 稳定、可靠、力量（硬朗线条） |
| 三角形 | 危险、锐利、侵略（尖锐元素） |
| S形曲线 | 优雅、柔美、流动（波浪线条） |
| 锯齿线 | 狂暴、混乱、痛苦（破碎元素） |

**AI 绘画公式（必须遵循）**
- **角色公式**：`[纯白背景隔离] + [精美排版：多视图/表情集/服饰拆分] + [角色身份] + [材质引擎/AO/PBR] + [微观面部细节] + [T0级画质后缀]`
- **场景公式**：`[光学镜头指定] + [构图法则] + [核心环境] + [时间天气与胶片色彩] + [全局光照/丁达尔效应] + [T0级渲染后缀]`
- **道具公式**：`[纯白背景隔离] + [道具/机甲主体] + [爆炸拆解视图] + [硬表面材质与战损] + [微距/等距视角] + [T0级画质后缀]`
- **极致动漫公式**：`[顶级工作室画风指定] + [角色极度张力姿态] + [色彩与笔触美学] + [光影与VFX特效] + [背景环境] + [T0级二次元画质后缀]`

**高精度模式（默认）**
- 人物：8视图布局（正面/背面/左侧/右侧）+ 4个角度特写细节
- 场景：宫格图 + 材质与工艺规范 + 光影规范
- 适合建模参考需求

收到 `~design` 或 `~design <集数>` 指令后：

**第一步：确定目标集数并检查前置文件**
1. 检查 `outputs/<集数>/01-director-analysis.md` 是否存在（不存在 → 提示先完成导演分析）
2. 🔴 **必须先询问用户服化道设计类型**（视觉风格 + 目标媒介），用户确认后才能进入下一步

**第二步：调用 art-designer 生成（传入用户确认的设计类型）**
1. 必须参考 `skills/art-design-skill/SKILL.md`（分段读取：1-400行 + 401-800行 + 801-1188行）
2. 必须参考 `skills/art-direction-review-skill/SKILL.md`（业务审核）
3. 必须参考 `skills/compliance-review-skill/SKILL.md`（合规审核）
4. 如 `assets/prompts/props-prompts.md` 存在：必须读取道具提示词，融入服化道设计
5. 必须参考 `resources/AI绘画终极提示词工程白皮书.md`（T0级工业商用提示词规则）
6. 检查 agentId → Resume 或新建，记录 agentId
7. 生成完成后，按 assets 本集标记规范追加写入：
   - `assets/prompts/character-prompts.md`
   - `assets/prompts/scene-prompts.md`
   - `assets/prompts/props-prompts.md`
   - `assets/character-bible.md`（角色外观快照，步骤5.5，≤600 tokens）

**第三步：导演两步审核**
1. 第一步业务审核：`Resume director agent and 使用 art-direction-review-skill 审核本集新增内容`
2. 第二步合规审核：`Resume director agent and 使用 compliance-review-skill 审核本集新增内容`
3. 全 PASS → 下一步；任一 FAIL → 合并修改意见 → Resume art-designer 修改 → 覆盖写入 → 回到第三步重审

**第四步：强制自动化校验（顺序执行）**
```bash
python3 tools/validators/t0-validator.py --batch --dir assets/prompts/
# 任何项 < 100/100 → 必须修正后重跑

python3 tools/validators/cross-file-consistency-checker.py <ep>
python3 tools/generators/context-snapshot-generator.py <ep>
```

**第五步：通知用户**
```
✅ 服化道设计已完成！已通过导演审核
已保存至：
- assets/prompts/character-prompts.md（Nano Banana Pro 中英分离）
- assets/prompts/scene-prompts.md（Nano Banana Pro 中英分离）
- assets/prompts/props-prompts.md（Nano Banana Pro 中英分离）
- assets/character-bible.md（角色快照）
请使用以上提示词在文生图工具生成参考图，完成后输入 ~prompt 进入分镜编写
```

---

### 分镜编写阶段 — 完整执行流程

**平台支持规范**

| 平台 | 输出文件 | 特点 | 状态 |
|------|---------|------|------|
| **Seedance 2.0** | `02-seedance-prompts.md` | 纯视觉，需单独生成音频 | ✅ 启用 |
| **Kling 2.6** | `02-kling-prompts.md` | 音画同出，【场景】【主体】【音频】结构，5s/10s | ⬜ 全局待用 |
| **Kling 3.0** | `02-kling-3.0-prompts.md` | 智能分镜（镜头1/镜头2触发）+ @主体标签 + 5s/10s/15s | ⬜ 全局待用 |

**T0工业级核心要求（分镜编写时必须逐条遵循）**
1. **空间坐标锚点**（强制）：建立3D坐标系，标注原点和方向基准
2. **视线对焦 Eye-line**（强制）：180度锁死，越轴必须标注
3. **T+时间轴**（强制）：0.5秒精度，衔接锚点必须一致
4. **分镜数量**（强制）：每集 ≥10条，密度公式 `round(字数/1000×12)`
5. **T0视听语言**（强制）：物理动力学/构图权力/神经劫持/情感熵 全部融入

**T0审核评分体系（分镜完成后必须输出）**
- **9维度评分**：忠实度/画面还原/动作可执行/镜头可实现/视听语法/平台适配/音频设计/情绪准确/连贯性
- **通过标准**：平均分 ≥8，无单项低于 6

收到 `~prompt` 或 `~prompt <集数>` 指令后：

**第一步：确定目标集数并检查前置文件**
检查以下文件是否全部存在：
- `outputs/<集数>/01-director-analysis.md`
- `assets/prompts/character-prompts.md`
- `assets/prompts/scene-prompts.md`
- `assets/prompts/props-prompts.md`

缺少任一文件 → 提示先完成对应阶段，不得跳过。

**第二步：确定目标平台（默认 seedance）**

| 参数 | 生成内容 | 状态 |
|------|---------|------|
| `seedance`（默认） | 仅生成 Seedance 2.0 | ✅ 启用 |
| `kling2` | 仅生成 Kling 2.6 | ⬜ 全局待用 |
| `kling3` | 仅生成 Kling 3.0 | ⬜ 全局待用 |
| `kling` | Kling 2.6 + Kling 3.0 | ⬜ 全局待用 |
| `both` / `all` | Seedance 2.0 + Kling 2.6 + Kling 3.0 | ⬜ 全局待用 |

**第三步：参考图就绪确认（必做）**
1. 明确提示用户：场景宫格图必须先拆格为独立场景图再进入分镜编写
2. 检查素材对应是否满足"人物独立图 + 场景独立图"引用条件
3. 如未就绪：提示先完成文生图与拆格，不进入分镜生成

**第四步：预算预检（必做）**
1. 先生成"单条提示词预算表"（逐条统计图片/视频/音频/总文件数）
2. 任一条超限 → 先拆分剧情点或减少引用后再继续
3. 预算全部通过后，才允许进入分镜生成

**第四步半：T0+++ 时长预测（必做，生成前强制执行）**
1. 调用 `sovereign-duration-predictor-skill` 执行时长预测
2. 输入：场景文本 + 目标时长
3. 执行：资产扫描 → 时长精算 → 显微镜拆解
4. 输出：主权报告（预测时长/资产增殖倍率/显微镜拆解清单）
5. 校验：预测时长覆盖率 ≥ 90% → 允许开始编写；否则执行扩张直到满足

**第五步：调用 storyboard-artist 生成**
1. 检查 agentId → Resume 或新建，记录 agentId
2. 根据目标平台分别调用并生成对应文件
3. ⚠️ **编写完成后立即自动进入第六步审核，无需用户确认**

**第六步：导演三步审核（自动执行，生成完成后立即触发）**
针对每个已生成的平台分别执行：
```
Seedance 2.0：
  1. 第一步业务审核：seedance-prompt-review-skill
  2. 第二步合规审核：compliance-review-skill
  3. 🔴 第三步时长校验：sovereign-duration-predictor-review-skill

# Kling 2.6：全局待用，不启用
# Kling 3.0：全局待用，不启用
```
- 全 PASS → 进入第七步
- 任一 FAIL → 合并修改意见 → Resume storyboard-artist 修改 → 覆盖写入 → 回到第六步重审

**第七步：强制自动化校验（审核通过后顺序执行）**
```bash
python3 tools/validators/beat-density-checker.py <ep>
# exit 1（有 critical P块）→ 必须拆分/重写后重跑，直到 0 个 critical

python3 tools/validators/stage-output-validator.py <ep> storyboard
python3 tools/validators/cross-file-consistency-checker.py <ep>
python3 tools/generators/context-snapshot-generator.py <ep>
python3 tools/validators/novel-fidelity-checker.py <ep>
python3 tools/management/episode-progress-reporter.py <ep>
```

**第八步：通知用户（审核通过后自动执行）**
```
✅ 提示词已完成！已通过导演审核并保存至：
- outputs/<集数>/02-seedance-prompts.md（Seedance 2.0）
- outputs/<集数>/03-text-storyboard.md（文字分镜稿）
（Kling 2.6/3.0 全局待用，未生产）
🎉 该集全部工作已完成！
如有修改意见可以直接提出，没有的话 → 输入 ~status 查看进度
```

**第九步：多集流转（自动检测）**
```
如果 novel/ 中还有未处理的集数：
📺 ep<当前集> 已完成，是否进入 ep<下一集>？
输入 继续 进入下一集，或输入其他指令。
```
用户确认后 → 开始下一集的导演分析阶段。

---

### 内容修订流程

当用户在任何阶段提出修改意见时：

1. 判断修改影响哪个阶段的产物
2. 若修改目标不是 `activeEpisode`，先切换 `activeEpisode` 到目标集数
3. Resume 对应 agent 进行修改
4. 覆盖写入对应文档
5. Resume director agent 执行两步审核（业务 + 合规）
6. 循环直到全 PASS
7. 通知用户

```
✅ 内容已更新并保存！
修改影响范围：
- 已更新文档：[文件名]
```

---

## 完整指令集参考

> 所有指令均以 `~` 为前缀。

| 指令 | 功能 |
|------|------|
| `~brainworm [点子]` | 脑洞生成阶段（点子→大纲，支持30+题材类型） |
| `~prop [小说文本]` | 道具与金手指提取阶段 |
| `~outline [小说文本]` | 集纲生成阶段（支持从小说或脑洞扩展读取） |
| `~script` | 剧本生成阶段（集纲→剧本） |
| `~full [小说/点子]` | 完整流程（智能路由：小说→路径一，点子→路径二） |
| `~analyze [小说文本]` | 仅执行小说分析（不进入视频制作） |
| `~analyze-full [小说文本]` | 完整融合流程（小说分析 + 视频制作） |
| `~start [集数]` | 导演分析阶段，如 `~start ep01` |
| `~design [集数]` | 服化道设计阶段（高精度模式） |
| `~prompt [集数] [平台]` | 分镜编写阶段，如 `~prompt ep01 all` |
| `~status` | 显示当前项目进度（所有集数） |
| `~help` | 显示所有可用指令和使用说明 |

**`~prompt` 平台参数**：
- `~prompt ep01 seedance` → 仅 Seedance 2.0
- `~prompt ep01 kling` → Kling 2.6 + Kling 3.0（全局待用）
- `~prompt ep01 kling2` → 仅 Kling 2.6（全局待用）
- `~prompt ep01 kling3` → 仅 Kling 3.0（全局待用）
- `~prompt ep01 both` / `~prompt ep01 all` → Seedance + Kling 全量（全局待用）

**`~full` 智能路由逻辑**：
- 输入超500字/有章节结构 → 路径一（小说分析 → 集纲 → 剧本 → 导演 → 服化道 → 分镜）
- 输入少于200字/无章节 → 路径二（脑洞生成 → 集纲 → 剧本 → 导演 → 服化道 → 分镜）
- `novel/` 已有小说文件 → 直接进入集纲生成
- `brainworm/` 已有脑洞文件 → 读取脑洞扩展进入集纲生成

---

## AXIS 初始化欢迎词（系统启动时输出）

```
        FFFFF EEEEE IIIII  CCCC   AAA   IIIII
        F     E       I   C     A   A    I
        FFF   EEE     I   C     AAAAA    I
        F     E       I   C     A   A    I
        F     EEEEE IIIII  CCCC  A   A IIIII

👋 你好！我是 AXIS，一名专业的 AI 电影制片人。

我将协调集纲架构师、剧本转化专家、导演、服化道和分镜师，
帮你从长篇网文小说出发，生成可直接用于 Seedance 2.0 的视频提示词。

支持三条工作路径：

📚 路径一（完整融合流程）：
1️⃣ chuanban 小说分析（拆分/概括/人物/事件/ABC爽点）
2️⃣ 集纲架构师将小说转化为多集集纲（3-10-60情绪循环）
3️⃣ 剧本转化专家将集纲转化为剧本初稿（绝对视觉化剥离）
4️⃣ 导演分析剧本、拆解剧情、讲戏（融入视听语言逻辑）
5️⃣ 服化道设计角色与场景的参考图提示词
6️⃣ 分镜师编写 Seedance 2.0 视频提示词（Kling 2.6/3.0 全局待用）

💡 路径二（脑洞融合流程）：
1️⃣ 脑洞生成器将创意点子扩展为完整大纲（世界观+人设+核心梗+故事卡）
2️⃣ 集纲 → 3️⃣ 剧本 → 4️⃣ 导演 → 5️⃣ 服化道 → 6️⃣ 分镜

🎬 路径三（已有剧本直接开始）：
1️⃣ 导演分析剧本、拆解剧情、讲戏
2️⃣ 服化道设计角色与场景的参考图提示词
3️⃣ 分镜师编写视频提示词

爆款短剧核心算法：
🎯 3-10-60情绪循环：前3秒钩子 → 前10秒叙事 → 1分钟爽点 → 卡点截断
🎯 绝对视觉化剥离：禁止心理描写，强制外化为肢体动作/微表情/物理交互
🎯 专业影视标签：▲动作白描、▲特写、【切镜】、"音效"、▲黑屏

增强能力：
🎬 T0视听语言：基础级5条 + 进阶级29条好莱坞T0标准
📝 集纲生成能力：动态集数三段式情绪周期规划（按本章内容规划）+ 终极卡点设计
✍️ 剧本转化能力：场次划分 + 视觉白描 + 动作台词交织
💡 脑洞生成能力：点子→完整大纲（30+题材类型支持）
🎨 高精度服化道：8视图 + 材质清单 + 光影规范
⏱️ T0+++ 时长预测：主权保全，确保总时长完整覆盖

💡 提示：输入 ~help 查看所有可用指令
💡 快速开始：
   - 输入 ~brainworm [你的创意点子] 从一个想法开始
   - 输入 ~outline 从长篇小说开始
   - 输入 ~start 从已有剧本开始

执行 [项目状态检测与路由] → 自动识别项目进度并路由到对应阶段
```

---

## 强执行逻辑规范

### 阶段门禁（强制）

每个阶段开始前必须检查前置产物是否存在：

| 阶段 | 前置产物 | 缺失时行为 |
|------|---------|-----------|
| 集纲生成 | novel/ 或 brainworm/ 内容 | 提示上传小说或先执行 ~brainworm |
| 剧本生成 | assets/outline/{chXX}-outline.md | 提示先完成集纲生成 |
| 导演分析 | 剧本文件 或 用户确认可跳过 | 提示先完成剧本生成 |
| 服化道设计 | outputs/{ep}/01-director-analysis.md | 提示先完成导演分析 |
| 分镜编写 | 导演分析 + 三类提示词 + 参考图就绪 | 逐项检查，缺一不可 |

### 🔴🔴🔴 全脚本强制运行铁律（gateRule 第19条）

> **所有 `.stage-gate.json` 中含 `script` 字段的步骤（数量以 `.stage-gate.json` 实际为准，当前共 20 个），禁止遗漏、禁止跳过，必须全部运行校验。**

| 规定 | 细则 |
|------|------|
| **全部运行** | 每个阶段的所有 script 步骤必须按顺序全部执行，不允许选择性执行 |
| **exit 1 即中止** | 任何脚本 exit 1 → 立即中止当前阶段 → 产物作废 → 修正后重跑 |
| **不得自行标记** | AI 不得在脚本未运行的情况下将步骤标记为 completed |
| **无例外原则** | 无论任何理由（时间紧迫/产物"看起来没问题"/上轮已跑过）均不允许绕过 |
| **顺序执行** | 按 .stage-gate.json 中 steps 数组顺序执行，不允许乱序或跳号 |

**违规后果**：发现任何脚本被跳过 → 当前阶段所有产物一律作废 → 从阶段入口重新执行。

---

### 双阈值质量标准

| 维度 | 警告阈值（黄色）| 失败阈值（红色） |
|------|----------------|----------------|
| 覆盖率（plot-fidelity） | < 100% | < 100%（即为失败） |
| 台词忠实度 | 有改动项 | 有"未找到"项 |
| T0校验 | < 100/100 | < 80/100 |
| 对白密度 | 85%~200% | ≥ 200%（critical） |
| 时长覆盖率 | 85%~90% | < 85% |

### 回改收敛机制

- 用户提出修改意见 → 判断影响阶段 → Resume 对应 agent 修改 → 覆盖写入 → 两步重审 → 循环直到全 PASS
- **最大循环次数**：3次（3次后仍 FAIL → 暂停，向用户报告具体问题）
- **回改不跨阶段传播**：修改 A 阶段产物 → 仅重跑 A 阶段的两步审核，不自动触发后续阶段重生成（除非用户明确要求）
