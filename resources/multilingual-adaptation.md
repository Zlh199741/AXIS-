# 多语言适配层

> 本文档提供多语言适配指导，包括英文提示词优化、中外审美差异处理、平台术语对照等
>
> 🔴 **适用范围**：本文档仅用于**图片生成提示词**（Midjourney / Stable Diffusion / DALL-E 等）和国际化场景。
> **Seedance 2.0 / Kling 视频提示词必须使用中文**，请勿将本文档的中→英翻译应用于视频提示词生成。

---

## 一、英文提示词优化

### 1.1 中英文表达差异

| 中文表达 | 英文优化 | 说明 |
|----------|----------|------|
| 帅气 | handsome, rugged | 强调轮廓感 |
| 漂亮 | beautiful, elegant | 强调整体美 |
| 冷酷 | cold, aloof, icy | 强调距离感 |
| 邪魅 | sinister, wicked | 强调邪恶感 |
| 仙气 | ethereal, celestial | 强调空灵感 |
| 霸气 | commanding, majestic | 强调气势 |
| 痞气 | roguish, mischievous | 强调痞感 |
| 禁欲 | restrained, stoic | 强调克制感 |

### 1.2 材质词汇对照

| 中文 | 英文 |
|------|------|
| 丝绸 | silk |
| 锦缎 | brocade |
| 棉麻 | cotton-linen |
| 皮革 | leather |
| 毛皮 | fur |
| 薄纱 | chiffon, sheer fabric |
| 蕾丝 | lace |
| 金属 | metallic |
| 玉石 | jade |
| 水晶 | crystal |

### 1.3 光效词汇对照

| 中文 | 英文 |
|------|------|
| 金光 | golden light |
| 银光 | silvery light |
| 圣光 | halo, divine light |
| 魔光 | arcane glow, mystical aura |
| 霞光 | iridescent, sunset glow |
| 灵光 | spiritual light |
| 佛光 | buddhist radiance |
| 血光 | blood-red glow |

---

## 二、平台术语对照

### 2.1 Seedance 术语

| 概念 | Seedance表达 |
|------|-------------|
| 剧情点 | Plot Point / Scene |
| 分镜 | Storyboard Frame |
| 运镜 | Camera Movement |
| 特写 | Close-up / Extreme Close-up |
| 远景 | Wide Shot / Long Shot |
| 推轨 | Dolly / Track |
| 摇镜 | Pan / Tilt |

### 2.2 Kling 术语

| 概念 | Kling表达 |
|------|----------|
| 主体参考 | Subject Reference |
| 智能分镜 | Smart Shot |
| 镜头1/镜头2 | Shot 1 / Shot 2 |
| 时长 | Duration |
| 禁用项：背景音乐/BGM | Forbidden generatable music content |
| 音效 | Sound Effects |

### 2.3 Midjourney/SD 术语

| 概念 | MJ/SD表达 |
|------|----------|
| 提示词 | Prompt |
| 权重 | Weight (::) |
| 负面提示词 | Negative Prompt (--no) |
| 宽高比 | Aspect Ratio (--ar) |
| 风格化 | Stylize (--s) |
| 变异度 | Chaos (--c) |
| 提示词一致性 | Prompt Weighting |

---

## 三、文化适配指南

### 3.1 中式审美 → 西式优化

**人物设计**：

| 中式特点 | 西式优化 |
|----------|----------|
| 丹凤眼 | Almond-shaped eyes, slanted eyes |
| 柳叶眉 | Thin arched eyebrows |
| 樱桃小口 | Full lips (调整) |
| 鹅蛋脸 | Oval face shape |
| 古典气质 | refined, elegant |
| 书卷气 | intellectual, scholarly |

**场景设计**：

| 中式元素 | 西式表达 |
|----------|----------|
| 亭台楼阁 | Pavilion, pagoda |
| 飞檐翘角 | Upturned eaves |
| 红墙金瓦 | Crimson walls, golden tiles |
| 雕梁画栋 | Carved beams, painted rafters |
| 假山流水 | Rock garden, water feature |
| 屏风隔断 | Screen divider |

