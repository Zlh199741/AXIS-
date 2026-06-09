---
name: visual-style-selector-skill
description: 视觉风格选择技能。在服化道设计前，引导用户选择艺术风格（写实/风格化/动漫电影/顶级人物CG质感等）和具体工作室风格（新海诚/扳机社/吉卜力等），确保视觉呈现与题材、情绪、目标受众完美匹配。
---

# 视觉风格选择技能

## [技能定位]

本技能是**导演分析阶段**和**服化道设计阶段**之间的关键桥梁，负责：
1. 基于题材类型、情绪基调、目标受众，推荐合适的视觉风格
2. 提供交互式选择界面，让用户明确视觉方向
3. 输出标准化的视觉风格规范文档，指导后续服化道设计和分镜编写

**核心价值**：
- 避免视觉风格的"隐式处理"，给用户明确的选择权
- 确保视觉风格与题材、情绪、受众的一致性
- 为服化道设计提供清晰的艺术方向指引

---

## [工作流位置]

```
导演分析阶段
     ↓
┌─────────────────────────┐
│  视觉风格选择阶段        │  ← 本技能
│ (题材风格+艺术风格)     │
└────────────┬────────────┘
     ↓
服化道设计阶段
```

---

## [完整风格体系架构]

### 体系总览

```
视觉风格选择体系
│
├─ 第一层：题材风格基调（自动匹配）
│   └─ 基于genre-adaptive-skill自动推荐色调、氛围、场景
│
├─ 第二层：主风格类型（用户选择）
│   ├─ 1. 写实风格 (Photorealistic)
│   ├─ 2. 风格化 (Stylized)
│   ├─ 3. 动漫电影风格 (Anime Film Style)
│   │   ├─ 3.1-3.8: T0级八大工作室风格
│   │   └─ 3.9: 日本动画界视觉风格体系（14个子分类）
│   ├─ 4. 概念艺术风格 (Concept Art)
│   ├─ 5. 漫画风格 (Comic/Manga Style)
│   └─ 6. 顶级人物CG质感 (Top-tier Character CG Style)
│
└─ 第三层：风格细化与混搭（可选）
    ├─ 单一风格深化
    └─ 多风格混搭组合
```

---

## [风格快速索引表]

### 按题材快速匹配

| 题材类型 | 推荐主风格 | 推荐子风格 | 备选方案 |
|---------|-----------|-----------|---------|
| 热血战斗 | 动漫电影 | 扳机社/飞碟社/Sakuga流派 | MAPPA暗黑美学 |
| 青春爱情 | 动漫电影 | 新海诚/京阿尼/少女漫风格 | 柔和粉彩流派 |
| 暗黑悬疑 | 动漫电影 | MAPPA/低饱和度暗黑流派 | 青年漫改编风格 |
| 治愈日常 | 动漫电影 | 吉卜力/京阿尼/柔和粉彩 | 背景美术流派 |
| 科幻机甲 | 动漫电影 | 扳机社/CG融合流派 | 概念艺术-硬表面科幻 |
| 奇幻冒险 | 动漫电影 | 吉卜力/飞碟社 | 概念艺术-史诗奇幻 |
| 都市现代 | 写实/动漫 | 新海诚/背景美术流派 | 数字转型期风格 |
| 复古怀旧 | 动漫电影 | 90年代复古/黄金时代 | 蒸汽波美学 |
| 升级流 | 动漫电影 | 顶级韩漫/少年漫风格 | 高饱和度流派 |
| 心理实验 | 动漫电影 | 心理视觉化/极简主义 | 低饱和度暗黑 |
| 角色定妆 | 顶级人物CG质感 | 冷白棚拍男主/冷瓷旗袍女主/月华银发神女 | 极致写实CG |

### 按视觉特点快速匹配

| 想要的视觉效果 | 推荐风格 | 关键词 |
|--------------|---------|--------|
| 极致光影效果 | 新海诚/飞碟社/京阿尼 | 丁达尔效应、体积光、粒子特效 |
| 强烈色彩冲击 | 扳机社/高饱和度流派 | 霓虹色彩、视觉爆炸 |
| 细腻情感表达 | 京阿尼/新海诚/少女漫 | 微表情、柔和光影 |
| 流畅动作场面 | Sakuga流派/扳机社/飞碟社 | 极致流畅、夸张透视 |
| 暗黑压抑氛围 | MAPPA/低饱和度暗黑/青年漫 | 冷色调、高对比阴影 |
| 治愈温暖感 | 吉卜力/柔和粉彩/京阿尼 | 手绘质感、温暖色调 |
| 复古怀旧感 | 90年代复古/黄金时代 | VHS滤镜、胶片颗粒 |
| 精美背景 | 新海诚/吉卜力/背景美术流派 | 超写实背景、环境叙事 |
| 技术未来感 | CG融合流派/概念艺术 | 3D-2D融合、硬表面 |
| 艺术实验性 | 心理视觉化/极简主义 | 抽象隐喻、符号化 |
| 顶级人物定妆照 | 顶级人物CG质感 | 瓷感皮肤、AI精修、冷白棚拍、人物特写 |

---

## [风格选择决策树]

### 决策流程图

