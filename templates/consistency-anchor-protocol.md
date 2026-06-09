# 一致性锚定词组协议（Cross-View/Module Consistency Anchor Protocol）

> 版本: 1.0
> 创建日期: 2026-03-26
> 说明: 所有视觉设计技能（角色/道具/场景）共享的一致性锚定词组规范，确保跨视图/跨模块AI生成的视觉一致性。

---

## 核心原理

**一致性锚定词组**是在开始生成任何视图/模块之前，从设计定义中提炼出的一段**跨所有提示词通用的固定文本**。该文本粘贴到每条提示词开头，确保AI在生成不同视图时始终参照同一个基准原型。

**强制规则**：
- 🔴 所有提示词的锚定词组必须**逐字相同**（审核时逐字比对）
- 🔴 锚定词组必须包含：名称 + 基准形态 + 核心辨识特征 + 全局色彩序列
- 🔴 锚定词组放置在每条提示词的**最开头**

---

## 三类锚定词组格式

### 1. 角色锚定词组（Character Anchor）

**适用技能**：art-design-skill、costume-prop-character-design-skill

**格式**：
```
[角色中英文全称], [基准体态描述（体型+头身比+肤色+年龄段）], [核心记忆点（1个最具辨识度的视觉符号）], global color palette: [主色#HEX] + [辅色#HEX] + [强调色#HEX]
```

**示例**：
```
Cui Yunxiu 崔云绣, slender East Asian female early 20s, 7.5 head-to-body ratio, fair porcelain skin, core memory point: silver-white long flowing hair with ice-blue eyes radiating cold elegance, global color palette: silver-white #E0E0E0 + ice-blue #81D4FA + jade-green #A5D6A7
```

---

### 2. 道具锚定词组（Prop Anchor）

**适用技能**：prop-concept-design-skill

**格式**：
```
[道具中英文全称], [基准形态描述（shape + 基准尺寸 + 主体材质色值）], [核心结构标志（2-3个最具辨识度的固定结构）], global material palette: [材质1色值] + [材质2色值] + [材质3色值] + ...
```

**示例**（详见 prop-concept-design-skill §六-A）：
```
Sword Immortal Sect·Flowing Cloud Ten-Sword Scabbard (剑仙宗·流云万剑匣), rectangular ancient sword case L120cm×W25cm×H30cm, black ebony wood body #221A17 with rounded edges, top-bottom split lid with central gilt-bronze locking clasp, integrated flowing-cloud handle on lid top, global material palette: ebony #221A17 + gilt bronze #D4AF37 + self-luminous cyan rune #00E5FF + translucent moonstone #E0F7FF + dark brown leather #3C2218
```

---

### 3. 场景锚定词组（Scene Anchor）

**适用技能**：scene-concept-design-skill

**格式**：
```
[场景中英文全称], [空间结构描述（形态 + 核心建筑/地貌 + 美术风格）], [核心固定元素标志（3-4个最具辨识度的元素）], global palette: [核心主色#HEX] + [辅助色#HEX] + ... + [特效色#HEX]
```

**示例**（详见 scene-concept-design-skill §六-A）：
```
Nine-Tailed Fox Ruby Crystal Cave (九尾狐红玉水晶洞穴), natural stalactite cavern with walls of translucent orange-red crystal rock formations, connected to snowy mountain exterior, Eastern fantasy warm cozy style, core elements: round white baby nine-tailed fox + campfire with grilled fish + geothermal hot spring with steam + orange-red crystal rock walls, global palette: deep brown #3E2723 + orange-red #E64A19 + crimson #B71C1C + warm gold #FFB300 + cream white #FFF8E1 + light cyan #B2EBF2 + dark navy #1A237E + pure black #000000
```

---

## 审核检查规则

审核技能在验证提示词时，必须对锚定词组执行以下检查：

| 检查项 | 标准 | 不通过处理 |
|--------|------|-----------|
| 锚定词组存在性 | 每条提示词开头是否包含锚定词组 | 🔴 缺失 → FAIL |
| 逐字一致性 | 所有提示词的锚定词组是否逐字相同 | 🔴 不一致 → FAIL |
| 名称完整 | 是否包含中英文双语名称 | 🔴 缺失 → FAIL |
| 基准形态 | 是否包含形态/尺寸/材质等基准描述 | 🟡 缺失 → 需补充 |
| 核心辨识特征 | 是否包含核心记忆点/结构标志/固定元素 | 🔴 缺失 → FAIL |
| 全局色彩序列 | 是否包含完整的HEX色值序列 | 🔴 缺失 → FAIL |

---

## 引用说明

本协议被以下技能引用：
- `skills/art-design-skill/SKILL.md`：角色锚定词组
- `skills/costume-prop-character-design-skill/SKILL.md`：角色工业化落地锚定词组
- `skills/prop-concept-design-skill/SKILL.md`：道具锚定词组（§六-A）
- `skills/scene-concept-design-skill/SKILL.md`：场景锚定词组（§六-A）
