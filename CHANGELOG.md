# AXIS 系统更新日志

> AXIS — AI-Powered Short Drama / Comic Production Pipeline  
> 项目：万界通告，哨兵阵亡（漫剧内测教学）  
> 仓库初始化：2026-04-22

---

## [v8.32] — 2026-06-09 · 系统冲突修复——清掉 5 处规则/文档不一致（孤儿阶段/角色格式双标/产物漏列/悬空触发词/agentId 口径漂移）

> 用户全量排查"AXIS 系统还有没有冲突的地方"，定位并修复 5 处规则层冲突。**仅改规则/数据源文件（CLAUDE.md / AXIS-workflow-stages.md / lib/workflow_paths.py），未触碰任何 outputs 项目产物。** Python 导入与终点判定已回归测试：`get_next_stage(路径一,分镜编写)=None` 不变，next-step-prompter 系列收尾报告触发不受影响。

### 变更
- `lib/workflow_paths.py`：新增 **`POST_EPISODE_STAGES = ["集间交接"]`** 常量 + 完整性约定 docstring——「集间交接」是集末收尾型阶段，紧跟「分镜编写」之后、**不进 PATH_SEQUENCES**（保「分镜编写」为内容终点，不破坏 next-step-prompter 终点判定），消除"唯一权威路径源不认识集间交接"的孤儿阶段冲突（该阶段在 AXIS-workflow-stages.md 阶段十一与 .agent-state.json 中实际使用）。
- `CLAUDE.md` / `AXIS-workflow-stages.md`（第二处服化道流程·1239 行）/ `skills/art-design-skill/references/execution-rules.md`（Nano Banana 输出规范）：**厘清"格式"与"版面"两个正交维度**——「中英分离（【中文描述段】+【英文描述段】，包在 `### Nano Banana Pro（中英文）` 标题下）」是角色/场景/道具**通用提示词格式**；「电影级角色提案板六区块」是**角色专属版面内容**（角色那两段正文须描述提案板、非泛化单图，由 pitch-board-validator/t0-validator 校验）。三处"每个角色/场景/道具"输出结构段统一补这条正交说明，消除"角色究竟走扁平块还是提案板"的误读；同步修正 CLAUDE.md 第四步通知里 character-prompts.md 的描述。
  > ⚠️ 自我修正：v8.32 初版曾把此项写成"角色不再产出 `### Nano Banana Pro（中英文）` 块、否则判 FAIL"——经复查 `art-design-template.md` 与 `art-design-skill/SKILL.md`，该表述**有误**（提案板的提示词正文恰恰写在该标题块内，标题不致 FAIL，缺六区块要素才致 FAIL），已按上述正交口径更正。
- `CLAUDE.md`（分镜编写阶段）：在【平台支持】Seedance、第五步产物清单、第七步通知三处**补齐 `03-text-storyboard.md` 文字分镜稿**——与文件结构区、该集完成判定（02-seedance + 03-text-storyboard 才算完成）、seedance-storyboard-skill 强制产物对齐，消除"完成判定要它、阶段产物清单却不列它"的自相矛盾。
- `CLAUDE.md`（子规则 9 触发条件说明）：删除**悬空的「manga 模式」触发词**（全系统未定义此模式；漫剧仅为 Q2 媒介选项），改为"动作戏等场景触发"。
- `AXIS-workflow-stages.md`（调用规则）：agentId 口径**对齐 CLAUDE.md 单一权威**——agentId 仅会话内有效/默认留空/为空正常，跨会话·跨集·回改靠**上下文快照**而非 agentId 持久化，阶段进度真值为 currentStage/stageHistory；消除两份文档对 agentId 持久化的口径漂移。

### 追加（用户"再跑"——更系统的逐文件深查）
> 这一轮先核架构再下结论。结果：**引用层零悬空**——CLAUDE.md/workflow-stages 引用的 19 个工具脚本、40 个 SKILL.md、resources/tools/references 全部文档、4 个根目录大文档**逐一存在**（4 个 `xxx/yyy` 仅为 9-A/9-C 报告模板占位符）；服化道三件套输出路径、台词零删减↔VDC（VDC 只压描述含水量、台词受保护并强制达标）均自洽。**唯一新发现 = 一处 v8.30/31 传播缺口**：
- `skills/sovereign-duration-predictor-skill/SKILL.md`（段内密度校验）+ `skills/sovereign-duration-predictor-review-skill/SKILL.md`（对白公式校验）：原文把 `口型0.4秒/字、画外音0.2秒/字` 标注为"语速3-4字/秒、与 seedance-storyboard-skill 口型公式一致"——该声明**已过期且自相矛盾**（0.4s/字=2.5字/秒≠3-4；storyboard 在 v8.30/31 已改为按戏型语速分档）。**修正为**：明确 0.4/0.2 是**密度校验保守预算**（与 `beat-density-checker.py` DIALOGUE_CHAR_SECONDS=0.40 / BUBBLE=0.20、对白密度表一致，故意偏慢留足空间），**区别于** storyboard 书写用的语速分档（慢3-4/日常默认4-5/快5-6，以导演「节奏/语速档」字段为权威），两套速率用途不同、不可互套。**0.4/0.2 数值本身正确、未改**，只更正过期交叉引用。
- `skills/seedance-storyboard-skill/seedance-超级饱满_原始完整版.md`（存档参考）：台词表"语速3-4字/秒"加**存档说明横幅**，指明书写一律以 SKILL.md 分档为准，防被误用；原始数值保留不动。
- 说明：sovereign 两文件内嵌的历史 changelog 段（"2026-05-31 增补…"）**刻意不改**——它们是当时的真实记录，重写历史不当。

### 追加二（用户"先处理1112和语速口径传播缺口"——全库补全）
> 对语速/对白预算口径做**全库穷尽扫描**，又揪出 0.3→0.4 改动的两个死角 + 模板写死旧速率；并闭环 1112 角色文件写读路径分歧。校验器侧（`beat-density-checker.py` 0.40/0.20）本就正确，全程未改数值逻辑。
- **1112 路径分歧闭环**：`CLAUDE.md` 第一步半提案板产出 + 分镜第一步前置检查两处——标明 **`assets/prompts/character-prompts.md` 为权威标准路径**（写=读同一文件）；`<角色项目目录>/character-prompts-pitch-board.md` 仅限"按角色项目目录"布局，且该布局下**分镜读取须指向同一 pitch-board 文件**，严禁写 pitch-board.md 却只读 assets 版造成写读错位。
- **语速/对白预算 0.3→0.4 死角补全**（旧值早已统一为口型0.4/画外音0.2，这些处漏改）：
  - `skills/novel-dialogue-extractor-skill/SKILL.md`（第198/273行）：口型预算 `字数×0.3秒` → `字数×0.4秒`（画外音/气泡 0.2秒），锚定 beat-density-checker / 对白密度表。
  - `skills/novel-dialogue-extractor-skill/templates/dialogue-extraction-template.md`（第35/53行）：同 skill 的模板版同步 0.3→0.4，消除"SKILL 说0.4、模板说0.3"的自相矛盾。
- **模板写死旧速率 → 改指戏型分档占位**：
  - `skills/seedance-storyboard-skill/references/enhanced-scene-templates.md`（两条对白示例）+ `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`（人声锚定表基准语速）：`语速[3-4字/秒]` → `语速[按戏型档:慢3-4/日常4-5/快5-6字/秒，取导演「节奏/语速档」]`，与 storyboard SKILL.md 分档一致。
- 全库复扫确认：对白"每字0.3秒速率"与模板"写死3-4字/秒"均已清零（留白类0.3、戏型分档表、review检查项、历史段为合法保留）。

---

## [v8.31] — 2026-06-09 · 「节奏/语速档」字段落地——戏份判定在导演层定一次、往下传（不再分镜层各猜）

> 用户追问"你怎么判断这是什么戏份来规划时间"→ 暴露根因：语速分档好用，但"这是什么戏份"之前没有权威来源，是分镜阶段现猜，猜错就拖/赶。本版把戏份判定钉死在导演层：导演分析每 P 必填「节奏/语速档」，分镜直接读取、禁止重判。**仅改 skill/模板/校验器，未动项目产物（outputs 已由用户重组为项目子目录，本会话未触碰）。**

### 变更
- `skills/director-skill/templates/director-analysis-template.md`：每 P 新增 **`节奏/语速档`必填字段**（慢 3–4 / 日常 4–5 / 快 5–6 字/秒 + 判定依据 + 同P跳档句覆盖）；整集骨架新增 **A4 本集节奏基调**默认。
- `skills/director-skill/SKILL.md`：第四步每 P 新增【节奏/语速档】产出要求——由导演按戏核①+情绪④定，**唯一权威出处、往下传、分镜禁重判**；缺 → 不合格。
- `skills/seedance-storyboard-skill/SKILL.md`：语速分档块标明**唯一来源＝导演分析「节奏/语速档」字段，分镜直接读取禁重判，缺则回退导演阶段**；八问落地追溯新增「节奏/语速档承接（决定时长）」。
- `skills/script-analysis-review-skill/SKILL.md`：硬门禁新增"每 P 节奏/语速档 + A4 节奏基调缺失→FAIL"。
- `skills/seedance-prompt-review-skill/SKILL.md`：台词镜双向查补"语速档须取自导演分析字段、分镜不得自行重判，缺→退回导演阶段"。
- `tools/validators/director-thinking-traceability-checker.py`：新增 **每 P「节奏/语速档」检测**（PACE_MARKERS，缺→warning）；语法校验通过、合成测试有/缺正确区分。

### 说明（非本会话改动）
- `outputs/ep01–ep03` 已被重组为项目子目录（`完美玩具/`、`刀_成片剧本/outputs/` 等），本会话全程只改 skills/resources/tools/CHANGELOG，未触碰任何 outputs 产物。

> 用户追问"每镜时长真的合理吗、会不会太拖"→ 排查发现旧表统一用 3–4字/秒（慢戏速率），套到快节奏短剧日常对话会普遍偏慢虚高（小雨小玉那场被我虚高 ~40%，误判"必拆 2 视频"，真实 ~13s 一个视频即可）。本版给时长表加按戏型的语速分档 + 两条防拖铁律。**仅改分镜相关 skill/模板/参考，未动项目产物。**

### 变更
- `skills/seedance-storyboard-skill/SKILL.md`：「时间段时长估算标准」加 **语速分档表**（慢戏 3–4 / 日常默认 4–5 / 快戏 5–6 字/秒）+ **两条防拖铁律**（快戏紧切不每句加 0.5s 留白；小动作叠说话不另计时）；台词镜行改为"字数÷语速(选档)+留白"，附"选错档逐镜累积=全片拖沓"示例。**此为语速分档权威源。**
- `skills/seedance-prompt-review-skill/SKILL.md`：台词镜检查改为**双向**——太短(说不完)→🔴 延长不缩词；**太慢/拖(快戏用慢档/每句硬加留白/动作另计时)→🟡 判拖沓压紧**。
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：第 5 条补语速分档一句话 + "用慢档把快戏拖沓→FAIL"。
- `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`：§五台词时长改引语速档（表内标"日常档参考"）；**修正"必拆 2 视频"误导**——注明日常戏 ~13s 多在一个视频内、之前按慢档虚高才得出拆 2 视频。
- `skills/seedance-storyboard-skill/references/timeline-continuity-rules.md`：§7.3 加语速分档指引，表降为"日常档参考"。

---

## [v8.29] — 2026-06-09 · 撤销错误的"一次生成=一个镜头"（一个视频≤15s·内部可多镜头切换）

> 用户纠正：**一个视频(一次生成)能装多个镜头切换,15s 是"一个视频"的上限,不是一个镜头的上限。** v8.27/v8.28 我错误地把"一次生成"等同"一个连续镜头"、并设了"≥2 硬切 FAIL"——与模型实际能力和真实 ep01 文件(P01a 13s 含多段多镜)都相反。本版全部撤回改对。**仅改分镜相关 skill/模板/参考,未动项目产物。**

### 变更（正确模型：视频(一次生成)≤15s ⊃ 多个镜头 1–4s；超 15s 才拆视频，视频间用 @分镜图接）
- `skills/seedance-storyboard-skill/SKILL.md`：「单镜头颗粒度」整段重写为「**视频单元 + 镜头切换 + 接点分镜图**」——原子生成单元＝视频(≤15s)·内部可多镜头切换；**撤销"一次生成 ≤1 硬切 / ≥2 硬切 FAIL"**；拆视频唯一硬线＝15s；@分镜图仅用于视频之间；补"台词镜时长≥字数÷语速+0.5s"。
- `skills/seedance-prompt-review-skill/SKILL.md`：审核项改为"单视频 >15s 未拆→FAIL"+"明确视频内多镜头切换合规、不得因切得多判 FAIL"+ 台词镜够说检查；**删除"一次生成 ≥2 硬切 FAIL"误伤项**。
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：第 5 条速查同步重写（视频≤15s·内部多镜头·超 15s 拆视频）。
- `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`：§五重写为"视频时长与镜头节奏"（视频≤15s 装 4–6 镜 + 视频拆分示例 + 台词字数÷语速）；示例一改注为"一个视频(13s)·恰为单一连续镜"；示例二改注为"可整条进一个视频(含多镜头切换)，>15s 才拆"。
- `skills/seedance-storyboard-skill/references/stitching-and-shot-handoff.md`：加**范围界定**——视频内部多镜头切换由模型一次生成(不属拼接)、本文件只管视频之间(>15s 才发生)；rename 引用 + §八对齐。
- `skills/seedance-storyboard-skill/references/timeline-continuity-rules.md`：§7.3 对齐说明改为"一个视频可装多镜头、多句对话同一视频内切，>15s 才拆视频"。

---

## [v8.28] — 2026-06-09 · 修正 v8.27 节奏 bug + @分镜接点图正式落地（短剧要快·硬切靠分镜图）

> 用户实例打脸 v8.27：「别人 15 秒 5 个镜头切完」，而 v8.27 的"单 P 优先 5–8s"把对话拖成 33s 节奏发懒。本版：① 废除 5–8s 下限，改"短剧快切 1–4s/镜、5 镜≈15s 正常"；② 把"硬切"明确为**镜头边界**事件、靠 **@分镜接点图**驱动（不在一次生成里塞多机位硬切）；③ 正式落地拼接方法论（基础vs变动数据/原画质抓帧/同机位复用/台词必配图/接点自检清单）。**仅改分镜相关 skill/模板/参考，未动项目产物。**

### 变更
- `skills/seedance-storyboard-skill/references/stitching-and-shot-handoff.md`：**新建**——AI 视频拼接与镜头接点方法论（无记忆/基础vs变动数据/快切节奏/切镜不拼镜头·分解再生成原理/@分镜接点图做法[原画质抓帧·同机位复用·台词必配图]/导演五法[跨景别·30°·过渡声音同步·气口·MatchCut]/接点自检清单/反面清单）。
- `skills/seedance-storyboard-skill/SKILL.md`：原「单 P 现实可执行约束」重写为「**单镜头颗粒度 + 接点分镜图**」——**废除 5–8s 下限**（改快切 1–4s/镜、5 镜≈15s 正常、禁为凑时长拖长）；硬切＝镜头边界、同一次生成内机位硬切 ≤1；接点靠 @分镜图驱动（变动数据更新）；FAIL 改为"一次生成内 ≥2 机位硬切 / 无理由拖长单镜"。
- `skills/seedance-prompt-review-skill/SKILL.md`：审核项重写——查"一次生成内 ≥2 机位硬切（未拆镜头/未用@分镜图）→FAIL"+"节奏发懒→🟡"+"接点缺@分镜图→🟡"；🔴 明确"5 镜/15s 快切序列合规、不得因切得快判 FAIL"（修正 v8.27 误伤）。
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：第 5 条速查同步重写（镜头=一次生成、快切 1–4s、@分镜图承接、废 5–8s）。
- `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`：§五时间密度表重写为"镜头时长与节奏（短剧要快）"（快切对话 2–4s 等）+ 接点 @分镜图提示；示例一/二改引新规则名。
- `skills/seedance-storyboard-skill/references/timeline-continuity-rules.md`：§7.3 密度表加对齐说明 + 重写为单镜口径（对话每句=一个镜头累加，非单镜 15s 切 4 刀）。

---

## [v8.27] — 2026-06-09 · 单 P 现实可执行约束（把机读层颗粒度拉回 Seedance 真实能力）

> 诚实校准：机读层原"单 P 内多次切镜 + 精确秒级时间码"比视频模型真实能力乐观（模型一次生成做不干净多机位硬切）。新增"一个 P = 一次生成 = 一个连续镜头"约束，把切镜挪到 P 边界——与既有"跨 P 一律切镜 + 首帧承接"规则同源延伸。**仅改分镜/审核 skill、模板、速查表，未动项目产物。**

### 变更
- `skills/seedance-storyboard-skill/SKILL.md`：「首帧承接边界」后新增 **「单 P 现实可执行约束」**——一个 P=一次生成=一个连续镜头；P 内硬切镜 ≤1（理想 0），多机位/不连续景别须**拆 P**（连续运镜不算切）；单 P 优先 5–8s、>10s 仅限一镜到底·0 硬切；明确不与密度公式/时长预测冲突（拆 P 使分镜数不减反增）；**单 P ≥2 次硬切 → FAIL**。
- `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`：示例一改为**单镜连续推进·0 硬切**（原 `【切近景】`→`【镜头继续推近，景别收到近景】`）使其本身合规；示例二（动作戏含硬切）加**拆 P 说明**（一镜到底保留 / 含硬切拆 P02a-d）；§五时间密度表重写——标注"段＝同镜头 beat 非切镜"、补单 P 时长上限与"含硬切怎么办"列。
- `skills/seedance-prompt-review-skill/SKILL.md`：第二步D 机读层检查新增 **「单 P 现实可执行约束」**审核（单 P ≥2 次硬切 → 🔴 FAIL；>10s 且含硬切 → 🔴 FAIL）。
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：「零·机读层唯一权威格式」新增第 5 条单 P 约束速查（硬切 ≤1、切镜拆 P、5–8s 优先、≥2 硬切 FAIL）。

---

## [v8.26] — 2026-06-09 · §2D/§1.9 落地到 Seedance 机读层（道术修复真正被门禁执行）

> 承接 v8.25：把新加的 §2D 短剧三标、§1.9 台词工艺、术层翻译表，从"知识库文字"接到"机读层强制门禁 + 校验器"，使其真正拦截。**仅改分镜/审核 skill、速查表、知识库与校验器，未动项目产物。**

### 变更
- `tools/validators/director-thinking-traceability-checker.py`：新增 **A4 短剧三标检测**（3秒钩子/1分钟爽点/卡点正则），非空壳导演分析缺 A4 → warning，提示"机读层首条无钩子可承接、末条无卡点可承接"（指向 director-thinking-layer §2D.2）；docstring 同步。语法校验通过、ep01/ep02 实跑正常（空壳集不叠加噪声）。
- `skills/seedance-storyboard-skill/SKILL.md`：「导演八问落地追溯」块扩充——新增 **③潜台词/台词动作动词承接**（台词零删改但语气/微表情/前置动作须承接潜台词）+ **A4 三标承接**（首条 P 机读层首段承接 3 秒钩子、末条 P 机读层末段承接卡点、爽点 P 价值翻转给足）+ **lite/full/beat 档位说明**（分析深度分档不进机读层、爽点卡点 P 必 full）。
- `skills/seedance-prompt-review-skill/SKILL.md`：第二步D 机读层检查新增 **「A4 短剧三标承接」**（首条无钩子/末条给完整闭环未卡点 → 🔴 FAIL）+ **「台词潜台词承接」**（台词被删改 → 🔴 FAIL 台词零删减铁律；潜台词无表演层承接 → 🟡）。
- `resources/unified-audiovisual-language-library.md`：第二层 ⓪ 翻译表加**权威关系声明**——本表为上游源头，机读层判分唯一权威是 cheatsheet「14 条+白名单」+ translation-audit-rules.md，冲突以门禁为准（防两表漂移）。
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：14 条对照表加**反向权威声明**，指明上游源头表为 unified 库第二层 ⓪，冲突以本表为准。

