---
name: top-tier-character-cg-skill
description: 顶级人物CG质感风格技能。定义 2.5D 动漫-CG 融合渲染的人物专用美术风格体系，涵盖皮肤质感（SSS/瓷肌/高光泽）、打光规范、材质渲染、色彩体系及完整中英文提示词前缀，并内置冷白棚拍男主、冷瓷旗袍女主、月华银发神女等可直接复制的复刻配方，适用于任何项目的角色立绘/设计稿/特写画面。
---

# 顶级人物CG质感风格技能（Top-tier Character CG Style）

[技能定位]
本技能定义一套**项目无关**的人物渲染风格标准——2.5D 动漫-CG 融合（Anime-CG Hybrid），可被任何 AXIS 项目的角色设计阶段引用。核心目标是在 AI 生图场景下稳定复现「顶级手游立绘 / 商业杂志封面级」人物质感。

> **与其他技能的关系**：
> - **art-design-skill**：负责角色设计方法论（铁律/流程/模板），本技能负责**渲染风格**
> - **aesthetic-vision-skill**：负责审美意图声明，本技能负责**技术参数落地**
> - **film-lighting-technique-skill**：负责场景光影语言，本技能负责**人物专属打光**
>
> **🔴 触发与路由（2026-05-30 补强）**：由 `visual-style-selector-skill` 选中「顶级人物 CG / 第6类」风格时注入本风格层；🔴 仅用于角色独立立绘 / T0 立绘 / 角色特写分镜，**禁止用于 `scene-prompts.md` 环境条目**；与 `art-design-skill` 女性设计铁律叠加时，本技能为「技术落地层（材质/打光/参数）」、art-design 为「设计语义层（记忆点/叙事）」，二者叠加不互相覆盖。

---

## 一、风格总论

| 维度 | 规格 |
|------|------|
| **渲染流派** | 2.5D 动漫-CG 融合（Anime-CG Hybrid），非纯 2D 平涂、非纯 3D 写实 |
| **质感基调** | High-Gloss 高光泽糖果流行美学，表面材质介于瓷器与塑胶之间 |
| **对标品质** | 顶级手游角色立绘（崩坏:星穹铁道/原神/明日方舟）/ 商业杂志封面级 AI 插画 |
| **打光范式** | 高调（High-Key）摄影棚光，纯白或极浅纯色背景，主光源从右上方 45° 入射 |
| **阴影特征** | 柔和边缘、大面积过渡、暗部偏冷偏紫，投影落在背景上而非角色身上 |
| **适用场景** | 角色设计稿 / T0立绘 / 角色特写分镜 / 商业宣传物料 / IP 形象定稿 |

---

## 二、皮肤质感深度规范

> 🔴 **核心定义**：瓷白高光泽 SSS 皮肤——零瑕疵、强散射、柔过渡、暖关节。

| 参数 | 规格 | 说明 |
|------|------|------|
| **次表面散射 (SSS)** | 强制开启 | 肩部、锁骨、手指关节、耳廓处必须透出粉色/珊瑚色血色 |
| **镜面高光** | 肩头/前臂/锁骨线/鼻尖/下唇 | 极亮白色高光条带，模拟高光泽润肤效果 |
| **瑕疵度** | 零毛孔、零痣、零纹理 | 纯净瓷娃娃感，但保留微妙的冷暖色彩渐变 |
| **关节过渡** | 关节区域偏暖粉红 | 指关节、肘部、膝盖处自然泛红 |
| **明暗交界** | 极其柔和 | 大面积柔光过渡，禁止硬阴影切割面部/身体 |
| **肤色色值范围** | `#FDE8D8` ~ `#F5C6AA` | 瓷白暖粉底色，禁止偏黄偏灰 |

### 皮肤质感提示词

**英文**：
```
porcelain-smooth luminous skin, flawless complexion with zero pores and zero blemishes,
visible subsurface scattering on shoulders collarbones and ear tips,
glossy specular skin highlights on nose bridge and lower lip,
warm pink undertone at finger joints elbows and knees,
ultra-soft shadow transitions, no hard shadow edges on skin,
anime-CG hybrid skin rendering, doll-like pristine clarity with subtle warm-cool color gradients
```

**中文**：
```
瓷白光泽感皮肤，零瑕疵零毛孔无斑无痣，
肩部锁骨耳尖处可见次表面散射透粉效果，
鼻梁与下唇镜面高光，
指关节肘部膝盖处自然偏暖粉红，
明暗过渡极其柔和无硬阴影切割，
2.5D动漫CG融合皮肤渲染，瓷娃娃般纯净感融合微妙冷暖色彩渐变
```

---

## 三、打光与背景规范

| 参数 | 规格 |
|------|------|
| **背景** | 纯白 `#FFFFFF` 或极浅纯色，禁止复杂环境（场景内使用时可替换） |
| **主光源** | 右上方 45° 柔光，色温 5500-6000K（偏自然白） |
| **补光** | 左侧低强度冷色补光，填充阴影但不消除 |
| **投影** | 角色右侧/右下方落一道柔和灰色投影在背景上 |
| **光比** | 主补光比 2:1 ~ 3:1（中等对比，不追求戏剧性） |
| **镜面高光** | 材质表面（PVC/漆皮/金属饰品）必须有明亮镜面反射 |

### 打光提示词

