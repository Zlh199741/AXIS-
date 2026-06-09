# 身材引擎 — 超维女性角色身材与气场生成规范 (V-MAX Pro)

> **唯一定义位置**：`resources/body-figure-engine.md`
> **引用方**：`art-design-skill` 角色公式 §2.3 / `aesthetic-vision-skill` §三体型矩阵 / `character-prompt-template` / CLAUDE.md 服化道阶段
> **适用范围**：所有女性角色的身材比例、个人特征、气场原型、镜头光影设计

---

## 一、破次元身材代码 (Hyper-Anatomy)

> 🔴 **强制规则**：所有女性主角/重要配角的角色提示词中，必须从以下四组词池中各选取至少1项组合写入英文描述段。禁止仅用 `supermodel` 等泛化词替代。

### 1.1 绝对比例

| 提示词 | 中文含义 | 适用场景 |
|--------|---------|---------|
| `impossible 10-heads body proportion` | 非人类十头身比例 | T0级角色（SSR恋人等） |
| `surreal anatomical perfection` | 超现实完美解剖结构 | T0级角色 |
| `extreme elongated silhouette` | 极致拉长的轮廓 | T0/T1级角色 |

### 1.2 逆天长腿

| 提示词 | 中文含义 |
|--------|---------|
| `hyper-elongated slender legs` | 超级纤长的双腿 |
| `endless legs` | 无尽的长腿 |
| `perfect leg muscle lines` | 完美的腿部肌肉线条 |

### 1.3 极致腰臀

| 提示词 | 中文含义 |
|--------|---------|
| `impossibly tiny waist` | 不可思议的极细腰身 |
| `exaggerated S-curve hourglass figure` | 夸张的S型沙漏身材 |
| `prominent collarbones and right-angled shoulders` | 极致锁骨与直角肩 |

### 1.4 体态气场

| 提示词 | 中文含义 |
|--------|---------|
| `statuesque posture` | 雕塑般的体态 |
| `dominating runway presence` | 统治级的T台气场 |
| `majestic body language` | 充满统治力的肢体语言 |

---

## 二、一眼万年视觉锚点 (The Visual Hooks)

> 🔴 **强制规则**：每个女性角色必须从以下四类中选择 **1~2项** 作为该角色的**永久绑定特征**，写入角色提示词的核心记忆点，全集保持一致，禁止漂移。

### 2.1 面部痣/印记

| 提示词 | 中文含义 |
|--------|---------|
| `a striking tear-drop mole under the left eye` | 左眼下的绝美泪痣 |
| `a tiny mole on the tip of her nose` | 鼻尖痣（极具辨识度） |

### 2.2 异色/特殊瞳孔

| 提示词 | 中文含义 |
|--------|---------|
| `amber-colored deep eyes` | 琥珀色深邃眼眸 |
| `subtle heterochromia` | 极其轻微的异色瞳（增加神秘感） |

### 2.3 骨相变异

| 提示词 | 中文含义 |
|--------|---------|
| `Liu Yifei's ethereal upper face mixed with a razor-sharp, aggressive jawline` | 仙气上半脸 + 极具攻击性的锋利下颌线 |

### 2.4 发丝特征

| 提示词 | 中文含义 |
|--------|---------|
| `jet-black extreme long hair with a single hidden silver strand` | 极长黑发中隐蔽的一缕银丝 |

---

## 三、四大终极气场原型 (The Ultimate Auras)

> 根据角色叙事定位选择气场原型，写入角色提示词的气质描述段。可混合使用，但主气场原型必须明确。

### 3.1 暗黑女王系 (The Dark Empress)

```
Cold, arrogant expression, piercing predatory gaze, pale porcelain skin contrasting with blood-red lips, dark high-fashion aura.
```
**情绪词**：冰冷傲慢 · 掠夺性眼神 · 冷白皮与嗜血红唇对比

### 3.2 废土神明系 (The Wasteland Goddess)

```
Ethereal yet battle-hardened, dust on flawless skin, melancholic but unyielding eyes, raw survivor energy.
```
**情绪词**：仙气但久经沙场 · 无瑕肌肤上的灰尘 · 忧郁但不屈的眼神