---

## [v8.25] — 2026-06-09 · 导演思维（道）+ 视听语言（术）双层深度修复至工业可信

> 针对评分中暴露的真实缺陷做内容级重写（非改标签）：术层删尽伪精度数字与伪神经科学，道层缝入短剧钩子学并去示例污染。**仅改 resources/ 知识库与伴随示例文件，未动项目产物。**

### 变更
- `resources/unified-audiovisual-language-library.md`：§五「29 条」**第二轮去伪精度重写**——逐条改为「craft 依据级别 / 怎么用 / 下沉术层」三行结构；**删除全部杜撰精度数字**（重心下沉身高 2%、运动模糊 V×0.7、眼嘴权重 1:9、杂质每分钟 +15%、重合度<5%、提前 12 帧、像素级<2% 等）；**删除伪神经科学措辞**（被捕食者凝视/触发大脑补全产生生理疼痛/神经系统短路）改用第零层真实机制解释。
- `resources/unified-audiovisual-language-library.md`：§五新增**数字三级诚实标签**（真实标准/启发式/人工规划）+ **「AI 视频模型不直接吃精确数字、要翻成自然语言」诚实声明**；维度三补**编号说明**（28/29 为稳定 ID 非顺序号，保跨文件引用不断）。
- `resources/unified-audiovisual-language-library.md`：第二层「动态模糊」表正名为**快门角度**并标注 180°＝真实标准、AI 模型需自然语言；第三层映射表标题由「29 条 T0 标准」改「29 条技法（稳定 ID）」；frontmatter 与「使用方式」章去「T0 标准」旧叫法、补道层前置说明。
- `resources/unified-audiovisual-language-library.md`：**新增第二层 ⓪「参数→AI 提示词自然语言翻译表」**（焦段/光比/光质/光源/快门/大气等 20 项 param→可直接粘贴的自然语言），并给第四层三个示例各补**「→自然语言提示词（喂模型用）」**改写——解决"战术层全是人工摄影参数、AI 模型不吃"的结构性短板，使战术层真正 AI-native。
- `resources/director-thinking-layer.md`：**新增 §2D 短剧/竖屏适配**——经典戏剧（麦基场景必转）×「3-10-60 钩子学 + 卡点不给闭环」四条和解规则 + 三尺度落法 + **lite/full/beat 三档分析档位**（解决高雅理论与爆款产物脱节、杀鸡用牛刀两大缺陷）。
- `resources/director-thinking-layer.md`：**新增 §1.9 台词工艺**（马梅特/品特：台词＝动作动词、潜台词＞字面、去说明、与台词零删减铁律对齐）；§5 道→术交接表扩成**通用规律 8 行**（原 3 行且全是单一示例）；§6 产出要求补 A4 短剧三标 + lite 档位 FAIL 红线。
- `resources/director-thinking-layer.md`：**去示例污染**——顶部加通用性声明、H1 去「本剧阐释」、§4 整段抽出，所有样例标 📌可剥离。
- `resources/director-thinking-layer-example.md`：**新建伴随示例文件**，承接原 §4 + 角色戏脊 + 道→术具体落点（样例项目《在言情文里…》），明确"做新项目时整篇可替换"。

---

## [v8.24] — 2026-06-08 · 修复隐性失效 #3：Resumable 机制对齐现实（agentId 跨会话不可持久→改用上下文快照）

> 排查确认：subagent 的 agentId **在本运行环境不跨会话持久化**，所以 `.agent-state.json` 里 agentId 全空、且"写盘下次 Resume"根本做不到——这是机制不可实现、非流程没执行。已把 CLAUDE.md 改成与现实一致。**仅改系统文件，未动项目产物与 .agent-state.json 本身。**

### 变更
- `CLAUDE.md`：[Resumable Subagents 机制] 整段重写为「上下文连续性」——明示 agentId 跨会话不可持久（agentId 全空是正常态，不再算缺陷）；连续性分两场景：① **会话内**用 agentId/名称实时 resume（不写盘）；② **跨会话/跨集/回改**用 **上下文快照**（`context-snapshot-generator.py`）作权威机制还原硬约束。
- `CLAUDE.md`：.agent-state.json schema 文档**对齐实际文件**（补 projectName/workflowPath/visualStyle/totalEpisodes/status + 每集 currentStage/stageHistory；agentId 降级为"会话内可选缓存·可空"）；文件结构注释同步更正。
- 诚实校准：快照工具文档自称"≤400 tokens"，实跑 ep02 为 ~11547 token（45 GSA 块）——CLAUDE.md 已注明"≤400 为设计目标、实际随P块数变化"，不照抄虚标。
- 🔴 实测：`context-snapshot-generator.py ep02` 正常生成（44 P块映射 + 45 GSA），权威机制可用；`.agent-state.json` 仍为合法 JSON。

### 未改（按用户边界保留）
- `outputs/*`、`assets/*`、`novel/*` 与 `.agent-state.json` 本身均未改（仅改了描述它的文档）。

---

## [v8.23] — 2026-06-08 · 排查修复：清除"29条"改名后的旧称残留（一致性）

> 系统排查发现 v8.22 正名后仍有两处沿用旧称"好莱坞T0级29条工业标准"，造成命名不一致，已修。

### 变更
- `resources/unified-audiovisual-language-library.md`：体系架构表里"29条工业标准"→"视听技法29条（已正名·见第五节）"。
- `agents/storyboard-artist.md`：unified 引用旧称→"视听技法29条为风格化速查·非工业标准"，并补 director-thinking-layer 道层 + 01-director-analysis.md 必读（与 director agent 对齐）。

### 未改（按用户边界保留）
- `outputs/*`、`assets/*`、`novel/*` 项目产物未动。

---

## [v8.22] — 2026-06-08 · 视听语言"旧29条"逐条重写：伪命名正名 + 标真实依据 + 假数字降级

> 用户指出上一版只加了"第零层"、29条旧伪命名内容原封未动（只贴免责声明）。本批**真改旧内容**：9 个维度全部正名为真实 craft 名，逐个标注真实理论依据，假精度数字降级为启发式。**仅改系统文件，不动小说项目产物。**

### 变更
- `resources/unified-audiovisual-language-library.md`：第五节 9 个维度标题**逐个正名**（原伪名移入括号作历史别名）并各加一行**真实理论依据**：
  - 维度一 物理动力学→**动作运动规律**（动画12原理）
  - 维度二→**构图与权力关系**（场面调度+Bruce Block+仰俯拍）
  - 维度三 神经劫持→**注意力引导与剪辑节奏**（Murch eye-trace+视线匹配+POV+库里肖夫）
  - 维度四→**景深调度与蒙太奇生义**（景深+爱森斯坦对位+图形匹配）
  - 维度五 生物本能→**生理拟真与表演细节**（明暗适应+恐怖谷）
  - 维度六 情感熵→**情绪的环境与时间表达**（Bruce Block对比递增+时间操控+通感音效）
  - 维度七 意志延伸→**留白·间离·主观介入**（空镜/枕镜+布莱希特间离+手持主观）
  - 维度八 神格化→**表现主义光影·静默·首尾呼应**（表现主义布光+动机光+静默+bookending）
  - 维度九 非人境→**实验/超现实视觉手法**（补色后像+实验电影）
- 第五节定位声明改为"逐条重写"，并明示**条目内具体数字（重心下沉2%、运动模糊V×0.7、眼嘴权重1:9、杂质+15%/分等）为风格化启发式起点、非验证标准、不得当硬指标校验**；真实可执行参数以第二层为准。

### 未改（按用户边界保留）
- `outputs/*`、`assets/*`、`novel/*` 等小说项目产物一律未动。

---

## [v8.21] — 2026-06-08 · 两组导演理论合并为一套「导演工作法」三尺度贯通（修"只用了八问"）

> 用户指出导演分析被矮化成"八问"（只用第一组），第二组（结构学/蒙太奇/剪辑/作者论）被晾在一边。本批把两组**合并成一套贯通工作法**：2A 宏观整集骨架→2B 每场八问→2C 镜头组接，并传导到模板/校验器/编排。**仅改系统文件，不动小说项目产物。**

### 变更
- `resources/director-thinking-layer.md`：§2 由"导演八问"重构为 **「导演工作法·三尺度贯通」**——2A 整集骨架（结构骨架范式+节拍归属/控制性主题/作者签名/价值曲线，用第二组）、2B 每场八问（用第一组，每P加"结构节拍归属"）、2C P与P组接（蒙太奇并置+默奇剪辑六法则，用第二组）；顶部说明与 §6 产出要求/FAIL 红线改为"三层缺一即不合格"。
- `skills/director-skill/templates/director-analysis-template.md`：新增**「整集骨架」文件头块（2A）**；每个 P 块新增 **「与下一P组接」行（2C）** 与 **结构节拍归属**。
- `skills/director-skill/SKILL.md`：第零步由"导演八问"升级为"导演工作法三尺度（2A/2B/2C）"。
- `tools/validators/director-thinking-traceability-checker.py`：新增 **2A 整集骨架缺失 / 2C 组接缺失** 检测（warning 级，空壳仍 critical），让"只做八问、两组没合并"可被校验发现。
- `CLAUDE.md` / `AXIS-workflow-stages.md` / `agents/director.md`：导演/分镜阶段中"导演八问"措辞统一为"导演工作法三尺度（整集骨架+八问+组接）"。

### 未改（按用户边界保留）
- `outputs/*`、`assets/*`、`novel/*` 等小说项目产物一律未动。

---

## [v8.20] — 2026-06-08 · 道→机读层落地闭环：分镜强制承接导演八问 + 新增追溯校验器（系统强制）

> 此前 v8.18/8.19 只把导演思维/视听理论接到"导演阶段"，**没流到 seedance 机读层、无强制**。本批补齐"最后一公里"：让分镜技能必须承接戏核、并新增校验器在阶段门禁强制拦截空壳。**仅改系统文件，不动小说项目产物。**

### 变更
- `tools/validators/director-thinking-traceability-checker.py`：**新增校验器**。检查 `01-director-analysis.md` 是否真含「导演八问」、机读层能否追溯戏核：导演分析缺失（而机读层已存在）或**全为反向指针空壳**→ critical；逐 P 缺①戏核/⑧表演与调度 → warning；导演 P 无对应机读层 P → warning。
- `tools/validators/skill-compliance-auditor.py`：分镜阶段（storyboard）审计计划新增"导演思维落地追溯"项——阶段门禁现会因空壳/缺失而 FAIL。
- `tools/validators/run_validators.py`：分集校验注册新增 `director-thinking-trace`（13→14 个分集校验器）。
- `skills/seedance-storyboard-skill/SKILL.md`：参考清单加 director-thinking-layer（道·必读）+ unified「第零层」（术·真实根基）；第六步"设计落地自检"新增**导演八问落地追溯强制条**——机读层每条 P 必须承接对应 P 的①戏核/④转折/⑧表演与调度；导演分析空壳则禁止生成、回退补"道"；只堆运镜光影无戏核 → 判"匠气"FAIL。
- `CLAUDE.md` / `AXIS-workflow-stages.md`：分镜阶段"必须参考/Must-Call"清单加 director-thinking-layer + 01-director-analysis.md（戏核来源），unified 引用改指「第零层真实根基」并标注"29条为风格化速查非工业标准"。
- 🔴 端到端实测：auditor ep02 storyboard 与 run_validators ep02 均已纳入并正确**拦截 ep02 导演分析空壳**（critical=1）。

### 未改（按用户边界保留）
- `outputs/*`、`assets/*`、`novel/*` 等小说项目产物一律未动；校验器仅"报告"存量缺陷，不修改项目文件。

---

## [v8.19] — 2026-06-08 · 补全导演思维第二组（结构/剪辑/作者论）+ 彻底完善视听语言（真实理论根基层）

> 用户质疑"好莱坞导演思维不止八条"——属实。本批①把导演思维从单场戏戏剧根基扩到**整片层**；②给视听语言补上**真正的学术骨架**并诚实定位自编的"29条"。**仅改系统文件，不动小说项目产物。**

### 变更
- `resources/director-thinking-layer.md`：新增 **§1B 第二组理论（好莱坞类型片层）**——结构学叙事八范式（坎贝尔·沃格勒英雄之旅 / 斯奈德 Save the Cat 15拍 / 西德·菲尔德范式 / 特鲁比22步 + 豪格/西格/哈蒙/托特）、库里肖夫+爱森斯坦蒙太奇、沃尔特·默奇剪辑六法则、作者论；引言与§1标题改为"两组"，参考书目补 9–15 项；声明"导演思维不止于此"。
- `resources/unified-audiovisual-language-library.md`：新增 **第零层·视听语言理论根基（真实出处）**——Bordwell&Thompson《Film Art》四大技术、Bruce Block《The Visual Story》七要素+对比/亲和视觉强度律、库里肖夫/爱森斯坦蒙太奇、默奇剪辑六法则、三点布光/伦勃朗光/明暗对照/动机光、焦段与色彩心理学（均附出处）。
- `resources/unified-audiovisual-language-library.md`：把"好莱坞T0级29条工业标准"**诚实降级**为"29条风格化执行启发式"，明示神格化/非人境/情感熵等为夸张自造命名、学术依据以第零层为准。

### 未改（按用户边界保留）
- `outputs/*`、`assets/*`、`novel/*` 等小说项目产物一律未动。

---

## [v8.18] — 2026-06-08 · 新增真·导演思维层（道）：八大经典理论根基 + 导演八问，与视听术层解耦

> 排查发现 AXIS 把摄影/剪辑/动画技术（29条T0）误当"导演思维"，缺真正的"道"（戏剧诠释）。本批补齐**有出处的真实导演理论层**，并与"术"层明确解耦。**仅改系统文件，不动任何小说项目产物（outputs/ 三集分析保持原样）。**

### 变更
- `resources/director-thinking-layer.md`：**新增**导演思维"道"层文件。综合八大经典源头（亚里士多德《诗学》突转+发现 / 埃格里《编剧的艺术》前提+人物三维+对立面统一 / 斯坦尼斯拉夫斯基目标+超目标+戏脊 / 卡赞戏脊法 / 麦基《故事》场景必须转+鸿沟+控制性主题 / 马梅特《论电影导演》场景目标+无修饰镜头并置 / 希区柯克悬念vs惊吓 / 卢梅特《拍电影》调度即潜台词），含**导演八问**操作框架、戏脊三层级、道→术交接、产出 FAIL 红线、参考书目。
- `resources/unified-audiovisual-language-library.md`：体系架构**定位更正**——本库是"视听执行层（术·怎么拍）"，其"战略/战术"仅指术内部两小层；旧版把 29条T0 误标为"导演思维（道）"已澄清；真正的道在 director-thinking-layer.md，调用顺序改为"先道后术"。
- `skills/director-skill/SKILL.md`：融合项新增第0条"导演思维层（道）第一优先"；讲戏第四步前置"第零步·导演八问"；写死的本项目戏核改为**通用（带示例）**，使技能可复用到任意小说。
- `skills/director-skill/templates/director-analysis-template.md`：每个 P 块新增强制"🎬 导演八问（道）"块（先于情绪钩子与视听要点）。
- `CLAUDE.md` / `AXIS-workflow-stages.md` / `agents/director.md`：导演分析"必须参考/Must-Call/Skill加载确认"清单均把 director-thinking-layer.md 列为**第一优先**，并标注 unified 库为"术层、非导演思维本身"。
- 全系统编号统一为「**导演八问**」（修正此前 六问/七问/8条 不一致：① 戏核/前提 ② 目标·阻碍·赌注·战术 ③ 潜台词 ④ 转折(价值±) ⑤ 发现 ⑥ 导演态度/控制性主题 ⑦ 信息差 ⑧ 表演与调度；⑤⑦为条件项）。

### 未改（按用户边界保留）
- `outputs/ep01-03/*`、`assets/*`、`novel/*` 等小说项目产物一律未动（用户明确：只完善系统，不碰项目文件）。

---

## [v8.17] — 2026-06-08 · 深度纠察修复：方向C 残留清理（文档批）+ 校验器 BUG/单一来源（代码批）

> 全系统 BUG 与冲突排查后分两批修复。文档批：清理方向C「单层」重构未清干净的双层残留。代码批：修一个静默空转的校验 BUG、建立禁词单一权威来源、修一处假失败。

### 变更（第一批 · 文档批）
- `skills/seedance-storyboard-skill/SKILL.md`：§三「T0工业级提示词模板」删除整段幸存的**双层模板**——核心原则「人读层/机读层分离 + 旧统一1000字上限」改写为方向C 单层原则；§3.1 文件结构+双层P01示例（约82行）收拢为指向模板文件的指针（单一权威）。
- `skills/seedance-storyboard-skill/SKILL.md`：§7.3 校验覆盖表改写为与 v8.15 精简后校验器一致（必需项仅 🎬单层成品 + 🎭台词审计；废除项明列不再检查）；删除已废除的「人读层 情绪钩子4行→FAIL」行。
- `skills/seedance-storyboard-skill/SKILL.md`：成品自检 7 维度表逐行「人读层→导演分析中标注的」「机读层→单层成品」；L143/224/374/551/596/650 六处「人读层」残留按方向C 改述（场景类型标注改为"P块开头"、用词转换规则、跨片衔接只写导演分析等）。
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：L15/96/254/298 四处「人读层」残留清理（场景类型标注位置、第八节自检对照源、有机运动字段、跨片衔接归属导演分析）。
- `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`：P01/P02 示例补 `> ⚡ 场景类型 | 使用模板` 标注行，与 SKILL/cheatsheet 的"必做"要求一致。
- `CLAUDE.md` / `AXIS-workflow-stages.md`：brainworm 段写死的「10集三段式」改为「动态集数三段式（示例10集）」，消除与"动态集数、禁止默认固定集数"原则的冲突。

### 变更（第二批 · 代码批）
- `tools/validators/cross-episode-consistency-checker.py`：**修 BUG** — 新增 `_extract_scenes_from_prompts()` 并在 `_collect_scene_info()` 调用，使其与角色侧对称、能读 `scene-prompts.md`（兼容 `[ep01/ep03][scene][剧本场景]` 等非标准/合并集数标记）。修复前场景恒 0、场景冲突检查静默空转；修复后实测场景 0→14、跨集巡检与色调统一检查正常运行。
- `tools/validators/_machine_banlist.py`：**新增** 机读层禁词「代码层单一权威清单」（FORBIDDEN_MACHINE_TERMS/ABSTRACT/PERFORMANCE 三表，从 template-validator 原样迁移，33/14/10 条不变）。
- `tools/validators/seedance-template-validator.py`：三张硬编码禁词表改为 `from _machine_banlist import ...`（零行为变化）；解决 SKILL「单一权威来源」声明与实现脱节（CONFLICT-5）。
- `tools/validators/machine-layer-leak-scanner.py`：`LEAK_RULES` 上方加说明注释，标明其为权威清单的「带上下文防误伤守卫的窄子集」，非竞争清单。
- `skills/seedance-storyboard-skill/SKILL.md`：禁词「唯一权威来源」措辞改为双层（机器真值=`_machine_banlist.py`、人读说明=`translation-audit-rules.md`），与实现一致。
- `tools/validators/beat-density-checker.py`：**修假失败（OBS-9）** — 节拍密度主源为 Seedance 文件、导演分析仅 fallback；改为只要主源在即可校验，仅当主源+fallback 均缺才报错（此前导演分析缺失会无条件 exit(1)）。实测 ep01（无导演分析）由硬挂转为正常输出节拍报告。