**英文**：
```
clean white background, soft shadow cast to the right,
high-key studio lighting from upper right at 45 degrees,
natural white color temperature (5500K), subtle cool fill light from left,
strong specular highlights on glossy materials and metallic accessories,
soft diffused light wrap around figure
```

**中文**：
```
纯白色背景，右侧柔和投影，
右上方45度高调摄影棚柔光，自然白色温（5500K），
左侧低强度冷色补光，
光泽材质与金属饰品上强烈镜面高光反射，
柔和散射光包裹人物轮廓
```

---

## 四、材质与服饰渲染规范

| 材质类型 | 渲染要求 | 提示词 |
|---------|---------|--------|
| **PVC / 乙烯基 / 漆皮** | 湿润感镜面反射，表面可见环境映射 | `wet-look glossy PVC with mirror reflection` |
| **丹宁牛仔** | 可见织纹，浅水洗褪色感，纽扣/拉链金属细节 | `light-wash denim with visible weave texture` |
| **金属饰品** | 高精度 PBR 金属渲染，宝石折射光 | `ornate gold jewelry with gemstone refraction, PBR metallic rendering` |
| **丝绸 / 缎面** | 柔光漫反射，色彩随褶皱渐变 | `silk satin with soft gradient folds` |
| **皮革** | 半哑光质感，边缘微磨损 | `semi-matte leather with edge wear detail` |
| **薄纱 / 蕾丝** | 半透明层叠，边缘柔焦 | `sheer layered fabric with soft-focus edges` |
| **毛绒 / 针织** | 纤维立体可见，柔和漫反射 | `visible fiber texture, soft diffuse reflection` |

---

## 五、色彩体系特征

| 特征 | 规格 |
|------|------|
| **饱和度** | 极高（80-100%），糖果色系优先 |
| **对比策略** | 高彩度互补色搭配（如青蓝发 × 柠檬黄服装） |
| **瞳色** | 必须为非自然色（琥珀金、宝石红、冰蓝、翡翠绿等） |
| **唇色** | 水光珊瑚红/玫瑰红，镜面光泽感 |
| **眼妆** | 暖桃/珊瑚色眼影 + 下睫毛区域泛红晕（营造日系病娇/人偶感） |
| **发色** | 鼓励高饱和非自然色（青蓝、粉紫、银白、樱粉、渐变等） |
| **整体色调** | 明快、干净、高亮度，禁止灰蒙蒙或脏色调 |

### 推荐色彩搭配方案

| 方案名 | 发色 | 服装主色 | 配饰色 | 情绪 |
|--------|------|---------|--------|------|
| 海洋糖果 | 青蓝 `#00D4FF` | 柠檬黄 `#FFE600` | 金 `#FFD700` | 活力·甜酷 |
| 暗夜玫瑰 | 银紫 `#C8A2C8` | 黑漆皮 `#1A1A1A` | 玫红 `#FF007F` | 暗黑·华丽 |
| 樱雪仙子 | 樱粉 `#FFB7C5` | 白缎 `#FFFAF0` | 银 `#C0C0C0` | 纯洁·梦幻 |
| 翡翠战姬 | 翡翠绿 `#50C878` | 深黑金 `#2D2D2D` | 金 `#FFD700` | 力量·高贵 |

---

## 六、完整风格前缀（可直接注入提示词开头）

### 英文完整前缀

```
2.5D anime-CG hybrid rendering, semi-realistic anime illustration,
top-tier gacha game character art quality, cel-shading blended with 3D volumetric lighting,
high-gloss candy-pop aesthetic, porcelain-smooth luminous skin with subsurface scattering,
clean white background, high-key studio lighting, strong specular highlights,
extremely detailed, 8K resolution, masterpiece, best quality
```

### 中文完整前缀

```
2.5D动漫CG融合渲染风格，半写实日系插画，
顶级手游角色立绘品质，赛璐珞着色融合三维体积光，
高光泽糖果流行美学，瓷白光泽皮肤带次表面散射，
纯白背景，高调摄影棚布光，强烈镜面高光，
超精细，8K画质，杰作级品质
```

### 推荐负面提示词

```
realistic photo, low quality, blurry, deformed hands, extra fingers,
visible pores, rough skin texture, wrinkles, moles, freckles,
dark background, complex background, low contrast, flat lighting,
sketchy lineart, rough brushstrokes, watermark
```

---

## 七、冷白瓷感棚拍男主复刻配方（可直接复制）

> **适用目标**：复现「冷白极简棚拍 + 瓷感无毛孔皮肤 + 黑白强对比 + 蓝灰黑发高光 + 超写实CG漫剧男主定妆照」这一类高端 AI 角色肖像风格。

### 风格核心参数

| 维度 | 规格 |
|------|------|
| **画面类型** | 超写实 CG 漫剧男主定妆照 / 商业精修棚拍肖像 |
| **色彩基调** | 高明度冷白色调、低饱和、黑白极简、轻微过曝背景 |
| **皮肤质感** | 冷粉白肤色、瓷感冷白皮肤、AI 精修无毛孔、柔焦磨皮、丝缎柔光反射 |
| **光影结构** | 大型柔光箱从左前上方打光，面部阴影极软，右侧脸部轻微冷灰紫柔影塑形 |
| **头发质感** | 黑色蓬松中长发，空气感层次，蓝灰色冷光高光，银灰色发丝反射 |
| **服装造型** | 黑色修身西装外套 + 白色衬衫微敞领口，强化黑白强对比 |
| **背景** | 纯白摄影棚背景，轻微过曝，禁止复杂环境 |

