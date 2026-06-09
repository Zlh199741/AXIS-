# 道具提示词输出模板（强制结构）

> 本模板为强制结构，所有标注【必填】的字段必须填写，否则判定为不合格

---

## [道具名]

### 基础形象

**核心记忆点**：[一句话描述，如：古代医书 + 线装 + 黄页]

**背景要求**：【必填】
- ✅ `strictly isolated on a pure white background, solid white backdrop, no cast shadows`
- ❌ 禁止出现：spread open on a desk / embedded in a wooden desk / held in palm / being offered on open palms

**视角要求**：【必填】
- ✅ `macro lens, 100mm`
- ❌ 禁止出现：close-up tension shot / dramatic lighting

**布光要求**：【必填】
- ✅ `clean bright studio lighting`
- ❌ 禁止出现：candlelight / moonlight / dramatic lighting / oil lamp lighting

**提示词（Nano Banana Pro - 中英文分离）**：

**【中文描述段】**：[纯中文自然语言叙事描述，可换行]

**【英文描述段】**：[纯英文一整段，不换行，包含所有技术关键词和渲染参数]

**【画面洁净负面约束】**：【必填】不要耀斑、不要镜头 flare、不要散景光斑、不要漂浮粒子、不要火星碎点、不要发光碎点、不要空气中的小色点、不要灰尘亮点、不要噪点、不要胶片颗粒、不要随机微高光、不要表面随机脏纹理、不要人物身上密集噪声。

**T0强制要素自检（道具专用5项）**：
- [ ] 纯白背景隔离：`pure white background` ✅/❌
- [ ] 微距视角：`macro lens / 100mm` ✅/❌
- [ ] 硬表面材质（至少2项）：`metal / bronze / leather / wood / silk` ✅/❌
- [ ] 渲染参数：`PBR / physically based rendering` ✅/❌
- [ ] T0级画质后缀：`masterpiece, ultra-detailed, 8K, sharp focus` ✅/❌
- [ ] 画面洁净负面约束：无耀斑/无镜头 flare/无散景光斑/无漂浮粒子/无噪点/无胶片颗粒/无随机脏纹理 ✅/❌

---

## 输出规范说明

### 道具提示词特殊要求

| 要求 | 说明 |
|------|------|
| **必须白底** | 道具用作素材参考，必须干净隔离，不能有场景背景 |
| **必须微距** | 使用 `macro lens, 100mm` 确保细节清晰 |
| **禁止场景化** | 不能写"放在桌上"、"被人拿着"等场景描述 |

### 黑名单关键词（道具禁用）

❌ `spread open on a desk`
❌ `embedded in a wooden desk surface`
❌ `held in a young man's palm`
❌ `being offered on open palms`
❌ `floating in mid-air`
❌ `candlelight illumination` / `moonlight` / `dramatic lighting`
❌ `close-up tension shot` / `dramatic oil lamp lighting`
❌ 不要耀斑 / 不要镜头 flare / 不要散景光斑
❌ 不要漂浮粒子 / 不要火星碎点 / 不要发光碎点
❌ 不要空气中的小色点 / 不要灰尘亮点
❌ 不要噪点 / 不要胶片颗粒 / 不要随机微高光
❌ 不要表面随机脏纹理 / 不要人物身上密集噪声

### 白名单关键词（道具必用）

✅ `strictly isolated on a pure white background`
✅ `solid white backdrop`
✅ `no cast shadows`
✅ `macro lens, 100mm`
✅ `clean bright studio lighting`
✅ `physically based rendering (PBR)`
✅ `masterpiece, ultra-detailed, 8K, sharp focus`
