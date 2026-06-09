---
name: cinematic-character-pitch-board-review-skill
description: 电影级角色提案板审核技能。审核 cinematic-character-pitch-board-skill 的产出，确保提案板的 6 区块版面完整、跨视图（A/B/C/D）基底严格一致、中性灰背景与电影感达标（提案板为 2026-05-31 起唯一角色标准，取代三栏式）。
---

# 电影级角色提案板审核技能

[技能说明]
    审核 cinematic-character-pitch-board-skill 的产出（角色提案板提示词文档）。
    确保提案板真正达到"对外提案 / 导演拍板"级别，而非仅确认格式完整。
    审核立场：你的任务是找出问题，而非确认通过。

    本审核技能必须参考：
    1. skills/cinematic-character-pitch-board-skill/SKILL.md：了解提案板规范与输出格式
    2. skills/art-design-skill/SKILL.md：确保与上游角色概念设计一致
    3. skills/aesthetic-vision-skill/SKILL.md：五问法 / 第7维度审美评分
    4. skills/compliance-review-skill/SKILL.md：合规检查
    5. tools/validators/pitch-board-validator.py：提案板 T0 校验
    6. tools/references/sensitive-word-dictionary.md：敏感词检测

[五问法口径 + 去重 · 2026-05-30 补强]
    - 🔴 第7维度"视觉美学意图"审核口径：五问法 Q1-Q5 须在提案板的【人读/元数据标注区】出现，且**不得混入**中英文生图描述段；若生图段正文夹带 Q1-Q5 文字 → FAIL（口径以 aesthetic-vision-skill 为唯一权威）。
    - 第7维度评分细则与 costume-prop-character-design-review-skill 重复的部分，统一引用 aesthetic-vision-skill 附录，不再各写一套。
    - PASS 引用 skills/templates/quality-threshold-standard.md（审核类三维各 ≥95）。

    调用方 Agent：
    - agents/director.md：导演 Agent 执行审核
    - agents/art-designer.md：服化道 Agent 自审

[文件结构]
    cinematic-character-pitch-board-review-skill/
    ├── SKILL.md                                    # 本文件（审核技能说明）
    └── templates/
        └── review-report-template.md               # 审核报告模板

[审核对象]
    cinematic-character-pitch-board-skill 产出的角色提案板提示词文档
    （如 不敢麻烦别人_动画改编/character-prompts-pitch-board.md）