```
开始
  │
  ▼
【题材分析】从导演分析提取题材类型
  │
  ▼
【受众定位】确定目标受众年龄层
  │
  ├─ 15岁以下 → 推荐：吉卜力/少年漫/高饱和度
  ├─ 15-25岁 → 推荐：扳机社/新海诚/韩漫/Sakuga
  ├─ 25-35岁 → 推荐：京阿尼/MAPPA/背景美术
  └─ 35岁以上 → 推荐：青年漫/黄金时代/写实
  │
  ▼
【情绪基调】确定主要情绪
  │
  ├─ 热血燃 → 扳机社/Sakuga/少年漫
  ├─ 甜蜜治愈 → 京阿尼/吉卜力/柔和粉彩
  ├─ 暗黑压抑 → MAPPA/低饱和度/青年漫
  ├─ 浪漫唯美 → 新海诚/少女漫/背景美术
  └─ 悬疑紧张 → 低饱和度/心理视觉化
  │
  ▼
【视觉优先级】确定核心视觉需求
  │
  ├─ 光影效果 → 新海诚/飞碟社/京阿尼
  ├─ 动作场面 → Sakuga/扳机社/飞碟社
  ├─ 背景环境 → 新海诚/吉卜力/背景美术
  ├─ 色彩冲击 → 扳机社/高饱和度/韩漫
  └─ 情感细腻 → 京阿尼/新海诚/少女漫
  │
  ▼
【技术约束】考虑制作成本
  │
  ├─ 高预算 → 飞碟社/CG融合/新海诚
  ├─ 中预算 → 京阿尼/MAPPA/背景美术
  └─ 低预算 → 极简主义/少年漫/数字转型期
  │
  ▼
【最终推荐】输出3个方案（保守/平衡/突破）
```

---

## [三层风格选择体系]

### 第一层：题材风格基调（自动匹配）

基于 `genre-adaptive-skill` 的题材分析，自动推荐基础风格：

| 题材类型 | 推荐色调 | 推荐氛围 | 典型场景 |
|---------|---------|---------|---------|
| 豪门总裁 | 奢华金/深蓝/黑 | 高级、冷艳 | 别墅、跑车、游艇 |
| 玄幻修仙 | 青蓝/紫金/墨绿 | 仙侠、飘逸 | 仙山、洞府、秘境 |
| 悬疑推理 | 冷灰/深蓝/暗红 | 压抑、紧张 | 密室、雨夜、废宅 |
| 甜宠治愈 | 粉色/暖黄/薄荷绿 | 温暖、柔和 | 咖啡厅、公园、家 |
| 末世生存 | 灰暗/血红/辐射绿 | 绝望、压抑 | 废墟、地下基地 |
| 职场逆袭 | 深蓝/白/黑 | 专业、锐利 | 写字楼、会议室 |
| 古代宫斗 | 朱红/金黄/墨绿 | 华丽、压抑 | 宫殿、御花园 |
| 惊悚恐怖 | 冷绿/暗红/黑 | 诡异、恐怖 | 鬼屋、医院、学校 |

### 第二层：艺术风格类型（用户选择）

提供6大艺术风格方向供用户选择：

#### 1. 写实风格 (Photorealistic)

**适用场景**：
- 现代都市题材（豪门、职场、悬疑）
- 需要强烈代入感的剧情
- 目标受众：25-40岁成人观众

**子选项**：
- **影视级写实**：`Photorealistic cinematic render, IMAX 70mm format, film grain`
- **游戏AAA写实**：`Hyper-realistic AAA game production render, Unreal Engine 5, ray tracing`
- **微距写实**：`100mm macro photography, f/1.2 aperture, shallow depth of field`

**关键词库**：
```
physically based rendering (PBR), ambient occlusion (AO), 
subsurface scattering (SSS), ray tracing global illumination,
intricate skin texture, visible pores, peach fuzz,
realistic eye reflection, detailed hair physics
```

---

#### 2. 风格化 (Stylized)

**适用场景**：
- 轻松娱乐向题材（甜宠、喜剧）
- 需要视觉冲击力的动作戏
- 目标受众：18-30岁年轻观众

**子选项**：
- **手绘风格**：`Overwatch hand-painted texture style, stylized rendering, bold outlines`
- **卡通风格**：`Stylized Fortnite rendering, vibrant colors, exaggerated proportions`
- **扁平插画**：`Flat illustration style, minimalist design, bold color blocks`

**关键词库**：
```
stylized rendering, hand-painted textures, bold outlines,
vibrant saturated colors, exaggerated expressions,
cel-shading, toon shader, graphic novel aesthetic
```

---

#### 3. 动漫电影风格 (Anime Film Style)

**适用场景**：
- 玄幻、奇幻、科幻题材
- 需要强烈情感渲染的剧情
- 目标受众：15-35岁二次元观众

**子选项（T0级八大工作室风格库）**：

> 以下风格定义来自《AI绘画终极提示词工程白皮书》，为工业级商用标准。

##### 3.1 扳机社 / 赛博张力 (Studio Trigger / Cyber Tension)
```yaml
核心特征:
  - 超动态视角和极端透视
  - 高对比度霓虹色彩
  - 视觉爆炸性冲击力
  - 粗黑轮廓线 + 冲击帧

T0级提示词:
  "Studio Trigger style, hyper-dynamic angle, high-contrast neon colors, 
   visual explosion, bold black outlines, extreme perspective, impact frame,
   best quality, ultra-detailed, masterpiece, official art, sharp focus, 
   vibrant colors, highly detailed eyes, detailed hair strands, dynamic lighting"

适用题材: 热血、机甲、科幻、赛博朋克
视觉特点: 夸张变形、几何图形化、强烈色彩冲击
代表作品: Kill la Kill、普罗米亚、天元突破
```