### 中文一键复制正向提示词

```
超写实CG漫剧男主定妆照，年轻亚洲男性，冷感贵公子气质，清冷疏离表情，半身肖像，人物居中构图，正面微微三分之二角度，眼神平静直视镜头，窄长精致脸型，流畅清晰下颌线，修长脖颈，高挺笔直鼻梁，细长眉眼，淡粉色薄唇，冷粉白肤色，瓷感冷白皮肤，AI精修肌肤，几乎无毛孔，无瑕疵皮肤，柔焦磨皮质感，丝缎般柔和皮肤反光，轻微次表面散射，鼻梁有柔和高光，脸颊有柔和高光，眼周带极淡粉色血色，嘴唇带自然淡粉血色，黑色蓬松中长发，发量厚，空气感层次发型，额前自然碎刘海，刘海轻微遮住额头，鬓角有细碎发丝，两侧头发自然蓬开，发尾微微外翘，黑发带蓝灰色冷光高光，银灰色发丝反射，湿润丝滑发丝质感，穿黑色修身西装外套，白色衬衫，衬衫领口微微敞开，黑白极简造型，纯白摄影棚背景，背景轻微过曝，高明度冷白色调，低饱和色彩，强烈黑白对比，冷灰紫柔和阴影，大型柔光箱从左前上方打光，高调棚拍光影，面部阴影极软，右侧脸部轻微灰影塑形，下颌和脖颈有细腻阴影，商业精修写真质感，高级人像摄影质感，3D角色渲染质感，真实摄影与CG融合，高清细节，干净画面，高级感，顶级AI角色肖像，精致五官，面部比例协调，皮肤通透，头发细节清晰，西装面料自然，画面干净无杂物
```

### 中文一键复制负面提示词

```
低质量，低清晰度，模糊，噪点，颗粒感，jpeg压缩痕迹，过度锐化，画面脏，背景脏，复杂背景，彩色背景，灰暗背景，暖色背景，黄色灯光，橙色灯光，暖色调过重，强烈硬阴影，脸部阴影过重，脸部脏灰，皮肤粗糙，真实毛孔明显，毛孔粗大，痘痘，痘印，雀斑，斑点，皱纹，黑眼圈，油腻皮肤，出汗，胡茬，胡子，络腮胡，老年感，疲惫感，肤色发黄，肤色暗沉，脸部变形，五官不对称，眼睛变形，斗鸡眼，眼距错误，鼻子歪斜，嘴巴畸形，嘴唇过厚，张嘴，露齿，牙齿，宽脸，圆脸，方脸，下巴过宽，脖子过短，身体比例错误，肩膀畸形，手，手指，多余手指，头发结块，塑料头发，棕色头发，黄色头发，发型杂乱肮脏，西装变形，衣领错误，纽扣错误，衣服脏，文字，水印，logo，签名，AI生成字样，多人，女性，儿童，老人，夸张动漫风，二次元插画风，厚涂风，油画风，卡通风
```

### SDXL / LibLib / ComfyUI 英文正向提示词

```
masterpiece, best quality, ultra detailed, ultra realistic, realistic CG render, high-end AI portrait, premium character concept photo, young East Asian male, cold noble male lead, elegant aloof expression, calm distant eyes, half body portrait, centered composition, slight front three-quarter view, looking directly at camera, narrow elegant face, refined jawline, long graceful neck, high straight nose bridge, slender sharp eyes, pale pink thin lips, cold pink-white skin tone, porcelain pale skin, flawless AI retouched skin, almost invisible pores, perfect smooth skin, soft beauty retouching, satin-like soft skin reflection, subtle subsurface scattering, gentle highlights on nose bridge, soft highlights on cheekbones, faint pink blood tone around eyes and lips, delicate clean facial structure, refined facial proportions, voluminous black medium-length hair, thick airy layered hairstyle, natural messy bangs falling over forehead, fine sideburn hair strands, slightly lifted hair on both sides, slightly flipped hair ends, black hair with blue-gray cool highlights, silver-gray hair reflections, silky moist hair texture, clear individual hair strands, black tailored suit jacket, white dress shirt with slightly open collar, minimalist black and white styling, clean luxury fashion, natural suit fabric, neat collar, pure white studio background, slightly overexposed white background, high-key cool white color grading, low saturation, strong black and white contrast, cool gray-purple soft shadows, large softbox lighting from upper front left, high-key studio portrait lighting, extremely soft facial shadows, subtle gray shading on right side of face, delicate jaw and neck shadows, soft diffused glow, polished commercial beauty portrait, realistic 3D character rendering, hybrid realistic photography and CG render, ultra clean image, premium AI male character portrait, high definition, sharp facial details, clean composition, no clutter
```

### SDXL / LibLib / ComfyUI 英文负面提示词