### 3.3 赛博财阀系 (The Cyber-Heiress)

```
Intellectual, calculating smirk, half-rimmed smart glasses, flawless symmetrical face, metallic cold light reflection on skin.
```
**情绪词**：高智商算计的冷笑 · 半框智能眼镜 · 完美对称脸 · 皮肤反射冷金属光

### 3.4 极繁国风系 (The Hyper-Oriental)

```
Modern ancient fusion, phoenix eyes (丹凤眼) with sharp eyeliner, majestic and unreachable vibe, modern Hanfu deconstruction.
```
**情绪词**：古今融合 · 锋利眼线的丹凤眼 · 不可触及的威严感

---

## 四、物理开挂镜头与极致光影 (The Lens & Lighting Cheat Codes)

> 🔴 **强制规则**：凡涉及角色全身镜头的场景提示词/分镜提示词，必须从以下词池中选取至少 **1项视角词 + 2项光影词**（主光+氛围光）。与 `aesthetic-vision-skill` §四入镜规范协同执行。

### 4.1 强化身材视角（必加）

| 提示词 | 中文含义 | 效果 |
|--------|---------|------|
| `Dynamic low-angle shot` | 动态低视角仰拍 | 强制拉长腿部比例 |
| `Full body shot from below` | 自下而上的全身镜头 | 视觉腿长放大 |
| `Wide-angle lens distortion at the edges` | 边缘广角畸变 | 极度拉伸四肢 |
| `Three-quarter view with slight low angle` | 三分视角微仰拍 | 展示倒三角/S曲线轮廓 |
| `Side profile silhouette against backlight` | 侧身逆光剪影 | 体型轮廓一击必杀 |
| `Camera positioned at knee level (~40cm), slight upward angle +12°` | 膝位机位微仰 | 身高感+压迫感并存 |

### 4.2 极致光影体系 (Ultimate Cinematic Lighting)

> ⚡ **设计哲学**：光影不是技术参数——**光影是角色的第二件衣服**。每一束光都在讲故事，每一片阴影都有叙事目的。

#### A. 轮廓光·勾魂系 (Rim & Edge Light)

| 提示词 | 中文含义 | 效果 | 适用情绪 |
|--------|---------|------|---------|
| `Cinematic dramatic rim light outlining silhouette` | 影视级戏剧性轮廓光 | 勾勒绝佳身材曲线/倒三角轮廓 | 英雄登场·命运降临 |
| `Sacred white backlight rim-tracing body contour` | 神圣白逆光追踪全身轮廓 | 从肩到胯S曲线完美显现 | 神性·不可触及 |
| `Double-edge rim light from opposing sides` | 双侧对向轮廓光 | 两侧剪影边缘同时亮起 | 对峙·两难·宿命 |
| `Hair light separating subject from dark background` | 发丝分离光 | 头发边缘发出天使般光晕 | 孤独中的希望 |
| `Razor-thin edge light on jawline and shoulders` | 极薄利刃光·下颌+肩线 | 刀削般勾勒骨相和肩宽 | 冷酷·危险·精英骨相 |

#### B. 明暗法·雕塑系 (Chiaroscuro & Sculpting)

| 提示词 | 中文含义 | 效果 | 适用情绪 |
|--------|---------|------|---------|
| `High contrast chiaroscuro` | 高对比度明暗法 | 强化体态立体感 | 力量·决断 |
| `Rembrandt triangle light on face` | 伦勃朗三角光 | 鼻侧形成三角亮斑，经典权威感 | 权力·智慧·内省 |
| `Chiaroscuro emphasizing muscle definition through fabric` | 明暗法穿透布料强化肌肉线条 | 制服下倒三角体格无处隐藏 | 潜伏力量被揭示 |
| `Split lighting — half face illuminated, half in total shadow` | 劈裂光·半脸全明半脸全暗 | 正邪/双面/选择的视觉隐喻 | 内心撕裂·二元对立 |
| `Under-lighting casting upward shadows on face` | 底光·阴影向上投射 | 恐怖/神性/超自然氛围 | 系统降临·非人力量 |

#### C. 色温冲突·叙事系 (Color Temperature Conflict)