##### 3.2 飞碟社 / 极致光污染 (Ufotable / Extreme Light Pollution)
```yaml
核心特征:
  - 超写实CGI特效与2D完美融合
  - 大规模发光粒子效果
  - 元素光环和能量流动轨迹
  - 电影级光影合成

T0级提示词:
  "Ufotable style, hyper-realistic CGI VFX blending with 2D, 
   massive glowing particle effects, elemental aura, flowing energy trails,
   seamless 2D-3D integration, spectacular visual effects, 
   cinematic lighting and compositing, breathtaking action sequences,
   best quality, ultra-detailed, masterpiece, official art"

适用题材: 战斗、奇幻、超能力、史诗
视觉特点: 华丽特效、光影极致、能量可视化
代表作品: 鬼灭之刃、Fate系列、空之境界
```

##### 3.3 顶级韩漫 / 暗黑大男主 (Korean Webtoon / Dark Protagonist)
```yaml
核心特征:
  - 锐利线条艺术
  - 暗黑阴影光环
  - 压迫性存在感
  - 垂直滚动构图优化

T0级提示词:
  "Korean Webtoon style, Solo Leveling art style, sharp line art, 
   dark shadowy aura, intimidating presence, vertical scroll format,
   high-contrast lighting, dramatic shadows, powerful stance,
   best quality, ultra-detailed, masterpiece, official art, 
   highly detailed eyes, sharp focus"

适用题材: 暗黑奇幻、升级流、复仇、都市异能
视觉特点: 冷峻线条、暗黑氛围、强者威压感
代表作品: 我独自升级、全职猎人、神之塔
```

##### 3.4 90年代复古 / 蒸汽波 (90s Retro / Vaporwave)
```yaml
核心特征:
  - VHS录像带滤镜
  - 柔和粉彩色调
  - 怀旧氛围感
  - CRT显示器扫描线 + 赛璐珞动画美学

T0级提示词:
  "90s retro anime style, VHS filter, muted pastel colors, 
   nostalgic atmosphere, CRT monitor scanlines, cel animation aesthetic,
   vintage anime quality, soft grain texture, retro color palette,
   best quality, masterpiece, official art, nostalgic lighting"

适用题材: 怀旧、青春、都市、科幻复古
视觉特点: 复古滤镜、柔和色彩、怀旧质感
代表作品: 新世纪福音战士、星际牛仔、攻壳机动队
```

##### 3.5 MAPPA / 混沌暴力美学 (MAPPA / Chaotic Violence)
```yaml
核心特征:
  - 电影级鱼眼镜头
  - 素描式线条艺术
  - 混乱动作场面
  - 粗糙质感 + 动态模糊

T0级提示词:
  "MAPPA studio style, cinematic fisheye lens, sketchy line art, 
   chaotic action, gritty texture, dynamic motion blur,
   intense visual impact, dark atmospheric color grading, 
   detailed character portrayal, cinematic storyboarding,
   best quality, ultra-detailed, masterpiece, official art"

适用题材: 暗黑、战斗、悬疑、暴力美学
视觉特点: 粗糙笔触、混乱构图、暴力张力
代表作品: 进击的巨人最终季、咒术回战、电锯人
```

##### 3.6 京阿尼 / 极致微观光影 (Kyoto Animation / Micro Lighting)
```yaml
核心特征:
  - 摄影级光影处理
  - 超精细闪烁眼睛
  - 细腻水面反射
  - 柔和环境光

T0级提示词:
  "Kyoto Animation style, photographic lighting, hyper-detailed sparkling eyes, 
   detailed water reflections, soft ambient light,
   ultra-detailed character animation, subtle facial expressions, 
   realistic daily life atmosphere, delicate color grading,
   best quality, ultra-detailed, masterpiece, official art, 
   highly detailed eyes, detailed hair strands"

适用题材: 日常、青春、情感、治愈
视觉特点: 极致细节、柔和光影、微表情刻画
代表作品: 紫罗兰永恒花园、轻音少女、声之形
```

##### 3.7 吉卜力 / 治愈系手绘 (Studio Ghibli / Healing Hand-drawn)
```yaml
核心特征:
  - 手绘水彩背景
  - 郁郁葱葱的绿色植被
  - 柔和阳光
  - 温暖大地色调 + 奇幻氛围

T0级提示词:
  "Studio Ghibli style, hand-painted watercolor background, lush greenery, 
   soft sunlight, warm earth tones, whimsical atmosphere,
   hand-drawn aesthetic, detailed natural environments, 
   gentle color palette, fantasy elements,
   best quality, ultra-detailed, masterpiece, official art"

适用题材: 奇幻、治愈、冒险、童话
视觉特点: 手绘质感、自然环境、温暖治愈
代表作品: 千与千寻、龙猫、哈尔的移动城堡
```

