---
name: donghua-vfx-system
description: 国漫特效系统。提供国产动画风格的VFX特效关键词库、分类体系、中英双语提示词、AI可行性评级，用于分镜编写时为画面注入国漫级别特效质感。
version: 1.0
---

# 国漫特效系统（Donghua VFX System）

## 模块定位

本模块是 Seedance 分镜编写技能的**国漫特效增强组件**。提供系统化的国产动画风格 VFX 特效关键词库，覆盖能量系统、元素系统、空间系统、觉醒系统、氛围系统五大类，确保提示词中的特效描述达到《灵笼》《斗破苍穹》《斗罗大陆》《完美世界》级别视觉质感。

**与战斗增强模块的关系**：
- `combat-enhanced-module.md` 管**动作逻辑**（怎么打、怎么动、因果链）
- `donghua-vfx-system.md` 管**视觉特效**（打出来是什么样、光效粒子怎么表现）
- 两者协同使用：先用战斗模块确定动作链，再用本模块注入特效视觉层

---

## 触发条件

当提示词需要以下视觉效果时，启用本模块：

| 类别 | 触发关键词 |
|------|-----------|
| 能量释放 | 斗气、灵气、真气、内力、气劲、功力、元力、仙力 |
| 元素法术 | 火焰、冰霜、雷电、风暴、水流、土石、暗影、光明 |
| 空间异变 | 撕裂、虚空、结界、封印、传送、时停、空间崩塌 |
| 觉醒变身 | 觉醒、暴走、武魂、法相、血脉、进化、破境、突破 |
| 环境渲染 | 天劫、异象、天地变色、日月无光、紫气东来 |

---

## 一、能量系统（Qi/Aura VFX）

> 国漫核心视觉标识——角色周身能量外放的视觉表现

### 1.1 斗气/灵气外放

| 特效名称 | 中文描述 | 英文提示词 | 视觉参数 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 气焰升腾 | 角色周身气焰如火焰般升腾 | blazing qi aura rising around character, energy flames surging upward, translucent flame-like aura | 颜色随修为：白→蓝→金→紫；高度=角色身高0.5-2倍 | ⭐⭐⭐ S级 |
| 能量光环 | 角色脚下/身周环形光环旋转 | rotating energy ring around character, circular aura halo at feet, glowing orbital rings | 1-3层同心环，不同转速，颜色渐变 | ⭐⭐⭐ S级 |
| 气浪脉冲 | 能量以脉冲波形式向外扩散 | qi shockwave pulse expanding outward, energy ripple radiating from character | 半球形扩散，地面尘土掀起，近处物体被吹飞 | ⭐⭐ A级 |
| 粒子风暴 | 大量能量粒子围绕角色旋转 | swirling energy particles storm around character, luminous particle vortex | 粒子数量500+，螺旋上升轨迹 | ⭐⭐⭐ S级 |
| 经脉透视 | 角色体内经脉发光可见 | glowing meridian lines visible through skin, internal energy channels illuminated | 线状发光沿人体经脉走向，皮肤半透明 | ⭐⭐ A级 |
| 气柱冲天 | 能量柱从角色头顶直射天空 | massive energy pillar shooting skyward from character, qi beam piercing clouds | 直径1-5米，高度穿云，周围云层被吹散 | ⭐⭐⭐ S级 |

### 1.2 能量凝聚形态

| 特效名称 | 中文描述 | 英文提示词 | 应用场景 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 掌心聚能球 | 手掌中凝聚的能量球体 | concentrated energy sphere in palm, glowing orb charging in hand | 蓄力攻击、展示实力 | ⭐⭐⭐ S级 |
| 指尖光点 | 手指尖端凝聚的微小能量点 | tiny energy point at fingertip, luminous dot at finger's end | 精准攻击、点穴、封印 | ⭐⭐⭐ S级 |
| 能量兵器 | 纯能量凝聚成武器形态 | energy-formed weapon, qi-materialized sword/spear, solid light blade | 凝气成剑/枪/盾 | ⭐⭐ A级 |
| 能量铠甲 | 能量在体表凝聚成铠甲 | energy armor forming on body surface, qi-crystallized protective shell | 防御时能量凝实 | ⭐⭐ A级 |
| 气刃/气弹 | 脱手的能量攻击体 | energy blade projectile, qi bullet shooting forward, crescent energy slash | 远程攻击 | ⭐⭐⭐ S级 |