| 提示词 | 中文含义 | 效果 | 适用情绪 |
|--------|---------|------|---------|
| `Warm tungsten 3000K backlight vs cold blue 6000K ambient fill` | 暖钨丝逆光 vs 冷蓝环境填充 | 双色温在角色身上碰撞，脸上出现冷暖交界 | 两个世界的交汇 |
| `Teal and orange split lighting on face` | 青橙劈裂色温 | 脸部一侧暖橙一侧冷青 | 内心冲突·转折 |
| `Golden system light from above meeting cold reality below` | 金色系统光自上 vs 冷色现实自下 | 超自然光与自然光对抗 | 天命降临凡身 |
| `Neon color bleed — magenta and cyan reflected on wet skin` | 霓虹色溢·洋红青色映射在湿润皮肤 | 都市夜景的色彩污染角色 | 迷失·赛博·情绪爆发 |

#### D. 体积光·神迹系 (Volumetric & God Rays)

| 提示词 | 中文含义 | 效果 | 适用情绪 |
|--------|---------|------|---------|
| `Volumetric light shafts cutting through dust particles` | 体积光束穿透飘浮粉尘 | 空气中可见的光柱，丁达尔效应 | 神圣·命运 |
| `God rays streaming through architectural crevice` | 神光从建筑裂缝倾泻 | 巨大光柱照在渺小角色身上 | 史诗·宿命·渺小感 |
| `Atmospheric haze catching rim light into visible light cone` | 大气薄雾将轮廓光变成可见光锥 | 角色被光的锥体"选中" | 天选者·被命运标记 |
| `Smoke-diffused backlight creating ethereal glow around figure` | 烟雾漫射逆光·角色周身浮现虚幻光晕 | 整个人在发光 | 觉醒·蜕变·超凡 |

#### E. 反射·镜像系 (Reflection & Mirror)

| 提示词 | 中文含义 | 效果 | 适用情绪 |
|--------|---------|------|---------|
| `Wet asphalt reflecting full figure creating double silhouette` | 湿柏油路反射全身·双重剪影 | 视觉身高翻倍，S曲线/倒三角延伸 | 史诗·强化体态 |
| `Puddle reflection capturing inverted dramatic sky` | 水坑映射倒转的戏剧性天空 | 脚下是另一个世界的入口 | 命运·双世界 |
| `3M reflective strip retroreflection under backlight` | 3M反光条逆光下逆反射爆闪 | 全身反光点同时亮起=英雄显现 | 叶锋专属·三光追迹 |
| `Chrome/glass surface reflecting fragmented figure` | 铬面/玻璃碎片映射破碎人影 | 角色在多重碎片中被拼接 | 精神崩溃·身份分裂 |

#### F. 极限质感光 (Texture-Revealing Light)

| 提示词 | 中文含义 | 效果 | 适用情绪 |
|--------|---------|------|---------|
| `Raking light at extreme angle revealing every surface texture` | 掠射光·极端角度揭示所有表面纹理 | 皮肤毛孔/布料纤维/金属划痕全部浮现 | 写实·细节控 |
| `Subsurface scattering warm orange glow on ear tips and fingertips` | 次表面散射暖橙光透过耳尖和指尖 | 皮肤半透明感，活生生的人 | 温度·生命力 |
| `Specular highlight tracing collarbone and forearm veins` | 高光追踪锁骨线和前臂静脉 | 骨骼/血管在光线下暴露无遗 | 危险美·精英体格 |
| `Wet fabric clinging to athletic physique, light tracing every fold` | 湿润布料贴合体格·光追踪每一道褶皱 | 雨夜/汗水场景的终极体态展示 | 力量释放·战斗后 |

### 4.3 大师级光影方案速查（场景→光影组合）