##### 3.8 新海诚 / 极致环境壁纸 (Makoto Shinkai / Ultimate Environment)
```yaml
核心特征:
  - 令人惊叹的黄昏天空
  - 发光的积雨云
  - 华丽镜头光晕
  - 丁达尔效应 + 超精细城市景观

T0级提示词:
  "Makoto Shinkai style, breathtaking twilight, glowing cumulus clouds, 
   gorgeous lens flare, Tyndall effect, hyper-detailed cityscape,
   photorealistic backgrounds with stylized characters, 
   dramatic volumetric lighting, emotional atmosphere, 
   cinematic composition, soft pastel color palette,
   best quality, ultra-detailed, masterpiece, official art"

适用题材: 青春、爱情、奇幻、都市
视觉特点: 超写实背景、极致光影、情感氛围
代表作品: 你的名字、天气之子、秒速五厘米
```

---

#### 3.9 日本动画界视觉风格体系 (Japanese Animation Visual Style System)

> 完整的日本动画界视觉风格分类体系，涵盖时代、流派、技术流派等多维度分类。

##### 按时代分类

**3.9.1 黄金时代 (1980s-1990s)**
```yaml
核心特征:
  - 赛璐珞手绘质感
  - 厚涂阴影和高光
  - 胶片颗粒感
  - 经典OVA美学

T0级提示词:
  "1980s-1990s classic anime style, cel animation aesthetic, hand-painted cels,
   thick painted shadows and highlights, film grain texture, OVA quality,
   retro color palette, vintage anime atmosphere,
   best quality, masterpiece, official art, nostalgic lighting"

代表作品: 阿基拉、攻壳机动队、新世纪福音战士、星际牛仔
适用题材: 科幻、机甲、赛博朋克、太空歌剧
```

**3.9.2 数字转型期 (2000s-2010s)**
```yaml
核心特征:
  - 数字上色过渡期美学
  - CG与2D混合
  - 清晰锐利的线条
  - 现代动画质感

T0级提示词:
  "2000s-2010s digital anime style, clean digital coloring, CG-2D hybrid,
   sharp crisp linework, modern animation quality, vibrant digital colors,
   detailed shading, contemporary anime aesthetic,
   best quality, ultra-detailed, masterpiece, official art"

代表作品: 死亡笔记、Code Geass、钢之炼金术师、Fate/Zero
适用题材: 悬疑、战略、奇幻、战斗
```

**3.9.3 现代高清时代 (2015s-Present)**
```yaml
核心特征:
  - 4K/8K超高清制作
  - 极致细节渲染
  - 电影级后期处理
  - 混合媒介技术

T0级提示词:
  "Modern high-definition anime style, 4K/8K ultra-HD production,
   extreme detail rendering, cinematic post-processing, mixed media techniques,
   photorealistic textures with stylized characters, advanced digital effects,
   best quality, ultra-detailed, masterpiece, official art, sharp focus"

代表作品: 鬼灭之刃、咒术回战、间谍过家家、葬送的芙莉莲
适用题材: 全题材适用
```

##### 按流派分类

**3.9.4 少年漫改编风格 (Shonen Adaptation Style)**
```yaml
核心特征:
  - 动态战斗作画
  - 夸张表情和动作
  - 鲜艳色彩
  - 热血氛围

T0级提示词:
  "Shonen anime adaptation style, dynamic battle animation, exaggerated expressions,
   vibrant energetic colors, hot-blooded atmosphere, action-packed composition,
   power aura effects, impact frames, speed lines,
   best quality, ultra-detailed, masterpiece, official art, dynamic lighting"

代表作品: 火影忍者、海贼王、我的英雄学院、鬼灭之刃
适用题材: 热血、战斗、冒险、成长
```

**3.9.5 少女漫改编风格 (Shojo Adaptation Style)**
```yaml
核心特征:
  - 柔和梦幻色调
  - 花瓣/星光等装饰效果
  - 细腻情感表达
  - 浪漫氛围

T0级提示词:
  "Shojo anime adaptation style, soft dreamy color palette, floral decorative effects,
   sparkling backgrounds, delicate emotional expressions, romantic atmosphere,
   gentle lighting, beautiful character designs, elegant compositions,
   best quality, ultra-detailed, masterpiece, official art, soft focus"

代表作品: 水果篮子、辉夜大小姐想让我告白、好想告诉你
适用题材: 爱情、校园、情感、治愈
```

**3.9.6 青年漫改编风格 (Seinen Adaptation Style)**
```yaml
核心特征:
  - 写实细腻画风
  - 成熟色调处理
  - 复杂叙事视觉化
  - 深度刻画

T0级提示词:
  "Seinen anime adaptation style, realistic detailed art style, mature color grading,
   complex narrative visualization, deep character portrayal, sophisticated atmosphere,
   subtle lighting, nuanced expressions, adult-oriented aesthetics,
   best quality, ultra-detailed, masterpiece, official art, cinematic quality"

代表作品: 寄生兽、东京食尸鬼、进击的巨人、MONSTER
适用题材: 暗黑、悬疑、心理、成人向
```

##### 按技术流派分类

**3.9.7 Sakuga流派 (作画狂热派)**
```yaml
核心特征:
  - 极致流畅的动作作画
  - 夸张透视和变形
  - 动态线条运用
  - 原画师个人风格强烈

T0级提示词:
  "Sakuga animation style, ultra-fluid motion, exaggerated perspective and deformation,
   dynamic line work, strong animator personality, impressive action sequences,
   detailed frame-by-frame animation, kinetic energy visualization,
   best quality, ultra-detailed, masterpiece, official art, motion blur effects"

代表作品: 一拳超人、灵能百分百、电锯人（战斗场景）
适用题材: 动作、战斗、超能力
特点: 强调动作的流畅性和冲击力
```

