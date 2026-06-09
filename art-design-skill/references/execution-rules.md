# 执行规则详细说明

> 📖 本文件从 art-design-skill/SKILL.md 提取，包含 Nano Banana Pro 输出规范、内容合规前置约束、前置鐵律、
> 读取上游产物、T0级提示词构建规则、变体铁律、角色公式、布光/画质/材质规范、T0标准校验、校验阻断机制。

---

## 三、执行流程（融合版）

### 第零步：Nano Banana Pro 输出规范（当前启用）

� **当前所有服化道提示词只输出 Nano Banana Pro 一个版本（中文段 + 英文段分离）**

#### Nano Banana Pro（中文段 + 英文段分离）

| 项目 | 说明 |
|------|------|
| **用途** | Nano Banana Pro、即梦等支持中英文混合输入的工具 |
| **格式** | 🔴 **中文一整段 + 英文一整段，两段分离输出** |
| **特点** | - **【中文描述段】**：纯中文一整段，不夹杂英文术语，自然语言叙事<br>- **【英文描述段】**：纯英文一整段，不换行，包含所有技术关键词和渲染参数<br>- 两段内容对应但语言完全分离<br>- 中文段侧重叙事描述，英文段侧重技术关键词 |
| **示例** | ```
**【中文描述段】**
爱死机超写实CGI角色设定参考图。纯白背景隔离无任何投影。20-30岁亚洲男性，极度瘦骨嶙峋……（纯中文一整段）

**【英文描述段】**
Love Death and Robots hyper-realistic CGI character model sheet, strictly isolated on a pure white background...（纯英文一整段）
``` |

#### 输出结构要求

每个角色/场景/道具按以下结构输出（🔴 中英分离＝通用提示词格式；**角色**的两段正文须描述「电影级角色提案板」六区块、非泛化单图，详见本 SKILL.md §三 角色唯一标准 / cinematic-character-pitch-board-skill）：

```
### Nano Banana Pro（中英文）

**【中文描述段】**

[纯中文一整段，不夹杂英文术语，自然语言叙事描述，包含角色外观、材质、视图、表情集等所有信息]

**【英文描述段】**

[纯英文一整段，不换行，包含所有技术关键词、渲染参数、防崩坏指令，直接可复制使用]
```

---

### 🔴 内容合规前置约束（执行前必须完成，违反=直接判定不合格）

> **视觉风格 ≠ 生成内容的上限。风格只决定美学调性，不授权生成平台违禁内容。**

**执行前必须完成以下3步：**

**Step 1：读取风格指南风险等级**
- 读取 `assets/visual-style-guide.md`，确认所选方案的风险等级
- 🔴 高风险方案（如爱死机/暗黑/赛博朋克）→ 强制执行 Step 2/Step 3
- 🟡 中风险方案 → 建议执行 Step 2

**Step 2：内容合规过滤规则（高风险方案强制）**

以下内容**禁止出现在任何提示词中**，无论风格指南如何要求：

| 禁止内容 | 合规替换方向 |
|----------|-------------|
| 血液/脓血/流血/血迹直接描写 | 用"液体""渗出物""暗色液体"替代 |
| 具体伤口特写（刮伤/溃烂/自残创伤） | 用"皮肤异常""损伤痕迹"模糊化 |
| 肉渣/肉块/肉体残留物 | 用"有机残留物""暗色残留"替代 |
| 未成年外观（<18岁）+ 施暴/性化组合 | 外观年龄必须≥20岁，或删除施暴表情 |
| 裙摆/服装"大腿根部裸露/完全裸露"的直接描写 | 改为"及大腿中部"或"合体短裙" |
| 露背"到腰际"的精确描写 | 改为"低背设计"不指定裸露高度 |
| 被掐脖子/被扇耳光的表情描述 | 改为"惊恐""防御姿态""受惊" |
| 器官脱落/下颌脱臼的直接描述 | 改为"损坏状态""面部扭曲" |

**Step 3：未成年人专项检查**
- 角色外观年龄 < 18岁时：**必须删除**所有施暴、性化、惊恐受创的相关表情/姿态描写
- 角色外观年龄 < 18岁 + 存在性感服装描写 → **必须**将年龄改为 ≥ 20岁或更换服装设计