| 场景类型 | 推荐光影组合 | 参考影片 |
|---------|-------------|---------|
| **英雄登场·逆光全身** | 轮廓光A1 + 反射E1 + 色温C1 | 《灵笼》《银翼杀手2049》 |
| **天命降临·系统激活** | 体积光D3 + 底光B5 + 色温C3 | 《沙丘》《降临》 |
| **孤独行走·都市夜景** | 霓虹C4 + 反射E1 + 轮廓光A4 | 《Drive》《银翼杀手》 |
| **对峙决断·高压特写** | 劈裂光B4 + 伦勃朗B2 + 掠射光F1 | 《教父》《无国界追凶》 |
| **觉醒蜕变·力量爆发** | 神迹D4 + 双侧轮廓A3 + 质感F3 | 《鬼灭之刃》《Arcane》 |
| **市井日常·烟火真实** | 色温C1(暖调为主) + 质感F2 + 发丝光A4 | 《寄生虫》《花样年华》 |

---

## 五、V-MAX 终极角色提示词模板

> 以下模板用于**场景变体**中女性角色的全身展示镜头（基础形象仍遵循纯白背景T0模板）。
> 方括号内为可替换变量，实际使用时根据角色设定填充。

```
(Masterpiece, 8k resolution, highest quality, photorealistic:1.2), [视角：Dynamic low-angle full body shot].

A striking Chinese female character with an [身材：impossible 10-heads body proportion, hyper-elongated slender legs, unrealistically perfect hourglass figure, statuesque posture].

Her face features [特征：Liu Yifei's ethereal facial structure combined with a razor-sharp jawline], highlighting a [记忆点：striking red tear-drop mole under her left eye], and [神态：a cold, arrogant expression with a piercing predatory gaze].

She is wearing [穿搭：avant-garde tight-fitting dark tech-wear/high-slit haute couture dress] that perfectly traces her exaggerated curves.

Set in [背景：a colossal, brutalist concrete architecture space].

[光影镜头：Cinematic dramatic rim light outlining her silhouette, wide-angle lens 24mm, f/1.8, highly detailed skin texture, ultra-sharp focus, Kodak Portra 400 film].
```

---

## 六、男性主角身材引擎 — 黑马型体格生成规范 (V-MAX Pro · Male)

> 🔴 **核心设计命题**："制服下藏着一个不应该是外卖员的身体。"
> 外表是市井凡人，骨骼是异界系统最高宿主。视觉反差越大，爽感越强。
> **适用范围**：所有男性主角/重要男性角色（当前项目：叶锋）

### 6.1 破次元体格代码 (Male Hyper-Anatomy)

> 🔴 **强制规则**：所有男性主角全身镜头提示词中，必须从以下三组词池各选取至少1项组合写入英文描述段。

#### 6.1.1 极致比例

| 提示词 | 中文含义 | 适用场景 |
|--------|---------|---------|
| `9-heads golden male body proportion` | 九头身黄金比例男体 | 全身镜头必加 |
| `perfect inverted triangle torso` | 完美倒三角躯干 | 制服下隐约可见 |
| `extreme shoulder-to-waist ratio` | 极致的肩腰比 | 正面/背面全身出场 |
| `broad powerful shoulders tapering to narrow athletic waist` | 宽厚肩膀收窄至精干腰线 | 侧面/三分视角 |

#### 6.1.2 精干型战力体格

| 提示词 | 中文含义 |
|--------|---------|
| `lean zero-fat functional muscle build` | 精干零脂肪功能型肌肉 |
| `defined forearm veins under skin` | 皮下清晰的前臂血管 |
| `compressed explosive athletic physique` | 蓄而未发的运动员体格 |
| `broad powerful shoulders under loose fabric` | 宽厚肩膀被宽松制服半遮 |
| `visible trapezius and deltoid outline through shirt` | T恤下隐约可见的斜方肌和三角肌轮廓 |
| `corded neck tendons suggesting suppressed tension` | 颈部肌腱暗示被压制的张力 |

#### 6.1.3 气场体态

| 提示词 | 中文含义 |
|--------|---------|
| `predatory stillness posture` | 肉食者般的静止感——不动时比动时更危险 |
| `dormant explosive energy in relaxed stance` | 放松站姿中潜伏的爆炸性力量 |
| `effortless dominant presence` | 不费力的统治气场 |
| `weight shifted to one leg, deceptively casual, coiled spring ready` | 重心偏移·看似随意·实为蓄力弹簧 |

---

### 6.2 一眼万年视觉锚点 (Male Visual Hooks · 永久绑定)