### 未改（按现状保留，附说明）
- `assets/prompts/scene-prompts.md` 的非标准场景标记（`[ep01/ep03][scene][剧本场景]`）：沿 v8.15「不动存量」原则保留，改由解析器容错处理（CONFLICT-6）。
- `semantic-consistency-validator.py` 对导演分析的硬依赖：保留（其本就需导演分析做"导演↔视频"一致性比对，阻断正确）；ep01 报缺失暴露的是数据缺口本身。
- `.agent-state.json` 的 agentId 全空（OBS-8）：属已完成项目的运行态记录，非代码缺陷，无可修项。

---

## [v8.16] — 2026-06-08 · 吸收 AI 视频拼接方法论：机读层补 3 规则 + 厘清「首帧承接」边界

> 评估外部「ai-video-stitching」拼接方法论后，仅抽取**能直接落到机读层文字**的净增量并入库；切镜策略/过渡镜头/抓帧工具/剪辑工作流等属导演分析或后期工作流的内容**不入机读层**。其内核「AI无记忆→显式喂数据」与现有 GSA / 禁BGM / 禁字幕 完全一致，本次为佐证而非推翻。

### 变更
- `skills/seedance-storyboard-skill/SKILL.md`：单层必含要素铁律表「镜头语言」行新增**相邻景别避免直切、优先跨级**（中景→特写）；「节奏」行新增**首/末段留"动作衔接、无台词"气口**（拼接留接口）。
- `skills/seedance-storyboard-skill/SKILL.md`：GSA 格式段新增**多角色联动重述**规则——一角色位姿变化时，同框其他角色被动改变的位置/朝向/视线须在本P GSA 一并重述。
- `skills/seedance-storyboard-skill/SKILL.md`：P8 FAIL条件下补**「首帧承接」边界厘清**——首帧承接仅用于让新镜头保持人物/空间一致，**非**伪造同一连续运镜；连续单镜头不跨P续接，跨P一律按切镜处理（防与拼接方法论误读为矛盾）。
- `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`：§一必含要素表「镜头语言/节奏」两行同步补景别跨级 + 气口；§四视听语言简则新增景别跨级、气口、切镜≠续接连续镜头三条。

---

## [v8.15] — 2026-06-08 · 方向C 收尾：清除旧双层死内容（模板重写 + 校验器精简 + 文档残留）

> 用户确认只做"清理"（不删存量 ep01-10）。本批把模板/规范/校验器里**与单层矛盾的旧双层死内容**清干净，并修一处模板↔校验器一致性。旧内容均在 git 历史可取回。

### 变更（清理批）
- `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`：**整文重写**（1074→约200行）为单层模板——删全部双层正文（导演分析人读层/起幅落幅/翻译审计表/密度表/钉子4行/微表情独立块/mm/英文运镜词条），保留并精炼单层有用内容（AI可执行性七律 M1-M7、角色强锚定、@引用语法、视听语言简则、时间密度、场景速查、单层 P 示例×2）。
- `tools/validators/seedance-template-validator.py`：`P_REQUIRED_SECTIONS` 删除所有注释掉的死代码（director_analysis/translation_audit/density_check），并把 起幅落幅/连续性/微表情/钉子 一并移出——单层 P 块必需项仅二：`machine_prompt`（🎬单层成品，靠 `### 🎬 Seedance` 头定位）+ `dialogue_audit`（🎭台词审计）。
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：五「翻译审计14条」→「成品用词转换14条」（内容保留，去流程）；删"每条P至少8条原则"；密度校验表 强制输出→已降级；十三 审计表瘦身排版→单层正文即成品（仅留🎭台词审计）；索引指针改名。
- `skills/seedance-prompt-review-skill/SKILL.md`：translation-audit-rules 指针改述为"用词转换参考"；删"翻译审计标准示范（ep01/ep02）"。
- 一致性修正：单层成品保留 `### 🎬 Seedance 提示词（单层成品）` 头（供校验器 machine_prompt 定位），模板示例×2 与骨架生成器同步补头。
- 🔴 端到端复测：骨架生成→校验，machine_prompt 正常识别、被删模块 warning 全消（10→2），剩余仅空骨架 TODO 内容项。

### 未删（按用户决策保留）
- 存量 ep01-10 旧双层产物（豁免保留，未删）。

---

## [v8.14] — 2026-06-08 · 方向C「官方对齐单层」重构（第二批 · 完成 + 端到端验证）

> 接 v8.13 第一批。本批补齐生成/审核/模板/手册/骨架生成器，并修一处闸门作用域；方向C 主体完成。
> 🔴 端到端验证：用改后的骨架生成器产单层骨架 → 校验器，`P_MISSING_DIRECTOR_ANALYSIS`/`P_MISSING_MACHINE_PROMPT` 等结构性 critical 已消失，剩余仅空骨架 TODO 内容项（位置/时间段/来源，填好即过）。

### 变更（第二批）
- `tools/validators/seedance-template-validator.py`：新增 `check_camera_move`（方向C·官方"运镜要具体"）——每条P机读层无任一景别/运镜词 → warning（不阻断）；新增 SHOT_SIZE_TERMS/CAMERA_MOVE_TERMS。已测不崩。
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：四要素表 双层→单层；删"人读层上限/每条P必附翻译审计表"；文件头两表 FAIL→推荐。
- `skills/seedance-storyboard-skill/translation-audit-rules.md`：定位降为「成品用词转换参考」（翻译审计表流程废除，14条转换内容保留）；frontmatter+标题同步。
- `skills/seedance-prompt-review-skill/SKILL.md`：第二步B 翻译审计检查→「成品禁用项零残留 + 运镜点名」；第二步C 对照对象 人读层→导演分析(01-director-analysis.md)+源剧本；删审计表存在性/可追溯检查。
- `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`：顶部加方向C 单层化公告，旧双层/14翻译段降为参考，冲突以 SKILL 单层标准为准。
- `Seedance 2.0 情绪-微表情-语气增强模块.md`：模块定位加方向C 注——6字段 mm/f 数字仅规划参考，成品不写；微表情/发声/情境素材照常用。
- `tools/generators/stage-scaffold-generator.py`：分镜骨架单层化（删人读层/起幅落幅/连续性/微表情块/钉子；机读层改景别+运镜点名+台词承载；保留台词审计）；修两处措辞回归（尾缀"禁止出现任何字幕"、音效"禁止背景音乐"）。
- `.githooks/pre-commit`（Gate B）：排除根目录方法论手册（`^Seedance*.md`）与 `skills/` 模板及文档——它们按设计含规划层 mm/英文运镜示例，是参考资料非交付物，不应被泄漏闸误拦；交付物（outputs/ep*、项目目录）仍照扫。

### 仍未动（低优先/不影响主流程）
- Kling 模板与 review-skill（全局待用·不启用）；`references/enhanced-scene-templates.md`、`references/timeline-continuity-rules.md`、`visual-language-logic-review-skill` 中的零散「翻译审计」字样（不驱动 Seedance 主流程）。
- 存量 ep01-10（按决策豁免，老格式保留）。

---

## [v8.13] — 2026-06-08 · 方向C「官方对齐单层」重构（第一批：校验器 + SKILL 核心）· 进行中

> 触发：用户"相信官方"——官方明确"别写 mm/f/ISO 数字"，据此裁定不照搬手册的 6字段-带数字格式，转向**单层官方对齐**：分镜文件＝可直接喂 Seedance 的成品，导演思考留在 `01-director-analysis.md`，去掉"人读层→翻译→机读层"的翻译层与翻译审计。决定（用户批准我的推荐）：①留 台词审计+人声锚定 为必需、其余工序表降级 ②存量 ep01-10 豁免、新标准只管以后 ③分镜文件不再内置人读层。
> 🔴 本版为**多批次重构的第一批**，尚未完成；剩余批次见末尾「待续」。

### 变更（第一批）
- `tools/validators/seedance-template-validator.py`：
  - `P_REQUIRED_SECTIONS` 移除 `director_analysis`（人读层）必需项——单层成品不在分镜文件内重写人读层；`check_human_layer` 在 human 缺失时本就 return，旧双层文件仍被完整校验，新单层文件自动跳过（天然 grandfather）。
  - `DOC_REQUIRED_SECTIONS` 仅保留 来源剧本/剧本行号范围/人声锚定表（critical）；素材对应表/角色锚定表/单条提示词预算表/剧本逐行覆盖审计 移入新 `DOC_RECOMMENDED_SECTIONS`（warning）。
  - 已测：语法 OK、不崩；ep01 critical 47→46（剧本逐行覆盖审计转 warning），剩余均为旧双层格式自带项（豁免）。
- `skills/seedance-storyboard-skill/SKILL.md`：
  - 「两层必含四要素铁律」→ 改写为「单层成品必含要素铁律」：新增「运镜必须点名且具体」硬要求；9维度/情绪钩子归属导演分析阶段，不要求出现在分镜成品。
  - 「第六步：三步自检」中的"翻译审计自检 + 100%覆盖人读层"作废，改为"对照源剧本+导演分析的成品自检"。

### 待续（后续批次）
- storyboard-generation-cheatsheet.md 单层化；translation-audit-rules.md 降级为"用词参考"；seedance-prompt-review-skill 去翻译审计维度+加运镜点名；~12 处 stale「翻译审计」引用清理（CLAUDE.md/AXIS-workflow-stages.md/templates/其他 review-skill）；四份手册加注"数字仅规划参考"；校验器新增「运镜点名」检查。

---

## [v8.12] — 2026-06-08 · 修正 v8.11 的措辞通杀：补回"抽象情绪词读不懂"边界

> 触发：用户提供四份 Seedance 权威手册（核心技能速查/情绪-微表情-语气增强/情绪与语气写法/微表情物理素材库100组）后发现 v8.11 改出了矛盾——其"严禁把理由表述为 Seedance 看不懂术语"是**通杀措辞**，会误伤项目核心铁律"Seedance 不理解抽象情绪词（AI 读不懂）"。v8.11 的实证结论（B 类技术术语读得懂、为可控性翻译）正确，但必须与 A 类（抽象情绪词真读不懂）分开表述。本次只精修措辞，不改翻译规则/校验阈值/产物。

### 变更
- `skills/seedance-storyboard-skill/translation-audit-rules.md`：版本 1.1→1.2；「为什么这样规定」段重写为 **(A)(B) 两类分治**——(A) 抽象情绪/心理词＝Seedance 真读不懂→物理化（微表情+发声方式，核心铁律不可否定）；(B) 影视技术术语/参数＝读得懂、为可控性+单条可执行性+中文统一而翻译。结尾改为"两类理由须分开表述，既不用'看不懂术语'通杀、也不否定'抽象情绪词读不懂'"。
- `skills/seedance-storyboard-skill/SKILL.md`：「零」段实证依据指引同步收窄——明确机读层禁项仅指**技术术语/参数类**，并加 ⚠️ 提示抽象情绪词属"真读不懂"另一类，二者勿混。

---

## [v8.11] — 2026-06-07 · 机读层翻译规则「理由」校正（核对官方/社区指南，破除"模型看不懂术语"误传）

> 触发：用户质疑"你确定 Seedance 看不懂专业术语吗？"。联网核对字节官方页 + apiyi（官方指南解读）+ seedance.tv + MindStudio + 火山引擎中文文档后确认：机读层翻译规则的**工程结论正确**（官方同样明确不建议写 mm/f/ISO/fps），但流传的**理由"Seedance 看不懂术语"是错的**——模型对运镜/景深/逆光等术语能识别并执行。本次只校正"理由表述"，不改任何翻译规则/校验阈值/产物。

### 变更
- `skills/seedance-storyboard-skill/translation-audit-rules.md`：版本 1.0→1.1；「核心原理」后新增「🧭 为什么这样规定（实证依据）」段，把四类禁令归到真实原因——①数值参数(mm/f/ISO)不可控且官方不建议 ②剪辑关系(J-Cut/库里肖夫/180°)单条文生视频不可执行 ③命名光法描述化命中率更高 ④英文运镜词为中文输出统一而改中文；并澄清 `0·X秒` 分段即 timeline prompting（推荐技巧），禁 `00:00` 仅为规避记号截断。明令"不得把理由表述为 Seedance 看不懂术语"。
- `skills/seedance-storyboard-skill/SKILL.md`：「零·机读层唯一权威格式声明」末尾加一行「🧭 为什么禁这些（实证依据）」指引，指向 translation-audit-rules.md 单一权威理由段，破除入口处误解。

---

## [v8.9] — 2026-06-07 · 阶段骨架生成器（创作前空壳预填，消灭格式重写循环）

> 触发：用户从"路径一每个流程哪些可脚本化"推进到"哪些可进一步脚本化"，确认从 ROI 最高的「集纲/导演/分镜 骨架生成器」落地。设计边界：脚本只铺确定性外壳（必需章节/字段标签/表头列名/三段式/时间轴结构），绝不预填任何剧情/台词/画面示例，占位符统一 `〔待填写〕`，从根因消除"AI 搭格式/漏字段→校验 FAIL→作废重写"的 token 循环，同时不侵入创作。

### 新增
- `tools/generators/stage-scaffold-generator.py`：阶段骨架生成器，三个子命令 outline / director / storyboard，按校验器必需项精确铺空壳：
  - `outline --chapter chXX --episodes N`：三段式归属 + N 集 3-10-60 空模板 → `assets/outline/{chXX}-outline.md`
  - `director --ep epXX --pblocks N`：5 大模块 + N 个 P 块讲戏骨架（叙事功能/情绪钩子4项/人物清单/场景清单）→ `outputs/{ep}/01-director-analysis.md`
  - `storyboard --ep epXX --pblocks N [--source ...]`：文件级表头（素材/角色/人声锚定表+预算表+逐行覆盖审计）+ 每 P 块全模块（人读层情绪钩子4行/T0九维度/机读层/微表情/钉子4行/翻译审计/密度/台词审计），并并行生成 `03-text-storyboard.md`
  - 安全护栏：目标文件非空时默认拒绝覆盖（防误删已填内容），需 `--force`；支持 `--stdout` 预览、`--out` 自定义路径。
  - 实测：三类骨架填空后均通过 `outline-validator` / `stage-output-validator`（0 critical；剩余 warning 均为待填的时长/时间段数字占位）。

### 变更
- `tools/management/next-step-prompter.py`：集纲/导演/分镜三阶段新增 `scaffold_cmd` 字段，下一步指令中以「🧱 第1步·骨架预生成」打印骨架命令（执行提示降为「第2步」）。由于 `stage-pipeline.py` 复用 next-step-prompter，"审计通过 → 下一步（含骨架命令）"闭环自动成立，无需改动编排器本身。非骨架阶段（如视觉风格选择）不显示该段。集数/P块数为规划决策，命令中以占位提示由 AI 填，不写死。
- 全量单元测试 190 项保持全绿。

---

## [v8.10] — 2026-06-07 · 小说分析抽取生成器（确定性统计/切分归脚本，定性判断留 AI）

> 触发：v8.9 之后继续推进第二梯队"小说分析抽取生成器"。原小说分析全靠 AI 读全本产出，其中"数数、切分、铺目录"是确定性工作却消耗大量 token。落地结论：把统计/切分/铺架脚本化，AI 只保留爽点分类、人物关系定性、概括正文等判断与归纳。

### 新增
- `tools/generators/novel-analysis-scaffold-generator.py`：小说分析抽取生成器，读取 `novel/` 下逐章拆分文件，写入 `assets/novel-analysis/{书名}/`，三个子命令（+`all`）：
  - `groups --per-group N`：每 N 章一组，生成 `概括/组X_第A-B章_概括.md` 骨架（章节标题 + 原文字数已铺好，AI 只写概括正文）
  - `events`：生成 `事件线追踪_chX-Y.md` 骨架（逐章时间锚点表 + 主线/支线表头，AI 只填每章事件与归类）
  - `characters`：人物共现统计——给定 `--characters` 名单时输出**精确出场频次表 + 同章共现矩阵**（纯计数，可直接采信）；未给名单时输出**高频候选词**（2-4字中文 n-gram 词频，明确标注「候选·需人工筛选」，不冒充角色结论）
  - 创作边界：脚本只产出确定性事实（计数/章节锚点/目录结构）与 `〔待填写〕` 空壳，定性结论全留 AI；含非空文件覆盖护栏（`--force`）、`--stdout` 预览、`--novel-dir` 指定拆分目录。
  - 实测：生成的 人物关系分析 / 事件线追踪 经 `novel-analysis-validator` 识别并 PASS；真实小说统计准确（女儿74次/江临35次/沈夜洲7次 + 同章共现矩阵）。
### 变更
- 全量单元测试 190 项保持全绿。

---

## [v8.11] — 2026-06-07 · 章节-集数-P块映射表（消除跨阶段对应漂移）

> 触发：v8.10 之后推进"章节↔集数↔P块映射表"。原本"某集对应小说哪几章"散落在集纲/导演/分镜里靠人/AI 记忆传递，`plot-fidelity-checker` 等只能靠 `--chapter` 手动传参或猜测。落地：把这层对应关系集中解析为一份权威 JSON，供下游直接读取。

### 新增
- `tools/generators/chapter-episode-map-generator.py`：从既有产物自动解析「集 ↔ 小说章节 ↔ P块」对应：
  - 集纲 `*-outline.md`：解析每集标题、`对应原著：序章 + 第1章 + 第2章`（回退内联 `（对应小说第3-4章）`，支持区间展开）、章节归属 chXX
  - `outputs/{ep}/01-director-analysis.md` / `02-seedance-prompts.md`：计数导演/分镜 P 块
  - 产出 `assets/chapter-episode-map.json` + 可读表格；`--stdout` 预览、`--ep` 单集查询、`--out` 自定义
  - 一致性告警：导演P≠分镜P、某集未标注对应章节时提示（不阻断）
  - 边界：只解析既有标注 + 计数，不臆造对应；缺标注/缺产物如实留 null/[]
  - 实测真实项目：ep01→ch01(序章/第1章/第2章) · ep02→ch02(第3-4章,导演46=分镜46) · ep03→ch03(第5-6章)
- `lib/episode_map.py`：映射读取助手（`resolve_chapter` / `resolve_novel_chapters` / `load_episode_map`），fail-soft，供任意工具复用。

### 变更
- `tools/validators/plot-fidelity-checker.py`：新增**映射回退**——仅在未显式传 `--chapter` 时，从 map 解析本集章节（显式 `--chapter` 优先，不覆盖；map 不可用静默回退原逻辑）。实测：显式传参行为不变（无回退提示）、省略时正确回退 ep02→ch02，**零回归**。
- 全量单元测试 190 项保持全绿。

---

## [v8.12] — 2026-06-07 · 分镜产物瘦身（方向B：翻译/密度审计表从必需降级；台词审计保留）