```
worst quality, low quality, normal quality, lowres, blurry, noise, grain, jpeg artifacts, over sharpened, dirty image, dirty background, complex background, colorful background, gray background, warm background, yellow lighting, orange lighting, overly warm tone, harsh shadows, hard facial shadows, dirty facial shadows, rough skin, visible pores, large pores, acne, acne scars, freckles, blemishes, wrinkles, dark circles, oily skin, sweaty skin, beard, mustache, stubble, old face, tired face, yellow skin, dull skin tone, deformed face, asymmetrical face, distorted eyes, crossed eyes, wrong eye distance, crooked nose, malformed mouth, thick lips, open mouth, teeth, wide face, round face, square face, wide chin, short neck, bad anatomy, bad body proportions, deformed shoulders, hands, fingers, extra fingers, clumpy hair, plastic hair, brown hair, yellow hair, dirty messy hair, distorted suit, wrong collar, wrong buttons, dirty clothes, text, watermark, logo, signature, AI generated text, multiple people, female, child, old man, anime style, illustration style, painterly style, oil painting, cartoon style
```

### 权重核心版

```
(超写实CG漫剧男主定妆照:1.5), (冷感贵公子气质:1.35), (瓷感冷白皮肤:1.6), (AI精修无毛孔肌肤:1.45), (柔焦磨皮质感:1.35), (丝缎般柔和皮肤反光:1.35), (冷粉白肤色:1.45), (黑色蓬松中长发:1.45), (空气感层次发型:1.35), (黑发带蓝灰色冷光高光:1.45), (银灰色发丝反射:1.35), (黑色修身西装外套:1.3), (白色衬衫微微敞开领口:1.25), (黑白极简造型:1.4), (纯白摄影棚背景:1.55), (背景轻微过曝:1.35), (高明度冷白色调:1.45), (低饱和色彩:1.35), (强烈黑白对比:1.35), (冷灰紫柔和阴影:1.25), (大型柔光箱从左前上方打光:1.45), (面部阴影极软:1.35), (真实摄影与3D角色渲染融合:1.45)
```

### 推荐生成参数

| 参数 | 推荐值 |
|------|--------|
| **尺寸** | `1024x1024` / `832x1216` |
| **采样器** | `DPM++ 2M Karras` |
| **步数** | `30-40` |
| **CFG** | `5.5-7` |
| **高清修复** | `1.5x-2x` |
| **高清修复去噪** | `0.25-0.4` |
| **脸部修复** | 轻度 |

### 使用铁律

- [ ] 必须保留「冷白色调、纯白棚拍、黑白强对比」三件套。
- [ ] 必须保留「瓷感冷白皮肤、无毛孔、柔焦磨皮、丝缎反光」皮肤组。
- [ ] 必须保留「黑发、蓝灰冷光高光、银灰发丝反射」头发组。
- [ ] 禁止加入暖阳、金色光、胶片黄、复杂背景，否则会破坏原图冷白高级感。
- [ ] 禁止强调真实毛孔、纪实摄影、粗糙皮肤，否则会偏离 AI 精修 CG 质感。

---

## 八、冷瓷民国旗袍棚拍女主复刻配方（可直接复制）

> **适用目标**：复现「冷白室内棚拍 + 瓷感少女肌 + 黑白蕾丝旗袍 + 松散盘发碎发 + 白色毛绒披肩」这一类高端 AI 漫剧女主肖像风格。

### 图像风格深度拆解

| 维度 | 规格 |
|------|------|
| **画面类型** | 超写实 CG 漫剧女主半身肖像 / 冷白室内人像写真 / 民国旗袍氛围定妆照 |
| **色彩基调** | 冷白、浅灰蓝、低饱和青灰背景、黑白蕾丝强对比，整体干净通透 |
| **皮肤质感** | 冷瓷白肌、无毛孔、柔焦磨皮、轻微透粉血色、鼻梁与肩头有湿润柔光高光 |
| **光影结构** | 窗边冷调自然光 + 柔光箱补光，面部亮区清透，暗部偏青灰蓝，发丝有冷白边缘光 |
| **妆容特征** | 水润杏眼、纤长睫毛、淡桃粉眼周、玻璃感红豆沙唇釉、妆面干净不厚重 |
| **头发质感** | 黑色松散低盘发，脸侧碎发自然垂落，单缕发丝跨过面部，黑色缎带发饰 |
| **服装材质** | 白色半透明蕾丝旗袍，黑色花纹刺绣与黑色滚边，黑色盘扣，白色毛绒披肩 |
| **背景** | 室内虚化背景，青灰墙面与淡雅花卉画作，浅景深，不抢人物主体 |

### 中文一键复制正向提示词

```
超写实CG漫剧女主定妆照，成年年轻亚洲女性，冷瓷旗袍美人，清冷温柔气质，半身肖像，竖构图，人物居中偏近景，头部微微倾斜，眼神安静直视镜头，精致鹅蛋脸，小巧下颌，修长脖颈，水润杏眼，纤长睫毛，淡桃粉眼周，鼻梁挺秀，鼻尖有柔和高光，玻璃感红豆沙唇釉，嘴唇水润微张，冷瓷白皮肤，瓷感无毛孔肌肤，AI精修柔焦皮肤，皮肤通透细腻，无瑕疵，无斑点，无粗糙纹理，脸颊带极淡粉色血色，肩头和锁骨有柔和丝缎高光，轻微次表面散射，黑色松散低盘发，发丝自然凌乱但精致，脸侧有细碎发丝垂落，一缕发丝轻轻掠过面部，黑色缎带发饰，发丝带冷白蓝灰高光，穿白色半透明蕾丝旗袍，黑色花纹刺绣，黑色滚边，黑色中式盘扣，蕾丝织纹清晰，服装半透明层次细腻，披白色毛绒披肩，毛绒纤维柔软蓬松，手指轻放胸前，长款淡粉色水晶美甲，手部精致自然，冷白室内棚拍光影，窗边冷调自然光，大型柔光箱补光，面部光线清透柔和，暗部偏青灰蓝，头发边缘有冷白轮廓光，背景为虚化室内青灰墙面和淡雅花卉画作，浅景深，背景柔和虚化，高明度冷白色调，低饱和色彩，黑白蕾丝强对比，画面干净通透，高级商业写真质感，真实摄影与3D角色渲染融合，顶级AI角色肖像，高清细节，皮肤光泽自然，发丝细节清晰，服装蕾丝材质精细
```