> 🔴 **强制规则**：以下特征全集保持一致，禁止漂移。每个男性主角必须从下方选取 **3~5项** 作为永久绑定特征。

#### 叶锋·永久绑定特征表

| 类型 | 特征 | 提示词 | 叙事功能 |
|------|------|--------|---------|
| **面部记忆点** | 左眉骨有一道浅淡旧疤（来历成谜） | `a faint old scar crossing the left eyebrow` | 暗示过去·危险经历的证据 |
| **眼神特征** | 疲倦但燃着危险深度的眼睛 | `tired yet smoldering eyes with dangerous depth` | 不自知的天选者·表面平静内核燃烧 |
| **骨相** | 男模级面部骨相：极致下颌线+高耸颧骨+深邃眉弓+挺直高鼻梁 | `international male model facial bone structure, razor-sharp chiseled jawline, prominent high cheekbones, deep brow ridge, tall straight nose bridge, deep-set eye sockets` | 男模级骨相藏在外卖员面孔里 |
| **发型锚点** | 美式前刺发型：两侧渐变推短至肤感，顶部蓬松纹理前刺尖刺刘海，哑光质感，自然黑发 | `modern American textured crop, sides tapered with skin fade, textured voluminous top styled forward into sharp spiky fringe, matte finish, natural black hair` | 精心打理的发型与外卖员身份的反差感 |
| **肢体锚点** | 右手中指有一圈骑车形成的老茧 | `calloused right-hand knuckles from delivery riding` | 底层劳动者的身份烙印 |
| **体态锚点** | 逆光下三处3M反光条同时亮起 | `three 3M reflective strips simultaneously glowing under backlight` | 叶锋唯一视觉符号——三光追迹 |

---

### 6.3 气场原型 (Male Ultimate Auras)

> 根据叙事阶段选择气场原型。叶锋当前阶段为 **6.3.1**，随剧情推进可混合叠加。

#### 6.3.1 黑马深伏系 (The Dormant Tiger) — 叶锋·初始态

```
Ordinary surface, extraordinary skeleton. Suppressed predatory stillness,
a young man who looks unremarkable until the light hits right.
The universe chose him and he doesn't know it yet.
Effortless dangerous calm, the quiet before a storm.
```
**情绪词**：寂静肉食者 · 不自知的天选者 · 外表凡尘·骨子里不属于这个世界 · 暴风雨前的死寂

#### 6.3.2 觉醒风暴系 (The Awakening Storm) — 叶锋·系统激活态

```
Eyes suddenly sharp, posture shifting from casual to combat-ready in one frame.
The delivery uniform becomes battle armor, ordinary accessories become tactical gear.
Storm energy crackling around still figure, golden system light descending from above.
The dormant tiger opens its eyes.
```
**情绪词**：瞳孔骤缩 · 制服变甲 · 金光破顶 · 沉睡的虎睁眼了

#### 6.3.3 废墟战神系 (The Ruin Sovereign) — 叶锋·后期态

```
Battle-worn but unbroken, delivery jacket torn revealing functional muscle beneath.
Blood-like golden system light radiating from scars and reflective strips.
Standing alone in destruction, the last man standing energy,
calm authority of someone who has already died once and returned.
```
**情绪词**：百战不折 · 制服残破露出真身 · 金光从伤痕渗出 · 死过一次的人的从容

---

### 6.4 男性主角物理开挂镜头 (Male Lens Cheat Codes)

> 🔴 **强制规则**：男性主角全身出场的场景提示词，必须选取 **1项视角词 + 2项光影词**（从 §四 极致光影体系中选取）。以下为男性主角专用视角强化。

**视角词（必选1项）**：

| 提示词 | 效果 | 最佳搭配光影 |
|--------|------|-------------|
| `Dynamic low-angle shot from below waist` | 强制拉长腿部/强化肩宽倒三角 | A1轮廓光 + C1色温冲突 |
| `Three-quarter view with slight low angle` | 展示倒三角轮廓最佳角度 | A5利刃光 + B3穿透明暗 |
| `Side profile silhouette against backlight` | 制服下倒三角+反光条同时爆发 | E3反光条逆反射 + D4烟雾光晕 |
| `Over-the-shoulder shot revealing back muscle outline through fabric` | 过肩镜头·背阔肌轮廓透过布料 | B3穿透明暗 + F4湿布贴合 |
| `Extreme close-up on forearm veins and calloused knuckles` | 前臂血管+老茧极致微距 | F1掠射光 + F2次表面散射 |

