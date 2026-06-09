# 5大核心设计流程详细方法论

> 📖 本文件从 art-design-skill/SKILL.md 提取，包含阶段1-5的完整设计方法论。
> 主文件仅保留流程概览图与链接。

---

### 阶段1：信息收集

**输入源识别**：
- 导演分析产出（人物清单、场景清单）
- 剧本/故事板中的角色描述
- 参考图像/情绪板（Mood Board）
- 技术约束文档（引擎要求、面数限制）

**核心信息提取清单**：

| 维度 | 提取内容 | 关键问题 |
|------|----------|----------|
| **基础属性** | 姓名、性别、年龄、种族、职业 | 角色是谁？什么身份？ |
| **视觉特征** | 体型、身高、面部特征、发型 | 长什么样？有什么标志性特征？ |
| **服装系统** | 主服装、配饰、鞋靴、道具 | 穿什么？带什么？ |
| **性格气质** | 性格关键词、情绪状态、气场 | 给人什么感觉？ |
| **世界观** | 时代背景、科技水平、文化环境 | 生活在什么世界？ |
| **功能需求** | 动画需求、绑定要求、面数限制 | 技术约束是什么？ |

#### Nano-Banana 专属信息结构化

针对Nano-Banana模型的结构化语言偏好，将收集的信息组织为以下YAML格式：

```yaml
角色档案:
  identity:
    name: "角色名称"
    age: "年龄段"
    occupation: "职业/身份"
    personality_tags: ["关键词1", "关键词2", "关键词3"]
  
  visual_profile:
    body_type: "体型描述"
    height_ratio: "头身比"
    distinctive_features: ["特征1", "特征2"]
  
  costume_system:
    primary_garment: "主服装详细描述"
    accessories: ["配饰1", "配饰2", "配饰3"]
    footwear: "鞋靴描述"
    key_props: ["道具1", "道具2"]
  
  material_palette:
    - material: "材质名称"
      description: "物理特性描述"
      reference: "现实参照物"
    - material: "材质名称"
      description: "物理特性描述"
      reference: "现实参照物"
  
  art_direction:
    target_style: "目标艺术风格"
    reference_works: ["参考作品1", "参考作品2"]
    mood_keywords: ["氛围词1", "氛围词2"]
```

### 阶段2：分析思考

#### 2.1 核心记忆点提炼系统（工业级核心）

基于「单点极致」原则，从以下维度提炼**1个核心记忆点**：

```
核心记忆点决策树:
│
├─► 形状记忆点
│   ├─ 独特剪影轮廓 (如：巨大肩甲、非对称结构)
│   ├─ 夸张比例特征 (如：九头身、Q版头身比)
│   └─ 标志性动态线 (如：S型曲线、力量感斜线)
│
├─► 元素记忆点
│   ├─ 符号化道具 (如：特定武器、标志性配饰)
│   ├─ 独特材质组合 (如：金属+有机组织的冲突)
│   └─ 文化符号融合 (如：赛博朋克+传统纹样)
│
└─► 生物记忆点
    ├─ 动物特征融合 (如：狼耳+机械义肢)
    ├─ 幻想生物结构 (如：龙鳞皮肤、羽翼)
    └─ 植物/矿物特征 (如：水晶生长、藤蔓缠绕)
```

**记忆点检验标准**：
- ☐ 3米外可通过剪影识别
- ☐ 能用一句话描述清楚
- ☐ 与角色人设强相关
- ☐ 非通用化设计（非"穿红衣服的女战士"）

#### 2.2 形状语言设计系统

基于角色人设与情绪，确定核心形状语言：

| 形状类型 | 情绪与应用 | 在提示词中的体现 |
|----------|------------|-----------------|
| 圆形 | 友好、柔软、可爱、安全、亲和 | 圆润线条、柔和轮廓 |
| 方形 | 稳定、可靠、力量、坚固、正统 | 硬朗线条、块状结构 |
| 三角形 | 危险、锐利、速度、侵略、神秘 | 尖锐元素、锋利轮廓 |
| S形曲线 | 优雅、柔美、流动、女性化、神秘 | 波浪线条、流动姿态 |
| 锯齿线 | 狂暴、混乱、痛苦、不稳定 | 破碎元素、动态噪点 |