---

### 🔴 前置铁律（每次执行前必须默读，违反直接判定不合格）

> **角色基础形象 + 道具 = 必须纯白背景**
> - 角色基础形象：`strictly isolated on a pure white background, solid white backdrop, no cast shadows`
> - 道具：`strictly isolated on a pure white background, solid white backdrop, no cast shadows, macro lens, 100mm`
> - **禁止**在基础形象/道具提示词中出现任何场景背景、场景光源（如 cinematic lighting、candlelight、moonlight、palace hall setting）
> - 变体（场景特定服装/状态）允许有场景背景
> - 输出后必须逐条自检：基础形象是否包含 `pure white background`？不包含 → 立即修复

### 第一步：读取上游产物
- 读取导演分析产出中的人物清单和场景清单
- 读取 gemini-image-prompt-guide.md 了解提示词写法规范
- ⚠️ 必须读取 AI绘画终极提示词工程白皮书.md 了解T0级工业商用提示词规则
- 读取 examples/ 下的示例文件,了解高质量提示词的写法标准
- 🔴 **时间锚定（强制）**：从剧本提取每个场景的「日/夜」标注，从导演分析提取对应色温/光源设定，交叉比对后确定场景唯一权威时间。场景提示词的光线描述、色温、Negative prompt 必须与上游时间标注一致。详见 `scene-concept-design-skill/SKILL.md` §时间锚定规则。
- 🔴 **场景唯一模板**：所有场景统一使用 v3.0（5层叙事架构·场景叙事模板），v1.0/v2.0 已废弃。每条场景必须在 `### 场景叙事模板 v3.0` 下方第一行置顶写入 `美术风格前缀：`，并从 `assets/visual-style-guide.md` 选用场景专用中文美术风格前缀。
- 🔴 **场景前缀禁写人物风格**：`美术风格前缀` 只允许用中文写环境/空间/材质/光影/界面风格，禁止写人物、角色、人像、皮肤、发丝、服装配饰、人体比例等人物风格描述；除 HEX 色值外不得夹英文。
- 🔴 **必须读取输出模板**（强制结构,防止自由文本输出）：
  - skills/cinematic-character-pitch-board-skill/templates/pitch-board-output-template.md (角色·电影级提案板唯一标准；旧三栏式 character-prompt-template.md 已删除)
  - templates/prop-prompt-template.md (道具提示词强制结构)
- 读取已有的 assets/prompts/character-prompts.md 和 assets/prompts/scene-prompts.md（如存在）
- 根据人物清单中的"素材状态"列，只为标注为"新增"或"变体"的**角色/道具**项设计提示词
- 角色/道具"复用"项跳过，不需要设计
- 🔴 **场景资产输出规则**：场景清单中的场景写入 `assets/prompts/scene-prompts.md` 时，统一使用 `### 场景叙事模板 v3.0` 标准格式；新增/变体场景必须生成，复用场景可引用已有条目但不得改写为全维度交付稿
- 🔴 **场景全维度交付边界**：`scene-concept-design-skill` 只在制片人/导演明确要求“单场景深度展开/全维度交付稿”时调用，产物必须单独写入 `outputs/<集数>/XX-scene-concept-[场景名].md`，不得写入 `assets/prompts/scene-prompts.md`
- 使用高精度模式进行设计

#### 2.1 核心记忆点提炼（工业级）
基于角色人设，提炼1个核心记忆点，并在提示词中贯穿始终。

#### 2.2 形状语言确定（工业级）
根据角色情绪，确定核心形状语言（圆/方/三角/S曲线/锯齿线）。

#### 2.3 T0级提示词构建（AXIS标准·2026-05-31 电影级角色提案板）

> 🔴 **2026-05-31 角色标准统一**：角色资产唯一标准 = **电影级角色提案板**（横版16:9 + 中性灰背景 + 六区块），权威构建规范见 `skills/cinematic-character-pitch-board-skill/SKILL.md` 与模板 `pitch-board-output-template.md`。下方为提案板要素与变体铁律（三栏式已彻底废除）。