### 1.3 能量颜色体系（国漫标准色谱）

| 能量等级/属性 | 颜色 | Hex参考 | 含义 | 典型角色 |
|-------------|------|---------|------|---------|
| 初级/普通 | 白色微光 | `#F0F0FF` | 刚入门、低阶 | 普通修士 |
| 中级/进阶 | 淡蓝 | `#4DA6FF` | 中等修为 | 内门弟子 |
| 高级/精锐 | 深蓝 | `#0047AB` | 强者之气 | 长老级 |
| 王级/顶尖 | 金色 | `#FFD700` | 王者霸气 | 宗主/帝皇 |
| 帝级/至尊 | 紫金 | `#9B59B6`→`#FFD700` | 至高无上 | 大帝/至尊 |
| 邪恶/魔道 | 血红+黑 | `#8B0000`+`#1A0000` | 邪气、杀意 | 魔道修士 |
| 混沌/始源 | 灰白混沌雾 | `#C0C0C0`渐变 | 超越一切法则 | 混沌之力 |
| 神圣/天道 | 纯白金边 | `#FFFFFF`+`#FFD700` | 天道之力 | 天道化身 |

**提示词用法**：
```
角色周身[金色/紫金/血红]斗气火焰升腾 → 
[golden/purple-gold/blood-red] qi aura flames rising around character
```

---

## 二、元素系统（Elemental VFX）

> 五行元素+雷电暗光的完整特效词库

### 2.1 火系特效

| 特效名称 | 中文描述 | 英文提示词 | 强度分级 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 烈焰缠身 | 火焰缠绕角色全身 | raging flames wrapping around entire body, fire engulfing character | L1 轻焰 | ⭐⭐⭐ S级 |
| 火海蔓延 | 地面大面积火海 | sea of fire spreading across ground, burning inferno carpet | L2 火海 | ⭐⭐⭐ S级 |
| 焚天烈焰 | 从天而降的火焰柱 | pillar of hellfire descending from sky, heaven-burning flame column | L3 天火 | ⭐⭐ A级 |
| 熔岩爆发 | 地面裂开喷出岩浆 | molten lava erupting from cracked ground, magma geyser | L3 岩浆 | ⭐⭐ A级 |
| 凤凰火翼 | 火焰凝聚成凤凰/翅膀形态 | phoenix fire wings spreading behind character, flame-formed bird wings | L2 化形 | ⭐⭐ A级 |
| 火焰旋涡 | 火焰形成龙卷风 | fire tornado vortex, spiraling flame whirlwind | L3 旋焰 | ⭐⭐ A级 |

### 2.2 冰系特效

| 特效名称 | 中文描述 | 英文提示词 | 强度分级 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 霜气弥漫 | 白色寒气从角色周围扩散 | frost mist spreading from character, icy vapor surrounding body | L1 寒气 | ⭐⭐⭐ S级 |
| 冰棱突起 | 地面冰柱尖刺突然长出 | ice spikes erupting from ground, frost stalagmites bursting upward | L2 冰棱 | ⭐⭐⭐ S级 |
| 冰封领域 | 以角色为中心地面冻结扩散 | freezing domain expanding from character, ground crystallizing into ice | L2 领域 | ⭐⭐ A级 |
| 冰龙化形 | 冰块凝聚成龙形攻击 | ice dragon forming from frost particles, crystalline dragon charging | L3 化形 | ⭐⭐ A级 |
| 暴风雪 | 大面积冰雪风暴 | raging blizzard with ice shards, snowstorm with razor ice | L3 风暴 | ⭐⭐ A级 |
| 绝对零度 | 一切瞬间冻结、时间仿佛停止 | absolute zero freeze, everything crystallizing instantly, time-stop ice | L4 极寒 | ⭐ B级 |