### 中文一键复制负面提示词

```
低质量，低清晰度，模糊，噪点，颗粒感，jpeg压缩痕迹，画面脏，背景杂乱，背景过清晰，复杂背景，强烈暖黄光，橙色灯光，脏灰皮肤，粗糙皮肤，真实毛孔明显，毛孔粗大，痘痘，痘印，雀斑，斑点，皱纹，黑眼圈，油腻皮肤，过度磨皮成塑料，肤色发黄，肤色暗沉，脸部变形，五官不对称，眼睛变形，斗鸡眼，眼距错误，鼻子歪斜，嘴巴畸形，牙齿外露，厚嘴唇，浓妆艳抹，欧美浓妆，烟熏妆，表情夸张，宽脸，方脸，短脖子，身体比例错误，肩膀畸形，手部畸形，手指畸形，多余手指，缺失手指，美甲变形，头发结块，塑料头发，发丝糊成一团，衣服变形，旗袍结构错误，蕾丝纹理混乱，盘扣错误，毛绒脏乱，文字，水印，logo，签名，AI生成字样，多人，儿童，老人，男性，暴露过度，低俗姿势，二次元平涂，厚涂插画，卡通风，油画风
```

### SDXL / LibLib / ComfyUI 英文正向提示词

```
masterpiece, best quality, ultra detailed, ultra realistic CG portrait, high-end AI female character portrait, adult young East Asian woman, cold porcelain qipao beauty, gentle aloof expression, half body portrait, vertical composition, centered close-up, slight head tilt, looking directly at camera, elegant oval face, small refined chin, long graceful neck, watery almond eyes, long delicate eyelashes, soft peach-pink eye makeup, straight delicate nose, soft highlight on nose tip, glossy rose bean lip tint, moist slightly parted lips, cold porcelain white skin, flawless poreless skin, AI retouched soft-focus skin, translucent delicate complexion, no blemishes, faint pink blood tone on cheeks, satin soft highlights on shoulder and collarbone, subtle subsurface scattering, loose black low bun hairstyle, refined natural messy hair strands, fine loose strands falling beside face, one thin hair strand crossing the face, black satin ribbon hair accessory, black hair with cool white and blue-gray highlights, white semi-transparent lace qipao, black floral embroidery, black piping, black Chinese frog buttons, clear lace texture, delicate translucent fabric layers, white fluffy fur shawl, soft visible fur fibers, hand gently placed near chest, long pale pink crystal manicure, elegant natural hands, cool white indoor studio lighting, cool daylight from window, large softbox fill light, clean translucent facial lighting, cyan-gray blue shadows, cool white rim light on hair edges, softly blurred indoor background, muted teal-gray wall and subtle floral painting, shallow depth of field, high-key cool white color grading, low saturation, strong black and white lace contrast, clean luminous image, luxury commercial portrait photography, hybrid realistic photography and 3D character rendering, premium AI drama heroine concept photo, high definition, sharp facial details, clear hair strands, fine lace material details
```

### SDXL / LibLib / ComfyUI 英文负面提示词

```
worst quality, low quality, normal quality, lowres, blurry, noise, grain, jpeg artifacts, dirty image, messy background, background too sharp, complex background, strong warm yellow lighting, orange lighting, muddy skin, rough skin, visible pores, large pores, acne, acne scars, freckles, blemishes, wrinkles, dark circles, oily skin, over-smoothed plastic skin, yellow skin, dull skin tone, deformed face, asymmetrical face, distorted eyes, crossed eyes, wrong eye distance, crooked nose, malformed mouth, exposed teeth, thick lips, heavy makeup, western heavy makeup, smoky makeup, exaggerated expression, wide face, square face, short neck, bad body proportions, deformed shoulders, bad hands, bad fingers, extra fingers, missing fingers, distorted manicure, clumpy hair, plastic hair, blurry hair mass, distorted clothes, wrong qipao structure, chaotic lace texture, wrong frog buttons, dirty fur, text, watermark, logo, signature, AI generated text, multiple people, child, old woman, male, overly revealing outfit, vulgar pose, flat anime style, painterly illustration, cartoon style, oil painting
```

### 权重核心版

```
(冷瓷旗袍美人:1.45), (超写实CG漫剧女主定妆照:1.5), (冷瓷白皮肤:1.55), (瓷感无毛孔肌肤:1.5), (AI精修柔焦皮肤:1.35), (脸颊极淡粉色血色:1.2), (肩头锁骨丝缎高光:1.3), (黑色松散低盘发:1.35), (脸侧细碎发丝:1.35), (一缕发丝掠过面部:1.25), (黑色缎带发饰:1.2), (白色半透明蕾丝旗袍:1.55), (黑色花纹刺绣:1.35), (黑色中式盘扣:1.3), (白色毛绒披肩:1.35), (冷白室内棚拍光影:1.45), (窗边冷调自然光:1.35), (大型柔光箱补光:1.3), (青灰蓝柔和暗部:1.25), (浅景深室内虚化背景:1.35), (低饱和冷白色调:1.35), (真实摄影与3D角色渲染融合:1.45)
```