**3.9.8 背景美术流派 (Background Art School)**
```yaml
核心特征:
  - 极致精美的背景绘制
  - 写实与风格化结合
  - 环境叙事
  - 氛围营造

T0级提示词:
  "Background art focused anime style, exquisitely detailed backgrounds,
   realistic-stylized hybrid environments, environmental storytelling,
   atmospheric scene composition, painterly background quality,
   photographic lighting on backgrounds, immersive world-building,
   best quality, ultra-detailed, masterpiece, official art"

代表作品: 新海诚作品、吉卜力作品、紫罗兰永恒花园
适用题材: 奇幻、治愈、都市、自然
特点: 背景即叙事
```

**3.9.9 CG融合流派 (CG Integration School)**
```yaml
核心特征:
  - 3D CG与2D手绘无缝融合
  - 复杂机械/建筑CG化
  - 特效粒子系统
  - 混合渲染技术

T0级提示词:
  "CG-2D integration anime style, seamless 3D-2D blending, CG mechanical details,
   particle effect systems, hybrid rendering techniques, photorealistic CG elements,
   hand-drawn character integration, advanced compositing,
   best quality, ultra-detailed, masterpiece, official art, ray tracing"

代表作品: 宝石之国、BEASTARS、电锯人、鬼灭之刃
适用题材: 机甲、科幻、奇幻、现代
特点: 技术与艺术的完美结合
```

##### 按色彩美学分类

**3.9.10 高饱和度流派 (High Saturation School)**
```yaml
核心特征:
  - 极其鲜艳的色彩
  - 强烈对比度
  - 视觉冲击力
  - 能量感

T0级提示词:
  "High saturation anime style, extremely vibrant colors, strong contrast,
   visual impact, energetic color palette, bold color choices,
   eye-catching compositions, vivid atmosphere,
   best quality, ultra-detailed, masterpiece, official art, vibrant colors"

代表作品: JoJo的奇妙冒险、普罗米亚、Kill la Kill
适用题材: 热血、奇幻、超现实
```

**3.9.11 低饱和度/暗黑流派 (Desaturated/Dark School)**
```yaml
核心特征:
  - 低饱和度色调
  - 暗黑压抑氛围
  - 冷色调主导
  - 高对比阴影

T0级提示词:
  "Desaturated dark anime style, low saturation color palette, oppressive atmosphere,
   cold color dominance, high-contrast shadows, gritty texture,
   moody lighting, somber tone, psychological depth,
   best quality, ultra-detailed, masterpiece, official art, dark aesthetic"

代表作品: 东京食尸鬼、进击的巨人、寄生兽、PSYCHO-PASS
适用题材: 暗黑、恐怖、悬疑、心理
```

**3.9.12 柔和粉彩流派 (Soft Pastel School)**
```yaml
核心特征:
  - 柔和粉彩色调
  - 梦幻氛围
  - 过曝高光
  - 治愈感

T0级提示词:
  "Soft pastel anime style, gentle pastel color palette, dreamy atmosphere,
   overexposed highlights, healing aesthetic, soft focus effects,
   warm gentle lighting, comforting visuals, ethereal quality,
   best quality, ultra-detailed, masterpiece, official art, soft lighting"

代表作品: 冰菓、吹响吧！上低音号、紫罗兰永恒花园
适用题材: 日常、治愈、青春、校园
```

##### 按叙事视觉化分类

**3.9.13 心理描写视觉化流派 (Psychological Visualization)**
```yaml
核心特征:
  - 抽象视觉隐喻
  - 超现实画面
  - 象征性构图
  - 意识流表现

T0级提示词:
  "Psychological visualization anime style, abstract visual metaphors,
   surreal imagery, symbolic compositions, stream of consciousness expression,
   mind-bending visuals, psychological depth, artistic interpretation,
   best quality, ultra-detailed, masterpiece, official art, experimental"

代表作品: 新世纪福音战士、少女革命、物语系列
适用题材: 心理、实验、艺术、哲学
```

**3.9.14 极简主义流派 (Minimalist School)**
```yaml
核心特征:
  - 简化线条和色彩
  - 留白运用
  - 符号化设计
  - 克制的视觉语言

T0级提示词:
  "Minimalist anime style, simplified lines and colors, negative space usage,
   symbolic design, restrained visual language, clean compositions,
   essential elements only, elegant simplicity,
   best quality, masterpiece, official art, minimalist aesthetic"

代表作品: 平家物语、乒乓、四叠半神话大系
适用题材: 艺术、实验、文艺、哲学
```

---

#### 4. 概念艺术风格 (Concept Art)

**适用场景**：
- 科幻、奇幻、末世题材
- 需要强烈世界观呈现
- 目标受众：核心向观众

**子选项**：
- **赛博朋克**：`Cyberpunk graphic novel style, neon-lit, high-tech low-life aesthetic`
- **史诗奇幻**：`Epic fantasy concept art, dramatic lighting, grand scale environments`
- **硬表面科幻**：`Hard surface sci-fi illustration, technical blueprint aesthetic`

**关键词库**：
```
concept art, matte painting, digital illustration,
dramatic atmospheric lighting, cinematic composition,
detailed environment design, epic scale
```

---

#### 5. 漫画风格 (Comic/Manga Style)

