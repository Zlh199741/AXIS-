---
name: east-asian-facial-parameters
description: art-design-skill 附属词库模块。提供东亚高定骨相、五官、体型的技术参数关键词，供角色五官描述的技术执行层使用。所有词库必须绑定叙事意图后方可调用，禁止作为"通用美颜滤镜"直接套用。
parent-skill: art-design-skill
version: v1.0
---

# 东亚高定骨相参数词库 (East Asian Haute Couture Facial Parameters)

> **调用前提**：本词库为技术执行层参考，必须在 `aesthetic-vision-skill` **五问法 Q2（视觉意象来源）** 完成填写后方可使用。  
> 每一个调用的参数，必须在五问法声明中有对应的叙事或情绪锚点。  
> **禁止用法**：直接堆砌词汇生成"好看的脸"。每个词汇必须有叙事理由。

---

## 一、骨相结构词库

### 1.1 整体面部骨相

| 关键词（英文） | 中文说明 | 叙事情绪适配方向 |
|---|---|---|
| `razor-sharp aggressive jawline` | 极具攻击性的锋利下颌线 | 危险感·权力感·不可接近 |
| `softly tapered oval jawline` | 柔和收窄的椭圆颌线 | 精巧·受害者感·脆弱对比 |
| `high prominent cheekbones casting micro-shadows` | 颧骨高耸投下微阴影 | 结构感·侵略性·非人精准 |
| `flat cheekbones wide mid-face` | 扁平颧骨·宽阔中庭 | 塑料感·量产廉价·劣化信号 |
| `sharply defined philtrum` | 极致清晰的人中线条 | 精密·算法感·非人完美 |
| `ethereal upper face dissolving into sharp lower face` | 上半脸仙气·下半脸锋利——两段式骨相冲撞 | 矛盾张力·内在危险感 |

### 1.2 额头与颅形

| 关键词（英文） | 中文说明 | 叙事情绪适配方向 |
|---|---|---|
| `smooth high forehead with invisible hairline` | 饱满光洁的高额头·发际线隐没 | 纯净·压迫·神性感 |
| `slightly rounded crown with soft temporal hollow` | 颅顶轻微弧圆·太阳穴轻微凹陷 | 精密高定·立体纵深 |

---

## 二、眼型与眉形词库

### 2.1 眼型（叙事分类）

| 眼型关键词（英文） | 中文说明 | 叙事情绪适配 | AXIS等级建议 |
|---|---|---|---|
| `almond-shaped eyes with sharp outer canthi` | 杏仁眼·外眼角极度上扬 | 锋芒·进攻性·统治感 | T0 SSR |
| `phoenix eyes (丹凤眼) with extended upper eyelid fold` | 丹凤眼·上眼睑延长 | 东方神秘·威严不可触及 | T0 SSR |
| `half-lidded heavy-lash monolid` | 半垂重睫单眼皮 | 冷漠·压抑感情·算法空洞 | T0 SSR |
| `wide double-eyelid with visible tear duct highlight` | 宽阔双眼皮·泪腺光点可见 | 脆弱感·表演性情绪·T1主角感 | T1 主角 |
| `asymmetric eyelid fold (one single, one double)` | 不对称眼皮·单双不一 | 廉价制造误差·劣化T2信号 | T2 N卡 |

### 2.2 瞳孔特征

| 关键词（英文） | 中文说明 | 叙事情绪适配 |
|---|---|---|
| `deep obsidian irises with zero light reflection` | 深黑色虹膜·反光归零 | 空洞·算法·非人 |
| `amber-colored deep irises with internal luminosity` | 琥珀色深邃虹膜·内发光 | 神秘·非人类暖意·矛盾吸引力 |
| `subtle heterochromia — one obsidian, one amber` | 极轻微异色瞳——一黑一琥珀 | 制造不对称恐怖谷·强记忆点 |
| `glassy irises with excessive specular highlight` | 玻璃质感虹膜·高光过度 | 廉价假眼感·T2劣化信号 |

### 2.3 眉形

| 关键词（英文） | 中文说明 | 叙事情绪适配 |
|---|---|---|
| `straight flat brows with sharp medial head` | 平直眉·内眉头锋利 | 冷静·算法·强制中性 |
| `slightly arched brows with defined peak` | 轻微拱形眉·峰点清晰 | 高定感·情绪可控 |
| `undefined soft brows` | 模糊柔和眉形 | 量产感·个性消失·T2信号 |