### 推荐生成参数

| 参数 | 推荐值 |
|------|--------|
| **尺寸** | `768x1344` / `832x1216` / `1024x1536` |
| **采样器** | `DPM++ 2M Karras` |
| **步数** | `32-42` |
| **CFG** | `5.5-7` |
| **高清修复** | `1.5x-2x` |
| **高清修复去噪** | `0.25-0.38` |
| **脸部修复** | 轻度，避免磨成塑料脸 |

### 使用铁律

- [ ] 必须保留「冷白室内光、青灰蓝暗部、低饱和」色彩结构。
- [ ] 必须保留「瓷感无毛孔、淡粉血色、肩颈丝缎高光」皮肤组。
- [ ] 必须保留「黑色松散低盘发、脸侧碎发、单缕发丝掠面」发型组。
- [ ] 必须保留「白色半透明蕾丝旗袍、黑色刺绣滚边、黑色盘扣、白色毛绒披肩」服化道组。
- [ ] 禁止暖黄室内灯、浓妆艳抹、复杂背景和粗糙真实毛孔。

---

## 九、月华银发神女玄幻CG复刻配方（可直接复制）

> **适用目标**：复现「深蓝月华逆光 + 银白长发 + 瓷白神女肌 + 红蓝宝石点缀 + 透明蓝纱与国风刺绣」这一类高端玄幻神女 AI 角色肖像风格。

### 图像风格深度拆解

| 维度 | 规格 |
|------|------|
| **画面类型** | 超写实 CG 玄幻神女特写 / 顶级国风手游角色立绘 / 月华神性肖像 |
| **色彩基调** | 深海蓝、月光银白、冷白高光为主，辅以宝石红、孔雀蓝、少量金色刺绣 |
| **皮肤质感** | 月瓷白肌、强 SSS、无毛孔、冷白透亮，鼻尖/唇峰/脸颊有湿润高光 |
| **光影结构** | 强烈月光顶侧逆光，银发与头饰高亮爆光，面部由冷白主光塑形，暗部为深蓝阴影 |
| **妆容特征** | 红粉眼影、红色眼线纹样、红宝石感瞳色、花钿额纹、水润玻璃唇 |
| **头发质感** | 银白色长卷发，发丝极细，月光高光强烈，局部接近白金色发光 |
| **服饰材质** | 深蓝透明纱袖、强镜面高光、国风山水刺绣、白鹤纹样、蓝金华丽头饰与垂坠珠饰 |
| **背景** | 深蓝黑玄幻背景，强景深虚化，局部宝石光斑与金属反射，突出人物神性 |

### 中文一键复制正向提示词

```
超写实CG玄幻神女角色特写，成年年轻亚洲女性，月华银发神女，清冷神性气质，华丽国风幻想角色，近景半身肖像，竖构图，人物居中，头部微微倾斜，眼神直视镜头，精致小脸，尖而柔和的下颌，修长脖颈，红宝石感眼眸，红粉渐变眼影，纤长浓密睫毛，眼尾有红色神纹线条，额头中央有红色花钿纹样，鼻梁挺秀，鼻尖有冷白高光，嘴唇水润微张，玻璃感玫瑰红唇釉，月瓷白皮肤，冷白透亮肤色，瓷感无毛孔肌肤，AI精修无瑕皮肤，柔焦但保留立体五官，强次表面散射，脸颊和鼻尖有湿润柔光高光，皮肤暗部带深蓝冷影，银白色长卷发，浓密蓬松长发，发丝极细极清晰，发丝被月光照亮，白金色强高光，银蓝色边缘光，华丽深蓝金色神女头饰，金属饰品高精度反射，垂坠流苏珠饰，红宝石与蓝宝石耳坠，穿深蓝透明纱袖，纱料半透明层次，蓝色纱袖有水面般镜面高光，国风刺绣华服，山水纹样刺绣，白鹤纹样，金色线绣细节，手部轻握纱袖靠近下巴，手指纤细自然，月光顶侧逆光，强烈冷白轮廓光，银发和头饰局部高光接近过曝，面部冷白主光塑形，暗部深海蓝阴影，深蓝黑玄幻背景，背景虚化，宝石光斑，金属反射光，强烈明暗对比，冷蓝银白色调，宝石红点缀，高级国风玄幻美学，真实摄影与3D角色渲染融合，顶级手游角色立绘质感，高清细节，皮肤通透，发丝清晰，珠宝折射，服装刺绣精细，神圣华丽，月下神女氛围
```

### 中文一键复制负面提示词

