# 角色增强模块与女性体型美学规范

> 📖 本文件从 art-design-skill/SKILL.md 提取，包含表情/情绪变化、动作/姿态、3D建模专用、光照变化模块，
> 以及女性角色体型美学规范（T0超模级/T1战术级/T2精灵级）与面部反大众化规范。

---

## 四、角色增强模块（融合版）

### 一、表情/情绪变化模块

#### 基础情绪（4种）
| 情绪 | 视觉描述 | 适用场景 |
|------|----------|----------|
| 平静 | 眉头舒展，眼神温和，嘴角自然放松 | 日常对话、思考、休息 |
| 惊讶 | 眉毛上扬，眼睛圆睁，嘴巴微张 | 震惊、意外、发现秘密 |
| 愤怒 | 眉头紧锁，眼神凌厉，嘴角下沉，肌肉紧绷 | 冲突、战斗、仇恨 |
| 悲伤 | 眉头上挑，眼眶含泪，嘴角下垂 | 失去、离别、悲伤事件 |

#### 进阶情绪（4种）
| 情绪 | 视觉描述 | 适用场景 |
|------|----------|----------|
| 喜悦 | 眉眼弯起，笑容展开，嘴角上扬 | 成功、团聚、开心时刻 |
| 恐惧 | 眼睛大睁，眉毛上扬，嘴唇颤抖 | 危险、害怕、恐怖事件 |
| 厌恶 | 眉头皱起，眼神嫌弃，嘴角撇向一侧 | 反感、讨厌、轻视 |
| 轻蔑 | 单侧眉毛微挑，眼神斜视，淡淡冷笑 | 藐视、不屑、高傲 |

### 二、动作/姿态模块

| 类别 | 内容 | 提示词体现 |
|------|------|----------|
| 站立 | 自然站立/丁字步/双手交叉/单手叉腰 | 体态描述 |
| 行走 | 行走正面/侧面/背面步伐 | 步伐动态 |
| 奔跑 | 奔跑正面/侧面/背面姿态 | 速度感 |
| 战斗 | 持械攻击/徒手格斗/防御姿态 | 力量感 |

### 三、3D建模专用模块（工业级增强）

#### 拓扑参考图
- 正面布线图：眼睛周围环形布线、鼻子三角结构
- 背面布线图：后脑勺布线、后颈线条
- 侧面布线图：眉弓-鼻梁-嘴唇-下巴连贯线条
- 全身布线图：脊椎走向、肩关节、手指

#### 材质球特写（3-4种）
每种材质需标注：
- PBR参数：Roughness/Metallic/Normal/Displacement
- 材质特性描述

#### 阴阳脸图（三视图）
- 正面受光：亮部60%/暗部40%
- 背面受光：亮部20%/暗部80%
- 侧面受光：亮部50%/暗部50%

#### 细节放大图
- 眼睛特写：虹膜纹理、眼神光、睫毛
- 嘴唇特写：唇纹、嘴角细节
- 手部特写：关节纹理、静脉、手纹
- 服装细节：刺绣、纽扣、缝线

### 四、光照变化模块

| 光源方向 | 效果 | 色温选择 |
|----------|------|----------|
| 正面光 | 平坦柔和 | 5500K中性 |
| 侧面光 | 立体感强 | 暖/冷可选 |
| 背光 | 剪影效果 | 轮廓发光 |
| 顶光 | 戏剧性强 | 阴影深重 |

---

## 四·五、女性角色体型美学规范（全局强制标准·反大众化）

> 🔴 **全局铁律**：AXIS所有女性角色**禁止使用"普通女性体型"**。每个女性角色必须按以下规范选择体型等级，并将**体型强制描述块**逐字写入提示词英文段和中文段。

### 体型选择矩阵（按人设选择）

| 体型等级 | 定义 | 适用人设 |
|---|---|---|
| **T0·超模级（默认首选）** | 时装周顶级超模·9.5头身·腿长占身高62%+·极致S曲线收腰 | 主角·女反派·高辨识度女性角色 |
| **T1·战术纤长级** | 女特种兵/武者·肌肉纤长劲健·腿型修长有力 | 战斗系·刺客·猎手·赏金猎人 |
| **T2·幻想精灵级** | 极度纤细骨感·腿如芦苇·飘逸无重力感 | 精灵·仙系·科幻仿生人·非人种族 |

### T0超模级体型强制描述块

> 以下两段**必须逐字嵌入**对应女性角色的提示词。不得删减，不得替换。

**英文强制段**（嵌入英文提示词角色描述部分）：
```
ultra-elongated runway supermodel physique, 9.5-head-height body ratio, legs occupying 62%+ of total body height, dramatic S-curve silhouette (narrow shoulders angling into impossibly cinched waist into wide flared hip arc), waist barely wider than head width, hip arc noticeably wider than shoulder width, perky natural bust (not exaggerated), defined lean elongated muscle throughout, gracefully tapered visible ankle bones, zero excess body fat, skin taut over lean frame — haute couture runway proportions, NOT average proportions, NOT generic female anime proportions
```

**中文强制段**（嵌入中文提示词角色描述部分）：
```
顶级时装周超模身材：9.5头身比，腿长占总身高62%以上；极度收腰（腰围仅略宽于头宽），胯宽明显大于肩宽——肩→腰→胯形成强烈压迫性S形流线；全身肌肉纤长零赘肉，皮肤紧贴骨骼，踝骨纤细突出。
```

### 女性角色面部反大众化（必须选择一种极端化方向）

| 方向 | 特征描述 | 提示词关键词 |
|---|---|---|
| **冷酷高骨感** | 颧骨突出·深眼窝·薄唇·刀削下颚线 | `sharp prominent cheekbones, deep-set eyes, razor jawline, thin lips` |
| **超长眼型** | 眼尾极长细挑·近乎水平延伸至太阳穴 | `extreme almond-eye elongation extending toward temples, nearly horizontal eye angle` |
| **异色/机械感** | 非人眼睛（LCD瞳·裂纹虹膜·纯色机械眼） | 参照角色人设选择对应词组 |
| **高冷模特神情** | 默认表情冷淡高傲（绝不主动亲和） | `default expression: cold haute-couture model blank stare, NOT approachable, NOT warm` |

### 女性角色反大众化红线

| 🔴 禁止行为 | ✅ 替换方向 |
|---|---|
| 头身比低于8.5 | 最低8.5头身，推荐9.5头身 |
| 腿型"正常比例" | 腿长60%+身高，提示词中**明确写入数值** |
| S曲线不明显 | 强制写明waist-to-hip差距（waist barely wider than head） |
| "普通亚洲美女"脸型 | 必须极端化**至少1个**面部特征 |
| 温柔亲和默认表情 | `cold condescending poise` / `haute couture blank stare` |
| 体态软弱无力 | 所有女角色保持`lean muscle definition` + `confident dominant posture` |