### 2.3 雷电系特效

| 特效名称 | 中文描述 | 英文提示词 | 强度分级 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 电弧缠绕 | 电弧在角色身体表面跳动 | electric arcs crackling on body surface, lightning dancing on skin | L1 微雷 | ⭐⭐⭐ S级 |
| 雷霆降世 | 天空劈下粗壮雷电 | massive lightning bolt striking from sky, divine thunder descending | L3 天雷 | ⭐⭐⭐ S级 |
| 雷云聚集 | 天空迅速聚集浓厚雷云 | dark thunderclouds rapidly gathering overhead, ominous storm brewing | L2 雷云 | ⭐⭐⭐ S级 |
| 连锁闪电 | 闪电在多个目标间跳跃 | chain lightning jumping between targets, electric arc bouncing | L2 连锁 | ⭐⭐ A级 |
| 雷域 | 整个区域被电弧网覆盖 | lightning domain, entire area covered with electric grid | L3 领域 | ⭐⭐ A级 |
| 紫色天劫雷 | 渡劫场景的紫金天雷 | purple-gold tribulation lightning from heavens, divine punishment thunder | L4 天劫 | ⭐⭐ A级 |

### 2.4 风系特效

| 特效名称 | 中文描述 | 英文提示词 | 强度分级 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 劲风环绕 | 可见的风流围绕角色 | visible wind currents swirling around character, air distortion | L1 劲风 | ⭐⭐ A级 |
| 风刃切割 | 肉眼可见的弧形风刃 | visible crescent wind blade slashing, air-cutting arc | L2 风刃 | ⭐⭐ A级 |
| 龙卷风暴 | 巨型风柱卷起碎片 | massive tornado lifting debris, destructive wind pillar | L3 风暴 | ⭐⭐ A级 |
| 真空刃 | 空气被切断后的真空裂痕 | vacuum slash, visible air gap from extreme wind blade | L3 真空 | ⭐ B级 |

### 2.5 土/岩系特效

| 特效名称 | 中文描述 | 英文提示词 | 强度分级 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 地面龟裂 | 脚下大地裂开纹路 | ground cracking beneath feet, earth fracture lines spreading | L1 裂纹 | ⭐⭐⭐ S级 |
| 岩柱升起 | 地面突起岩石柱子 | stone pillars erupting from ground, earth columns rising | L2 岩柱 | ⭐⭐⭐ S级 |
| 山体崩塌 | 整座山体碎裂倒塌 | entire mountain crumbling, massive rockslide collapse | L4 山崩 | ⭐⭐ A级 |
| 碎石悬浮 | 破碎的岩石碎片悬浮空中 | broken rock fragments floating in mid-air, levitating debris | L2 悬浮 | ⭐⭐⭐ S级 |
| 沙暴 | 沙尘暴席卷整个场景 | sandstorm engulfing the scene, swirling sand and dust | L3 沙暴 | ⭐⭐ A级 |

### 2.6 水系特效

| 特效名称 | 中文描述 | 英文提示词 | 强度分级 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 水流操控 | 水流被意念操控悬浮 | water stream manipulated by will, levitating water ribbons | L1 水流 | ⭐⭐ A级 |
| 水龙化形 | 水凝聚成龙形冲击 | water dragon formed from liquid, aqua serpent charging | L2 化形 | ⭐⭐ A级 |
| 海啸巨浪 | 巨大海浪冲击 | massive tsunami wave crashing, towering tidal wave | L4 海啸 | ⭐⭐ A级 |
| 水幕屏障 | 水流形成的防护壁 | water curtain barrier, liquid shield wall | L1 水幕 | ⭐⭐ A级 |

---

## 三、空间系统（Spatial VFX）

> 国漫中最具视觉冲击力的特效类型

### 3.1 空间撕裂/破碎