```
低质量，低清晰度，模糊，噪点，颗粒感，jpeg压缩痕迹，画面脏，背景杂乱，背景过亮，暖黄光，橙色调，肤色发黄，肤色暗沉，粗糙皮肤，真实毛孔明显，毛孔粗大，痘痘，痘印，雀斑，斑点，皱纹，黑眼圈，油腻皮肤，塑料皮肤，脸部变形，五官不对称，眼睛变形，斗鸡眼，眼距错误，鼻子歪斜，嘴巴畸形，牙齿外露，嘴唇干裂，宽脸，方脸，短脖子，身体比例错误，手部畸形，手指畸形，多余手指，缺失手指，银发变灰，银发变黄，头发结块，发丝糊成一团，头饰混乱，珠宝变形，耳坠错误，额纹错误，服装刺绣混乱，透明纱变塑料布，布料脏乱，颜色过饱和，廉价cosplay感，文字，水印，logo，签名，AI生成字样，多人，儿童，老人，男性，二次元平涂，低端网游风，厚涂插画，卡通风，油画风
```

### SDXL / LibLib / ComfyUI 英文正向提示词

```
masterpiece, best quality, ultra detailed, ultra realistic CG fantasy goddess portrait, premium Chinese fantasy character art, adult young East Asian woman, moonlit silver-haired goddess, cold divine aura, luxurious guofeng fantasy design, close-up half body portrait, vertical composition, centered composition, slight head tilt, looking directly at camera, delicate small face, soft pointed chin, long graceful neck, ruby gemstone eyes, red-pink gradient eyeshadow, long dense eyelashes, red divine markings near outer eyes, red floral forehead ornament, straight delicate nose, cool white highlight on nose tip, moist slightly parted lips, glossy rose-red glass lips, moon porcelain white skin, cold translucent pale skin tone, flawless poreless skin, AI retouched perfect skin, soft-focus skin with sculpted facial volume, strong subsurface scattering, moist soft highlights on cheeks and nose tip, deep blue cool shadows on skin, silver-white long wavy hair, voluminous long hair, ultra fine clear hair strands, hair illuminated by moonlight, platinum white strong highlights, silver-blue rim light, ornate deep blue and gold goddess headdress, high precision metallic reflections, dangling tassel ornaments, ruby and sapphire earrings, deep blue transparent gauze sleeves, translucent layered fabric, water-like specular highlights on blue gauze, Chinese fantasy embroidered robe, landscape embroidery, white crane motif, fine golden thread embroidery, hand gently holding gauze sleeve near chin, slender natural fingers, strong moonlight top-side backlight, intense cold white rim light, near-overexposed highlights on silver hair and headdress, cool white key light sculpting the face, deep ocean blue shadows, dark navy fantasy background, blurred background, gemstone bokeh, metallic reflected light, high contrast lighting, cool blue and silver-white color grading, ruby red accents, luxurious Chinese fantasy aesthetic, hybrid realistic photography and 3D character rendering, top-tier gacha game character illustration quality, high definition, translucent skin, sharp hair strands, gemstone refraction, fine embroidered costume details, sacred gorgeous moon goddess atmosphere
```

### SDXL / LibLib / ComfyUI 英文负面提示词

```
worst quality, low quality, normal quality, lowres, blurry, noise, grain, jpeg artifacts, dirty image, messy background, background too bright, warm yellow lighting, orange tone, yellow skin, dull skin tone, rough skin, visible pores, large pores, acne, acne scars, freckles, blemishes, wrinkles, dark circles, oily skin, plastic skin, deformed face, asymmetrical face, distorted eyes, crossed eyes, wrong eye distance, crooked nose, malformed mouth, exposed teeth, dry cracked lips, wide face, square face, short neck, bad body proportions, bad hands, bad fingers, extra fingers, missing fingers, silver hair turning gray, yellowish silver hair, clumpy hair, blurry hair mass, chaotic headdress, distorted jewelry, wrong earrings, wrong forehead mark, chaotic embroidery, transparent gauze looking like plastic sheet, dirty fabric, oversaturated colors, cheap cosplay look, text, watermark, logo, signature, AI generated text, multiple people, child, old woman, male, flat anime style, low-end online game style, painterly illustration, cartoon style, oil painting
```

### 权重核心版

```
(月华银发神女:1.55), (超写实CG玄幻神女角色特写:1.5), (冷白神性气质:1.35), (月瓷白皮肤:1.55), (瓷感无毛孔肌肤:1.45), (强次表面散射:1.35), (皮肤暗部深蓝冷影:1.25), (红宝石感眼眸:1.35), (红粉渐变眼影:1.25), (红色花钿纹样:1.3), (银白色长卷发:1.55), (白金色强高光:1.4), (银蓝色边缘光:1.35), (深蓝金色神女头饰:1.4), (垂坠流苏珠饰:1.3), (红宝石与蓝宝石耳坠:1.35), (深蓝透明纱袖:1.45), (水面般镜面高光:1.35), (国风山水刺绣华服:1.4), (白鹤纹样:1.25), (月光顶侧逆光:1.45), (深蓝黑玄幻背景:1.35), (冷蓝银白色调:1.4), (宝石红点缀:1.25), (真实摄影与3D角色渲染融合:1.45)
```

### 推荐生成参数

| 参数 | 推荐值 |
|------|--------|
| **尺寸** | `768x1344` / `832x1216` / `1024x1536` |
| **采样器** | `DPM++ 2M Karras` |
| **步数** | `35-45` |
| **CFG** | `5.8-7.2` |
| **高清修复** | `1.5x-2x` |
| **高清修复去噪** | `0.28-0.42` |
| **脸部修复** | 轻度或关闭，优先保留妆容和额纹 |

### 使用铁律