**剪影设计原则**：
1. **3秒识别原则**：3米外、3秒内可通过剪影识别角色
2. **负空间利用**：剪影内部的负空间形状要有节奏感
3. **对比与节奏**：大/中/小形状的层次对比
4. **独特轮廓**：至少1个独特的轮廓特征（非标准人体）

**动态线设计**：
```
动态线类型:
├─ 稳定动态线 (水平/垂直) → 稳重、权威、静止
├─ 流动动态线 (S曲线) → 优雅、柔美、魔法感
├─ 力量动态线 (斜线/对角线) → 运动、攻击、紧张
└─ 螺旋动态线 → 混乱、疯狂、能量爆发
```

**直曲线造型法则**：
- **直线区域**：骨骼突出处、肌肉紧绷处、机械结构
- **曲线区域**：肌肉饱满处、脂肪堆积处、有机组织
- **转换逻辑**：直线与曲线的转换要符合解剖/机械结构

#### 2.3 艺术风格定义矩阵

**风格定位决策树**：

```
目标艺术风格
    │
    ├─► 写实风格 (Photorealistic)
    │   ├─ 影视级写实: "Photorealistic cinematic render, IMAX 70mm format"
    │   ├─ 游戏AAA写实: "Hyper-realistic AAA game production render, Unreal Engine 5"
    │   └─ 微距写实: "100mm macro photography, f/1.2 aperture"
    │
    ├─► 风格化 (Stylized)
    │   ├─ 手绘风格: "Overwatch hand-painted texture style, stylized rendering"
    │   ├─ 卡通风格: "Stylized Fortnite rendering, vibrant colors"
    │   └─ 动漫风格: "Extreme anime style, [指定工作室] aesthetic"
    │
    ├─► 动画工作室风格 (Anime Studio Style) ★ 新增
    │   ├─ 必须引用: tools/references/anime-style-presets.md（24种动画风格定义）
    │   ├─ 必须引用: tools/references/anime-style-prompt-templates.md（NanoBanana Pro 200%还原度提示词模板）
    │   ├─ 24种可选风格ID:
    │   │   ANIME_SHONEN（少年热血）/ ANIME_MAKOTO（新海诚）/ ANIME_GHIBLI（吉卜力）
    │   │   ANIME_TRIGGER（TRIGGER爆能）/ ANIME_UFOTABLE（ufotable数码）/ ANIME_WIT（立体机动）
    │   │   ANIME_MAPPA（暴力美学）/ ANIME_IG（赛博科技）/ ANIME_JOJO（JOJO立）
    │   │   ANIME_LDR（爱死机超写实）/ ANIME_KYOANI（京都精致）/ ANIME_SHAFT（实验风）
    │   │   ANIME_SEINEN（青年写实）/ ANIME_MECHA（机甲硬核）/ ANIME_PA（P.A.原创）
    │   │   ANIME_A1（轻改风）/ ANIME_CLOVER（现代时尚）/ ANIME_SHOUJO（少女梦幻）
    │   │   ANIME_CEL（经典赛璐璐）
    │   │   ── 3D动画风格 ──
    │   │   3D_PIXAR（皮克斯3D）/ 3D_DREAMWORKS（梦工厂）/ 3D_SPIDERVERSE（蜘蛛侠漫画）
    │   │   3D_ARCANE（奥术手绘3D）/ 3D_ILLUMINATION（照明卡通）
    │   └─ 使用方法: 
    │       1. 从anime-style-presets.md选择对应风格
    │       2. 从anime-style-prompt-templates.md复制对应模板
    │       3. 在模板基础上添加具体角色/道具/场景描述
    │       4. 保留Negative prompt确保风格纯度
    │
    └─► 概念艺术 (Concept Art)
        ├─ 科幻风格: "Cyberpunk graphic novel style, neon-lit"
        ├─ 奇幻风格: "Epic fantasy concept art, dramatic lighting"
        └─ 工业设计: "Hard surface technical illustration, exploded view"
```

**动画风格选择流程**（新增）：