[审核流程]

    第一步：建立整体理解
        - 读取上游 art-design-skill 的角色概念设计
        - 读取同角色既有提案板/存量资产（assets/prompts/character-prompts.md，若存在）作为基底对照
        - 读取待审核的提案板文档
        - 明确审核立场：找出问题，而非确认通过

    第二步：版面区块完整性审核
        | 检查项 | 标准 | 评分 |
        |--------|------|------|
        | 顶部细条 | 角色名+年龄+身高+风格方向+性格关键词齐全 | 0-10 |
        | A 主视觉立像 | 85mm 全身立像 + 金色身高刻度尺 | 0-10 |
        | B 全身五视图 | 正/3·4正侧/纯侧/3·4背/背齐全 | 0-10 |
        | C 头部六视图 | 正/3·4正侧/纯侧/低头/抬头/动态扭头齐全 | 0-10 |
        | D 情绪肖像 | 50mm 中近景，中列·上 | 0-10 |
        | E 服装拆解 | 4-6 张 100mm 微距 ±3° 旋转 | 0-10 |
        | F 色板备注 | HSB 色板 ≥4 色含 HEX | 0-10 |

    第三步：跨视图一致性审核
        | 检查项 | 标准 | 方法 |
        |--------|------|------|
        | 脸型/眼型一致 | A/B/C/D 同一人 | 逐视图对比 |
        | 发型轮廓一致 | A/B/C/D 同一发型 | 逐视图对比 |
        | 服装款式一致 | A/B 同一套服装 | 逐视图对比 |
        | 配饰/道具位置一致 | A/B 配饰位置不漂移 | 逐视图对比 |
        | 跨视图基底一致 | A/B/C/D 同一基底人物（如有存量资产一并对照） | 跨视图/跨文件对照核心字段 |

    第四步：背景与电影感审核
        | 检查项 | 标准 |
        |--------|------|
        | 中性灰背景 | #BEC1C4~#C7CACD，非纯白/纯黑 |
        | 无场景元素 | 无卧室/办公室/医院/街景等场景 |
        | 统一光源 | 5500-6000K 主光右上 45° + 左侧冷补光，光比 2:1~3:1 |
        | 不对称构图 | 非机械九宫格，含 ±2-5% 错位 + 动态扭头偏出网格 |
        | 演员气质 | 呼吸感/重心/肌肉张力，非摆拍模特 |
        | 画面洁净 | 无 flare/散景/漂浮粒子/噪点/水印 |

    第五步：材质真实性审核
        | 检查项 | 标准 |
        |--------|------|
        | 皮肤 PBR+SSS | 次表面散射 + 鼻梁下唇柔光 + 关节偷暖粉红 |
        | 布料三重细节 | fabric fibers / weave / wrinkle |
        | 金属/皮革 | 金属真实反射不过亮 / 皮革哑光颗粒纹 |
        | 无塑料蜡像感 | 无冷白假人脸、无偶像化糖果浓妆 |

    第六步：提示词质量审核
        | 检查项 | 标准 |
        |--------|------|
        | T0校验 | 通过 tools/validators/pitch-board-validator.py |
        | 中英文双段 | 中文段（Nano Banana Pro）+ 英文段（Midjourney/Flux）齐全 |
        | 6区块覆盖 | 中英文段都完整覆盖 6 区块 |
        | 画面洁净负面约束 | 标准短句版存在 |

    第七步：视觉意图达成度审核（审美维度·最高权重15分）

        > ⚠️ 本步是第2-6步的超越：前几步审核"有没有"，本步审核"好不好"。

        Step 1: 检查五问法落位是否合规（口径见 aesthetic-vision-skill §二·单一权威）
        - 五问法（📐Q1-Q5）须出现在提案板文档的【人读层 / 元数据标注区】（如「📐 视觉美学意图声明」章节）→ 出现 = 允许且推荐 ✅
        - 🔴 五问法不得混入喂给生图模型的中文段（Nano Banana Pro）/ 英文段（Midjourney/Flux）正文 → 若混入则该项 FAIL（生图正文须为纯画面描述）
        - 五问是否全部回答（Q1-Q5）？
        - Q1情绪词是具体情绪词（如「克制×隐忍×疲惫温柔」）还是通用词（如「酷×帅×强」）？

        Step 2: 评估Q1情绪词在产出中的可感知度
        - 不看五问声明，直接看 D 情绪肖像描述，第一句话能写出什么感受？
        - 把自诉的第一句话与Q1情绪词对比：是否一致？

        Step 3: 逆向溯源设计决策
        | 审核项 | 审核问题 | 判断方法 |
        |--------|--------|--------|
        | Q3形状语言 | 声明的主导形状在实际造型中是否可见？ | 形态对照审核 |
        | Q4配色情绪 | 每个颜色的"情绪贡献"是否在 HSB 色板与画面中生效？ | 对照各色区域情绪 |
        | Q5世界观位置 | 与同项目其他角色的视觉阶级差异是否清晰？ | 对照同项目其他角色 |

[评分表格式]

    请使用以下格式输出审核结果（完整版见 templates/review-report-template.md）：

    ```
    ## 审核结果

    ### 三维评分规则（必须执行）

    版面完整性评分（0-100分）：
    □ 6 区块是否齐全（顶部细条/A/B/C/D/E/F）？（0-33分）
    □ 身高刻度尺 + 五视图 + 头部六视图是否齐全？（0-33分）
    □ HSB 色板（≥4色含HEX）+ 材质微距（4-6件）是否齐全？（0-34分）

    一致性评分（0-100分）：
    □ 五官/眼型/发型在 A/B/C/D 是否一致？（0-33分）
    □ 服装/配饰/道具在 A/B 是否一致？（0-33分）
    □ 跨视图（A/B/C/D）基底是否一致？（如有存量资产一并对照）（0-34分）

    电影感与美术气质评分（0-100分）：
    □ 中性灰背景规格 + 统一光源是否达标？（0-33分）
    □ 不对称美术构图 + 演员气质是否达标？（0-33分）
    □ 五问法 Q1 情绪词在产出中是否可感知（第7维度）？（0-34分）

    通过标准（参考 skills/templates/quality-threshold-standard.md，审核类 C级）：
    - 版面完整性 ≥ 95分
    - 一致性 ≥ 95分
    - 电影感与美术气质 ≥ 95分
    - 任一维度低于95分 → 业务审核 FAIL

    ### 业务审核评分表

    | # | 审核维度 | 分值 | 得分 | 问题说明 |
    |---|---------|------|------|---------|
    | 1 | 版面区块完整性 | 17分 | | |
    | 2 | 跨视图一致性 | 18分 | | |
    | 3 | 背景与电影感 | 15分 | | |
    | 4 | 材质真实性 | 13分 | | |
    | 5 | 提示词质量（中英双段+T0） | 12分 | | |
    | 6 | 合规检查 | 10分 | | |
    | **7** | **视觉意图达成度** | **15分** | | **最高权重审美维度** |
    | **总分** | | **100分** | **__分** | |

    ### 第7维度「视觉意图达成度」评分标准（🔴 单一权威：引用 aesthetic-vision-skill §五 附录）

    > 本维度的 4 档评分标准（A 15分 / B 12分 / C 8分 / D 0分）、3 条快速 FAIL 通道、逆向溯源三问，一律以
    > `skills/aesthetic-vision-skill/SKILL.md` §五「视觉意图达成度审核细则（第7维度·15分）」为唯一裁决，本处不再复制。
    > 本维度与 `costume-prop-character-design-review-skill` 第7维度共用同一 aesthetic-vision §五 附录，避免双份维护漂移。
    > 提案板专属落位口径（五问法须在「📐 视觉美学意图声明」人读 / 元数据区、禁止混入中英文生图描述段）见上方第七步 Step 1。

    ### 问题清单
    | # | 维度 | 严重程度 | 问题描述 | 修改建议 |
    |---|------|---------|---------|---------|
    ```