- [ ] 必须保留「深蓝黑背景、冷蓝银白主色、宝石红点缀」色彩结构。
- [ ] 必须保留「月瓷白皮肤、强 SSS、深蓝冷影、湿润高光」皮肤组。
- [ ] 必须保留「银白长卷发、白金强高光、银蓝边缘光」发丝组。
- [ ] 必须保留「红色花钿、红粉眼妆、红蓝宝石耳坠、深蓝金色头饰」妆造组。
- [ ] 必须保留「透明蓝纱、镜面高光、国风山水刺绣、白鹤纹样」服饰材质组。
- [ ] 禁止暖黄光、廉价 cosplay 感、低端网游风和粗糙真实毛孔。

---

## 十、使用指引

### 独立使用（角色设计稿 / T0立绘 / IP物料）

直接使用「§六 完整前缀」 + 角色描述 + 服饰材质关键词（§四）

### 叠加到项目场景中

1. 移除本风格的「纯白背景」条目
2. 替换为项目对应的场景背景描述
3. 保留皮肤质感（§二）+ 材质渲染（§四）子集
4. 打光规范（§三）与场景打光合并，取场景光为主、本风格光为辅

### 与 art-design-skill 协作

1. art-design-skill 完成角色设计方法论（五问法 → 设计铁律 → 服化道定义）
2. 本技能注入渲染风格层（皮肤/打光/材质/色彩），生成最终提示词
3. 两者叠加顺序：**设计内容在前，渲染风格在后**

### 检查清单

- [ ] 皮肤是否呈瓷白高光泽感？（非哑光、非写实毛孔）
- [ ] SSS 是否在肩部/锁骨/耳尖/关节处可见？
- [ ] 镜面高光是否出现在鼻梁/下唇/材质表面？
- [ ] 色彩饱和度是否 ≥80%？
- [ ] 瞳色是否为非自然色？
- [ ] 明暗过渡是否柔和无硬切割？
- [ ] 负面提示词是否已注入？

---

## 十一、接入工作流（硬路由 · 与 visual-style-selector / art-design 的边界）

### 触发条件表（与 visual-style-selector 对接）

| 触发来源 | 触发条件 | 是否引用本技能 | 落地范围 |
|---|---|---|---|
| visual-style-selector | 选定风格 ID = `TOP_TIER_CHARACTER_CG`（顶级人物CG质感） | ✅ 引用：注入 §六 完整前缀 + 对应子配方（§七/§八/§九） | 仅角色独立立绘 / 人物特写 / 定妆照 / 妆造材质参考 |
| visual-style-selector | 选定其它风格 ID | ⬜ 不引用本技能 | 按所选风格执行 |
| 服化道角色设计 | 需要「真实摄影质感 + 3D角色渲染 + 瓷感皮肤」的高端人物图 | ✅ 引用：作为渲染层叠加在 art-design 设计内容之后 | 同上，仅角色 |

> 口径与 `skills/visual-style-selector-skill/SKILL.md` §6「顶级人物CG质感·使用限制」、`tools/references/style-preset-library.md`（风格来源同指本技能）保持一致，三处同源。

### 🔴 硬路由限制（不可越界）

- ✅ 仅用于：角色独立立绘 / 人物特写分镜 / 定妆照 / 角色海报 / 服化道·妆造材质参考。
- 🔴 **禁止用于 `assets/prompts/scene-prompts.md`（场景提示词）**：本技能不是场景 / 建筑 / 道具 / 空间的美术风格前缀。
- 🔴 场景提示词一律使用项目 `assets/visual-style-guide.md` 的场景专用美术风格前缀；本技能「入项目场景」时按 §十「叠加到项目场景中」处理——仅保留皮肤（§二）/ 材质（§四）子集、移除「纯白背景」条目，不得把整套人物风格整体注入场景。

### 🔴 与 art-design 女性体型铁律的合并 / 覆盖规则

- 分层职责：**体型 / 比例 / 面部反大众化** = `art-design-skill` §女性体型铁律 + `aesthetic-vision-skill` §三 体型矩阵（T0/T1/T2）为唯一权威；**渲染层（皮肤 / 打光 / 材质 / 色彩）** = 本技能。
- 叠加顺序：art-design 女性体型铁律（体型层 · 在前）→ 本技能（渲染层 · 在后），即「设计内容在前、渲染风格在后」。
- 🔴 冲突即覆盖：本技能女性配方（§八 / §九）若出现「邻家 / 亲和 / 普通体型 / 温柔默认表情」等弱化体型铁律的倾向，**一律以 art-design 女性体型铁律强制覆盖回 T0/T1/T2**（头身比最低 8.5、推荐 9.5；腿长占总身高 60%+；S 曲线明显；面部至少极端化 1 项）。
- 本技能只增渲染质感，**不得删改、不得弱化**女性体型铁律的任何强制项。

---

## 十二、版本信息

- 版本: 1.1
- 更新日期: 2026-05-31
- 更新内容（1.1）：新增 §十一 接入工作流——补「与 visual-style-selector 触发条件表 + 仅用于角色独立立绘 / 🔴 禁止用于 scene-prompts」硬路由；写清与 art-design 女性体型铁律的合并 / 覆盖规则（体型层以 art-design + aesthetic-vision §三 为唯一权威，本技能仅叠加渲染层，冲突强制覆盖回 T0/T1/T2）。