**🔴 提案板 8 项强制要素**（写入时不得删减）：① 横版大画幅 16:9 ② 中性灰提案板背景 #BEC1C4~#C7CACD（非纯白/纯黑/无场景） ③ 六区块（顶部细条 + 区块A主视觉立像 + B全身5视图转面 + C头部6视图研究 + D情绪肖像 + E服装拆解 + F色板） ④ 区块A 85mm 立像 + 金色身高刻度尺 ⑤ HSB 色板 ≥4 色含 #HEX（区块F） ⑥ 区块E 4-6 张 100mm 微距 ⑦ 同一基底人物（A/B/C/D 严格一致） ⑧ 核心渲染参数 PBR/AO/SSS/UE5/Octane ≥2 项。

**🔴 变体生成铁律**（提案板格式）：
- 基础形象 + 变体均为电影级角色提案板（横版16:9 + 中性灰背景 + 六区块）
- 同一角色不同情绪/服装/状态的变体：仅复制提案板并修改 区块D 情绪肖像 / 区块E 服装拆解 / 顶部细条情绪关键词；**区块A 主视觉、区块B 转面、区块C 头部研究必须保持同一基底人物**
- 禁止跳过变体生成：每个主要角色至少 1 个变体
- 变体命名格式：`### 变体A：[服装/状态描述]`
- 🔴 每个变体提示词必须与基础形象一样完整（六区块 / HSB / 身高刻度尺 / 渲染 / 防崩坏齐全），禁止简写

**🔴 变体一致性铁律**：
- 变体是同一角色在不同环境/状态下的形象，必须一眼看出是同一人
- 一致性锚定（中文段）："与基础形象为同一人，保持五官、体型、发型、肤色完全一致，仅[具体变化]发生变化"；（英文段）`same character as base design, maintaining identical facial features, body proportions, hairstyle, and skin tone, only [specific changes] differ`
- 不变：五官轮廓 / 体型比例 / 发型基础结构 / 肤色基调 / 核心记忆点
- 可变：服装装备 / 状态变化 / 表情情绪 / 妆容配饰
- ❌ 禁止：变体五官或体型与基础明显不同、看起来像另一个人、背景出现场景元素（提案板背景恒为中性灰）

#### 2.4 角色公式（按顺序·v2.0）

```
[横版16:9提案板] + [中性灰提案板背景#BEC1C4~#C7CACD] + [顶部细条标题] + [区块A 85mm主视觉立像+金色身高刻度尺] + [区块B 全身5视图转面] + [区块C 头部6视图研究] + [区块D 情绪肖像] + [区块E 服装配件4-6张100mm微距] + [区块F HSB色板≥4色含HEX] + [🔴 身材引擎词汇（女性角色强制）] + [高调影棚柔光5500-6000K + PBR/AO/SSS/UE5/Octane] + [T0级画质后缀]
```

🔴 **身材引擎强制融入规则（女性角色）**：
- **必须读取** `resources/body-figure-engine.md`（📌 唯一定义位置）
- 英文描述段中必须融入 §一（身材代码）中至少4项词汇（绝对比例/长腿/腰臀/体态各1项）
- 必须从 §二（视觉锚点）中选取1~2项作为角色永久绑定特征，写入核心记忆点
- 根据角色叙事定位从 §三（气场原型）中选择主气场，写入气质描述
- 禁止仅用 `supermodel` / `beautiful` 等泛化词替代身材引擎的具体术语

#### 2.5 高级影棚布光
- Clean bright studio lighting with no background shadows
- 可选：Rim lighting, softbox, Rembrandt lighting

#### 2.6 T0级画质后缀（必加）
```
masterpiece, best quality, ultra-detailed, 8k resolution, sharp focus
Unreal Engine 5 render, physically based rendering (PBR), Octane Render
Please avoid any text, watermarks, blurred edges, distorted anatomy, or low-quality plastic textures
```

#### 2.7 材质与工艺细节（高精度模式）
- 提取3-4种关键材质，列出独立的"材质与工艺细节"块
- 每种材质需标注：材质名称、材质特性（如光泽度、纹理、手感）

### 第三步：场景与道具设计（已迁移至专项技能）

> 🔴 **场景全维度设计**已迁移至 `skills/scene-concept-design-skill/SKILL.md`
> 🔴 **道具全维度设计**已迁移至 `skills/prop-concept-design-skill/SKILL.md`
> 本技能（art-design-skill）专注于**角色概念设计**。