| 特效名称 | 中文描述 | 英文提示词 | 视觉细节 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 空间裂缝 | 空间出现黑色裂缝 | spatial rift tearing open, black crack in reality, void fissure | 裂缝边缘发紫光/白光，内部漆黑或可见异界 | ⭐⭐ A级 |
| 空间碎裂 | 空间如玻璃般碎裂 | space shattering like glass, reality fracturing into shards | 碎片悬浮，各碎片折射不同画面 | ⭐⭐ A级 |
| 虚空吞噬 | 黑洞般的吞噬效果 | void vortex consuming everything, black hole suction | 中心漆黑，边缘扭曲拉伸 | ⭐⭐ A级 |
| 空间折叠 | 空间被折叠扭曲 | folded space distortion, warped reality bending | 画面扭曲如哈哈镜 | ⭐ B级 |

### 3.2 结界/领域

| 特效名称 | 中文描述 | 英文提示词 | 视觉细节 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 半球结界 | 半球形能量屏障 | hemispherical energy barrier, dome-shaped force field | 半透明+六边形网格纹理+受击波纹 | ⭐⭐⭐ S级 |
| 领域展开 | 以角色为中心改变空间法则 | domain expansion, reality-altering zone spreading from character | 扩散圆形波纹，域内色调/法则改变 | ⭐⭐ A级 |
| 封印阵法 | 地面/空中的封印魔法阵 | seal formation on ground, glowing runic circle, binding array | 符文旋转+层层套叠+发光 | ⭐⭐⭐ S级 |
| 时间停止 | 时间冻结，万物静止 | time freeze, everything suspended in mid-air, frozen moment | 飞溅物悬停、雨滴静止、灰尘不落 | ⭐⭐⭐ S级 |

### 3.3 传送/召唤

| 特效名称 | 中文描述 | 英文提示词 | 视觉细节 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 传送阵 | 脚下发光传送阵 | glowing teleportation circle beneath feet, transport array activating | 符文旋转→光柱升起→人物消失/出现 | ⭐⭐⭐ S级 |
| 空间门 | 撕开的空间通道 | spatial portal opening, dimensional gateway | 椭圆形发光门框，内部可见目的地 | ⭐⭐ A级 |
| 召唤降临 | 从天而降/从阵中浮出 | summoned entity descending from above, emerging from magic circle | 巨大阴影→实体从光中凝聚 | ⭐⭐ A级 |

---

## 四、觉醒系统（Awakening VFX）

> 国漫最爽的名场面——角色突破/觉醒/暴走的特效表现

### 4.1 突破/进阶

| 特效名称 | 中文描述 | 英文提示词 | 演出流程 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 破境突破 | 修为突破瓶颈 | realm breakthrough, cultivation level-up, barrier shattering | ①身体泛光→②能量暴涨→③气柱冲天→④天象异变 | ⭐⭐ A级 |
| 血脉觉醒 | 隐藏血脉激活 | bloodline awakening, dormant lineage activating | ①瞳孔变色→②身体纹路发光→③气质骤变→④血脉之力具现 | ⭐⭐ A级 |
| 武魂显现 | 身后出现武魂虚影 | martial spirit manifesting behind character, soul projection appearing | ①背后光芒→②巨大虚影凝聚→③武魂完全显现 | ⭐⭐ A级 |
| 法相天地 | 身后巨型法相投射 | giant dharma image projected behind, colossal spiritual avatar | ①光芒汇聚→②模糊巨影→③清晰法相与角色同步动作 | ⭐ B级 |

### 4.2 暴走/失控

| 特效名称 | 中文描述 | 英文提示词 | 视觉变化 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 魔化暴走 | 邪气侵蚀、理智丧失 | demonic berserk transformation, dark energy corruption | 皮肤出现黑色纹路、眼睛变红/黑、气焰从金变血红 | ⭐⭐ A级 |
| 杀意释放 | 杀气具象化 | killing intent materialized, murderous aura visualization | 角色身后出现巨大骷髅/恶鬼虚影、周围生物恐惧颤抖 | ⭐⭐ A级 |
| 力量失控 | 能量不受控制外泄 | power overload, uncontrolled energy discharge | 身体裂纹发光、能量不规则爆发、周围物体被波及 | ⭐⭐ A级 |

### 4.3 瞳术变化（国漫经典名场面）