> 触发：用户质疑 02-seedance-prompts.md 里每个 P 块都带的「翻译审计 / 密度校验 / 台词审计」三张表是否必要——它们明确「不喂给模型」，且是 AI **自评 PASS**（与「禁止 AI 自标 PASS」铁律冲突）。选定方向B。
> 🔴 落地中发现**重要边界**：台词审计表是「非配音台词」（如屏幕文字渲染成空白块）的**唯一逐字留存处**，删除会破坏 `check_source_script_coverage` 的源剧本逐字覆盖（属忠实度记录，非自评）。故最终方案：**仅翻译审计 + 密度校验降级，台词审计保留为必需。**

### 关键依据
- 翻译零残留：`check_machine_layer_forbidden`（直接扫机读层禁用术语）——独立于翻译审计表，故翻译审计表可降级
- 节拍密度：`beat-density-checker`——独立于密度校验表，故密度校验表可降级
- 台词逐字：`check_source_script_coverage`（读来源剧本逐字比对）依赖台词在文件中逐字出现；**配音台词**在机读层逐字出现，但**非配音台词**（屏幕文字等）仅在台词审计表逐字留存 → **台词审计表保留为必需**
- 内容校验函数对缺表优雅 no-op，翻译/密度降级为「可选」：表在则照常校验，表缺不再判 critical

### 变更
- `tools/validators/seedance-template-validator.py`：`P_REQUIRED_SECTIONS` 注释掉 translation_audit / density_check 两项；dialogue_audit 保留必需。
- `tools/validators/stage-output-validator.py`：storyboard `required_per_p` 注释掉「📐翻译审计表 / ⏱密度校验表」两项；「🎭台词审计表」保留 critical。
- `tools/generators/stage-scaffold-generator.py`：storyboard 骨架不再铺翻译/密度两表，保留台词审计表（含表头）+ 微表情/钉子4行。
- `AXIS-workflow-stages.md`：分镜「编写中强制检查项」更新为修订版方向B口径。
- 实测：含三表的存量文件仍 critical=0 PASS（表在则校验）；全量单元测试 190 项全绿。
- ⏪ 可回退：取消两个校验器中两处注释即恢复翻译/密度为必需。

---

## [v8.13] — 2026-06-07 · 存量分镜批量瘦身工具（兑现方向B的 token 节省）

> 触发：方向B 改了「校验器不再强制」，但存量 seedance 文件里的表还在。需要一个安全的批量剥离工具兑现节省。

### 新增
- `tools/management/slim-seedance-audit-tables.py`：批量剥离存量 Seedance 提示词文件里的 **📐翻译审计 + ⏱密度校验** 两表（🔴 **不剥离台词审计**——见 v8.12 边界，删之会破坏源剧本逐字覆盖）。
  - 安全设计：默认 dry-run 仅预览（删几节/省多少行字节），`--apply` 才改写且默认写 `.bak` 备份（`--no-backup` 关闭）；剥离边界严格（从表标题到下一个 `####/###/##` 或 `---` 或 EOF），删后折叠多余空行不破坏 P 块分隔。
  - 用法：单文件 / `--dir 目录` / `--scan-all` 全仓扫描。
  - 实测（不敢麻烦别人_动画改编/02-seedance-prompts.md）：剥离 62 个翻译/密度小节、省 1046 行 / 63KB（约 30%）；剥离后 `seedance-template-validator` 仍 **critical=0 PASS**，台词审计 31 节完整保留。
  - 🔬 反例验证：若误删台词审计，会触发 10 个 `SOURCE_DIALOGUE_NOT_COVERED`（非配音台词逐字丢失）——印证 v8.12 的台词审计保留决策。

---



> 触发：用户提出"AXIS 路径每个流程用脚本校验输出能否节省 token 并 100% 按模板输出"，并逐步推进到"审核能否脚本化""其他流程能否脚本化"。落地结论：规则类校验/审计/编排全部脚本化（确定性、0 模型 token、fail-closed），模型仅在「创作生成」与「审美/语义判断」两个不可替代点介入。

### 新增
- `tools/validators/dialogue-sync-checker.py`：台词跨产物逐字同步校验。比对同集 seedance/kling26/kling30 平行成片提示词，逐 P 块提取引号台词，检测 D01 漂移 / D02 丢失（critical）/ D03 多余（warning）。补齐了 cross-file-consistency 不覆盖的"同一句台词在多个产物间是否逐字一致"缺口。已注册进 `run_validators.py`（分集校验器 12→13）。
- `tools/validators/skill-compliance-auditor.py`：Skill 合规审计聚合器（子规则 9-B/9-C 脚本化）。按阶段（outline/script/director/style/design/storyboard）自动跑齐该阶段 workflow 规定的全部校验器，覆盖审计四维度（尤其「工具调用」维度），直接渲染成 9-C 标准报告表（默认文本 / `--md` / `--json`），fail-closed。修正了沿用旧逻辑把"warning 级退出码（如 compliance-keyword exit 2）"误判 FAIL 的问题：能明确解析到 critical=0 时信任解析结果。
- `tools/management/stage-pipeline.py`：阶段一条龙编排器。串联「审计 → 放行判定 → 下一步指令」：调 skill-compliance-auditor 全 PASS 则自动调 next-step-prompter 输出下一步执行指令，有 FAIL 则中止并列修复项（fail-closed，exit 1）。零状态文件副作用，复用 STAGE_PLANS 与 PATH_SEQUENCES 单一权威。FAIL/PASS 两条分支均实测通过。

### 变更
- `tools/validators/run_validators.py`：VALIDATORS 表新增 `dialogue-sync`（ep 模式）；docstring 分集校验器计数 12→13。
- `AXIS-workflow-stages.md`：分镜出口门禁加入 dialogue-sync 与"推荐一键 skill-compliance-auditor"；子规则 9-B 新增「脚本化执行」与「一条龙编排」段；9-C 模板注明应由脚本自动生成。
- `CLAUDE.md`：子规则 9-B 新增 skill-compliance-auditor 与 stage-pipeline 脚本化执行入口，详情指向 workflow-stages.md 单一权威。
- `.stage-gate.json`：分镜阶段 step 名"四校验器统一通关"→"全校验器统一通关（run_validators·含台词跨产物同步）"（run_validators 已含 dialogue-sync，无需另登记，避免重复执行）。

### 修复
- `tools/validators/cross-file-consistency-checker.py`：第 1034 行字符串字面量内误用 ASCII 双引号（`"承接PXX"`）导致 `SyntaxError`、脚本完全无法运行——由 skill-compliance-auditor 对 design 阶段的审计暴露（fail-closed 价值印证）。内层引号改为中文「」，`py_compile` 通过，功能恢复。



> 触发：用户复制单条机读层提示词逐条喂 Seedance，质疑 GSA 首行 `承接P09同一坐位` 等写法——模型逐条独立生成、对其它 P 零记忆，根本无法识别"承接PXX"。定位根因：`spatial-continuity-checker.md` 的状态机规则把"继承上一镜结束状态"示范成把 `（同 P04 结束位置）` 写进锚点，导致全线产物在机读层堆积无效跨片引用。修正口径：继承＝在本镜 GSA 用绝对站位**重写全**，画面级承接靠**首帧承接**（上一条尾帧/构图定格作参考图）实现，跨片叙事意图只写人读层。

### 变更
- `tools/references/spatial-continuity-checker.md`：3.3 黑名单新增"跨P/跨镜文字引用"行；4.1 加 🔴 修正块（继承≠跨片引用 + 首帧承接 + 区分本镜内"终态"合法）；第八节示例一去掉"（同 P04 结束位置）"改绝对站位重写；第七节验收清单黑名单项补跨P引用核查。
- `skills/seedance-storyboard-skill/SKILL.md`：场景站位锁定铁律「同场景连续P」改为"绝对站位重写、禁跨片引用"；GSA黑名单补"跨P文字引用"；新增 P8 FAIL 条件；12 项检查⑫同步。
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：「零·机读层唯一权威格式」新增第 4 条 GSA 跨片引用禁令。
- `skills/seedance-prompt-review-skill/SKILL.md`：机读层格式审核第 1 条补"GSA 跨片引用→FAIL"。
- `tools/_gsa_injector.py`：🔴 修复机械源头——`is_new_scene=False` 分支原自动注入 `同场景继承{prev_pid}终态`（跨片指针），改为只写本镜绝对场景名，靠角色绝对站位自洽承接。
- `tools/validators/cross-file-consistency-checker.py`：C08 GSA 黑名单新增跨片引用词（承接/继承/同一坐位/匹配剪辑，硬拦截 FAIL；"终态"单独合法不纳入）；C08-c 提示语措辞由"继承上一P终态"改为"绝对站位重写"。
- `母亲玩具坏了/今天好热啊_AXIS-Seedance视频提示词_T0标准版.md`：清除全部 P 块机读层 GSA 内的"承接PXX/同一坐位/匹配剪辑承接"跨片引用，并在文件头机读层格式声明补禁令（本文件为产品示范，一并对齐）。

## [v8.6] — 2026-06-01 · 系统级深度排查并修复 23 处 Bug/规则冲突（五遍全量审查）

> 触发：用户要求"深度检查 AXIS 智能体系统流程路径中存在的 Bug 和冲突"，经五遍交叉核查（lib/workflow_paths.py、AXIS-workflow-stages.md、CLAUDE.md 三份权威源 + agents/ + lib/ 全模块 + 状态文件 + .stage-gate.json + 融合模块 + CLI），定位 23 处问题并全部修复。根因：目录重构与规则演进后 CLAUDE.md 主体及部分文档/示例未批量回改，破坏了"单一权威来源"。

### 变更
- `CLAUDE.md`：
  - 【Bug1 路径漂移】`tools/cross-episode-consistency-checker.py`→`tools/validators/...`；`tools/t0-validator.py`→`tools/validators/t0-validator.py --batch --dir assets/prompts/`；`tools/{virtual-lighting-camera-library,camera-movement-master,style-preset-library,emotion-quantization-system,multimodal-dynamic-fusion,cross-platform-converter,quality-prechecker}.md`→`tools/references/...`；文件结构 tools/ 树重写为 validators/references/generators/management 真实子目录布局。
  - 【Bug2】服化道口径明确"只输出 Nano Banana Pro 单版本"（删双版本残留）。
  - 【Bug3】新增 [视觉风格选择阶段] 独立章节 + [完整流程] 补第5步 + 指令集补 `~style` + 导演通知改指向 ~style/~design。
  - 【Bug4】删除不存在的 `costume道具角色设计/`（改指 costume-prop-character-design-skill）、`dynamic-manga-writer/`（删文件结构条目 + manga 平台选项）。
  - 【Bug5/6】集纲/剧本输出统一 `{chXX}-outline.md`/`{chXX}-script.md`；去硬编码"10集/蓄能期1-3加压期4-7升级期8-10"改为动态集数 + 三段式按总集数1/3均分 + 集纲阶段加"动态集数确认"。
  - 【Bug8/12】视听语言标准 27条→29条（3处）。
  - 【Bug10】outputs/ 文件结构由 ep01~ep06 过时快照改为 ep{NN} 通用模板（补 00-dialogue-extraction.md / 03-text-storyboard.md）。
  - 【Bug17】assets 标记规范补 `[epNN][props]` 道具标签定义。
- `AXIS-workflow-stages.md`：
  - 【Bug2】"A/B 双版本"改为"Nano Banana Pro 单版本"（含产物标注）。
  - 【Bug7】角色提案板由"主要必出·次要可选"统一为"全部角色必出·唯一标准"（Checklist ★→✅ + 提案板校验由⚪可选改为🔴必须运行）。
  - 【Bug9】~prompt 默认平台标题"默认 all"→"默认 seedance"。
  - 【Bug13/14】.agent-state.json 标准结构去 `agents` 嵌套层（与调用规则/实际文件一致）+ 新增 stageHistory/currentStage 标准枚举表（统一 -completed/-inherited，禁中英混搭与 complete 无 d）。
  - 【Bug15】"共41个 script 步骤"→"以 .stage-gate.json 实际为准，当前共20个"。
  - 【Bug17】道具标签 `[epNN][prop]`→`[epNN][props]`。
- `agents/art-designer.md`：【Bug2】删 A/B 双版本规范改 Nano Banana Pro 单版本；【Bug1】`tools/t0-validator.py`→`tools/validators/t0-validator.py`。
- `agents/storyboard-artist.md`：【Bug11】审核清单 kling-prompt-review/kling-3.0 + 指令集 kling/kling2/kling3/both/all 全部加 ⏸️ 暂停标记。
- `tools/management/next-step-prompter.py`：【Bug21】`tools/unified-audiovisual-language-library.md`→`resources/...`、`skills/storyboard-generation-cheatsheet.md`→`skills/seedance-storyboard-skill/...`、`skills/cross-platform-converter-skill/SKILL.md`→`tools/references/cross-platform-converter.md`；【Bug22】脑洞产物 世界观.md/人设.md→世界观扩展.md/人设卡片.md；【Bug23】detect_path 默认路径 路径三→路径一（与 engine_cli 一致）；【Bug20】进度条 elif 去除对 next_stage 的依赖（修复完成末阶段时前序阶段误标⬜）。
- `lib/file_parser.py`：【Bug18】新增 `_zh_to_int` 支持复合中文数字（十一/二十/二十一…上限99），修复"第十一集"及以上集数解析为 None 的崩溃；【Bug17】AssetParser 头正则兼容 prop/props。
- `lib/label_parser.py`：【Bug17】_TYPE_MAP 兼容历史单数 `prop`→PROPS。
- `融合模块/chuanban-chaishu-skills/skills/abc-fenxi/skill.md`→`SKILL.md`：【Bug16】修大小写（Linux 大小写敏感系统加载失败）。
- `.agent-state.json`：【Bug14】stageHistory/currentStage 枚举值统一为标准中文 -completed/-inherited。
- `README.md`：【Bug19】"每个生产 Skill 都配 review-skill"修正为"核心生产 Skill 配对 + 部分由共享审核器覆盖"。
- 【扩展全工程广扫·同类残留清零】：
  - `skills/costume-prop-character-design-skill/SKILL.md`（2处）、`skills/costume-prop-character-design-review-skill/SKILL.md`（3处）、`tools/references/quality-prechecker.md`（1处）：`tools/t0-validator.py`→`tools/validators/t0-validator.py`（Bug1 同类残留）。
  - `.windsurf/workflows/axis-stage-gate.md`：服化道出口"A/B 双版本"→"Nano Banana Pro 单版本"（Bug2 同类）；stageHistory `novel-analysis-complete`→`小说分析-completed`（Bug14 同类）。
  - `AXIS-workflow-stages.md`：欢迎词"进阶级27条"→"29条"（Bug8 同类残留）。
  - `skills/short-drama-scriptwriter-review-skill/SKILL.md`（4处）、`skills/script-analysis-review-skill/SKILL.md`（2处）：权威路径 `assets/{outline,novel}/01-short-drama-*.md`→`{chXX}-*.md`（Bug5 同类残留）。`tools/validators/plot-fidelity-checker.py` 的 `01-short-drama-*` 为有意保留的旧名回退默认（优先 {ch}→回退旧名→glob 全目录），属向后兼容设计，不改。
- 验证：`python3 -m py_compile`（4 文件）OK；`python3 tests/run_all.py` 190 tests 全绿；.agent-state.json JSON 合法；next-step-prompter ep01 导演分析 正确输出"下一步：视觉风格选择"；全工程残留扫描（27条/扁平tools路径/双版本/失效skill引用）已全部清零。

---

## [v8.5] — 2026-05-31 · 校验器新增「POV 主观第一视角·自拍脸」检查（用户指令；补盲区）

> 触发：用户发现《今天好热啊》(全片林夏主观第一视角) 机读层在非反射镜头里描写了林夏自己的脸（眼睑/眼眶/嘴角/嘴唇/笑得 等共 7 处），但 `seedance-template-validator.py` 报"全 PASS"——因为旧校验器**根本不检查"POV 角色描写自己的脸"**（SKILL.md 有规则但无强制）。这是校验器盲区，导致反复给出错误的"无问题"结论。

### 变更
- `tools/validators/seedance-template-validator.py`：新增 `check_machine_layer_pov_face` 检查 + `detect_pov_character` / `extract_anchor_characters` 辅助，并接入 `validate_file` 主流程。
  - 触发条件：文件头声明「主观第一视角」且「不拍/不露正脸」时才启用（非 POV 片不触发）。
  - 规则：扫描机读层时间段行，命中 POV 角色自己的面部词（眼睑/眼眶/瞳孔/睫毛/眼角/嘴角/嘴唇/抿住/鼻翼/下颌/脸颊/笑得/含泪/皱眉/挑眉/酒窝）→ 判 critical FAIL。
  - 三重豁免防误伤：① 整行含反射标记（反光/反射/倒映/映出/黑镜/熄屏/水汽/护网/窗玻璃/玻璃门/杯壁/镜面）→ 跳过；② 子句含其他角色名（取自角色锚定表）或 @图片2+ → 是别人的脸、合规；③ 子句含否定/约束（不拍/不露/严禁 等）→ 跳过。
  - 单元烟测：林夏嘴角(非反射)=抓1条 / 黑镜映出嘴角=豁免 / 陈屿嘴角=豁免 / 不露正脸=豁免，零误伤。
- 已知小限制：POV 角色取自文件头声明（如"林夏"），童年同体角色（小夏）在角色锚定表中作他角色处理，其面部描写不会被本检查拦（当前文件无此情况）。
- 回归：《今天好热啊》清理后该检查 0 命中、三处合法反射镜头(P11/P12/P14)正确豁免，整体仍 PASS 0/0。

---

## [v8.4] — 2026-05-31 · 修复 machine-layer-timing-checker 末段密度假阳性（用户校验《今天好热啊》时发现）

> 触发：用户要求严格校验《今天好热啊》并追问运镜。`machine-layer-timing-checker.py` 报 P02/P04/P11 各一个"末段密度超 200字/秒 critical"（共3 critical+4 warning），但经排查这 3 段全是各 P 块**最后一个时间段**——根因是 `strip_meta_lines` 只认 `音效：`，认不出官方模板实际写法 `音效层：`/`尾缀：`/`> 后期…`，导致段后的"音效层+尾缀"（300+字）被计入末段字数，制造假阳性（与 v8.2 同类）。

### 变更
- `tools/validators/machine-layer-timing-checker.py`：`strip_meta_lines` 重写——行首归一化去除 `*＃#>` 强调/引用符后，新增对 `音效层：`（含 `**音效层**：`）、`尾缀：`、`> 后期建议` 引用块的识别并 break。修复后《今天好热啊》该校验器 critical 3→0、warning 4→0（PASS）；ast 语法 OK；时间段分隔符 `·` 双接受（v8.3 P2）保留不变。
- 结论：3 个密度 critical 与 4 个 warning 全为校验器假阳性，**内容本身未改一字**（未误伤台词与描述）。

---

## [v8.3] — 2026-05-31 · Seedance 机读层模板 7 项优化（用户指令"全做"）

> 触发：用户要求优化 AXIS Seedance 提示词模板并指出可优化点。排查发现根因＝**双模板矛盾**：附件④（6层堆栈/6字段/00:00·00:03/{}台词/<>音效/@image_N）与官方机读层规范（GSA首行/70%自然语言/0-Xs秒/独立音效层/参考@图片N）冲突；虽 v8.1 已"融合补强"且 SKILL.md 第237行有冲突边界条款，但条款藏得深、附件④无适用范围声明，导致生成方/审核方反复误用（《今天好热啊》文件头自称"6层堆栈"正文却是自然语言即典型症状）。用户决策"全做"P0-P7。P1/P2 因影响 6 个 python 校验器＋约20个存量产出，采用向后兼容实现（不破坏存量）。