```
Step 1: 确认项目是否采用动画风格
  └─ 是 → 进入Step 2
  └─ 否 → 使用上述其他风格分类

Step 2: 根据题材选择对应工作室风格
  ├─ 热血战斗 → ANIME_SHONEN / ANIME_TRIGGER
  ├─ 青春恋爱 → ANIME_MAKOTO / ANIME_KYOANI
  ├─ 奇幻冒险 → ANIME_GHIBLI / ANIME_SHONEN
  ├─ 机器人 → ANIME_MECHA / ANIME_TRIGGER
  ├─ 暴力悬疑 → ANIME_MAPPA / ANIME_SEINEN
  ├─ 赛博朋克 → ANIME_IG / ANIME_MAPPA
  ├─ 魔法少女 → ANIME_SHOUJO / ANIME_SHAFT
  └─ 超写实成人 → ANIME_LDR

Step 3: 打开anime-style-prompt-templates.md
  └─ 找到对应风格章节（如"二、ANIME_MAKOTO"）

Step 4: 根据需求选择模板类型
  ├─ 角色提示词模板 → 复制"角色提示词模板"
  ├─ 道具提示词模板 → 复制"道具提示词模板"
  └─ 场景提示词模板 → 复制"场景提示词模板"

Step 5: 在模板基础上添加具体描述
  ├─ 保留基础模板的所有技术参数
  ├─ 添加具体角色/道具/场景的详细描述
  ├─ 保留Negative prompt（确保风格纯度）
  └─ 确保100%还原该工作室的视觉特征
```

#### 2.4 技术规范分析

**建模约束清单**：

| 约束类型 | 检查项 | 标准值 |
|----------|--------|--------|
| **拓扑要求** | 面数限制、四边面比例、极点位置 | 根据项目定义 |
| **绑定需求** | 骨骼数量、变形要求、表情 blendshape | 根据项目定义 |
| **材质层数** | PBR贴图数量、特殊材质效果 | 基础色/法线/粗糙度/金属度/AO |
| **UV规范** | UV利用率、接缝位置、Texel密度 | ≥75%利用率 |
| **输出格式** | 文件格式、命名规范、版本控制 | FBX/OBJ + 贴图包 |

**光影逻辑分析**：

```
主光源分析:
  ├─ 方向: [顶光/侧光/逆光/底光]
  ├─ 色温: [暖光(2700K)/中性(5600K)/冷光(9000K)]
  ├─ 光质: [硬光/柔光]
  └─ 强度: [主光/补光/轮廓光比例]

氛围光分析:
  ├─ 环境光: [室内/室外/封闭空间]
  ├─ 反射光: [地面反射/墙面反射]
  └─ 特效光: [体积光/辉光/镜头光晕]
```

#### 2.5 关键词提炼系统

**T0级核心质感词库调用**：

从以下维度提取关键词填充到提示词公式：

| 维度 | 核心关键词类别 | 示例 |
|------|----------------|------|
| **渲染参数** | PBR/AO/SSS/Ray Tracing | `physically based rendering`, `ambient occlusion` |
| **光学镜头** | 焦段/光圈/格式 | `85mm lens`, `f/1.2 aperture`, `IMAX 70mm` |
| **微观细节** | 皮肤/毛发/眼睛 | `intricate skin texture`, `visible pores`, `peach fuzz` |
| **排版视图** | 多视图/拆分图 | `full body turnaround`, `facial expression sheet` |
| **材质特性** | 物理属性 | `subsurface scattering`, `metallic roughness` |

#### 2.6 生物元素设计系统

**动物元素融合方法论**：

```
生物设计四步法:

Step 1: 物种定位
  ├─ 基于角色人设匹配动物物种
  ├─ 提取物种的「核心辨识度特征」
  ├─ 提取物种的「固有文化词条」（如：狼=忠诚/野性）
  └─ 提取物种的「标志性生物功能」

Step 2: 特性选取
  ├─ 选取1个核心物种特性做强化（单点极致）
  ├─ 可选：反差设计（选取物种的非刻板印象特性）
  └─ 避免：多特性混乱堆砌

Step 3: 特征融合
  ├─ 保留核心辨识度特征（不可简化过度）
  ├─ 结构拟人化/功能化适配
  ├─ 造型语言统一（与角色整体形状语言一致）
  └─ 避免：生硬的元素拼接

Step 4: 功能与行为设计
  ├─ 基于生物功能设计角色功能性结构
  ├─ 基于标志性行为完成行为嫁接
  └─ 强化角色的叙事与情绪表达
```