[PASS/FAIL 标准]

    PASS 条件（必须全部满足）：
    - 业务审核总分 ≥ 80分
    - 无单项低于 5 分
    - 三维评分各项 ≥ 95分
    - 五问法（阶段0）已完成且 Q1 为具体情绪词
    - pitch-board-validator.py 校验通过
    - 合规审核通过

    FAIL 条件（任一满足）：
    - 缺失任一版面区块（顶部细条/A/B/C/D/E/F）
    - 五官/比例/发型/服装在 A/B/C/D 出现漂移
    - 与同角色工业资产基底严重不一致
    - 背景为纯白/纯黑或出现场景元素
    - HSB 色板缺失或无 HEX
    - 五问法未完成 OR Q1 为通用词
    - pitch-board-validator.py 未通过
    - 合规审核未通过

[合规检查项]
    - [ ] 无政治敏感内容
    - [ ] 无版权侵权风险（无明星/IP形象引用）
    - [ ] 无色情/暴力尺度问题
    - [ ] 角色设计无歧视性刻板印象
    - [ ] 英文提示词无违禁词汇
    - [ ] 视觉设计无宗教敏感符号

[跨技能集成声明]

    调用方 Agent：
    - agents/director.md：导演 Agent 执行审核
    - agents/art-designer.md：服化道 Agent 自审

    上游技能：
    - skills/cinematic-character-pitch-board-skill/SKILL.md：审核其产出

    下游技能：
    - skills/costume-prop-character-design-skill/SKILL.md：审核通过的提案板供工业资产生成对齐

    必须引用：
    - skills/cinematic-character-pitch-board-skill/SKILL.md：提案板规范
    - skills/aesthetic-vision-skill/SKILL.md：五问法 / 第7维度审美评分
    - skills/compliance-review-skill/SKILL.md：合规标准
    - tools/validators/pitch-board-validator.py：提案板 T0 校验
    - tools/references/sensitive-word-dictionary.md：敏感词库

[诊断指南]

    | 问题 | 检查 | 修复 |
    |------|------|------|
    | 区块缺失 | 逐区块清点 | 补齐缺失区块 |
    | 视图不一致 | 叠加对比各视图 | 以 A 区主视觉为基准统一修正 |
    | 跨视图基底对不上 | 对照各区块/存量资产 | 锁定核心字段统一 |
    | 背景不达标 | 检查背景规格 | 强制中性灰 + 删场景元素 |
    | 构图机械 | 检查是否九宫格平铺 | 加错位 + 动态扭头偏出网格 |
    | 五问法走过场 | 检查 Q1 是否通用词 | 改为具体情绪词，重新逆向溯源 |
    | T0未通过 | 运行 pitch-board-validator.py | 按校验报告逐项修复 |

[术语表]

    | 术语 | 英文 | 定义 |
    |------|------|------|
    | 提案板 | Pitch Board | 给导演/投资方看的对外角色提案视觉物 |
    | 基底人物 | Base Character | 跨资产共享的同一角色定义 |
    | 第7维度 | 7th Dimension | 视觉意图达成度，审美最高权重维度 |
    | 五问法 | Five Questions | 阶段0视觉美学意图声明 Q1-Q5 |
    | SSS | Subsurface Scattering | 皮肤次表面散射 |
    | 演员气质 | Actor Presence | 真实演员被捕捉的瞬间感，非摆拍模特 |

[版本信息]
    - 版本: 1.2
    - 创建日期: 2026-05-29
    - 更新日期: 2026-05-31
    - 说明：新建审核技能，为 cinematic-character-pitch-board-skill 提供配对审核，
      含 6 区块版面完整性、跨视图一致性、与工业资产基底对照、第7维度审美评分。
    - 更新内容（1.1）：第七步 Step 1 五问法审核改为「落位合规」口径——五问法须在人读 / 元数据区出现、不得混入中英文生图描述段（口径见 aesthetic-vision-skill §二·单一权威）
    - 更新内容（1.2）：第7维度 4 档评分标准与 FAIL 通道由「本地复制」改为「引用 aesthetic-vision-skill §五 附录」单一权威——与 costume-prop-character-design-review-skill 第7维度共用同一附录，消除双份维护漂移