### 第四步：输出

按照以下标准格式输出：
- 🔴 **角色提示词** → 追加到 `assets/prompts/character-prompts.md`（本技能负责）
- **场景提示词** → 由 `scene-concept-design-skill` 写入 `assets/prompts/scene-prompts.md`（已迁移）
- **道具提示词** → 由 `prop-concept-design-skill` 写入 `assets/prompts/props-prompts.md`（已迁移）
首集时创建文件，后续集数追加新增/变体条目到文件末尾。

**🔴 变体输出强制要求**：
1. **基础形象**：每个角色/道具必须先生成基础形象（纯白背景隔离）
2. **场景变体**：根据导演分析和剧本需求，为每个主要角色生成场景变体
   - 主角/重要配角：至少2-4个变体（对应不同服装/状态）
   - 次要角色：至少1个变体（如有剧情需求）
3. **变体必须包含完整T0要素**：表情集、服饰拆分、多视图、渲染参数、微观细节、防崩坏指令
4. **禁止只生成基础形象**：如果只输出基础形象而跳过变体，直接判定为不合格

### 第四步半：白皮书T0标准校验（强制）

⚠️ 输出后必须进行白皮书校验，确保符合T0级工业商用标准！

使用 tools/validators/t0-validator.py 进行校验：

**角色提示词校验（7项强制要求）**：
- ✅ 纯白背景隔离：strictly isolated on a pure white background
- ✅ 表情集：facial expression sheet featuring 4 close-up headshots
- ✅ 服饰拆分：separated clothing breakdown with RGB color palette
- ✅ 多视图：full-body front/side/back view + close-up headshot
- ✅ 核心渲染参数：PBR/AO/Unreal Engine 5/Octane Render（至少2项）
- ✅ 微观细节：皮肤纹理/毛孔/眼球反光/发丝物理（至少2项）
- 🔴 **场景变体**：主要角色必须有场景变体，变体也必须包含完整T0要素（1-6项）

**场景/道具校验**：已迁移至对应专项技能
- 场景校验 → `skills/scene-concept-design-skill/SKILL.md` §步骤7
- 道具校验 → `skills/prop-concept-design-skill/SKILL.md` §步骤6

**额外检测**：
- ✅ 极致动漫风格：8大工作室风格至少指定1个
- ✅ 防崩坏指令：必须包含防崩坏指令

校验命令：
```bash
python tools/validators/t0-validator.py --batch --dir assets/prompts/
```

### 🔴 校验阻断机制（强制执行，违反=任务失败）

**执行要求**：
1. 运行校验命令后，**必须**截图或复制完整校验输出
2. 在输出文件末尾附上"📋 T0校验报告"章节，包含：
   - 校验命令
   - 校验结果截图/文本
   - 通过项数量 / 总项数量
   - 失败项列表（如有）
   - 🔴 **变体统计**：每个角色的变体数量（基础形象+变体总数）
3. **阻断规则**：
   - ❌ 未运行校验 → 判定为不合格，拒绝进入导演审核
   - ❌ 未贴校验结果 → 判定为不合格，拒绝进入导演审核
   - ❌ 校验未全部通过 → 必须修复 → 重新校验 → 直到全部通过
   - 🔴 **未生成变体 → 判定为不合格**：主要角色只有基础形象而无场景变体，直接拒绝
   - 🔴 **变体缺少T0要素 → 判定为不合格**：变体必须包含完整T0要素（表情集、服饰拆分、多视图等）

**校验报告模板**：
```markdown
## 📋 T0校验报告

**校验时间**：[时间戳]
**校验命令**：`python tools/validators/t0-validator.py --batch --dir assets/prompts/`

**校验结果**：
- ✅ 通过项：[X] / [总数]
- ❌ 失败项：[Y] / [总数]

**失败项详情**（如有）：
1. [角色名/道具名] - 缺失：[缺失的强制要素]
2. ...

**白底专项检查**：
- ✅ 所有基础形象包含 `pure white background`：是/否
- ✅ 所有道具包含 `pure white background` + `macro lens`：是/否
- ❌ 黑名单关键词检测：[列出违规项]
```

校验未通过 → 修改提示词 → 重新校验 → 校验通过后才能进入导演审核