**适用场景**：
- 快节奏动作题材
- 需要强烈视觉符号化
- 目标受众：漫画读者群体

**子选项**：
- **日式少年漫**：`Shonen manga style, dynamic action lines, bold inking, screentone effects`
- **美式漫画**：`American comic book style, bold colors, halftone dots, dramatic shadows`
- **韩漫风格**：`Korean webtoon style, vertical scroll composition, soft digital coloring`

**关键词库**：
```
manga style, comic book aesthetic, bold inking,
action lines, speed lines, screentone effects,
dramatic panel composition, graphic storytelling
```

---

#### 6. 顶级人物CG质感 (Top-tier Character CG Style)

**适用场景**：
- 角色立绘 / T0 人物定妆照 / 人物特写
- 服化道材质参考 / 妆造参考 / 角色海报
- 需要“真实摄影质感 + 3D角色渲染 + 瓷感皮肤”的高端人物图

**独立风格ID**：`TOP_TIER_CHARACTER_CG`

**来源Skill**：`skills/top-tier-character-cg-skill/SKILL.md`

**子选项**：
- **冷白瓷感棚拍男主**：冷白极简棚拍、黑白强对比、蓝灰黑发高光、瓷感男主皮肤
- **冷瓷民国旗袍棚拍女主**：冷白室内棚拍、冷瓷白肌、黑白蕾丝旗袍、松散盘发碎发、白色毛绒披肩
- **月华银发神女玄幻CG**：深蓝月华逆光、银白长发、瓷白神女肌、红蓝宝石、透明蓝纱与国风刺绣

**关键词库**：
```
top-tier character CG rendering, 2.5D anime-CG hybrid rendering,
realistic photography and 3D character render fusion,
porcelain flawless skin, AI retouched soft-focus skin,
subsurface scattering, satin-like skin highlights,
ultra detailed hair strands, premium character concept portrait,
high-end commercial beauty retouch, clean luxury composition
```

**调用模板**：
```markdown
[风格]顶级人物CG质感
  - 子配方: 冷白瓷感棚拍男主 / 冷瓷民国旗袍棚拍女主 / 月华银发神女玄幻CG
@参考Skill: skills/top-tier-character-cg-skill/SKILL.md
```

**使用限制**：
- 仅用于人物、服化道、妆造、角色特写。
- 不作为场景环境、建筑、道具、空间专用美术风格前缀。
- 场景提示词仍必须使用项目 `assets/visual-style-guide.md` 中的场景专用中文美术风格前缀。

---

## [选择流程]

### 步骤1：分析输入

从导演分析文档中提取：
```yaml
题材类型: [从genre-adaptive-skill获取]
情绪基调: [从导演分析的情绪曲线获取]
目标受众: [从项目定位获取]
核心场景: [从场景清单获取]
```

### 步骤2：推荐风格

基于分析结果，推荐3个风格方案：

```markdown
## 推荐方案

### 方案A - 保守方向
- **艺术风格**: [风格名称]
- **推荐理由**: [基于题材/受众/场景的匹配度]
- **参考作品**: [具体作品名称]
- **风险等级**: 低

### 方案B - 平衡方向
- **艺术风格**: [风格名称]
- **推荐理由**: [基于题材/受众/场景的匹配度]
- **参考作品**: [具体作品名称]
- **风险等级**: 中

### 方案C - 突破方向
- **艺术风格**: [风格名称]
- **推荐理由**: [基于题材/受众/场景的匹配度]
- **参考作品**: [具体作品名称]
- **风险等级**: 高
```

### 步骤3：用户选择

通过交互式问答确认：
1. 选择方案（A/B/C）
2. 如选择动漫电影风格，进一步选择具体工作室风格
3. 确认是否需要混搭风格（如：新海诚背景 + 扳机社人物）

### 步骤4：输出规范文档

生成 `assets/visual-style-guide.md`：

```markdown
# 视觉风格规范 - [项目名]

## 选定风格

**主风格**: [风格名称]
**子风格**: [具体工作室/流派]
**参考作品**: [作品列表]

## 核心提示词

### 全局风格前缀
```
[完整的风格提示词模板]
```

### 色彩规范
- 主色调: [色彩描述 + Hex色号]
- 辅助色: [色彩描述 + Hex色号]
- 强调色: [色彩描述 + Hex色号]

### 光影规范
- 主光源: [方向/色温/强度]
- 氛围光: [描述]
- 特效光: [描述]

### 镜头规范
- 常用焦段: [焦段列表]
- 景深处理: [浅景深/深景深]
- 运镜风格: [描述]

## 应用指南

### 角色设计
- [具体应用要点]

### 场景设计
- [具体应用要点]

### 道具设计
- [具体应用要点]

### 分镜编写
- [具体应用要点]
```

---

## [风格混搭指南]

### 混搭基本原则

**三大黄金法则**：
1. **主次分明**：必须有一个主导风格（占比60-70%）+ 一个辅助风格（占比30-40%）
2. **元素分离**：不同风格应用于不同元素（如：背景vs人物、静态vs动态）
3. **基调统一**：混搭风格的色调、光影、情绪必须协调一致

### 混搭组合矩阵

#### 推荐混搭组合（兼容性高）