---

### 6.5 叶锋·三光追迹专属光影方案 (The Three-Star Light System)

> 🌟 **叶锋的视觉核心标识**：逆光场景下，三处3M反光条（夹克肩部 + 腰带侧面 + 鞋后跟）同时亮起，形成"倒三角+竖线+水平"三点星光结构。
> 3米外看到的是**战士剪影**，走近才发现是**外卖员制服**——这就是叶锋的全部设计哲学。

**三光追迹完整提示词模块**（全身逆光出场必须注入）：

```
Strong backlight (warm tungsten 3000K) from upper-right rear,
simultaneously illuminating three 3M reflective strips:
— shoulder reflective strips forming upper triangle vertex,
— tactical belt side reflector forming mid-body anchor point,
— heel reflector strip forming ground-level base,
creating dramatic three-point star-light constellation against dark background.
Inverted triangle warrior silhouette visible at distance,
delivery uniform identity revealed only at close range.
Wet asphalt below reflecting the three light points into six,
doubling the constellation effect.
```

---

## 七、V-MAX 男性主角终极提示词模板

> 以下模板用于**场景变体**中男性主角的全身展示镜头（基础形象仍遵循纯白背景T0模板）。
> 方括号内为可替换变量，实际使用时根据角色设定填充。

### 7.1 基础形象模板（纯白背景·服化道用）

```
(Masterpiece, 8K resolution, highest quality, photorealistic CG:1.2),
Chinese top-tier animation character design (Ling Long/Douro Continent quality).

A striking Chinese male character, early 20s, 185cm tall, with [体格：9-heads golden male body proportion,
international male model physique, perfect inverted triangle torso, extreme shoulder-to-waist ratio,
lean elongated athletic build with defined muscle lines without excessive bulk].

Face: [骨相：international male model facial bone structure, razor-sharp chiseled jawline,
prominent high cheekbones, deep brow ridge, tall straight nose bridge, deep-set eye sockets],
[记忆点：a faint old scar crossing the left eyebrow],
[眼神：tired yet smoldering eyes with dangerous depth],
[发型：modern American textured crop, sides tapered with skin fade,
textured voluminous top styled forward into sharp spiky fringe, matte finish, natural black hair],
[体态：predatory stillness expression, dormant explosive energy].

Wearing [穿搭：complete outfit with multi-layered tactical accessories, PBR material detail].

Pure white background, solid white backdrop, no cast shadows,
physically based rendering, subsurface scattering skin, defined forearm veins,
8K ultra-detailed, masterpiece, official art, sharp focus.
```

### 7.2 场景变体模板（逆光英雄·极致光影版）

```
(Masterpiece, 8K resolution, highest quality, photorealistic CG:1.2),
[视角：Dynamic low-angle shot from below waist, camera at knee level].

A striking Chinese male character, 185cm tall, with [体格：9-heads golden body proportion,
international male model physique, perfect inverted triangle torso, extreme shoulder-to-waist ratio,
lean elongated athletic build with defined muscle lines, broad powerful shoulders under loose orange jacket].

Face: [骨相：international male model facial bone structure, razor-sharp chiseled jawline,
prominent high cheekbones, deep brow ridge, tall straight nose bridge,
tired yet smoldering dangerous eyes],
[记忆点：a faint old scar crossing left eyebrow],
[发型：modern American textured crop with sharp spiky fringe styled forward,
matte finish natural black hair],
[体态：predatory stillness expression].

Wearing [穿搭：orange delivery uniform jacket with PBR reflective strips,
multi-layer tactical accessories].

Set in [背景：night urban environment, dramatic atmosphere].

[极致光影：Cinematic dramatic rim light (warm tungsten 3000K) outlining inverted triangle torso silhouette,
three 3M reflective strips simultaneously glowing — shoulder + belt + heel — three-point star-light effect,
high contrast chiaroscuro emphasizing muscle definition through fabric,
warm backlight from streetlight vs cold blue ambient fill creating dual color temperature on skin,
wet asphalt reflecting full figure creating double silhouette,
volumetric light shafts cutting through atmospheric haze,
subsurface scattering warm glow on ear tips and exposed forearm skin,
specular highlight tracing collarbone and forearm veins through fabric tension,
Kodak Portra 400 film aesthetic, 8K ultra-detailed, masterpiece].
```