### 变更
- **P0 消除双模板矛盾**（机读层唯一权威＝自然语言格式）：
  - `skills/seedance-storyboard-skill/SKILL.md`：顶部新增「🔴🔴 零·机读层唯一权威格式声明」，钉死机读层唯一合法格式＝自然语言，列明附件④6层堆栈/6字段/00:00·00:03/{}/<>/@image_N 全部仅人读层、进机读层即 FAIL。
  - `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：顶部新增「🔴🔴 零·机读层唯一权威格式」同口径声明。
  - `skills/seedance-prompt-review-skill/SKILL.md`：顶部新增「🔴🔴 零·机读层唯一权威格式（审核基准）」，明确不得因机读层用自然语言而误判、不得因未用6层堆栈而误判。
  - `Seedance_2.0_核心技能速查手册_6层堆栈_6字段_台词_微表情递进链(1).md`（附件④）：顶部新增「🔴🔴 适用范围声明」——本文件全部内容仅供人读层/帧规划层，严禁照搬进机读层。
- **P1 命名消歧（向后兼容，不重命名 token）**：机读层首行 token 仍固定 `[Global Spatial Anchor:]`（中文别称"空间锚点GSA"仅文档用），保留英文 token 兼容 `_gsa_injector.py`/`cross-file-consistency-checker.py`/`beat-density-checker.py`/全部存量产物；在 SKILL.md GSA 段＋附件④声明中显式标注它 ≠ 附件④人读层标签 `[GLOBAL]`，机读层禁出现 `[GLOBAL]`。
- **P2 时间轴分隔符（向后兼容双接受）**：推荐机读层时间段用中点 `0·Xs秒：` 规避 `-` 截断风险，旧式 `0-Xs秒：` 仍兼容。同步：`tools/validators/seedance-template-validator.py` `TIME_SEGMENT_RE` 与 `tools/validators/machine-layer-timing-checker.py` 时间段正则放宽为 `[-~－–—·・]`（py_compile/regex 自测三种分隔符均接受）；SKILL.md＋生成速查表加规范说明。
- **P3 固化台词内联唯一模板**：SKILL.md＋生成速查表钉死唯一带占位符句式（承载方式→台词原文→人声锚定ID→固定音色→语速→音量→气息→尾音→停顿，字段顺序不可变），"气声说出：…"等自由写法判不合规。
- **P4 字数上限改分级**：统一1000字 → 无台词P≤700 / 含台词P≤1100 / 情绪长镜·多台词P≤1300；台词字数永不计入门禁、永不因字数删台词（呼应台词零删减铁律）。同步 SKILL.md、生成速查表、审核 skill（含字数列门禁与格式检查两处）。
- **P5 GSA 白名单增环境状态继承槽**：SKILL.md GSA 段＋`tools/references/spatial-continuity-checker.md` 新增 `环境状态：` 字段（仅开关态：空调已启动/冷白光已铺/温度感转凉/音环境接通），用于跨P继承关键环境变化；禁写描述性渲染与情绪词。
- **P6 允许词/禁止词一页对照白名单**：`storyboard-generation-cheatsheet.md` 新增「五-A」一页对照表（景别/运镜/焦段/光影/剪辑/构图/情绪 七类的 ✅允许 vs ❌禁止），与 translation-audit-rules.md 同口径。
- **P7 审计表瘦身（交付排版）**：`storyboard-generation-cheatsheet.md` 新增「十三、交付排版」——审计表生成时仍必出（不出＝FAIL不变），但交付时折叠进 `<details>` 或文末「附录·逐P自检审计表」，正文聚焦机读层；校验器仍逐P扫描，缺表照 FAIL。
- 说明：v8.3 是把 v8.1"融合补强"决策（保留官方机读层硬规范＝自然语言为唯一机读层标准）显性化、去歧义化，并补足分隔符/台词模板/字数分级/环境槽/白名单/排版六项工程化优化。

---

## [v8.2] — 2026-05-31 · 修复 seedance-template-validator 过期假阳性（用户指令排查）

> 触发：用户质疑校验器过严——连 CLAUDE.md 钦定的 EP01「标准示范版」实测都 critical=82。排查确认校验器有真 bug，与官方模板/标准示范的实际措辞脱节，制造大量假阳性。修复后 EP01 critical 82→24，清掉 58 个假阳性，且对真问题文件（今天好热啊）仍正确 FAIL（校验器未被削弱）。

### 变更
- `tools/validators/seedance-template-validator.py`：
  - **尾缀检查**（MACHINE_SUFFIX_MISSING）：旧版要求三条死字符串「禁止出现任何字幕/视频不要有背景音乐/禁止出现任何文字气泡」，连官方模板与 EP01 的实际尾缀都误杀。改为 `REQUIRED_SUFFIX_GROUPS` 语义分组（①禁屏幕文字/字幕 ②禁背景音乐），每组命中任一同义表述即合规，与官方模板尾缀措辞对齐。EP01 该项 11→0。
  - **人声锚定ID**（VOICE_ANCHOR_ID_MISSING）：`VOICE_ANCHOR_RE` 旧正则只认「人声锚定V2」（ID在后），认不出标准写法「按V2人声锚定表」（ID在前）。新增 `V(?:sys|\d+)\s*人声锚定` 分支。EP01 该项 14→2。
  - **音色情绪参数**（VOICE_CONTROL_INCOMPLETE）：旧版要求每个台词时间段重复全部6项（人声锚定/音色/语速/音量/气息/尾音）；实际标准是完整参数定义在文件级「人声锚定表」、时间段按「按V2人声锚定表…固定音色」引用即可。新增 table_anchored 判定，引用人声锚定表+音色即视为合规（与 EP01 标准示范一致）。EP01 该项 14→2。
  - VOICE_ABSTRACT_TONE 子检查同步豁免 table_anchored 行。
  - **音效层禁令豁免**（MACHINE_AUDIO_FORBIDDEN）：旧版对整段 re.search，导致「禁止任何可生成音乐内容（…音乐铺底等）」这类**禁令举例**里的音乐词被误判为违规（官方模板音效层同样措辞）。改为按句切分 + 禁令豁免：某句含否定词（禁止/无/不/只保留…）时，该句内音乐词视为禁令举例、跳过；真正的肯定式音乐使用（如「古筝渐入烘托」）仍正确拦截。
  - py_compile OK；EP01 82→24；今天好热啊 仍正确 FAIL（mm/f值/英文术语/无0-3秒分段/无音效层等真问题）。
- 说明：EP01 剩余 24 critical 属 B 类——EP01 demo 自身用了旧格式（台词审计旧列名「原文载荷」应为「源剧本原文台词」等），非校验器 bug，留待后续 demo 回炉。

---

## [v8.1] — 2026-05-31 · 4 个 Seedance 表演层附件融合补强官方输出模板（用户指令）

> 触发：用户用 AXIS 校验器实测「今天好热啊」文件 FAIL（critical=95），发现该文件按附件的「6层堆栈」写法（[GLOBAL]+焦段mm+f值+英文运镜术语+00:00·00:03 时间码）而非 AXIS 官方机读层规范（0-3秒自然语言+音效层+尾缀+禁术语），两套规范冲突。用户决策：不二选一，把 4 个附件「融合补强」进 AXIS 官方 Seedance 输出模板——保留官方机读层硬规范，把附件的方法论作为表演层补强接入，并钉死冲突边界。

### 新增
- `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`：新增「零·补强、🎭 表演层增强四件套」权威小节——0.1 四件套分工与调用层（①总调度/②100组微表情物理词库/③台词语气万能公式/④方法论总纲+§39递进链）；0.2 🔴 冲突边界（附件④的 焦段mm/光圈f值/英文运镜术语 只进人读层，机读层按14原则转自然语言、时间段用 0-3秒 而非 00:00·00:03）；0.3 台词语气万能公式（场景状态+声音大小+语速+停顿+尾音+台词原文）；0.4 微表情物理化（含主观第一视角镜只取可拍身体物理的铁律）。

### 变更
- `skills/seedance-storyboard-skill/templates/seedance-prompts-template-enhanced.md`：①改写规则行的「表演层增强」升级为四件套引用；②💥微表情段调用指引改为查附件②词库/附件④§39递进链 + 主观视角取材规则；③人声锚定表上方新增 §0.3 万能公式指针。
- `skills/seedance-storyboard-skill/SKILL.md`：§3.2.1 由「情绪-微表情-语气增强模块」升级为「表演层增强四件套」，每条执行要求对应到具体附件，新增冲突边界与主观视角微表情规则。
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：§十二 升级为「表演层增强四件套」，引用表同步列出 4 个附件与冲突边界。
- `tools/validators/seedance-template-validator.py`：FORBIDDEN_PERFORMANCE_WORDS 的 warning 提示文案由「参考附件①」扩展为「查附件②词库/附件④§39 拆物理描述、按附件③拆人声参数」；注释同步标注四件套。py_compile OK，实测运行正常。
- 🔴 边界总则：4 个附件均为表演层增强，优先级 源剧本原文 ＞ 项目资产 ＞ 官方模板（14原则+机读层规范）＞ 四件套；不得改写源剧本台词、不替代逐行覆盖审计与台词审计；附件的 6字段技术参数与英文术语严禁进入机读层。

---

## [v8.0] — 2026-05-31 · 3 个吃灰的 Seedance 表演层附件强制接入分镜编写阶段（用户指令）

> 触发：用户指出 4 个 Seedance 2.0 表演层附件中，只有「情绪-微表情-语气增强模块」被真正接入，另外 3 个（核心技能速查手册 / 情绪与语气写法手册 / 微表情物理描述素材库100组）放在文件里吃灰，要求确保 AXIS 三条流程路径（~full / ~brainworm / ~start）在输出 Seedance 提示词时都能调用到。三条路径最终都汇聚到【分镜编写阶段】，故在该阶段全部 5 个权威接入位置补挂剩余 3 个附件。

### 变更
- `CLAUDE.md`：分镜编写阶段参考文件列表，在「情绪-微表情-语气增强模块」后补挂 3 个附件为 🔴 必须参考（核心技能速查手册_6层堆栈 / 情绪与语气提示词写法手册 / 微表情物理描述素材库_100组）。
- `AXIS-workflow-stages.md`：①分镜上游必需文件清单、②铁律级 Skill 强制调用 Must-Call Checklist（✅ 列表）两处，均补挂上述 3 个附件（权威 Single Source of Truth，三路径共用）。
- `agents/storyboard-artist.md`：storyboard-artist 参考资源列表，在表演层增强模块后补挂 3 个附件为 🔴 必做。
- `skills/seedance-storyboard-skill/SKILL.md`：资源清单在「表演层增强模块」后新增「核心方法论速查 / 情绪语气写法 / 微表情物理词库」3 条 🔴 必须参考。
- 接入边界保持不变：4 个附件均为表演层增强，调用优先级低于源剧本原文、项目角色/场景/道具资产、AXIS Seedance 模板；不得改写源剧本台词、不得替代逐行覆盖审计与台词审计。

---

## [v7.9] — 2026-05-31 · 角色提案板模板新增影视级渲染必加项 + 两项目角色回填（用户指令）

> 触发：用户要求角色提示词模板新增必加内容（轮廓光 / 发丝光 / 柔光镜 / 小景深），并给「今天好热啊」「不敢麻烦别人」两项目角色提示词加 影视级游戏CG / 次世代3A质感 / 超写实PBR材质渲染 / 4K极致细节 / 柔光电影打光 / 浅景深。

### 变更
- `skills/cinematic-character-pitch-board-skill/SKILL.md`：真实材质铁律新增「🔴 影视级渲染必加」（影视级游戏CG / 次世代3A质感 / 超写实PBR材质渲染 / 4K极致细节 / 柔光电影打光：低强度轮廓光+发丝光+柔光镜 / 浅景深小景深；基础形象与变体均不得省略）。
- `skills/cinematic-character-pitch-board-skill/templates/pitch-board-output-template.md`：中/英文段渲染句注入上述影视级渲染必加项；T0自检清单新增「影视级渲染必加」「柔光电影打光必加」两项。
- `母亲玩具坏了/今天好热啊_AXIS角色提示词.md`：6 角色中/英文段渲染句回填 影视级游戏CG/次世代3A/超写实PBR/4K/柔光电影打光(轮廓光+发丝光+柔光镜)/浅景深；t0 character 实测仍 PASS（6/6×100）。
- `不敢麻烦别人_动画改编/character-prompts-pitch-board.md`：5 角色中/英文段渲染句同样回填；t0 character 实测仍 PASS。

---

## [v7.8] — 2026-05-31 · 新增「场景设定板（单图六区块）」并接入 AXIS（用户指令）

> 触发：用户提供《后院高墙·场景设定》参考图，要求深度复刻为提示词模板并接入 AXIS 系统。新增第三种场景交付物——单图六区块场景设定板（正面+俯视双视图 + 结构分析图 + 材质拆解 + HSB色板）。

### 新增
- `skills/scene-concept-design-skill/templates/scene-design-board-template.md`：场景设定板标准模板（占位符·中英文双段），含三铁律——🔴两视图同源（同一场景母版仅相机角度不同）/ 🔴白灰底板（#ECECEC~#DADADA）/ 🔴六区块齐全。🔴 **通用版面模板·不绑定题材风格**（东方古风/现代/赛博朋克/末世/西幻/科幻/恐怖等任意题材共用同一版面，题材为 `{{}}` 占位填空；校验器只校验版面不校验风格）。
- `skills/scene-concept-design-skill/examples/scene-board-example.md`：《后院高墙》填充范例（白灰底），scene-board-validator 实测 PASS 16/16。
- `tools/validators/scene-board-validator.py`：场景设定板校验器（软失败模式；强制 六区块 + 两视图同源声明 + 白灰底 + ≥4 HSB色 + 中英双段 + 防崩坏；exit 0 通过/跳过、1 critical FAIL）。py_compile OK，实测样本 PASS。

### 变更
- `skills/scene-concept-design-skill/SKILL.md`（1.2→1.3）：双输出路由升级为**三输出路由**（A批量V3.0 / B 13条工业稿 / C 场景设定板）；新增 §九 场景设定板专节（六区块 + 三铁律 + 校验 + 输出 `outputs/<集数>/XX-scene-board-[场景简称].md`）。
- `agents/art-designer.md`：新增「场景设定板（路由C）」交付边界 + 输出路径 + 校验挂载；顺修过时「art-design-skill 分三次读 1188 行」（实际约 330 行）为完整读取。
- `AXIS-workflow-stages.md`：服化道 Must-Call 的 scene-concept-design-skill 标注路由C场景设定板 + 校验器；同修 1188 行过时引用。
- 删除根目录重复件 `场景设定板_复刻提示词模板.md`（模板已收归技能目录 templates/ + examples/，避免双份漂移；分析要点并入 SKILL §九）。

---

## [v7.7] — 2026-05-31 · 角色标准统一：电影级角色提案板取代三栏式（用户指令）

> 触发：用户指令「删除三栏式布局模板，统一改成电影级角色提案板，同步更新所有相应文件」。采用增量安全迁移：提案板为唯一角色标准；存量三栏式 grandfather 兼容、不强制重生、不删项目输出资产。

### 验证器（增量式·实测通过）
- `tools/validators/t0-validator.py`：character 规则放宽为「提案板 OR 三栏式」双收（只加关键词、不删旧词）——背景(纯白/中性灰#BEC1C4)、布局(三栏式/六区块·区块A)、面部(面部特写/头部研究/情绪肖像)、多视图(+turnaround/五视图)、配饰(微距/服装拆解)、比例(黄金比例/身高刻度尺)；CHARACTER_FULL_T0_MARKERS 增 电影级角色提案板/区块A/zone a/pitch board。实测：py_compile OK；存量三栏式(今天好热啊) exit=0 不崩；提案板(红绫V2)结构规则全过(仅差 [ep 资产标记)。

### 模板删除 + 标准翻转（提案板=唯一角色标准）
- `art-design-skill/templates/character-prompt-template.md` & `character-enhanced-template.md`：三栏式模板内容改为**废弃指向桩**（指向 pitch-board-output-template.md）。
- `art-design-skill/SKILL.md`：角色交付物=电影级角色提案板（取代三栏式）；「8项强制要素」表改为提案板六区块要素；变体铁律改提案板格式。
- `art-direction-review-skill/SKILL.md`：审核标准说明 + T0评分(5×20) + 2处格式可执行项 + 诊断指南全部由三栏式改为提案板六区块。
- `CLAUDE.md`：服化道第一步半升级为「角色唯一标准·提案板取代三栏式」，所有角色必出提案板。
- `AXIS-workflow-stages.md`（Must-Call 权威源）：角色阶段标题 + 产出物注释 + 8项强制要素改为提案板。
- `skills/templates/template-library.md`：提案板用途由「与三栏式并列共存」改为「唯一标准·取代三栏式」。
- `costume-prop-character-design-skill/SKILL.md`：3处分工措辞由「三栏式工业资产」改「电影级角色提案板」。
- `art-design-skill/templates/art-design-template.md`：方案A由三栏式改提案板六区块。
- `art-design-skill/references/execution-rules.md`：§2.3 加提案板权威 banner + 要素映射、§2.4 公式改提案板公式；旧三栏式细则标 grandfather。
- `art-design-skill/examples/character-prompt-examples.md`：加历史 banner（三栏式示例标 grandfather，新角色用提案板）。
- `电影级角色设定板_固定布局模板.md`：顶部加「唯一标准·取代三栏式」总纲，覆盖全文旧「并列共存/不替代」表述。

### 残留清理（用户复审「确保没有残留 / 没引发冲突」后补漏）
- `cinematic-character-pitch-board-skill/SKILL.md`（v1.1→v1.2）：清除全篇旧框架——description / 职责划分 / Stage Gate / 一致性铁律 / 上下游 / 诊断 / 学习路径 / 评分 / 版本说明 共 12 处「与三栏式并列共存·不可互替·不替代·提案板→再出三栏式工业资产·前置环节」改为「提案板=唯一标准，下游为 3D 建模/分镜/Seedance 引用」。
- `cinematic-character-pitch-board-review-skill/SKILL.md` + `templates/review-report-template.md`：5+2 处「与三栏式工业资产基底一致」改为「跨视图 A/B/C/D 基底一致（存量资产一并对照）」。
- `art-design-skill/SKILL.md`：补修顶部摘要第 11 行残留「流程位序=提案板→三栏式工业资产」（与 §三 已改部分自相矛盾）；目录列表两个三栏式模板标注「已废弃→改用提案板」。
- 🔴 `agents/art-designer.md`（执行层缺口·最关键，用户追问"角色用哪个模板"时发现）：服化道实际生成角色的【门禁0】原 view_file 已废弃的 `character-prompt-template.md` 且强制旧三栏式结构（A版本/B-1/B-2/B-3）；现改为 view_file `pitch-board-output-template.md` + 提案板六区块结构；行 3/19/71/97「8视图白底 / 双版本」角色格式同步改提案板；并修正过时的「art-design-skill 1188 行分三次读取」（实际约 330 行）。
- `art-design-skill/references/execution-rules.md`：「必须读取输出模板」角色项由 character-prompt-template.md 改指向 pitch-board-output-template.md。
- 🔴 `cinematic-character-pitch-board-skill/templates/pitch-board-output-template.md`（agent 实际读取的活模板·最关键）：T0自检项「与三栏式工业资产基底一致」改「跨视图 A/B/C/D 基底一致」；底部「衔接：提案板确认后再用 costume-prop 出三栏式纯白工业资产」改「下游=3D 建模/分镜/Seedance 引用，不再另出三栏式」——消除活模板里指向已废除流程的活指令。
- `art-design-skill/SKILL.md` 版本注 + `examples` frontmatter：残留「提案板与三栏式共享基底 / v2.1 三栏式」措辞改为「取代三栏式 / 历史 grandfather」。
- 复审实测（第三轮·用户复核"确保没有残留"）：活指令三栏式残留 = 0；剩余 三栏 字样全部属于「废弃/取代声明 + grandfather 历史参考(execution-rules 历史构建表/examples 历史示例，均在历史 banner 下) + CHANGELOG 历史 + 存量项目输出资产 + 验证器向后兼容关键词」；服化道链全指 pitch-board-output-template.md；三栏式存量/提案板/pitch-board-validator 三回归 exit=0。

### 彻底删除（用户「不需要三栏式·废弃的就删除」指令 — 第四轮，不再 grandfather）
- 🔴 物理删除 3 个三栏式文件：`art-design-skill/templates/character-prompt-template.md`、`character-enhanced-template.md`、`examples/character-prompt-examples.md`。
- `execution-rules.md`：删除历史三栏式 8 项要素表 + 三栏式变体铁律正文，替换为提案板要素 + 提案板变体铁律；§2.3 banner 改「三栏式已彻底废除」。
- 🔴 `t0-validator.py` character 规则**移除全部三栏式关键词**（不再向后兼容）：1_background 仅认中性灰（删纯白背景）、2_layout 仅认六区块（删三栏式布局/three-column）、7_proportion 仅认身高刻度尺（删黄金比例）、CHARACTER_FULL_T0_MARKERS + CHARACTER_AUDIT_EXPECTED_ITEMS 同步去三栏式 → character 校验现在**只认提案板**。
- `电影级角色设定板_固定布局模板.md`：删除「提案板 vs 三栏式」对照表 + 「先提案板再三栏式」铁律，改为提案板唯一标准单列表。
- art-design-skill 目录列表删除 3 个已删文件条目；execution-rules / agent「废弃为桩」措辞改「已删除」。

### 影响（用户已授权 B3 全删重来）
- 🔴 存量三栏式角色资产（今天好热啊/完美玩具/刀 等）现 t0-validator --type character **FAIL**（缺中性灰/六区块/身高刻度尺），需回炉重生成为提案板（实测今天好热啊已 FAIL=1）。
- 提案板(不敢麻烦别人) 100/100 PASS；道具/场景规则未受影响（道具仍纯白工业资产）。

---

## [v7.6] — 2026-05-30 · 根治「AI 假装跑校验/假完成」+ 实测暴露历史集漂移

> 触发：用户质疑能否保证每步不漂移、严格按模板输出。实跑校验暴露：ep01-03『分镜编写』被标 completed，实测 seedance-template-validator FAIL（ep01 critical=84，含台词未逐字覆盖/缺必填列章节/缺人声锚定/缺尾缀）——证明"标记完成 ≠ 真通过"。

### 代码级根因修复
- `tools/management/run-stage-checks.py`：原仅更新**步骤级** step.status，从不更新 `stages[].status` 与 `episodeProgress[ep][stage]`，导致脚本 FAIL 而高层仍显示 completed（"假完成"根因）。本次新增：每个阶段跑完后，按该阶段脚本失败数自动把**阶段级 + 集级状态**写为 failed / completed（exit code 派生），并打印 `🔁 阶段级/集级状态依 exit code 写为：X`。

### 反造假硬契约（.stage-gate.json gateRules 新增）
- 规则 14：带 script 阶段的状态只能由 run-stage-checks.py 依真实 exit code 写入；AI/人工禁止手动标 completed；唯一依据是 exit code。
- 规则 15：validator 升级后历史集必须重跑回炉；未 exit=0 一律 failed，禁止以"曾经通过"放行。

### 据实改状态（实测重跑）
- ep01/ep02/ep03『分镜编写』经 run-stage-checks.py 重跑实测 FAIL（4/5、5/5、4/5 项失败）→ `.stage-gate.json` 三集状态已从 completed 据实改为 **failed**，等待回炉修复至 exit=0。

---

## [v7.5] — 2026-05-30 · Skill 全量深度审计后系统补强（P0 中央件 + 服化道提案板标准化，进行中）

> 触发：用户要求深度通读 48 个 SKILL.md 后按 A+C+D+E+F 全量补强，并将电影级提案板并入服化道角色流程。本条记录已落地的中央件，分簇 P1 对齐随后追加。

### P0-1 · 阈值单一裁决（消除「能生成必FAIL」循环）
- `skills/templates/quality-threshold-standard.md` 升 v1.2：新增「生成自检线（≥92）vs 审核交付线（≥95）」分层定义；新增"加权分/X制 与 三维评分冲突时以三维评分为唯一裁决"规则；明确脑洞/时长/桥接等异量纲技能的 PASS 统一回落到本表等级，桥接/结构类生成端必须满足配对 review 的硬性字段（McKee 五节点 / 纠葛≥5）以避免系统性 FAIL。

### 新增 · 电影级提案板并入服化道角色标准流程
- `CLAUDE.md` [服化道设计阶段] 第一步半：电影级角色提案板由「⚪ 可选」升级为「★ 主要角色（主角+重要配角）必出」；明确流程位序（提案板拍板 → 再出三栏式工业资产）与"同一基底人物"双向核对铁律（pitch-board-review × art-direction-review）。
- `skills/art-design-skill/SKILL.md`：技能定位处补「主要角色标准交付·电影级提案板」交叉引用，指向 cinematic-character-pitch-board-skill。
- `AXIS-workflow-stages.md`（Must-Call 单一权威源）：服化道阶段提案板由「⚪ 可选加载」同步升级为「★ 主要角色必出 / ⚪ 次要可选」，两处标记（加载清单 + 审核清单）与 CLAUDE.md 一致，消除"CLAUDE 必出 vs 权威源可选"的不一致。

### P1-B · compliance 审核绑定自动化（消除子串误杀类问题）
- `compliance-review-skill/SKILL.md`：新增「第零步·强制自动化扫描」前置门禁（`compliance-keyword-checker.py`，exit1→FAIL / exit2→人工复核 / exit0→进入人工）；新增「子串误杀白名单 SOP」（compliance-whitelist.json context_patterns，覆盖「色情⊂音色情绪控制」「性感⊂惯性感」类）；色情/低俗评分补「暴露度分级量表」（领口深度 / 镜头距离 / 镜头时长）。

### P0-3 + P1-C · 分镜主链 / 时长 / 光影
- `seedance-storyboard-skill` ＆ `seedance-prompt-review-skill`：机读层术语统一为「禁止列表（mm/J-Cut/伦勃朗光/丁达尔/钟面）vs 允许列表（特写/推镜/长焦镜头等可执行影视词）」，两侧互指 translation-audit-rules 为同一标准，消除「30%影视词 vs 术语零残留」误杀。
- `seedance-prompt-review-skill`：新增「第三步·时长校验」（读 `outputs/<集数>/00-duration-sovereign-report.md` + 各 P 秒数求和 ≥ 目标）。
- `sovereign-duration-predictor-skill`(+review)：主权报告落盘路径固定 `outputs/<集数>/00-duration-sovereign-report.md` + frontmatter 字段；对白时长公式统一约 0.4s/字。
- `film-lighting-technique-skill`：新增「Seedance 机读层改写对照表」（伦勃朗光/丁达尔/蝶形光 → 可执行画面描述）；时钟方位改画面方位词。
- `storyboard-generation-cheatsheet.md`（收尾对齐）：对白铁律 `字数×0.3秒` → `口型 字数×0.4秒 / 画外音 字数×0.2秒`，消除与 sovereign-duration-predictor/SKILL/seedance-review 已统一的 0.4s 口径残留矛盾。

### P0-2 + P1-D · 五问法决策 + 美术簇对齐
- `aesthetic-vision-skill`：五问法定为单一权威——「📐 Q1-Q5 写人读/元数据区允许，禁止混入中英文生图描述段」，消除「禁止写入 vs 要求写入」矛盾。
- `art-direction-review-skill`：T0 审核项对齐 art-design v2.1「三栏式」；审核对象补 props / pitch-board；新增「未附 t0-validator / pitch-board-validator → 直接 FAIL」门禁。
- `scene-concept-design-skill`：明确「V3.0 资产 vs 13 条全维度稿」双路径默认路由；解决「场景无人物 vs SSR 入镜」冲突。
- `costume-prop-character-design-review-skill` ＆ `cinematic-character-pitch-board-review-skill`：五问法审核项统一按 aesthetic-vision 口径。

### P0-4/5 + P1-E · 生成核心（⚠️ 诚实修订：E 簇子 Agent 大部失败，下列为 git 核对后的真实状态）
- ✅ `short-drama-scriptwriter-skill/SKILL.md`：已写入「台词零删减铁律（优先级最高）」+ 集纲精彩台词必须全量落地。
- ✅ `novel-dialogue-extractor-skill/SKILL.md`：F-PACE「[可删减]」改为「仅标优先级、不得删除」+ 删减须用户显式授权 + 落盘路径 `assets/novel-analysis/{书名}/对话清单.md` + 台词零删减铁律。
- ✅ `short-drama-architect-skill`：经 git 核对，本就合规（描述已含"按章动态规划集数"、故事梗概≤150字、通过标准已引用 quality-threshold-standard），无需改动。
- ⏳ 待修（未完成）：`short-drama-architect-review-skill`「分镜连贯性」错配维度需改「集间叙事衔接/钩子—爽点因果链」；`story-card-bridge` 生成端 McKee 五节点未补全；`director-skill` 梗概字数对齐仅 1 行改动需复核。

### ✅ 第二批补强完成（剩余 27 个 Skill，全部 git 核对，"全做"模式）
- chuanban 融合 6 个：路径对齐 `assets/novel-analysis/`、补「融合分析报告.yaml」步骤、front matter/字段映射（情绪类型/3-10-60/可改编集数）、abc 文件名说明。
- chuanban 字数统一（收尾）：分章概括字数全模块统一为「约500字」——以操作提示 `sub-agent-prompt.md「严格限定500字」`＋用户指南/README/AI部署说明为准；回退 fen-zhang SKILL 的 4 处 600 与 chai-shu 欢迎页 1 处离群 600，消除 500/600 漂移。
- 生成审核对：`short-drama-architect-review`（"分镜连贯性"错配改"集间叙事衔接/钩子—爽点因果链"+集纲结构校验）、`short-drama-scriptwriter-review`（台词忠实度审计+去心理化分级）、`script-analysis-review`（集纲模块FAIL项+权威输入路径）。
- `story-card-bridge`：生成端补 McKee 五节点强制字段表；`story-card-bridge-review`：通过线统一引用阈值表。
- `director-skill`：故事梗概对齐为「一句话标题≤50 + 故事梗概≤150」。
- `brainworm-generator`(+review)、`genre-adaptive`(+review)：题材索引/竞品必填/集数比例制/3-10-60逐集检查/术语统一/阈值引用。
- `plot-psyche-double-helix`(+review)：绝对视觉化桥接节+节点命名统一+映射可填表。
- `character-interaction-design`(+review)：输出标准块+群演>8 FAIL+性暗示构图评分维+阈值引用。
- `visual-language-logic-review`、`visual-style-selector-review`（补PASS/案例/百分制）、`kling-3.0-prompt-review`（修审核文件名为 02-kling-3.0-prompts.md）。
- `cinematic-character-pitch-board`(+review)：Stage Gate + 五问法写人读区/禁混入生图段（与 aesthetic-vision 口径）；`costume-prop-character-design`：阈值统一+与 art-design 分工；`top-tier-character-cg`：visual-style-selector 触发路由+禁用于 scene-prompts。
- 注：pitch-board×2 与 top-tier-cg 三个文件为 git 未跟踪新文件，改动已写入（grep 确认），git diff 无法显示。
- ⏳ 仍可选 P2：统一全文确认码、补 Must-Call 触发、genre 30+ 题材完整索引（装饰性，未做）。

---

## [v7.4] — 2026-05-29 · 深度评估「优先改进建议」全量修复（P0/P1/P2 五项）

> 触发：用户对系统深度打分后要求「四、优先改进建议 全部深度严格修复」。本轮完成 5 项，全部实测验证。

### P2 · 安全（门禁执行去 shell 注入面）
- `tools/management/run-stage-checks.py`：门禁脚本执行从 `shell=True`（字符串）改为 `shlex.split` + `shell=False`（argv 列表）；解释器名替换移到分词后；新增命令解析失败的 failed 兜底。实测 `剧本生成`/`小说分析`（含单引号中文参数 `--book '在言情文里女主选择谁谁才是男主'`）均正确解析执行。

### P0 · 剧本逐字台词门禁落地（完成 v7.3 遗留「待验证」）
- `tools/validators/novel-dialogue-fidelity-checker.py`：新增 `--all-chapters`，原著台词比对扩展到 `novel/` 全部 `.txt`（新增 `gather_all_novel_dialogues()`，按标准化文本去重）。根因：剧本含跨章/预告/回忆台词，单章节定位会把这些**合法原著原文**误判为「自创台词」。默认（prompt 目标 / 单章节）行为零改动。
- `.stage-gate.json`：`剧本生成` 阶段新增硬门禁步骤「台词逐字忠实度校验」`required:true` → `novel-dialogue-fidelity-checker.py {ep} --target script --chapter {ch} --all-chapters`。实测 ep01/02/03 = 57/63/44 条**全 exact、0 漂移**通过；`run-stage-checks.py ep01 剧本生成` 端到端 ✅ 通过 2/失败 0。

### P1 · 测试覆盖（138 → 190 全绿）
- 新增 `tests/unit/test_novel_dialogue_fidelity_checker.py`（normalize_quotes/normalize_text/similarity 子串规则/get_threshold/extract_novel/extract_script/match_all 状态机/`gather_all_novel_dialogues` 含文件系统）。
- 新增 `tests/unit/test_seedance_template_validator.py`（split_into_p_blocks/extract_section/机读层人读层抽取/TIME_SEGMENT_RE/QUOTED_PAYLOAD_RE/SEVERITY_ORDER）。
- 新增 `tests/unit/test_cross_file_consistency_checker.py`（extract_p_ids/_extract_scene_from_section/check_c08 空·缺失·合规三分支/Issue 契约）。
- 扩展 `tests/unit/test_beat_density_checker.py`（_is_bubble_context / _is_system_or_ui_text）。
- `python3 tests/run_all.py` → Ran 190 tests, OK。

### P1 · Must-Call 清单单一权威（消除双份漂移）
- `AXIS-workflow-stages.md` §「铁律级 Skill 强制调用 Must-Call Checklist」声明为**唯一权威来源**。
- `CLAUDE.md` 子规则 9 删除重复的 7 段逐阶段清单，改为指向上者；消除既有漂移：服化道阶段 broken path `skills/costume道具角色设计/SKILL.md`、分镜阶段 `27条`（实为 29 条）与缺失的 aesthetic-vision/scene-concept-design/prop-concept-design 等审核项。子规则 9-A 强制实读规则保留不变。

### P0 · README 补全
- `README.md` 从 2 行占位（`# AXIS- / 自动化`）补为完整文档：核心理念、三条工作流路径、目录地图、常用 CLI（engine_cli / run_validators / run-stage-checks / tests / reset_project）、阶段门禁机制、状态文件说明。