| 特效名称 | 中文描述 | 英文提示词 | 视觉细节 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 瞳孔变色 | 瞳孔颜色骤变 | iris color suddenly changing, eye color transformation | 极特写：瞳孔从黑→金/红/紫，虹膜纹路变化 | ⭐⭐⭐ S级 |
| 瞳孔花纹 | 瞳孔出现特殊花纹 | mystical pattern forming in iris, runic pupil design | 极特写：花纹如齿轮/花瓣/符文旋转显现 | ⭐⭐⭐ S级 |
| 竖瞳 | 瞳孔变为竖直 | vertical slit pupil forming, reptilian eye transformation | 极特写：圆瞳缓缓收缩为竖瞳，光反射改变 | ⭐⭐⭐ S级 |
| 双瞳异色 | 左右眼不同颜色 | heterochromia activation, dual-colored eyes | 极特写：一金一紫/一红一蓝 | ⭐⭐⭐ S级 |

---

## 五、氛围系统（Atmospheric VFX）

> 烘托画面氛围的环境特效

### 5.1 天象异变

| 特效名称 | 中文描述 | 英文提示词 | 触发条件 | AI可行性 |
|---------|---------|-----------|---------|---------|
| 天地变色 | 天空颜色骤变 | sky color dramatically shifting, heavens darkening/reddening | 大战开始、强者降临 | ⭐⭐⭐ S级 |
| 日月无光 | 日月被遮蔽 | sun and moon dimming, celestial bodies losing light | 至尊级战斗、天道惩罚 | ⭐⭐ A级 |
| 紫气东来 | 东方涌来紫色祥云 | purple auspicious clouds rolling from the east, royal qi descending | 帝王出世、至宝出现 | ⭐⭐ A级 |
| 天劫降临 | 天空裂开降下天罚 | heavenly tribulation descending, sky splitting open with divine punishment | 渡劫突破 | ⭐⭐ A级 |
| 血月 | 月亮变为血红色 | blood moon rising, crimson lunar eclipse | 邪恶力量觉醒、大凶之兆 | ⭐⭐⭐ S级 |
| 极光异象 | 天空出现极光般光幕 | aurora-like phenomenon in sky, celestial light curtain | 远古遗迹激活、空间异变 | ⭐⭐⭐ S级 |

### 5.2 环境渲染特效

| 特效名称 | 中文描述 | 英文提示词 | 用途 | AI可行性 |
|---------|---------|-----------|------|---------|
| 落叶纷飞 | 大量树叶飘散 | leaves scattering in the wind, autumn foliage drifting | 高手对峙、气场压制 | ⭐⭐⭐ S级 |
| 樱花飘零 | 樱花瓣漫天飞舞 | cherry blossom petals drifting everywhere, sakura storm | 唯美战斗、暴力美学 | ⭐⭐⭐ S级 |
| 尘土飞扬 | 大量尘土被掀起 | massive dust cloud rising, debris and dirt flying | 强力冲击、着地震动 | ⭐⭐⭐ S级 |
| 水面波纹 | 水面因力量波动产生涟漪 | water surface rippling from energy pressure, concentric waves | 气场释放、力量压制 | ⭐⭐⭐ S级 |
| 碎石悬浮 | 小石块脱离地面悬浮 | small rocks levitating from ground, pebbles floating upward | 能量蓄积、力场影响 | ⭐⭐⭐ S级 |
| 衣袂飘动 | 衣服/头发无风自动 | clothes and hair billowing without wind, fabric floating from energy | 能量外放、气场释放 | ⭐⭐⭐ S级 |
| 地面凹陷 | 脚下地面被压力踩凹 | ground caving in beneath feet, footprint crater from pressure | 力量释放、重力压制 | ⭐⭐⭐ S级 |

### 5.3 光效渲染