### 7.3 觉醒态模板（系统激活·金光破顶）

```
(Masterpiece, 8K resolution, highest quality, photorealistic CG:1.2),
[视角：Three-quarter low-angle shot, camera below eye level].

Same character as base design. Chinese male, [体格：9-heads proportion,
inverted triangle torso now fully visible as posture shifts to combat-ready,
shoulders squared, weight centered, compressed explosive energy releasing].

Face: [觉醒态：pupils suddenly contracted, jaw clenched, dangerous depth in eyes now fully ignited,
scar on left eyebrow catching golden light from above].

[极致光影：Golden system light descending from directly above — supernatural point light source,
casting sharp circular light pool on hair crown and shoulders,
warm tungsten backlight from environment creating dual-source conflict on figure,
under-lighting component from golden light casting dramatic upward face shadows,
atmospheric haze catching golden light into visible descending god-ray cone,
three 3M reflective strips catching both gold and warm tungsten — creating six-color star points,
smoke-diffused golden aura forming ethereal crown-like halo around head,
razor-thin edge light on jawline — bone structure knife-sharp under supernatural illumination,
wet ground reflecting golden light into an inverted cathedral of light below figure,
subsurface scattering on ear tips and fingertips showing warm gold instead of usual orange,
high contrast chiaroscuro — delivery uniform shadows vs golden-lit shoulders = "armor reveal" effect,
8K ultra-detailed, masterpiece, physically based rendering].
```

---

## 八、与 AXIS 体系的协同关系

| 协同对象 | 协同方式 |
|---------|---------|
| `aesthetic-vision-skill` §三 体型矩阵 | 本引擎的女性身材代码（§一）为体型矩阵的 T0/T1 级提供**具体提示词实现** |
| `aesthetic-vision-skill` §四 入镜规范 | 本引擎的极致光影体系（§四·6类30+词条）与入镜规范的低机位仰拍、85mm长焦、逆光轮廓**协同叠加** |
| `art-design-skill` §2.3 T0级提示词构建 | 角色提示词的英文描述段中必须融入本引擎 §一~§二（女）/ §六.1~§六.2（男）的词汇 |
| `character-prompt-template` | 角色 A/B 版本提示词中必须体现身材引擎词汇；男性主角使用 §七 三版模板 |
| `assets/visual-style-guide.md` §六 | 叶锋男性主角规范与本引擎 §六 完全对齐，视觉-style-guide 中的提示词以本引擎为权威来源 |
| 分镜提示词（场景变体·女性） | 涉及女性角色全身出场的P块，必须融入 §四 的视角词 + 光影体系A/B类 |
| 分镜提示词（场景变体·叶锋） | 叶锋全身出场的P块，必须融入 §六.4 视角词 + §六.5 三光追迹模块 + §四 光影体系C/E类 |
| `电影摄影-AI提示词库.md` §五 打光方案 | 本引擎 §四.3 大师级速查表与提示词库中8套打光方案**直接挂钩**，按情绪场景联动查阅 |

---

**版本**：v2.0（V-MAX Pro 增强版 · 2026-04-15 重大升级）
**变更摘要**：
- §四 光影：从2条基础词扩展为6类30+极致光影词条，新增情绪标注+场景速查表
- §六 新增：男性主角身材引擎（叶锋专用）— 体格代码·视觉锚点·3阶段气场原型·专属三光追迹光影方案
- §七 新增：男性主角终极提示词三版模板（基础形象/逆光英雄/觉醒态）
- §八 更新：协同关系扩展，男女双引擎统一管理

**建立时间**：2026-04-12
**最后更新**：2026-04-15
**适用范围**：AXIS 5.0 全项目 · 男女角色设计与分镜 · 叶锋专属标识系统