### 3.2 宗教/神话适配

| 中文概念 | 英文表达 | 注意事项 |
|----------|----------|----------|
| 佛教 | Buddhism, Buddhist | 避免具体佛像 |
| 道教 | Taoism, Taoist | 可用mystical |
| 仙侠 | Celestial, Immortal | fantasy风格 |
| 神话 | Mythology, Legendary | 通用性强 |
| 阵法 | Magical formation | Arcane circle |
| 符咒 | Talisman, Charm | Mystical symbols |

---

## 四、国际化注意事项

### 4.1 避免的文化冲突

| 类别 | 注意项 |
|------|--------|
| 手势 | 某些手势在不同文化中有不同含义 |
| 颜色 | 白色=丧事(东亚) / 纯洁(西方) |
| 数字 | 4=死(中日) / 吉利(西方) |
| 动物 | 龙=吉祥(中国) / 邪恶(西方) |
| 食物 | 某些食材有文化禁忌 |

### 4.2 通用化策略

1. **视觉符号替代**：
   - 特定手势 → 通用肢体语言
   - 文化特定物品 → 功能相似但更通用的物品

2. **抽象化表达**：
   - 具体文化元素 → 通用氛围描述
   - 特定场景 → 通用场景类型

---

## 五、翻译质量评估

### 5.1 评估标准

| 维度 | 标准 |
|------|------|
| 准确性 | 语义是否准确传达 |
| 自然度 | 是否符合英文表达习惯 |
| 关键词覆盖 | 关键视觉词汇是否保留 |
| 风格匹配 | 语气是否匹配目标场景 |

### 5.2 常见翻译问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 关键词遗漏 | 直译导致丢失 | 补充关键词 |
| 语法不自然 | 中式英语 | 重新表达 |
| 文化误解 | 文化差异 | 本地化处理 |
| 风格不匹配 | 语气偏差 | 调整用词 |

---

## 六、快速参考表

### 6.1 常用词汇速查

| 场景 | 中文 | 英文 |
|------|------|------|
| 人物 | 少年 | Young man, teenage boy |
| 人物 | 少女 | Young woman, teenage girl |
| 人物 | 老者 | Elderly man, senior citizen |
| 人物 | 美女 | Beautiful woman, gorgeous lady |
| 人物 | 俊男 | Handsome man, good-looking guy |
| 服装 | 古装 | Period costume, traditional attire |
| 服装 | 铠甲 | Armor, plated armor |
| 服装 | 道袍 | Robe, monastic robe |
| 场景 | 宫殿 | Palace, grand hall |
| 场景 | 牢狱 | Dungeon, prison cell |
| 场景 | 战场 | Battlefield, war zone |
| 场景 | 森林 | Forest, woods |
| 场景 | 山巅 | Mountain peak, summit |
| 场景 | 海边 | Seaside, shore, coastline |
| 氛围 | 阴森 | Gloomy, eerie, sinister |
| 氛围 | 神秘 | Mysterious, enigmatic |
| 氛围 | 浪漫 | Romantic, dreamy |
| 氛围 | 紧张 | Tense, suspenseful |
| 氛围 | 恐怖 | Horrific, terrifying |
| 氛围 | 温馨 | Cozy, warm, comforting |
| 特效 | 火焰 | Flames, fire, blazing |
| 特效 | 冰霜 | Ice, frost, freezing |
| 特效 | 雷电 | Lightning, thunder |
| 特效 | 光芒 | Radiance, glow, beam |
| 特效 | 雾气 | Mist, fog, haze |

### 6.2 提示词后缀速查

| 类型 | 后缀 |
|------|------|
| 画质 | masterpiece, best quality, ultra-detailed |
| 分辨率 | 8k, 4k, high resolution |
| 渲染 | Unreal Engine 5, Octane Render, PBR |
| 摄影 | DSLR, professional photography |
| 灯光 | cinematic lighting, volumetric lighting |
| 避免 | no text, no watermark, no blur |

---

**版本**：1.0
**更新日期**：2026-03-15