| 主风格 | 辅助风格 | 应用方式 | 适用题材 | 效果 |
|-------|---------|---------|---------|------|
| 新海诚 | 京阿尼 | 背景用新海诚，人物用京阿尼 | 青春爱情、校园 | 唯美细腻 |
| 吉卜力 | 柔和粉彩 | 吉卜力手绘质感+粉彩色调 | 治愈、童话 | 温暖梦幻 |
| 扳机社 | 高饱和度 | 扳机社动作+高饱和色彩 | 热血、机甲 | 极致冲击 |
| MAPPA | 低饱和度暗黑 | MAPPA分镜+暗黑色调 | 悬疑、战斗 | 压抑紧张 |
| 飞碟社 | CG融合 | 飞碟社特效+CG技术 | 奇幻、超能力 | 华丽震撼 |
| 新海诚 | 背景美术 | 双重强化背景表现力 | 都市、自然 | 极致环境 |
| 韩漫 | 少年漫 | 韩漫线条+少年漫动作 | 升级流、战斗 | 锐利爽快 |
| Sakuga | 扳机社 | Sakuga流畅+扳机社夸张 | 动作、格斗 | 动作极致 |
| 京阿尼 | 少女漫 | 京阿尼细腻+少女漫装饰 | 爱情、日常 | 精致浪漫 |
| 90年代复古 | 蒸汽波 | 复古滤镜+蒸汽波色彩 | 科幻复古 | 怀旧未来 |

#### 谨慎混搭组合（需要技巧）

| 主风格 | 辅助风格 | 潜在冲突 | 解决方案 | 适用场景 |
|-------|---------|---------|---------|---------|
| 吉卜力 | MAPPA | 温暖vs暗黑冲突 | 用吉卜力环境+MAPPA人物刻画 | 暗黑童话 |
| 新海诚 | 扳机社 | 写实vs夸张冲突 | 背景写实+动作夸张分离 | 都市超能力 |
| 极简主义 | 高饱和度 | 克制vs强烈冲突 | 极简构图+局部高饱和 | 艺术实验 |
| 写实 | 风格化 | 真实vs抽象冲突 | 场景写实+人物风格化 | 现代奇幻 |
| 心理视觉化 | 少年漫 | 抽象vs直白冲突 | 现实用少年漫+心理用抽象 | 心理战斗 |

#### 禁止混搭组合（兼容性差）

| 风格A | 风格B | 冲突原因 | 替代方案 |
|------|------|---------|---------|
| 吉卜力 | 韩漫 | 手绘温暖vs锐利暗黑完全对立 | 选择其一或用过渡风格 |
| 极简主义 | 飞碟社 | 克制简约vs华丽特效完全矛盾 | 选择其一 |
| 90年代复古 | 现代高清 | 技术时代冲突 | 选择其一或用数字转型期 |
| 柔和粉彩 | 低饱和度暗黑 | 色彩情绪完全相反 | 选择其一 |

### 混搭应用场景

#### 场景1：背景与人物分离

**最常用的混搭方式**

```yaml
配置:
  背景风格: 新海诚/吉卜力/背景美术流派
  人物风格: 京阿尼/少女漫/少年漫
  
优势:
  - 背景极致精美
  - 人物表现力强
  - 互不干扰
  
注意事项:
  - 光影方向必须统一
  - 色调必须协调
  - 人物不能过于风格化导致违和
```

#### 场景2：静态与动态分离

**适合动作戏的混搭方式**

```yaml
配置:
  静态场景: 京阿尼/柔和粉彩/数字转型期
  动作场景: Sakuga/扳机社/飞碟社
  
优势:
  - 日常细腻
  - 战斗爆发
  - 对比强烈
  
注意事项:
  - 转换要自然
  - 不能割裂感太强
  - 保持角色一致性
```

#### 场景3：现实与心理分离

**适合心理题材的混搭方式**

```yaml
配置:
  现实世界: 写实/数字转型期/青年漫
  心理世界: 心理视觉化/极简主义/抽象
  
优势:
  - 现实可信
  - 心理震撼
  - 叙事层次丰富
  
注意事项:
  - 明确区分两个世界
  - 转换要有视觉标识
  - 心理世界不能过于晦涩
```

#### 场景4：色彩分级混搭

**通过色彩统一不同风格**

```yaml
配置:
  主风格: 任意风格
  色彩分级: 统一的色彩滤镜
  
示例组合:
  - 扳机社动作 + 青橙色调 = 电影感热血
  - MAPPA暗黑 + 冷蓝色调 = 极致压抑
  - 新海诚背景 + 暖黄色调 = 怀旧温暖
  
优势:
  - 色彩统一化解风格冲突
  - 增强情绪表达
  - 提升整体质感
```

### 混搭实战案例

#### 案例1：青春爱情短剧

```yaml
题材: 校园青春爱情
目标: 唯美细腻、情感充沛

混搭方案:
  主风格: 新海诚（60%）
    - 应用于: 所有背景、环境、天空
    - 特点: 超写实背景、极致光影、黄昏氛围
  
  辅助风格: 京阿尼（40%）
    - 应用于: 人物作画、表情细节、日常场景
    - 特点: 细腻微表情、柔和光影、真实感
  
  统一元素:
    - 色调: 柔和粉彩+暖黄
    - 光影: 统一的柔和自然光
    - 情绪: 温暖、治愈、浪漫

提示词整合:
  "Makoto Shinkai style backgrounds with Kyoto Animation character animation,
   breathtaking twilight sky, hyper-detailed cityscape, soft pastel color palette,
   photographic lighting, hyper-detailed sparkling eyes, subtle facial expressions,
   gentle warm lighting, romantic atmosphere, emotional depth,
   best quality, ultra-detailed, masterpiece, official art"
```