| 特效名称 | 中文描述 | 英文提示词 | 用途 | AI可行性 |
|---------|---------|-----------|------|---------|
| 丁达尔光 | 光束穿过烟尘/水汽 | Tyndall effect light beams through dust/mist, god rays | 神圣感、希望感 | ⭐⭐⭐ S级 |
| 逆光剪影 | 强逆光下角色变为剪影 | dramatic backlight silhouette, rim light character outline | 神秘感、气势感 | ⭐⭐⭐ S级 |
| 能量辉光 | 整个画面被能量光芒笼罩 | energy glow illuminating entire scene, luminous overexposure | 大招释放瞬间 | ⭐⭐⭐ S级 |
| 星芒闪烁 | 十字星芒光效 | cross-shaped lens flare, starburst light effect | 高光点强调、武器反光 | ⭐⭐⭐ S级 |
| 色温对撞 | 冷暖色光在画面中对抗 | warm vs cool color temperature clash, dual-toned lighting | 对峙双方、善恶对立 | ⭐⭐⭐ S级 |

---

## 六、国漫特效组合套餐（常用场景速查）

> 直接复制到提示词中使用，已按 AI 可行性优化

### 6.1 🔥 觉醒爆发套餐

**适用**：角色突破/觉醒/暴走名场面

```
中文描述：
角色双眼瞳孔骤变[金色/血红]，周身[金色/紫色]气焰猛然升腾如火焰般炸开，
脚下地面龟裂凹陷碎石悬浮，强烈气浪脉冲向外扩散掀起尘土落叶，
衣袂头发无风自动猎猎飞舞，一道能量光柱从头顶冲天而起直破云层，
天空颜色骤变乌云翻涌。

英文提示词：
character's iris suddenly turning [golden/blood-red], blazing [golden/purple] qi aura 
explosively rising around entire body like raging flames, ground cracking and caving in 
beneath feet with rock fragments levitating, powerful qi shockwave expanding outward 
kicking up dust and leaves, clothes and hair billowing wildly without wind, massive 
energy pillar shooting skyward piercing through clouds, sky color dramatically shifting 
with dark clouds churning.
```

**AI可行性**：⭐⭐ A级（建议分2条P：①瞳孔特写+气焰升腾；②气柱冲天+天象变色）

### 6.2 ⚡ 天劫渡劫套餐

**适用**：渡劫突破、天道惩罚场景

```
中文描述：
天空迅速聚集浓厚紫黑色雷云层层叠叠遮天蔽日，雷云中电弧闪烁不断，
一道粗壮的紫金色天劫雷从云层中劈下，照亮整个大地，
雷电击中角色/目标瞬间白光爆闪，地面炸出巨型弹坑碎石飞溅，
电弧在弹坑中持续跳动残留3秒。

英文提示词：
thick purple-black thunderclouds rapidly gathering layer upon layer blocking the sky, 
electric arcs flickering constantly within clouds, a massive purple-gold tribulation 
lightning bolt striking down from clouds illuminating the entire land, blinding white 
flash at impact point, ground exploding into a massive crater with debris flying, 
residual electric arcs crackling in crater for 3 seconds.
```

**AI可行性**：⭐⭐⭐ S级（雷电+爆炸是AI强项）

### 6.3 🗡️ 剑气斩击套餐

**适用**：剑修出招、远程斩击

```
中文描述：
角色挥剑画出弧线，一道半月形[白色/金色]剑气脱手飞出，
剑气经过之处空气扭曲留下一道可见的切割痕迹，
剑气命中目标瞬间爆炸，金色火花迸溅冲击波环形扩散，
地面被剑气切出一道深深的沟壑。

英文提示词：
character swinging sword in an arc, a crescent-shaped [white/golden] sword qi 
projectile flying forward, air distortion visible along its path leaving a cutting trail, 
upon hitting the target — explosion with golden sparks scattering and circular shockwave 
expanding, ground sliced open into a deep gash by the sword energy.
```

**AI可行性**：⭐⭐ A级

### 6.4 👁️ 瞳术觉醒套餐

**适用**：瞳术激活、血脉觉醒特写