**拟人化程度分级**：

| 级别 | 动物特征 | 人类特征 | 适用场景 |
|------|----------|----------|----------|
| **Level 1** | 完全动物形态 | 穿着/道具 | 纯动物角色、宠物 |
| **Level 2** | 动物头+人类身体 | 直立行走、服装 | 兽人、福瑞角色 |
| **Level 3** | 动物元素点缀 | 基本人类形态 | 半兽人、元素法师 |
| **Level 4** | 仅保留象征性特征 | 完全人类形态 | 人类角色、轻微变异 |

**生物特征提取表**：

| 动物 | 核心辨识度特征 | 文化词条 | 生物功能 | 可融合元素 |
|------|----------------|----------|----------|------------|
| 狼 | 尖耳、尾巴、群居 | 忠诚、野性、团队 | 夜视、嗅觉 | 耳饰、披风、团队标记 |
| 鹰 | 锐眼、羽翼、钩喙 | 自由、远见、高贵 | 飞行、俯冲 | 眼罩、肩甲、披风纹样 |
| 蛇 | 鳞片、竖瞳、柔韧 | 智慧、危险、诱惑 | 毒液、蜕皮 | 鳞甲、纹身、武器 |
| 龙 | 角、翼、尾、鳞 | 力量、神秘、古老 | 飞行、吐息 | 角饰、背甲、武器 |
| 猫 | 竖瞳、肉垫、尾巴 | 神秘、独立、敏捷 | 夜视、平衡 | 眼型、手套、尾饰 |
| 鹿 | 角、大眼、纤细 | 优雅、灵性、自然 | 敏捷、警觉 | 头饰、眼型、身形 |

### 阶段3：素材准备

**关键材质识别（至少3-4种）**：

| 材质 | 类型 | 物理特性 | 视觉描述 |
|------|------|----------|----------|
| 主服装材质 | 布料/皮革 | roughness: 0.3-0.8 | 详细的视觉描述 |
| 配饰材质 | 金属/宝石 | metallic: 0.0-1.0 | 光泽、纹理描述 |
| 皮肤材质 | 有机 | subsurface scattering | 毛孔、绒毛细节 |
| 毛发材质 | 有机 | anisotropic | 发丝飘动效果 |

### 阶段4：头脑风暴

**多方案生成策略**：

| 方案 | 特征 | 风格倾向 | 风险 |
|------|------|----------|------|
| **方案A - 保守方向** | 基于需求的最直接诠释 | 写实/传统/经典 | 低 |
| **方案B - 平衡方向** | 保守基础上增加设计亮点 | 半写实/现代融合 | 中 |
| **方案C - 突破方向** | 大胆创新、强烈风格化 | 风格化/实验性 | 高 |

**方向锁定决策矩阵**：

```
评估维度          权重    方案A    方案B    方案C
─────────────────────────────────────────────────
符合需求          30%     ▓▓▓▓▓    ▓▓▓▓░    ▓▓▓░░
视觉冲击力        20%     ▓▓▓░░    ▓▓▓▓░    ▓▓▓▓▓
技术可行性        20%     ▓▓▓▓▓    ▓▓▓▓░    ▓▓░░░
制作成本          15%     ▓▓▓▓▓    ▓▓▓▓░    ▓▓▓░░
创新性            15%     ▓▓░░░    ▓▓▓▓░    ▓▓▓▓▓
─────────────────────────────────────────────────
综合得分                  78       85       72

决策: 选择综合得分最高的方案
```

**逐层深化检查表（L1-L7）**：