#### 案例2：暗黑战斗短剧

```yaml
题材: 暗黑奇幻战斗
目标: 压抑紧张、视觉冲击

混搭方案:
  主风格: MAPPA暗黑美学（70%）
    - 应用于: 整体氛围、色调、分镜
    - 特点: 鱼眼镜头、素描线条、暗黑色调
  
  辅助风格: 飞碟社特效（30%）
    - 应用于: 战斗场景、能量特效
    - 特点: 粒子效果、发光光环、华丽特效
  
  统一元素:
    - 色调: 低饱和度+冷蓝+暗红
    - 光影: 高对比阴影、戏剧性光源
    - 情绪: 压抑、暴力、震撼

提示词整合:
  "MAPPA studio style with Ufotable VFX elements, cinematic fisheye lens,
   sketchy line art, dark atmospheric color grading, gritty texture,
   massive glowing particle effects during battle scenes, elemental aura,
   high-contrast shadows, oppressive atmosphere, intense visual impact,
   best quality, ultra-detailed, masterpiece, official art"
```

#### 案例3：治愈日常短剧

```yaml
题材: 日常治愈
目标: 温暖舒适、细节丰富

混搭方案:
  主风格: 吉卜力（50%）
    - 应用于: 自然环境、整体氛围
    - 特点: 手绘水彩、郁郁葱葱、温暖色调
  
  辅助风格: 柔和粉彩流派（50%）
    - 应用于: 色彩分级、光影处理
    - 特点: 粉彩色调、过曝高光、梦幻感
  
  统一元素:
    - 色调: 温暖粉彩+大地色
    - 光影: 柔和阳光、漫反射
    - 情绪: 治愈、温暖、安心

提示词整合:
  "Studio Ghibli style with soft pastel color grading,
   hand-painted watercolor background, lush greenery, soft sunlight,
   gentle pastel color palette, dreamy atmosphere, overexposed highlights,
   warm earth tones, healing aesthetic, whimsical atmosphere,
   best quality, ultra-detailed, masterpiece, official art"
```

### 混搭检查清单

在确定混搭方案前，检查以下项：

- [ ] 主次风格比例明确（60/40或70/30）
- [ ] 应用元素清晰分离（背景/人物、静态/动态等）
- [ ] 色调基调统一协调
- [ ] 光影方向和强度一致
- [ ] 情绪表达不冲突
- [ ] 没有使用禁止混搭组合
- [ ] 提示词整合后逻辑通顺
- [ ] 参考作品风格可验证

---

## [质量检查清单]

选定风格后，检查以下项：

- ☐ 风格与题材类型匹配
- ☐ 风格与情绪基调一致
- ☐ 风格与目标受众契合
- ☐ 风格与核心场景适配
- ☐ 提示词库完整可执行
- ☐ 色彩/光影/镜头规范明确
- ☐ 输出文档格式规范

---

## [常见问题]

**Q: 如何选择动画工作室风格？**
A: 
1. 看题材：青春爱情→新海诚/京阿尼，热血动作→扳机社/骨头社
2. 看情绪：治愈温暖→吉卜力，暗黑压抑→MAPPA
3. 看受众：大众向→吉卜力/新海诚，核心向→扳机社/ufotable

**Q: 可以混搭多个工作室风格吗？**
A: 可以，但需要：
1. 明确主次（一个主风格 + 一个辅助风格）
2. 确保不冲突（如：新海诚背景 + 京阿尼人物 ✓，吉卜力 + MAPPA ✗）
3. 统一光影和色调基调

**Q: 写实风格和动漫风格可以混搭吗？**
A: 可以，常见组合：
- 写实背景 + 风格化人物（如新海诚）
- 写实材质 + 卡通比例（如皮克斯）

---

## [扩展资源（电影摄影三件套，风格参数查阅时按需参考）]

| 需求 | 查阅文件 |
|------|---------|
| 按风格类型/场景类型检索代表作视觉参数 | `resources/电影摄影-40+代表作视觉分析.md`（40+部电影按8类场景分类，含色温/光比/调色风格/构图特征） |
| 色彩叙事/调色风格参考，辅助色彩基调选择 | `resources/电影摄影-主文件(技法+设备+工作流程).md`（技法七：色彩叙事 + 高级专题：调色风格） |

---

## [版本信息]

- **版本**: 1.0
- **创建日期**: 2026-03-18
- **适配模型**: Gemini Nano-Banana系列、Seedance 2.0、Kling 3.0
- **覆盖风格**: 5大类 + 8个动画工作室风格


[🔐 全文读取确认码 — 仅全文阅读至此处方可获得]

    你已读完 visual-style-selector-skill/SKILL.md 全文（1071行）。

    **强制操作**：在你输出的"📊 Skill 合规审计报告"中，必须包含以下完整字符串（逐字复制，不得修改）：

    ```
    ✅ VISUAL-STYLE-SELECTOR-SKILL 全文读取确认：STYLE-SELECTOR-CERTIFIED-风格预设库已激活-色彩基调已加载
    ```

    ❌ 审计报告中缺少此确认码 → 判定为未完整读取 visual-style-selector-skill/SKILL.md → 视觉风格选择技能输出直接不合格