```
中文描述：
极特写镜头：角色瞳孔急剧收缩，虹膜颜色从黑色渐变为[金色/血红/紫色]，
瞳孔中缓缓浮现[齿轮状/花瓣状/符文状]花纹旋转排列，
眼球表面映射出周围能量光芒，泪腺处溢出一滴[血泪/金色泪珠]。

英文提示词：
extreme close-up: character's pupil rapidly contracting, iris color gradually shifting 
from black to [golden/blood-red/purple], mystical [gear-shaped/petal-shaped/runic] 
patterns slowly forming and rotating within the pupil, energy reflections visible on 
eyeball surface, a single [blood tear/golden teardrop] welling from tear duct.
```

**AI可行性**：⭐⭐⭐ S级（眼睛特写是AI强项）

### 6.5 🌑 空间破碎套餐

**适用**：空间撕裂、强者碰撞导致空间崩坏

```
中文描述：
两股力量正面碰撞的中心点，空间如镜面般出现裂纹并迅速蔓延，
裂缝边缘散发紫色/白色光芒，碎裂的空间碎片悬浮翻转各自映射不同画面，
中心出现漆黑的虚空吞噬力场，周围物体被引力扭曲拉伸。

英文提示词：
at the collision point of two forces, space cracking like a mirror with fractures 
spreading rapidly, purple/white glow emanating from crack edges, shattered spatial 
fragments floating and rotating each reflecting different scenes, a dark void 
gravitational field forming at center, surrounding objects warped and stretched 
by gravitational pull.
```

**AI可行性**：⭐⭐ A级（建议简化为裂缝+光效，避免过于复杂的多画面折射）

### 6.6 🔮 封印/阵法套餐

**适用**：封印结界、召唤阵法

```
中文描述：
角色脚下/面前展开一个[金色/血红/蓝色]发光法阵，
法阵由3-5层同心圆组成，每层刻有不同符文以不同速度旋转，
符文依次亮起从外圈向内圈激活，法阵中心凝聚能量光球逐渐膨胀，
法阵表面有半透明的能量薄膜如水面波纹般律动。

英文提示词：
a [golden/blood-red/blue] glowing magic formation expanding beneath/before the character, 
formation composed of 3-5 concentric rings each inscribed with different runes rotating 
at different speeds, runes lighting up sequentially from outer ring inward, energy orb 
condensing at formation center gradually expanding, semi-transparent energy membrane 
on formation surface rippling like water.
```

**AI可行性**：⭐⭐⭐ S级（法阵是AI表现最好的特效之一）

---

## 七、特效强度与环境破坏联动

> 与 `combat-enhanced-module.md` 的环境破坏系统（第六章）对接

| 特效强度 | 环境破坏等级 | 典型特效 | 环境表现 |
|---------|------------|---------|---------|
| L1 微弱 | L1 轻微 | 气焰升腾、电弧缠绕、霜气弥漫 | 地面裂纹、衣袂飘动、碎石微动 |
| L2 中等 | L1-L2 | 能量脉冲、冰棱突起、火海蔓延 | 地面龟裂、碎石悬浮、树木折断 |
| L3 强力 | L2-L3 | 气柱冲天、天雷降世、焚天烈焰 | 山体碎裂、建筑倒塌、天地变色 |
| L4 毁灭 | L3-L4 | 领域展开、空间碎裂、绝对零度 | 方圆百米荒芜、空间裂缝、天劫 |
| L5 灭世 | L4-L5 | 法天象地、虚空吞噬 | 山川移位、日月无光、天地崩塌 |

---

## 八、AI平台特效适配指南

### 各平台特效生成能力对比

| 特效类型 | Seedance 2.0 | Kling 2.6 | Kling 3.0 | 最佳选择 |
|---------|-------------|-----------|-----------|---------|
| 能量气焰/光环 | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Seedance/Kling 3.0 |
| 雷电/闪电 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 三平台均可 |
| 火焰/爆炸 | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Seedance/Kling 3.0 |
| 冰霜/冰柱 | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Kling 3.0 |
| 粒子效果 | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Seedance/Kling 3.0 |
| 空间裂缝 | ⭐⭐ | ⭐ | ⭐⭐ | Seedance |
| 法阵/符文 | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Kling 3.0 |
| 瞳孔特写 | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Seedance/Kling 3.0 |
| 天象（云/雷/月） | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 三平台均可 |
| 碎石悬浮 | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Seedance/Kling 3.0 |
| 大型化形（龙/凤） | ⭐ | ⭐ | ⭐⭐ | Kling 3.0（用远景+剪影） |
| 法天象地/巨型法相 | ❌ | ❌ | ⭐ | 全部困难（用远景暗示） |