### 🔧 复查补丁（用户追问后发现并修复的系统级漏洞）
> 自查发现 P0b 起初**只是项目局部修复**：只改了当前 `.stage-gate.json`，未改 `reset_project.py` 的 `STAGES_TEMPLATE`（生成所有新项目门禁的模板）。该模板与 live 已严重脱节，新项目 reset 后会丢失大量 script 门禁。本次**全量对齐**模板到 live 强门禁套件：
- 小说分析 + `novel-analysis-validator.py`（省略 `--book`，`detect_book(None)` 自动识别分析目录）。
- 集纲生成 + `stage-output-validator.py {ep} outline --chapter {ch}`（`ch01` 通用化为 `{ch}`）。
- 剧本生成 + `plot-fidelity-checker.py {ep}` + `novel-dialogue-fidelity-checker.py {ep} --target script --chapter {ch} --all-chapters`。
- 视觉风格选择 + `visual-style-validator.py --file assets/visual-style-guide.md`。
- 服化道设计：`T0自动化校验` 步骤补回 `t0-validator.py --batch --dir assets/prompts` script。
- 分镜编写 + 模板校验 / 文字分镜校验 / 跨文件一致性 / `run_validators.py {ep}` 四道 script 门禁。
- 新增整个 `集间交接` 阶段（进度报告 / 快照 / 下一步 / 增量基线 / 仪表盘 5 个 script）。
- `ep1_progress` 补 `_chapter`、`集间交接`，确保 `{ch}` 占位符可被 `run-stage-checks` 解析。
- **门禁规则统一**：`reset_project.py` 的 `GATE_RULES` 由 `{description, rules:[10 字符串]}` 改为与 live `.stage-gate.json` 同构的 `array of {id, rule}`；两边内容合并去重为 **13 条**权威规则（原模板审核流程铁律 + live 的脚本不可跳过/子步骤即时同步/快照传递/集间交接操作铁律），修正 live 原 typo「校本校验」→「脚本校验」；结构对齐 `/api/gaterules`（返回数组）契约。
- 验证：`py_compile` 通过；`.stage-gate.json` `python3 -m json.tool` 通过；`reset_project.py --dry-run` 成功构建新模板（含数组 gateRules）、**零写入** live 文件。

---

## [v7.3] — 2026-05-29 · 剧本阶段台词逐字校验能力（深度评估 P0·改动①）

> 触发：深度评估发现"剧本台词被改/缩写/意译"在剧本阶段无逐字校验拦截 —— `plot-fidelity-checker` 只比对剧情事件覆盖、不逐字比对台词；`novel-dialogue-fidelity-checker` 原仅校验分镜 seedance/kling 文件（硬定位 `outputs/{ep}/`，剧本阶段无此文件，挂上去会因找不到文件 exit 1 形成假红灯）。

### 新增
- `tools/validators/novel-dialogue-fidelity-checker.py`：新增 `--target {prompt|script}` 参数（默认 `prompt`，**现有分镜 seedance/kling 校验行为零改动**）。`--target script` 时读取 `assets/novel/{chapter}-script.md`，用新增 `extract_script_dialogues()` 按剧本格式（`角色（修饰）："台词"`）提取台词，复用既有 `difflib` 比对引擎与 `extract_novel_dialogues` 原著台词提取，逐字核对剧本台词是否忠实原著。docstring 用法与 `--target` 帮助同步更新。

### 待验证（暂未挂门禁）
- 尚未接入 `.stage-gate.json` 剧本生成阶段门禁。原因：`tools/management/run-stage-checks.py` 不区分 `required` 软失败（任一脚本非零退出即整体 `exit 1`），若剧本把原著长台词分句/子串化，可能造成首次比对误报。计划：先对 ep01-ep03 只读跑 `--target script` 实测匹配率，确认无误报后再升级为剧本阶段硬门禁。

---

## [v7.2] — 2026-05-29 · 系统健壮性与一致性修复（深度评估后续·8 项改进）