---

## 三、皮肤质感词库

### 3.1 T0 级皮肤（SSR）

```
warm ivory glass skin (#F5EDE5) — subsurface scattering warm amber glow (#FFD5A0),
micro-pore texture visible under raking light, 
luminous depth without plastic shine,
skin temperature: living warmth with uncanny valley precision
```

### 3.2 T1 级皮肤（主角 SR）

```
warm ivory skin (#F0EFE8) — soft SSS glow, 
natural micro-texture, slight imperfection at nose bridge,
approachable but clearly premium
```

### 3.3 T2 级皮肤（N卡劣化）

```
warm-toned plastic skin (#E8C4A0) — SSS absent,
flat diffuse reflection, visible pore texture coarse,
skin reads as "trying to be glass skin but failing" —
the formula was copied but the depth was not
```

---

## 四、面部记忆点词库（Visual Hooks）

> 每个角色**最多选1项**。记忆点必须在五问法 Q2「视觉意象来源」中说明其叙事贡献，禁止无理由叠加。

| 记忆点类型 | 关键词（英文） | 叙事贡献要求 |
|---|---|---|
| **泪痣** | `a striking tear-drop mole under the left eye` | 必须说明：这颗痣代表什么叙事符号（脆弱/危险/阶级标志） |
| **鼻尖痣** | `a tiny precise mole on the tip of the nose` | 适合廉价感/量产感叙事（T2信号） |
| **异色瞳** | `subtle heterochromia — warm amber left, deep obsidian right` | 必须绑定"内在矛盾"或"非人感"叙事 |
| **隐秘银发丝** | `jet-black extreme long hair with a single hidden silver strand` | 适合"被系统标记过的存在"叙事 |
| **颧骨微疤** | `a hairline scar across the left cheekbone, barely visible` | 适合废土/幸存者叙事；T0慎用（破坏完美度） |

---

## 五、叙事绑定使用规则

### ✅ 正确用法示范

```
五问法 Q2 声明：
→ 体型/姿态意象：顶级超模 × 仿生机械肢体
→ 记忆点叙事锚点：左眼泪痣 = "完美设计品上唯一的人工划痕，证明它被生产出来是为了被消耗的"

→ 调用词库：
   骨相：ethereal upper face + razor-sharp jawline（上仙下锋·叙事矛盾显性化）
   眼型：half-lidded heavy-lash monolid（情绪封锁·算法空洞）
   皮肤：T0 warm ivory glass skin（恐怖谷精准暖意）
   记忆点：tear-drop mole under left eye（消耗品标记）
```

### ❌ 禁止用法

- ❌ 直接复制多个记忆点叠加（泪痣 + 异色瞳 + 银发丝 = 特征过载，辨识度归零）
- ❌ 将气场原型（暗黑女王/废土神明）作为叙事锚点（通用大众审美，违反 `aesthetic-vision-skill` 禁止清单）
- ❌ 使用任何明星姓名作为骨相参照（`刘亦菲式`等表述禁止直接出现在AXIS输出中，骨相应通过具体几何参数描述）
- ❌ 跳过五问法直接调用词库生成提示词

---

## 六、与 aesthetic-vision-skill 的联动声明

本词库在 `aesthetic-vision-skill` 体型矩阵（§三）和面部反大众化四方向（§三）的框架下运作：

| aesthetic-vision-skill 方向 | 对应本词库推荐参数 |
|---|---|
| **恐怖谷极限精准** | T0玻璃肌 + `razor-sharp jawline` + `obsidian irises with zero reflection` + `sharply defined philtrum` |
| **反常规比例极端化** | `phoenix eyes` + `high prominent cheekbones` + `ethereal upper face + sharp lower face` 两段式冲撞 |
| **情绪极端固化** | `straight flat brows` + `half-lidded monolid` + `zero light reflection irises` |
| **廉价制造感暴露** | `asymmetric eyelid fold` + `glassy irises with excessive highlight` + T2塑料皮肤 + `undefined soft brows` |

---

**版本**：v1.0  
**建立时间**：2026-03-29  
**适用范围**：AXIS 5.0 全项目  
**上级技能**：`art-design-skill` / 审美前置：`aesthetic-vision-skill`