### AI不友好特效的替代方案

| 难以生成的特效 | 替代方案 |
|--------------|---------|
| 法天象地巨型法相 | → 用远景剪影+光芒暗示规模，不拍清晰全身 |
| 化形生物（龙/凤） | → 用能量轮廓+光效拖尾暗示形态，远景呈现 |
| 空间多画面折射 | → 简化为裂缝+发光边缘，不做碎片内画面 |
| 经脉透视 | → 用体表发光纹路替代，不做X光式透视 |
| 多人同时释放特效 | → 分条P各拍一人特效，后期交叉剪辑 |
| 绝对零度瞬间冻结 | → 分两帧：正常→完全冰封，用硬切表现 |

---

## 九、与本项目视觉风格对接

> 针对《万界通告，哨兵阵亡》的特效适配

### 现实层特效规范

现实层以**写实CG**为基调，特效需克制、有物理感：
- ✅ 允许：系统金字发光、称谓光效、轻微环境扰动（碎石微动、衣角飘）
- ✅ 允许：车祸物理特效（金属碎片、玻璃飞溅、路面擦痕）
- ❌ 禁止：大规模能量特效（现实层不存在修仙力量）
- ❌ 禁止：天象异变（现实层是正常人类世界）

**现实层特效提示词模板**：
```
subtle golden glow from floating title above character's head,
faint energy distortion around system text, 
realistic debris physics (metal scraping, glass shattering),
volumetric light through dust particles
```

### 虚拟层特效规范

虚拟层以**MAPPA暗黑+3D全息**为基调，特效需夸张、有冲击力：
- ✅ 允许：聊天气泡爆炸粒子、冲击帧、全息文字发光
- ✅ 允许：各角色专属能量色彩（无极魔尊=血红、机械之主=钴蓝等）
- ✅ 允许：MAPPA式丢帧冲击特效
- ❌ 禁止：温暖色调特效（虚拟层必须冷色调）

**虚拟层特效提示词模板**：
```
explosive particle scatter from chat bubbles, 
impact frame with radial speed lines,
[blood-red/cobalt-blue/iron-grey] energy aura around character title,
3D holographic text shattering into glowing fragments,
MAPPA-style frame-skip impact effect
```

### 未来章节预留（战斗场景激活后）

当剧情进入战斗场景（预计ch04+）后，完整启用本模块的能量/元素/空间/觉醒系统。

---

## 十、特效提示词写入规范

### 写入位置

特效描述应写在提示词的**动作描述之后、音效标注之前**：

```
...角色挥剑斩出（动作描述），
一道金色半月形剑气脱手飞出空气扭曲（特效描述），
剑气命中目标爆炸金色火花迸溅冲击波环形扩散（特效+打击感），
"唰——"剑气飞出 "轰——"命中爆炸（音效标注）...
```

### 特效密度控制

| P块时长 | 推荐特效数量 | 说明 |
|--------|------------|------|
| 5-8s | 1-2个特效 | 简洁，聚焦核心效果 |
| 8-12s | 2-3个特效 | 适中，主特效+环境反应 |
| 12-15s | 3-5个特效 | 丰富，主特效+环境+氛围 |

### 🔴 铁律：特效不能脱离动作因果链

- 每个特效必须有**力量来源**（谁释放的？怎么释放的？）
- 每个特效必须有**物理后果**（对环境造成了什么？）
- 禁止"无源特效"——特效不能凭空出现，必须有前置动作

---

## 版本信息

- 版本: 1.0
- 创建日期: 2026-04-21
- 本模块为 Seedance 分镜编写技能的国漫特效增强组件
- 与 `combat-enhanced-module.md`（动作逻辑）协同使用
- 与 `assets/visual-style-guide.md`（视觉风格规范）保持一致

---

**© 2026 AXIS Donghua VFX System v1.0**