> 触发：用户深度评估 AXIS 系统后，按改进建议执行。聚焦门禁强制力、安全、状态一致性、文档对齐、测试覆盖。

### 安全 / 正确性
- `tools/validators/run_validators.py`：统一校验入口改为 **fail-closed** —— 子进程崩溃（Traceback）、非零退出码、脚本缺失/异常一律计入失败，新增 `total_errors` 统计，不再因"解析不到 critical 数字"而默认放行；修正过时 docstring（实为 12+1 个校验器，非 4 个）。
- `axis-web/backend/main.py`：修复 `/api/validate` 命令注入（`shell=True`+拼接用户参数 → `shell=False`+`shlex` 分词+参数白名单+ep 正则校验）；修复 `derive_ep_status` 阶段完成判定字段值不匹配（`"complete"` → 兼容 `"complete"/"completed"` 且按 key 排除元字段）。

### 门禁强制力
- `engine_cli.py`：新增 `--mode gate --ep <集> --stage <阶段>`，委托既有 `tools/management/run-stage-checks.py` 执行阶段门禁并以退出码反映通过与否（此前 engine_cli 仅只读查看、不执行门禁）；新增 `check_project_consistency()` 在每次运行时校验 `.stage-gate.json` 与 `.agent-state.json` 的 projectName 一致性；修复 `cmd_next_step` 将 import 失败误判为"全部阶段完成"的吞异常 bug。

### 一致性 / 文档对齐
- `agents/director.md`：5 处 `tools/batch_review.py` → 实际路径 `tools/management/batch_review.py`；修复第73行编码损坏字符。
- `CLAUDE.md` / `AXIS-workflow-stages.md` / `.windsurf/workflows/axis-stage-gate.md` / `skills/script-structure-diagnosis-skill` / `skills/script-structure-diagnosis-review-skill` / `skills/story-card-bridge`：移除指向不存在文件的引用 —— 道具提取对齐到 `art-designer` + `prop-concept-design-skill` + `costume-prop-character-design-review-skill`（依据 workflow-stages 阶段三定义）；小说分析对齐到融合模块 chuanban-chaishu-skills；agents 文件结构补 `visual-style-selector.md`、删不存在的 `prop-system-extractor.md`/`novel-analyzer.md`。
- `CLAUDE.md`：修正开场白"支持两条工作路径"笔误（实列三条）；删除剧本阶段通知重复行。
- `.stage-gate.json`：清理脏数据 —— 小说分析门禁脚本残留的他项目书名 `贵族学院小绿茶` → 当前项目 `在言情文里女主选择谁谁才是男主`。

### 测试 / 工程卫生
- 新增 `tests/unit/test_t0_validator.py`：为 T0 校验器补 15 个单元测试（关键词检测/防崩坏/返回契约/未知类型/clean_text/heading_level），全部通过。
- 删除死代码 `lib/validator.py` + `tests/unit/test_validator.py`（仅被自身测试引用，无生产调用）。
- 删除悬空符号链接 `lib/lib`（指向已迁移的旧项目路径）；归档 7 个一次性脚本至 `tools/generators/_archive/`。

### 路径体系统一（用户确认后执行）
- 以 `lib/workflow_paths.py` 的 3 条路径为唯一权威，统一 `CLAUDE.md`：任务定义/总体规则的"四条路径"→三条，并补全道具与金手指提取、视觉风格选择阶段；智能路由"路径三=直接进集纲"重述为"路径一/二中途续跑"，消除与代码"路径三=导演开始"的语义冲突。

### 状态隔离（档位 A·用户确认后执行）
- `lib/io_utils.py`：新增共享函数 `check_project_consistency(root)`，统一多项目脏数据混淆检测。
- `engine_cli.py`：改用共享版（消除内联重复）；`tools/management/stage-step-updater.py`：写状态前接入一致性校验告警。
- 说明：`reset_project.py` 的 STAGES_TEMPLATE 本身不含硬编码书名（结构干净），残留书名系绕过该工具手动编辑所致；档位 B（projectId/归档）、档位 C（每项目独立目录）仍待后续按需推进。

### axis-web 安全审查第二轮（用户确认后执行）
- `axis-web/backend/main.py`：修复 `/api/browse`、`/api/read` 的**路径遍历前缀绕过**漏洞（`str.startswith` → `Path.relative_to` + ROOT `resolve()`，抽出 `ensure_within_root`）；`/api/validate` 的 `extra_args` 拦截 `..`；`read_json` 补 JSON/IO 异常处理。
- 前端审查：`client.js`（错误处理 + `encodeURIComponent`）、`StudioPage.jsx`（`react-markdown`、无 `dangerouslySetInnerHTML`）健康，无需改动。

### 测试覆盖扩展
- 新增 `tests/unit/test_compliance_keyword_checker.py`（14 测试：词库索引/白名单/去重/扫描）、`tests/unit/test_beat_density_checker.py`（9 测试：P 块提取/时长解析）。
- 全套件：115 → **138 测试全绿**。

---

## [v7.1] — 2026-05-06 · 场景叙事模板 V3.0.1 增量吸收（向下兼容）

### 背景
对比候选场景模板（5 层叙事 + 空间分层 + 构图独立 + 灯光分层 + 风格化负面 + 输出要求）与现行 V3.0，确认候选模板**框架更工业化**但**叙事性、灯光工业参数、AI 出图稳定性、洁净度兜底**均明显弱化。决策：**不替换**为候选模板，**增量吸收**其 5 个工业化优点为 V3.0.1 推荐字段，向下兼容。

### 新增
- `skills/scene-concept-design-skill/SKILL.md` 新增 §八·5「场景叙事模板 V3.0 资产格式 + V3.0.1 增量字段」章节：
  - 8.5.1 V3.0 五层叙事架构骨架代码块
  - 8.5.2 V3.0 强制字段（10 项·缺一即 critical）
  - 8.5.3 V3.0.1 增量推荐字段（5 项·向下兼容·命中加分·非 critical）
  - 8.5.4 升级判定（5/5 完全升级 / 1-4 部分升级 / 0 纯 V3.0）
  - 8.5.5 决策表（5 类场景的版本推荐）
- `tools/validators/t0-validator.py` 新增 `RECOMMENDED_FIELDS_V3_1` 推荐字段扫描：
  - 核心主体硬锁 / 空间分层补充 / 构图独立段 / 灯光分层 / 风格化负面
  - 命中字段计入 `passed_items`，缺失字段不入 `missing_items`，不阻断 critical
  - 公开输出条目级命中率（fully_upgraded / partial_upgraded）

### 变更
- `assets/prompts/scene-prompts.md`：
  - 顶部声明区追加 V3.0.1 增量字段说明（5 个推荐字段 marker 列表）
  - 首条「现代书房·电脑屏幕前」升级为 V3.0.1 完整示范：
    - 在 ② 空间叙事体之后追加 3 个推荐字段（核心主体硬锁、空间分层补充、构图独立段）
    - ③ 光影情绪引擎重写为灯光分层格式（保留 3200K/7500K 色温，新增主光/辅光/高光集中/阴影/光比）
    - ⑤ 技术封印末尾追加风格化负面（不要海报式摆拍/不要游戏CG界面感/不要概念草图感等）
  - 其余 7 个场景保持纯 V3.0（仍合法 PASS）

### 校验回归
- `python3 tools/validators/t0-validator.py --type scene --file assets/prompts/scene-prompts.md` → ✅ PASS 100/100
- 8 个场景全部 V3.0 强制要素命中（11 项 passed_items）
- 首条示范场景 V3.0.1 推荐字段 5/5 全命中（passed_items 包含「场景叙事模板v3.0.1全部推荐字段命中 ✓（1条目）」）
- 0 critical / 0 missing
- 现行 8 个 V3.0 场景资产、scene-concept-design-skill、scene-prompts-standard.md 全部零回归

### 不替换的原因
候选模板若直接替换会击穿：T0 校验器（V3.0 五层结构 + 置顶中文前缀 + HEX + 人物词拦截硬写死）、8 个 EP01-EP03 V3.0 资产、`assets/prompts/scene-prompts-standard.md` 全维度交付稿副本、`scene-concept-design-skill §八` 模板、双层融合（写实CG + MAPPA暗黑）风格前缀体系、`absolutely no people` 硬约束、`Material as Time Evidence` 叙事钩子、色温 K + HEX 工业参数。

---

## [v7.0] — 2026-04-30 · 电影感精确词汇参考表 + 全链路引用更新

### 新增
- `resources/电影感精确词汇参考表.md`：
  - 电影感七层模型（光比/色彩分离/景深/镜头光学/大气介质/构图/胶片质感）
  - 逐维度中英对照精确词汇表
  - 经典电影风格锚点（6部代表作）
  - 电影感增强行模板示例（可直接插入⑤技术封印层）
  - 负面提示词参考（排除非电影感渲染）

### 变更
- 9个文件新增引用 `resources/电影感精确词汇参考表.md`：
  - `skills/art-design-skill/SKILL.md`（扩展资源·电影摄影三件套）
  - `skills/film-lighting-technique-skill/SKILL.md`（扩展资源·电影摄影三件套）
  - `skills/film-lighting-technique-review-skill/SKILL.md`（按需查阅）
  - `skills/scene-concept-design-skill/SKILL.md`（电影摄影扩展资源）
  - `skills/director-skill/SKILL.md`（电影摄影扩展）
  - `agents/director.md`（按需查阅）
  - `skills/seedance-storyboard-skill/SKILL.md`（两处·电影摄影三件套）
  - `skills/seedance-prompt-review-skill/SKILL.md`（按需查阅）
  - `tools/references/virtual-lighting-camera-library.md`（互补资源）
- `assets/prompts/scene-prompts.md`：头部注释新增⑤技术封印层电影感词汇参考指引
- `assets/prompts/scene-prompts.md`：全部场景「绝对禁止」条目统一为「人物/角色/人影/剪影/路人」，空间叙事体描述统一为「绝对无人物」

---

## [v6.9] — 2026-04-29 · v3.0 场景模板中文前缀置顶与场景专用美术风格校验

### 新增
- `assets/visual-style-guide.md`：
  - 新增「现实层场景专用中文美术风格前缀」
  - 新增「虚拟层场景专用中文美术风格前缀」
  - 明确场景前缀只用中文描述环境/空间/材质/光影/界面，不写人物、角色、人像、皮肤、发丝、服装配饰等人物风格描述

### 变更
- `skills/art-design-skill/templates/art-design-template.md`：
  - v3.0 模板在 `### 场景叙事模板 v3.0` 下方第一行置顶 `美术风格前缀：`
  - `风格锚` 字段明确不得写人物风格标签
- `skills/art-design-skill/references/execution-rules.md`：
  - 场景唯一模板规则同步新增前缀置顶要求
  - 新增场景前缀必须中文、禁写人物风格要求
- `skills/scene-concept-design-skill/SKILL.md`：
  - 场景无人物铁律同步升级为「美术风格前缀置顶 + 禁写人物风格」
- `assets/prompts/scene-prompts.md`：
  - 现有全部 v3.0 场景条目补齐置顶 `美术风格前缀：`
- `tools/validators/t0-validator.py`：
  - `FUSION_FIELDS_V3` 新增「美术风格前缀」必填项
  - 新增逐条场景校验：`美术风格前缀：` 必须位于 `<!-- ① 灵魂句 -->` 之前
  - 新增中文前缀校验：除 HEX 色值外，场景前缀禁止夹英文
  - 新增人物风格词拦截：场景前缀禁止包含人物/角色/人像/皮肤/发丝/服装配饰等词

---

## [v6.8] — 2026-04-29 · 废弃 v1.0/v2.0，场景叙事模板 v3.0 为唯一标准

### 删除
- 场景模板 v1.0（融合输出模板9字段）和 v2.0（段落填空式）正式废弃
- `t0-validator.py`：删除 FUSION_FIELDS_V1、FUSION_FIELDS_V2、多版本检测逻辑
- `art-design-template.md`：删除三版兼容说明、删除v2.0对比列

### 变更
- `tools/validators/t0-validator.py`：
  - 只保留 FUSION_FIELDS_V3（唯一标准）
  - T0_CHECKS 字段名全部改为 v3.0 术语（视线路径/叙事暗线/光影情绪引擎/色彩封印/风格锚/禁止项）
  - 旧格式条目（v1.0/v2.0）自动标记为「需升级为v3.0」
  - 限制项检测简化为「绝对无人物」必须存在
  - 所有注释清理为 v3.0 基准
- `art-design-template.md`：
  - 唯一模板声明，v1.0/v2.0已废弃
  - v3.0 模板每层添加 Skill 引用注释（①灵魂句→scene-concept-design-skill ②空间叙事体→camera-movement-master+visual-language-logic ③光影→film-lighting-technique-skill+virtual-lighting-camera-library ④材质→material-tagging-tool ⑤技术封印→camera-movement-master+visual-style-selector-skill+style-preset-library）
- `assets/prompts/scene-prompts.md`：头部注释同步为16条场景已全部完成 v3.0 重写
- `assets/prompts/scene-prompts.md`：现有16条场景已全部完成 v3.0 转换，并通过 T0 场景校验 100/100
- `execution-rules.md`：场景唯一模板 v3.0
- `scene-concept-design-skill/SKILL.md`：清理旧版本号引用
- ✅ 现有16条旧格式场景条目已按 v3.0 格式重写完成

---

## [v6.7] — 2026-04-29 · 场景叙事模板 v3.0（5层叙事架构）

### 新增
- `skills/art-design-skill/templates/art-design-template.md`：
  - 场景模板从 v2.0（段落填空式）升级为 v3.0（5层叙事架构）
  - 5层结构：①灵魂句 → ②空间叙事体（视线路径式） → ③光影情绪引擎 → ④材质时间证据 → ⑤技术封印
  - 核心变化：从"填参数"升级为"讲故事"——禁止清单式描述，改用视线路径式叙事

### 变更
- `tools/validators/t0-validator.py`：v3.0 字段支持
- `assets/prompts/scene-prompts.md`：头部注释更新
- `skills/art-design-skill/references/execution-rules.md`：v3.0 场景模板指引
- `skills/scene-concept-design-skill/SKILL.md`：时间锚定规则清理

---

## [v6.6] — 2026-04-29 · 场景输出模板 v2.0（22变量版）

### 新增
- `skills/art-design-skill/templates/art-design-template.md`：
  - 场景输出模板升级为 v2.0（段落式，22个变量，适配多风格项目）
  - 替代旧版融合输出模板 v1.0（9字段 labeled bold fields）
  - 新增3个项目级变量：`[风格定位]`、`[风格标签]`、`[风格排除项]`（支持写实CG/纯2D动画等）
  - **新增22变量速查映射表**（全部附推荐值），按6大类组织：
    - A. 项目级变量（风格定位/标签/排除项 × 5种风格类型）
    - B. 场景设定变量（地点/时间/天气，时间×色温关联表）
    - C. 主体与空间分层（主体/画面位置/三层纵深/叙事痕迹）
    - D. 镜头语言（焦段×情绪隐喻/机位×高度/构图方式/情绪关键词×镜头+光线联动）
    - E. 光线与材质（光源类型×色温×方向/辅光/7大材质类）
    - F. 色彩设计（主色/辅助色/强调色 占比+6种情绪调性配色方案含HEX）
  - 映射表来源索引：camera-movement-master / virtual-lighting-camera-library / visual-style-guide / style-preset-library / scene-concept-design-skill
  - 旧版 v1.0 条目继续有效，校验器同时支持新旧两版

### 变更
- `tools/validators/t0-validator.py`：
  - T0_CHECKS["scene"] 扩展关键词，同时匹配 v1.0 和 v2.0 格式
  - FUSION_FIELDS 拆分为 FUSION_FIELDS_V1（8字段）+ FUSION_FIELDS_V2（9段落标记）
  - 每条场景条目自动检测模板版本，按对应字段集校验
  - 主体字段人物检测兼容 v2 `核心视觉主体是` 段落格式
  - 修复 v1.0 误检：移除从未使用的「动作」字段检查

### 同步
- `art-design-template.md` 场景提示词规范：主体字段铁律覆盖 v1+v2 双格式
- 现有 `scene-prompts.md`（16条 v1.0 条目）通过校验 100/100

---

## [v6.5] — 2026-04-28 · 三位一体重构（校验器体系升级）

### 重构
- `tools/validators/machine-layer-timing-checker.py`：
  - Rule 7 聚合计算改为类型分离：气泡字数×BUBBLE_CHAR_SPEED(0.20) + 口型字数×AGG_NARRATION_SPEED(0.25)（原版混合计算偏宽松）
  - 常量体系全部加关系注释（分段级 Rule 4/5 vs P块聚合级 Rule 7 的速率差异说明）
  - 新增 `--strict` 标志：Rule 7 critical 阈值从 2.0× 降至 1.5×，接入 CI 时可开启
  - **修复 Rule 编号注释错误**：代码内注释由错误的"规则 1/2/3/4/5"改为与 docstring 对齐的正确编号
    - 前置检查（无编号）：声明时长缺失
    - 规则 1：机读层最大结束时间 ≤ 声明时长
    - 规则 2：时间段间隙/重叠检测
    - 规则 3：单段内容密度
    - 规则 4+5：单段对白时间预算（口型 / 气泡分别计算）
    - 规则 6：P块时长 ≤ P_BLOCK_MAX_DURATION（从"规则 1"内嵌中拆出独立标注）
    - 规则 7：P块级对白总量聚合（保持不变）

### 新建
- `tools/validators/run_validators.py`：统一校验入口，一条命令运行全部 4 个校验器
  - 执行顺序：machine-layer-timing → seedance-template → dialogue → beat-density
  - 输出结构化汇总报告（per-ep × per-validator 矩阵）
  - 支持 `all` / `--strict` / `--verbose` / `--json` 参数
  - 退出码：0=全部 critical=0，1=存在 critical（可接 CI）
  - 用法：`python tools/validators/run_validators.py ep01 ep02` 或 `... all`

- `tools/validators/p_block_budget_planner.py`：P块对白预算计划器，写 P块前先算预算
  - 速率常量与 machine-layer-timing-checker.py 严格同步（三者共享同一常量体系）
  - 输出：最小推荐时长、舒适时长、拆分方案建议
  - 三种模式：
    - 交互模式（无参数）：逐步输入规划参数
    - 快速模式：`--bubble 80 --sync 15 --duration 15`
    - 批量扫描：`--scan ep01` / `--scan all`（扫描已存在P块的预算状态）

### 同步（Workflow）
- `axis-stage-gate.md` 分镜编写阶段：
  - 入口新增 `p_block_budget_planner.py --scan <集数>` 预检步骤（编写前强制预算核查）
  - 出口新增 `run_validators.py <集数>` 统一校验步骤（替代分散的单独调用）

---

## [ep10-fix] — 2026-04-28 · EP10 P块重构 + 机读层时序修复

### EP10 重构内容
- `outputs/ep10/02-seedance-prompts.md`：P块由 5 拆分为 11 子块（P01 不变，其余全部拆分）
  - P02(15s) → P02-a(7s) + P02-b(10s)：叶锋摊牌 / 玄女天才论+语塞
  - P03(12s) → P03-a(6s) + P03-b(8s)：群聊安慰+定理 / 追问验证+来日方长
  - P04(15s) → P04-a(7s) + P04-b1(5s) + P04-b2(5s)：私聊前置+揭露 / 备份星图 / 叶锋承诺
  - P05(12s) → P05-a(7s) + P05-b(7s)：我加入+介绍对象 / 师爷狂喜+羞红+黑屏