| 层级 | 深化内容 | 检查标准 | 设计铁律关联 |
|------|----------|----------|--------------|
| **L1 - 轮廓** | 剪影识别度 | 3米外可识别角色 | 辨识度铁律 |
| **L2 - 比例** | 头身比/肢体比例 | 符合风格定位 | 可信度铁律 |
| **L3 - 形状** | 核心形状语言/直曲线分布 | 统一且服务情绪 | 情绪优先铁律 |
| **L4 - 服装** | 款式/结构/层次 | 符合世界观设定 | 可信度铁律 |
| **L5 - 材质** | 质感/纹理/光泽 | 可指导PBR制作 | 技术实现铁律 |
| **L6 - 细节** | 磨损/装饰/功能件/叙事元素 | 有故事性、服务人设 | 情绪优先铁律 |
| **L7 - 表情** | 神态/气质/情绪/表演性 | 符合角色性格 | 情绪优先铁律 |

### 阶段5：迭代实现

AI生成步骤：

```
Step 1: 生成锚点图
  └─ 输入: 基础角色描述 + 纯白背景
  └─ 输出: 正面标准照（用于后续一致性控制）
  └─ 检查: 比例正确、风格符合

Step 2: 生成多视图
  └─ 输入: 锚点图参考 + 完整提示词
  └─ 输出: 四视图设定表
  └─ 检查: 各视图比例一致、特征统一

Step 3: 生成材质球
  └─ 输入: 材质特写提示词
  └─ 输出: 4个材质细节图
  └─ 检查: 质感真实、PBR参数可执行

Step 4: 生成表情集
  └─ 输入: 表情范围描述
  └─ 输出: 表情变化表
  └─ 检查: 表情自然、符合角色性格

Step 5: 合成定妆单
  └─ 输入: 所有生成元素
  └─ 输出: 完整Model Sheet
  └─ 检查: 排版规范、信息完整
```

**标准提示词模板（可直接使用）**：

```markdown
A professional [目标艺术风格] character model sheet, presented as a single integrated technical design document on a clean, pure white studio background.

The central and upper sections feature four consistent views of the same character: [详尽角色视觉描述，包含身份、体型、服装、配饰]. These views include front, back, three-quarter front, and three-quarter back, with consistent proportions and anatomy.

The lower section displays [数量] detailed material close-ups: [材质1描述 with PBR parameters], [材质2描述 with PBR parameters], [材质3描述 with PBR parameters], [材质4描述 with PBR parameters].

Additional technical specifications include: facial expression sheet showing [表情范围], separated clothing breakdown diagram, exact RGB color palette diagram with hexadecimal codes.

Rendered with physically based rendering (PBR), ambient occlusion (AO), subsurface scattering (SSS) for skin, ray tracing global illumination, shot on 85mm lens with f/1.4 aperture for portrait detail, IMAX 70mm format quality, intricate skin texture with visible pores and peach fuzz, realistic eye reflection, detailed hair physics, 8k resolution, Unreal Engine 5, Octane Render, cinematic lighting.
```

**审核检查清单**：

| 检查项 | 标准 | 状态 |
|--------|------|------|
| 多视图一致性 | 各视图比例、特征完全一致 | ☐ |
| 材质标注清晰 | 每种材质有明确PBR参数 | ☐ |
| 纯白背景合规 | 背景干净、无杂色、易抠图 | ☐ |
| 技术约束明确 | 面数/绑定/UV要求已标注 | ☐ |
| 风格统一 | 符合项目整体美术方向 | ☐ |
| 与需求匹配 | 覆盖所有需求点 | ☐ |
| 可生产性 | 下游团队可直接使用 | ☐ |

**迭代优化策略**：

| 问题 | 可能原因 | 修复策略 |
|------|----------|----------|
| 多视图不一致 | 锚点图未固定 | 使用统一锚点图，添加`consistent character`关键词 |
| 材质塑料感 | 缺少PBR参数 | 增加`physically based rendering`, `ambient occlusion` |
| 面部不自然 | 微观细节不足 | 添加`intricate skin texture`, `visible pores`, `peach fuzz` |
| 背景不干净 | 纯白描述不够强 | 前置`clean pure white background`, `isolated on white` |
| 风格杂乱 | 艺术风格不明确 | 指定具体参考`in the style of [参考作品]` |
| 光影平淡 | 缺少摄影术语 | 添加镜头参数`85mm lens`, `f/1.4 aperture` |