### 修复（机读层时序 critical × 3）
- **P02-b**：`10-12秒` 超出声明 10s → 合并入 `8-10秒`（语塞+沉默+硬切P03 合段）
- **P03-a**：`4-8秒` 超出声明 6s → 改为 `4-6秒`
- **P05-b**：`7-8秒` 超出声明 7s → 合并入 `6-7秒`（投影关闭+师爷不舍+黑屏 合段）

### 校验结果（修复后）
- machine-layer-timing：✅ PASS（critical=0 / warning=17）
- seedance-template：✅ PASS（critical=0 / warning=1·MACHINE_TIMESEGMENT_MISMATCH P03-b 4s vs 8s·可接受）
- dialogue：✅ PASS（clean）
- beat-density：⚠️ WARN（critical=0 / warning=7·全为密度偏紧·无需修复）

---

## [v6.4] — 2026-04-28 · 台词零删减铁律全局强制

### 新增
- `CLAUDE.md`：[总体规则] 新增「台词零删减铁律」— 严禁以任何理由（含时长不足/语速过快/密度超标）精简、缩短、概括、删减、合并或改写台词；台词超出时间段容量时只允许扩展时长或拆分时间段；AI 审核/建议阶段不得建议精简台词
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：新增 §五B「台词零删减铁律」速查章节

### 变更
- `skills/seedance-storyboard-skill/SKILL.md`：「台词完整保留铁律」升级为「台词零删减 — 优先级最高」，新增三条强制规则（禁止以时长不足为由精简、所有对白类型均受保护、AI不得建议精简）+ FAIL条件升级为全集回退重审

---

## [ep05-complete] — 2026-04-26 · EP05 分镜阶段完成

### EP05 完成项
- `outputs/ep05/01-director-analysis.md`：EP05 导演分析完成（第5章·数学是天才的试金石·5P·66s）
- `outputs/ep05/02-seedance-prompts.md`：Seedance 2.0 提示词 P01-P05 完成；校验全部通过
  - seedance-template-validator：✅ PASS（critical=0 / warning=6）
  - beat-density-checker：✅ PASS（critical=0 / warning=11）
  - dialogue-checker：✅ PASS（critical=0 / warning=0）
- `outputs/ep05/03-text-storyboard.md`：文字分镜稿生成完成（22镜·66s·P01-P05）
- `assets/prompts/character-prompts.md`：新增 老导师 [ep05] 文字锚点描述
- `assets/prompts/scene-prompts.md`：新增 张院长办公室·论文地砖变体 [ep05][scene]
- `.stage-gate.json`：ep05 所有阶段标记 completed
- `.agent-state.json`：ep05 status=completed / currentStage=分镜编写-completed

### 修复（本集验证过程中）
- 补全文档级三表（素材对应表/角色锚定表/单条提示词预算表）
- P03-P05 T0 视听语言扩展为 9 维度
- 移除机读层所有 mm 数值（改为描述式焦段）
- P03/P04/P05 机读层补充画面位置词
- P03/P04/P05 机读层 suffix 统一含"禁止出现任何字幕"
- P02/P03/P05 机读层叙述性代词替换为具名角色
- P03 beat-density：381% → 147%（删去快速对白引号·压缩估算台词）
- P04 beat-density：105%（已为警告级·通过）
- P05 beat-density：375% → 188%（大幅压缩对白行数+字数）

---

## [v6.3] — 2026-04-26 · 补充文字分镜稿生成步骤（修复历史遗留死规则）

### 新增
- `agents/storyboard-artist.md` 步骤 5.5：Seedance 文件写入后立即生成 `03-text-storyboard.md`，包含完整格式规范（`#### 镜 NNN` + 六字段表 + 画面/台词/音效）及 `text-storyboard-validator.py` 校验阻断

### 变更
- `agents/storyboard-artist.md`：输出文件清单新增 `03-text-storyboard.md`；阻断规则新增缺失该文件时拒绝进入导演审核
- `skills/seedance-storyboard-skill/SKILL.md`：第零步输出文件清单新增 `03-text-storyboard.md`；阻断规则同步；第三步半新增文字分镜稿存在性检查 + 深度校验命令

### 修复
- 根因：v4.0 只建了 `text-storyboard-validator.py` 和 gate 门禁，但未在 agent/skill 中添加生成步骤，导致 8 集全部缺失。本次补全执行层
- `tools/management/next-step-prompter.py`：分镜阶段 outputs 列表补充 `03-text-storyboard.md`（脚本层漏同步）

---

## [v6.2] — 2026-04-26 · 角色提示词模板移除 MJ V7 系列

### 变更
- `skills/art-design-skill/templates/character-prompt-template.md`：移除 B版本（MJ V7/Niji 7）展示位，基础形象和变体均只保留 Nano Banana Pro（中英文两段分离）
- `skills/art-design-skill/templates/character-enhanced-template.md`：标题由"A/B 双版本输出模板"改为"Nano Banana Pro 输出模板"；B版本区块改为 ~~删除线~~ + ⏸️ 暂停
- `skills/art-design-skill/references/execution-rules.md`：第零步规范由"A/B 双版本强制"改为"仅 Nano Banana Pro"；B版本 MJ V7 三条规范区块标注暂停；输出结构示例同步更新
- `skills/art-design-skill/SKILL.md`：执行流程概要第零步表格和文档描述同步更新

---

## [v6.1] — 2026-04-26 · Kling 平台暂停 + CHANGELOG 强制同步铁律

### 变更
- `skills/seedance-storyboard-skill/SKILL.md`：第零步平台铁律由"三平台强制全出"改为"仅 Seedance 2.0，Kling 2.6/3.0 暂停启用"；第三步半校验同步更新
- `agents/storyboard-artist.md`：frontmatter 描述、角色能力、输出规范、协作模式步骤4.5/5全面同步 Kling 暂停规则
- `CLAUDE.md`：`~prompt` 默认行为由"三平台全出"改为"仅 Seedance 2.0"；Kling 审核条目标注 ⏸️ 暂停启用；新增规则 10）CHANGELOG 强制同步铁律
- `agents/director.md`：阶段三前置检查由三平台校验改为仅 Seedance 2.0；Kling 2.6/3.0 审核节标注暂停
- `skills/seedance-storyboard-skill/storyboard-generation-cheatsheet.md`：一、三平台铁律 → 仅 Seedance 2.0
- `AXIS-全流程指令合集.md`：产出清单去掉 Kling 文件；铁律第7条更新；新增第11条 CHANGELOG 强制同步
- `tools/management/next-step-prompter.py`：outputs 列表 Kling 条目注释掉；invoke_hint 同步

### 新增
- `CLAUDE.md` 规则 10）：CHANGELOG 强制同步铁律 — 任何系统规则文件变更必须同步更新 `CHANGELOG.md`，否则视同操作未完成

---

## [v6.0] — 2026-04-25 · Seedance v2 增强版 + 模板校验器

### 新增
- **Seedance v2 增强版提示词**：ep02、ep04 等集数新增 `02-seedance-prompts-v2.md`，采用 v6.0 增强模板标准
  - 新增「翻译审计」前验格式（先从人读层提取应翻译清单，再核查机读层）
  - 新增「情感熵三子项」独立逐行核查（①环境熵增 ②时间弹性→特写拆解 ③通感模拟）
  - 新增「钉子4行」叙事价值总结模块
  - 新增「台词审计」模块（导演阐述 vs 机读层 100% 原文匹配校验）
- **Seedance 模板校验工具**：`tools/validators/seedance-template-validator.py`
  - 覆盖文件级（素材表/角色锚定表/预算表）+ P块级（16 个子模块）全量校验
  - 支持 Protocol A-F 合规检测（零代词/六维饱满/视觉法医/防融图/声音三层/台词100%）
  - 支持 `--strict` 模式、`--json` 输出、单文件或整集批量校验
- **ch02 浮叠模式**：虚拟聊天群从 ch01「独立空间」升级为浮叠层（半透明 70-80% 叠加现实画面），首次在 ep04 P10 亮相

### 变更
- `seedance-prompts-template-enhanced.md` 升级至 v6.0，对白层新增三种口型标注（清晰口型/嘴唇微动/非清晰口型）与 `无口型台词` 标记规范
- 密度校验表新增「含对白」「对白最低时长」列，强化对白密度管控

---

## [v5.0] — 2026-04-24 · 14 集全量产出 + 项目收尾

### 新增
- **ep05 ~ ep14 全量产出**：完成 14 集三平台提示词（Seedance 2.0 + Kling 2.6 + Kling 3.0）
- **项目收尾阶段**（阶段十）：批量审核 + 最终项目报告 + 交付包生成
- **交付包**：`万界通告，哨兵阵亡-交付包.zip`

### 变更
- `.stage-gate.json` 项目收尾阶段标记为 `completed`

---

## [v4.0] — 2026-04-23 · 工业级校验矩阵 + 集间交接

### 新增
- **阶段十一：集间交接**：每集分镜完成后强制执行进度报告、上下文快照、增量基线、项目仪表盘
- **自动化校验工具矩阵**（`tools/validators/`，共 23 个校验器）：
  - `beat-density-checker.py` — Seedance 节拍密度校验（≥200% critical 强制拆分）
  - `plot-fidelity-checker.py` — 剧情忠实度校验（加权覆盖率 100%）
  - `novel-dialogue-fidelity-checker.py` — 台词忠实度校验
  - `cross-episode-consistency-checker.py` — 跨集一致性巡检
  - `cross-file-consistency-checker.py` — 跨文件一致性校验
  - `semantic-consistency-validator.py` — 语义一致性校验
  - `stage-output-validator.py` — 产物结构校验
  - `novel-fidelity-checker.py` — 原文忠实度校验
  - `dialogue-checker.py` — 台词校验
  - `quality-prechecker-runner.py` — 质量预检
  - `watch-and-validate.py` — 文件监控校验
  - `text-storyboard-validator.py` — 分镜格式校验
  - `visual-style-validator.py` — 视觉风格规范校验
  - `t0-validator.py` / `run-t0-all.py` — T0 白皮书标准校验
  - `compliance-keyword-checker.py` — 合规关键词检查
  - `content-feasibility-checker.py` — 内容可行性检查
  - `cross-chapter-hook-checker.py` — 跨章钩子检查
  - `brainworm-validator.py` — 脑洞生成校验
  - `outline-validator.py` — 集纲校验
  - `novel-analysis-validator.py` — 小说分析校验
  - `prop-extraction-validator.py` — 道具提取校验
  - `p-block-diff-checker.py` — P块差异检查
- **生成类工具**（`tools/generators/`，共 8 个）：
  - `context-snapshot-generator.py` — 上下文快照生成
  - `cross-platform-converter.py` — 跨平台转换（Seedance → Kling 2.6 + Kling 3.0）
  - `duration-predictor.py` — 时长精算
  - `emotion-quantization.py` — 情绪量化与 BGM 同步
  - `material-tagger.py` — 素材标注
  - `trailer-generator.py` — 30 秒预告片生成
  - `style-preset-query.py` — 风格预设查询
  - `inject_v2_modules.py` — v2 模块注入
- **管理类工具**（`tools/management/`，共 11 个）：
  - `stage-step-updater.py` — 子步骤状态实时同步
  - `episode-progress-reporter.py` — 集数进度报告
  - `next-step-prompter.py` — 下一步操作指引
  - `incremental-update.py` — 增量更新基线
  - `project-dashboard.py` — 项目仪表盘（支持 Mermaid）
  - `batch_review.py` — 批量审核
  - `build-delivery-package.py` — 交付包构建
  - `reset-stage.py` / `reset_project.py` — 阶段/项目重置
  - `run-stage-checks.py` — 阶段校验批量执行
  - `stage-gate-sync.py` — 门禁状态同步
- **门禁规则**（`.stage-gate.json` gateRules，共 19 条铁律）：
  - Rule 18：Skill 全文强制读取铁律（≤1000行一次性读取；>1000行分段读取）
  - Rule 19：41 个含 script 步骤禁止遗漏、禁止跳过
- **对白密度计算参数表**：口型对白 0.40s/字、气泡/画外音 0.20s/字、系统消息 0.15s/字

### 变更
- `AXIS-workflow-stages.md` 新增子规则 9-A/9-B/9-C（Skill 全文强制读取 + 输出后合规审计 + 审计报告模板）
- `.stage-gate.json` 分镜编写阶段扩展至 24 个子步骤

---

## [v3.0] — 2026-04-23 · 多 Agent 协作 + 全流程四条路径

### 新增
- **四条工作路径**：
  - 路径一（完整融合）：小说分析 → 集纲 → 剧本 → 导演 → 服化道 → 分镜
  - 路径二（脑洞融合）：脑洞生成 → 集纲 → 剧本 → 导演 → 服化道 → 分镜
  - 路径三（下游融合）：集纲 → 剧本 → 导演 → 服化道 → 分镜
  - 路径四（原有流程）：导演 → 服化道 → 分镜
- **8 个 Agent 定义**（`agents/`）：
  - `director.md` — 导演（全程审核）
  - `art-designer.md` — 服化道设计师
  - `storyboard-artist.md` — 分镜师
  - `short-drama-architect.md` — 集纲架构师
  - `short-drama-scriptwriter.md` — 剧本转化专家
  - `prop-system-extractor.md` — 道具与金手指提取
  - `novel-analyzer.md` — 小说分析融合入口
  - `brainworm-generator.md` — 脑洞生成
- **Resumable Subagents 机制**：`.agent-state.json` 按集隔离 agentId，集内 resume 跨集不混用
- **融合模块**（`融合模块/chuanban-chaishu-skills/`）：完整集成 chuanban 小说理解层（拆分/概括/人物/事件线/ABC爽点）
- **脑洞生成能力**：brainworm-generator-skill + 审核 Skill
- **全流程指令合集**：`AXIS-全流程指令合集.md`（`~full` / `~outline` / `~script` / `~director` / `~style` / `~art` / `~storyboard` / `~check` / `~status`）

### 变更
- `CLAUDE.md` 从单 Agent 配置升级为制片人多 Agent 调度架构
- 强执行逻辑升级：阶段门禁 / 双阈值放行 / 回改收敛 / Delta-first / 跨集巡检 / Skill 显式加载

---

## [v2.0] — 2026-04-22 · 39 技能包 + 三平台产出

### 新增
- **39 个技能包**（`skills/`）：
  - 核心生成技能：director-skill / art-design-skill / seedance-storyboard-skill / short-drama-architect-skill / short-drama-scriptwriter-skill
  - 增强技能：sovereign-duration-predictor-skill（T0+++ 时长预测）/ film-lighting-technique-skill / character-interaction-design-skill / genre-adaptive-skill / aesthetic-vision-skill
  - 审核技能：seedance-prompt-review / kling-prompt-review / kling-3.0-prompt-review / art-direction-review / script-analysis-review / compliance-review 等 14 个 review skill
  - 可选技能：visual-language-logic / plot-psyche-double-helix / script-structure-diagnosis / story-card-bridge
- **三平台同时产出**：Seedance 2.0 + Kling 2.6 + Kling 3.0，缺一不可
- **Kling 3.0 支持**：智能分镜 / 主体参考 / 15 秒超长生成
- **T0+++ 时长预测与主权保全**：NAF 叙事资产忠诚度 / XEE 无限扩张系数 / VDC 价值密度压缩 / 工业算力扩张引擎
- **知识库**（`resources/`）：
  - `unified-audiovisual-language-library.md` — 好莱坞 T0 级 29 条视听语言标准
  - `advanced-seedance-guide.md` — 高级 Seedance 2.0 指南
  - 微表情库、多语言适配、性能优化等
- **工具参考库**（`tools/references/`）：
  - `camera-movement-master.md` — 完整运镜工具箱
  - `cross-platform-converter.md` — 跨平台转换器
  - `spatial-continuity-checker.md` — 全局空间锚点连续性检查
  - `ai-generation-predictor.md` — AI 视频生成效果预测
  - `quality-prechecker.md` — 实时质量预检系统
  - `style-preset-library.md` — 7 种风格预设模板
  - `emotion-quantization-system.md` — 情感量化与 BGM 同步系统
  - `multimodal-dynamic-fusion.md` — 多模态动态融合系统
- **两步审核工作流**：业务审核（阶段专属 Skill 评分表）+ 合规审核（compliance-review-skill）
- **v2.1 三栏式角色布局**：纯白背景 / 三栏 20-60-20 / 面部特写 / 多视图 / HSB 色板 / 配饰微距 / 黄金比例
- **五问法声明**（Q1-Q5）：每个设计必须填写视觉冲击点 / AI 表达词汇 / 错误规避 / 变体 / HSB 锁定

---

## [v1.0] — 2026-04-22 · 项目初始化

### 新增
- **项目创建**：AXIS 漫剧内测教学全量备份上传至 GitHub
- **原著导入**：`novel/` 目录 170 章原著文件（《万界通告，哨兵阵亡》）
- **小说分析产出**：`assets/novel-analysis/万界通告，哨兵阵亡/`（拆分 / 概括 / 人物关系 / 事件线 / ABC 爽点）
- **集纲产出**：`assets/outline/` ch01-ch14 共 28 个集纲文件
- **ep01 全阶段完整产出**：导演分析 + 服化道设计 + 三平台分镜
- **10 阶段工作流定义**：`AXIS-workflow-stages.md`
  - 阶段一：小说分析（融合模块）
  - 阶段二：脑洞生成
  - 阶段三：道具与金手指提取
  - 阶段四：集纲生成
  - 阶段五：剧本生成
  - 阶段六：导演分析
  - 阶段七：视觉风格选择
  - 阶段八：服化道设计
  - 阶段九：分镜编写
  - 阶段十：全剧收尾
- **核心配置文件**：
  - `CLAUDE.md` — 制片人系统提示词
  - `.agent-state.json` — Agent 状态记录
  - `.stage-gate.json` — 阶段门禁配置
- **Windsurf 工作流**：
  - `/axis-stage-gate` — 阶段门禁检查清单
  - `/delete-files` — 删除文件前完整检查流程
- **3-10-60 情绪循环算法**：前 3 秒钩子 → 前 10 秒叙事 → 1 分钟爽点 → 卡点钩子
- **绝对视觉化剥离原则**：禁止心理描写，强制外化为肢体动作/微表情/物理交互
- **axis-web 前端原型**：`axis-web/`（React + Vite）+ 后端 `axis-web/backend/`（Python FastAPI）

---

## 系统架构概览

```
AXIS 漫剧全流程生产管线
├── 输入层
│   ├── novel/                 原著小说（170章）
│   └── brainworm/             创意脑洞
├── 分析层
│   ├── 融合模块/              chuanban 小说理解
│   └── assets/novel-analysis/ 分析产出
├── 创作层
│   ├── assets/outline/        集纲（14章×2集）
│   ├── assets/prompts/        角色/场景/道具提示词
│   └── assets/               character-bible + visual-style-guide
├── 产出层
│   └── outputs/ep01~ep14/     三平台提示词×14集
├── 技能层
│   └── skills/               39个技能包（生成+审核）
├── 工具层
│   ├── tools/validators/      23个校验器
│   ├── tools/generators/      8个生成器
│   └── tools/management/      11个管理工具
├── 质量层
│   ├── .stage-gate.json       19条铁律门禁
│   └── 两步审核工作流          业务审核+合规审核
└── 交付层
    └── 交付包.zip             全量打包
```

---

*本文件由 AXIS 系统自动维护，记录系统架构、功能模块和工具链的演进历程。*
