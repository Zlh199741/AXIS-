# 《我不是没事，我是不敢有事》电影级角色提案板（Pitch Board 版）

> **本文件用途**：用于"对外提案 / 美术指导对内拍板"——给导演、美术指导、制片、投资方看的**电影级角色提案板**。
>
> **与同目录 `character-prompts.md` 的边界**：
> - 本文件（提案板）：**横版大画幅 16:9 + 中性灰提案板背景 + 不对称美术指导构图 + 6 区块固定布局**。
> - `character-prompts.md`（工业资产）：**纯白背景 + 严格隔离 + 三栏式布局**，给后续分镜/Seedance/Kling 视频生成引用。
> - 两者**共享同一基底人物**（五官/比例/发型/服装/配饰/道具完全一致），**不可互替**。
>
> **来源剧本**：`不敢麻烦别人_动画改编/我不是没事我是不敢有事_专业动画剧本.md`
>
> **应用模板**：`/Users/ahui/Desktop/智能体/AXIS-漫剧内测教学/电影级角色设定板_固定布局模板.md`

---

## 一、全局视觉铁律（写入提示词时不得删减）

1. **一致性铁律**：A/B/C/D 中所有角色视图必须为**同一人**——五官比例、发型轮廓、皮肤色温、身材比例、服装款式、配饰位置、道具持握方式**严格一致**，禁止任何角度的脸型偏移、年龄漂移、服装替换。
2. **真实材质铁律**：皮肤须 PBR 物理材质（SSS 次表面散射 + 鼻梁下唇柔和高光 + 关节偷暖粉红）；布料须 fabric fibers / weave / wrinkle 三重细节；金属须真实反射但避免过亮高光；皮革须哑光颗粒纹+缝线细节。
3. **演员气质铁律**：角色像**真实演员被镜头捕捉的瞬间**，不是平面摆拍模特；微表情、肌肉张力、呼吸感、重心、肩颈姿态都要带"真实人感"。
4. **电影感铁律**：色调克制、对比适中、留呼吸空间；不做高饱和度网红美学、不做偶像化糖果美学、不做塑料蜡像感、不做冷白假人脸。
5. **画面洁净铁律**：禁止文字水印 logo（除已声明的标注层）、镜头 flare、散景光斑、漂浮粒子、噪点、胶片颗粒、随机微高光、表面随机脏纹理。
6. **职业版面铁律**：所有标注（角色名/身高刻度/性格关键词/材质备注）必须**清晰可读**但**不喧宾夺主**，字体锁定统一：印刷标注一律 Inter（西文/数字）+ 思源黑体（中文），手写手记一律 Caveat，严禁混入第三种字体。
7. **妆造与眼神光铁律（2026-05-30 美学升级·解决"妆照不好看"）**：所有角色面部必须有完整妆造质感才算"好看"——清透裸妆底（哑光通透不假面）、根根分明自然眉、纤长上扬睫毛+卧蚕珠光高光、淡桃粉眼影极淡晕染、唇部水光唇釉微反光、颧骨自然腮红、发丝根根高光+额前空气感碎发；**男性**改为下颌/颧骨/鼻影修容立体+喉结+利落眉峰+极淡干净胡青；**小女孩**保持童真无妆、只提皮肤通透+奶气腮红+眼神光；**母亲**保持端庄年龄感、修整自然眉+唇色润泽、不丑化不枯槁。双眼必有 10–11 点钟方向 catchlight 眼神光、眼球湿润通透有神。好看来自"骨相+光+质感"，**禁止**网红浓妆/磨皮假面/糖水滤镜/欧美夸张烟熏眼/过曝死白；疲惫与克制只体现在眼神，不靠丑化五官。

---

## 二、全局风格前缀（每个提示词共用）

**中文风格前缀**：
电影级角色设定板，横版大画幅 16:9，中性灰提案板背景（#BEC1C4 至 #C7CACD 渐变，极轻微亚麻布纹/纸面纹理，左上略暖右下略冷，无纯白无纯黑，禁止彩色光斑/散景虚化/场景元素），构图被美术指导设计过、略带手作感、避免机械对称网格；AXIS 顶级人物 CG 质感（top-tier character CG quality），2.5D 动漫-CG 融合渲染（半写实日系底子 + 现实家庭剧角色情绪表演），精致五官结构（鹅蛋脸/柔和尖下巴、水润杏眼+纤长睫毛、高挑鼻梁+鼻尖柔光、淡桃粉眼周、玻璃感水润唇色），完整妆造（根根分明自然眉 + 纤长上扬睫毛 + 卧蚕珠光高光 + 淡桃粉眼影极淡晕染 + 水光唇釉微反光 + 颧骨自然腮红 + 发丝根根高光与额前空气感碎发；男性改为下颌/颧骨/鼻影修容立体 + 喉结 + 利落眉峰 + 极淡胡青）+ 双眼 10–11 点钟方向明亮 catchlight 眼神光，暖粉底瓷白光泽肌肤（#FDE8D8~#F5C6AA）+ 强 SSS 次表面散射（肩部锁骨耳尖透粉、关节偷暖粉红）+ 鼻梁与下唇镜面高光 + 明暗极柔过渡；电影级柔光美人布光 5200-5600K，大柔光箱蝶形/环形主光从右上 45° 制造颧骨与鼻翼柔和立体，左侧低强度冷色补光（光比约 3:1、保留立体而非平光洗白），一道低强度发丝轮廓光把发缘与背景分离，双眼 10–11 点钟方向明亮 catchlight 眼神光，A/B/C/D 四视觉区块共享同一光源；写实 3D 材质渲染，影视级游戏CG·次世代3A质感·超写实PBR材质渲染 + AO + SSS + Octane Render + Unreal Engine 5 + 4K极致细节，柔光电影打光（低强度轮廓光勾边 + 发丝光透发 + 柔光镜柔化）+ 浅景深小景深焦外柔化，发丝级细节，眼球湿润反光，布料纤维真实，演员气质而非摆拍模特。

**English style prefix**:
Cinematic character pitch board, horizontal large-format 16:9, neutral gray pitch-board background gradient from #BEC1C4 to #C7CACD with subtle linen weave / paper grain texture, slightly warm at upper-left and slightly cool at lower-right, no pure white, no pure black, no colored bokeh, no scene elements, art-directed slightly hand-laid composition, never mechanical grid; AXIS top-tier character CG quality, 2.5D anime-CG hybrid rendering (semi-realistic Japanese illustration base + realistic family-drama emotional performance), refined facial features structure (oval face with soft pointed chin, watery almond eyes with long delicate eyelashes, high straight nose bridge with soft tip highlight, subtle peach-pink eye area, glossy moist natural lips), complete makeup (natural feathered brows + long curled upper lashes + pearly under-eye highlight + softly diffused peach-pink eyeshadow + glossy lip with sheen + natural cheekbone blush + hair-strand highlights with airy wispy bangs; for male: jaw/cheekbone/nose-side contouring + Adam's apple + crisp arched brows + light clean stubble) + bright catchlight in both eyes at 10-11 o'clock, warm pink-undertone porcelain luminous skin (#FDE8D8 to #F5C6AA) with strong SSS, soft specular highlights on nose bridge and lower lip, ultra-soft shadow transitions; soft cinematic beauty lighting 5200-5600K, large softbox butterfly/loop key from upper right at 45° giving gentle cheekbone and nose-side dimensionality, low-intensity cool fill from left (about 3:1 ratio, dimensional not a flat wash), a low-intensity hair rim light, bright catchlight in both eyes at 10-11 o'clock, Zones A/B/C/D share the same lighting; realistic 3D material rendering, cinematic game CG, next-gen AAA quality, hyper-realistic PBR material rendering + AO + SSS + Octane Render + Unreal Engine 5, 4K ultra-detailed, soft cinematic lighting (low-intensity rim light + hair light + soft-focus diffusion) + shallow depth of field, hair-strand detail, moist eye reflection, realistic fabric fibers, actor presence not catalog model.

---

## 三、角色 1：成年女主｜总说"没事"的妻子

### 3.1 基础形象

#### 角色信息卡

```yaml
角色名称: 成年女主｜总说"没事"的妻子
年龄: 28-32 岁
身高: 165cm
体型: 纤细匀称、肩颈微收、身长腿略瘦
风格方向: 电影级风格化写实（半写实日系 + 现实家庭剧情绪）

性格关键词: 克制 / 隐忍 / 疲惫温柔 / 习惯性把需求咽回去 / 不愿麻烦别人

外貌特征:
  脸型: 精致鹅蛋脸 + 柔和尖下巴
  眼睛: 水润杏眼 + 纤长睫毛 + 眼尾轻微下压 + 眼下淡青灰疲惫影
  发型: 暖黑中长发，自然垂落到锁骨下方
  肤色: 暖粉底瓷白光泽肌肤（#FDE8D8~#F5C6AA），强 SSS 透粉
  独特记忆点: 习惯性攥紧衣角的手部动作 + 习惯性微笑前的迟疑眼神

服装设定:
  上装: 雾灰针织开衫（细薄羊毛混纺）
  下装: 深灰直筒长裤（家居棉质）
  外层: 米白色棉质内搭
  鞋子: 低调白色家居拖鞋
  配件: 素银婚戒（细窄银圈、镜面反射很弱、有极轻微日常划痕）
  道具: 无（手中习惯性攥住衣角）

场景气质: 二十多岁至三十岁初的现实生活流家庭主妇，疲惫温柔但克制，不做网红化妆
```

#### HSB 色板（≥4 色）

- 🎨 暖黑发色：H=25, S=38, B=20，`#33251F`
- 🎨 暖粉底肌肤色：H=20, S=18, B=96，`#F5D5C4`
- 🎨 雾灰家居针织衫：H=35, S=7, B=78，`#C7C1B7`
- 🎨 低饱和奶茶内搭色：H=30, S=16, B=86，`#DBCCB8`
- 🎨 眼下疲惫淡青灰：H=215, S=12, B=58，`#828A94`

#### 配饰/材质微距清单（5 件，作为 E 区块输入）

- 📌 细薄针织袖口：羊毛混纺纤维，边缘轻微起毛，低反差织纹，袖口被手指攥出浅褶
- 📌 素银婚戒：细窄银圈，边缘圆润，镜面反射很弱，有极轻微日常划痕
- 📌 米白内搭领口：棉质软布，洗旧自然边缘
- 📌 眼部微表情特写：眼尾轻微下压，眼球反光湿润但不大哭，眼下有淡青灰疲惫影
- 📌 指尖皮肤细节：暖粉底肌通透皮肤，指关节偷暖粉红，指甲短而干净，按压时指腹泛白，SSS 透光感可见

#### 【中文描述段】（Nano Banana Pro 直喂版）

电影级角色设定板，横版大画幅 16:9，中性灰提案板背景（#BEC1C4 至 #C7CACD 渐变，极轻微亚麻布纹/纸面纹理，左上略暖右下略冷，无纯白无纯黑，禁止彩色光斑/散景虚化/场景元素）。整张画面被切为 6 个固定功能区块，构图像被美术指导设计过、略带手作感、避免机械对称网格。

【顶部细条·标题区】横跨整张顶部 6% 高度，文字左对齐至主视觉右缘：「成年女主｜总说"没事"的妻子 · 28-32岁 · 身高 165cm · 电影级风格化写实 · 克制／隐忍／疲惫温柔／习惯性把需求咽回去」，印刷标注统一用 Inter（西文/数字）+ 思源黑体（中文），手写注释统一用 Caveat（极少量），严禁第三种字体，文字清晰可读但不喧宾夺主。

【区块A·主视觉角色立像】左列·全高 24% 宽 × 94% 高（第一梯队·双主块之一·竖向贯通全高），85mm 全身正面演员气质立像，自然站姿、重心一边略低一边略高、肩颈带真实呼吸感与肌肉张力；二十八到三十二岁现实生活流女性，身高 165cm，纤细匀称体型，头身比 7.5；精致鹅蛋脸 + 柔和尖下巴，水润杏眼 + 纤长睫毛 + 眼尾轻微下压 + 眼下淡青灰疲惫影，高挑鼻梁鼻尖柔和高光，淡桃粉眼周，玻璃感水润唇色；暖黑中长发自然垂落到锁骨下方；暖粉底瓷白光泽肌肤通透有血色，肩部锁骨耳尖 SSS 透粉；穿雾灰针织开衫（细薄羊毛混纺）+ 米白棉质内搭 + 深灰直筒家居长裤 + 低调白色家居拖鞋，左手无名指素银婚戒，双手习惯性攥住开衫下摆形成浅褶；微表情是"习惯性微笑前的迟疑眼神"——克制、隐忍、不愿麻烦别人。立像左侧紧贴一根金色细线竖向身高刻度尺（2% 宽），标头/肩/腰/膝/脚踝高度与 cm 数字。

【区块B·全身多角度转面图】右列·上 48% 宽 × 54% 高（第一梯队·画面最大主块），横向 5 视图等距排列：正面 → 3/4 正侧 → 纯侧面 → 3/4 背 → 背面，每个视图为 50mm 全身像，五官/身材比例/发型轮廓（暖黑中长发垂落锁骨）/服装款式（雾灰针织开衫+米白内搭+深灰直筒裤+白色家居拖鞋）/婚戒位置/手部攥衣角动作与主视觉立像严格一致；底线允许 ±2-4% 高低错位（中间纯侧面下沉 3-4%，两边各上浮 2%），避免机械对称。

【区块C·头部研究图】中列·下 28% 宽 × 44% 高（第二梯队），6 张头部研究：正面 / 3/4 正侧 / 纯侧面 / 低头 / 抬头 / 动态扭头回望，2 行 × 3 列，每张 85mm-105mm 头部特写，鹅蛋脸+柔和尖下巴、水润杏眼+纤长睫毛、高挑鼻梁鼻尖柔光、淡桃粉眼周、玻璃感水润唇色、暖黑中长发与主视觉严格一致，光源方向与色温一致；其中"动态扭头回望"那一张放大到约 1.15× 并向下溢出网格 8%，像额外补的研究稿贴上去，捕捉她"被叫住时下意识的克制式回头"。

【区块D·电影感情绪肖像】中列·上 28% 宽 × 50% 高（第二梯队·定情绪脸），50mm 中近景肖像（胸像或半身），偏左对齐留右侧呼吸空间，电影色调（克制对比、保留 SSS 透粉肤感），眼神带"克制／习惯性把需求咽回去"中最具情绪张力的一刻——嘴唇微张又闭回去、眼眶湿润但不落泪、眉间未皱却已紧绷，与主视觉同一光源同一色温但情绪强度提升一档。

【区块E·服装与配件拆解】右列·下横条 48% 宽 × 20% 高（第三梯队·堆叠于 B 之下），5 张 100mm 微距细节拍立得感小图，分别展示：① 细薄针织袖口（羊毛混纺纤维，边缘轻微起毛、低反差织纹、被手指攥出浅褶）；② 素银婚戒（细窄银圈、镜面反射很弱、极轻微日常划痕）；③ 米白内搭领口（棉质软布、洗旧自然边缘）；④ 眼部微表情特写（眼尾轻微下压、眼球湿润反光、眼下淡青灰疲惫影）；⑤ 指尖皮肤细节（暖粉底肌通透、指关节偷暖粉红、指甲短而干净、按压时指腹泛白、SSS 透光可见）；每张带轻微旋转 ±3° 模拟贴在画板上，旁边用 Caveat 手写体细线标注材质名称（羊毛混纺/925银/棉布/SSS皮肤）。

【区块F·美术备注与色板】右列·中横条 48% 宽 × 20% 高（第三梯队·堆叠于 B 之下），HSB 色板（暖黑发色 H=25 S=38 B=20 `#33251F`、暖粉底肌肤色 H=20 S=18 B=96 `#F5D5C4`、雾灰家居针织衫 H=35 S=7 B=78 `#C7C1B7`、低饱和奶茶内搭色 H=30 S=16 B=86 `#DBCCB8`、眼下疲惫淡青灰 H=215 S=12 B=58 `#828A94`）+ 材质关键词「羊毛混纺/棉/925银/瓷白光泽肌」+ 性格关键词「克制／隐忍／疲惫温柔／习惯性把需求咽回去」+ 风格定位「电影级风格化写实·半写实日系」，色板色块与文字框允许轻微错开。

整张光源统一：电影级柔光美人布光 5200-5600K，大柔光箱蝶形/环形主光从右上 45° 进入制造颧骨与鼻翼柔和立体，左侧低强度冷色补光（光比约 3:1、保留立体而非平光洗白），一道低强度发丝轮廓光把发缘与背景分离，双眼 10–11 点钟方向明亮 catchlight 眼神光；皮肤 PBR 物理材质（SSS 次表面散射、鼻梁下唇柔和高光、关节偷暖粉红、明暗极柔过渡），针织布料展示 fabric fibers/weave/wrinkle 三重细节，素银哑光反射，棉布纤维清晰。AXIS 顶级人物 CG 质感，2.5D 动漫-CG 融合渲染，realistic 3D material rendering，影视级游戏CG·次世代3A质感·超写实PBR材质渲染 + AO + SSS + Octane Render + Unreal Engine 5 + 4K极致细节，柔光电影打光（低强度轮廓光勾边 + 发丝光透发 + 柔光镜柔化）+ 浅景深小景深焦外柔化，发丝级细节，眼球湿润反光，演员气质而非摆拍模特。

绝对禁止：纯白背景、纯黑背景、彩色光斑、散景虚化、漂浮粒子、镜头 flare、噪点、胶片颗粒；禁止粗糙毛孔/皮肤斑点噪声/塑料蜡像感/冷白假人脸/偶像化糖果浓妆/网红磨皮/低幼夸张二次元平涂；禁止文字水印 logo（标注区文字除外）；禁止任何角度脸型偏移/年龄漂移/服装替换/婚戒漂移；禁止机械对称九宫格、严禁全部正放微距小图、严禁背景出现卧室/办公室/医院等场景元素。

#### 【English description block】

Cinematic character pitch board, horizontal large-format 16:9, neutral gray pitch-board background gradient from #BEC1C4 to #C7CACD with subtle linen weave / paper grain texture, no pure white, no pure black, no colored bokeh, no scene elements, art-directed slightly hand-laid composition.

[Top thin band] full top width 6% high, text left-aligned to right edge of main visual: "Adult Female Lead | The Wife Who Always Says I'm Fine · Age 28-32 · Height 165cm · Cinematic stylized realism · restrained / forbearing / weary-tender / habitually swallowing her needs", printed labels strictly in Inter (Latin/numerals) + Source Han Sans (CJK), handwritten notes strictly in Caveat (minimal), no third typeface.

[Zone A · Hero full-body portrait] left column, full height, 24% width × 94% height (Tier 1, one of two main blocks · vertical full-height), 85mm full-body front portrait with actor presence, natural stance with slightly uneven weight distribution, shoulder and neck carrying real breathing tension; 28-32 year old realistic Asian woman, height 165cm, slim balanced body type, head-to-body ratio 7.5; refined oval face with soft pointed chin, watery almond eyes with long delicate eyelashes and slightly drooping outer corners with subtle blue-gray under-eye fatigue shadow, high straight nose bridge with soft tip highlight, subtle peach-pink eye area, glossy moist natural lip color; warm black medium-long hair falling naturally just below the collarbone; warm pink-undertone porcelain luminous skin with visible SSS pink translucency on shoulders, collarbones, ear tips; wearing misty-gray fine-knit wool-blend cardigan + off-white cotton inner top + dark gray straight home trousers + simple white home slippers, plain silver wedding ring on left ring finger, both hands habitually clutching the cardigan hem creating shallow creases; micro-expression captures the hesitation just before her habitual reassuring smile—restrained, forbearing, unwilling to be a bother. A thin gold vertical height ruler (2% width) flush to the left edge marks head/shoulder/waist/knee/ankle heights with cm numbers.

[Zone B · Full-body turnaround] right column, top, 48% width × 54% high (Tier 1, largest block on canvas), five 50mm full-body views in horizontal row: front → 3/4 front-side → pure side → 3/4 back → back; facial features, body proportions, warm black hair silhouette, garment cut (misty knit cardigan + off-white inner + dark gray trousers + white home slippers), wedding ring placement, hem-clutching hand pose identical to Zone A; baseline varies ±2-4% (middle pure-side dropped 3-4%, flanks raised 2%).

[Zone C · Head studies] middle column, lower, 28% width × 44% high (Tier 2), six 85-105mm head close-ups: front / 3/4 front-side / pure side / head down / head up / dynamic over-shoulder glance, 2 rows × 3 columns, all features (oval face, almond eyes, soft nose tip, peach-pink eye area, warm black medium-long hair) identical to Zone A under same light; the "over-shoulder glance" portrait scaled to ~1.15× and overflowing the grid downward by ~8%, capturing her restrained instinctive turn-back when called.

[Zone D · Cinematic emotional portrait] middle column, upper, 28% width × 50% high (Tier 2, the emotion face), 50mm mid-close portrait, breathing space on right, cinematic restrained tone with preserved SSS pink skin translucency; eyes carry the most charged moment of her "swallowing her needs"—lips parting then closing again, eyes moist but not crying, brow not yet furrowed but already tense; same lighting as main visual, emotional intensity escalated one notch.

[Zone E · Wardrobe & accessory breakdown] right column, lower bar, 48% width × 20% high (Tier 3, stacked below Zone B), five 100mm macro Polaroid-feel detail tiles: ① fine-knit wool-blend cuff (slight edge fuzz, low-contrast weave, shallow creases from clutching); ② plain silver wedding ring (narrow band, soft round edges, very subtle daily scratches, weak mirror reflection); ③ off-white cotton inner collar (worn-soft natural edge); ④ eye micro-expression closeup (drooping outer corner, moist eye reflection, blue-gray under-eye shadow); ⑤ fingertip skin detail (warm pink-undertone translucent skin, joint warm pink flush, short clean nails, fingertip whitening when pressing, visible SSS); each tile rotated ±3° as if pinned, handwritten labels "wool blend / 925 silver / cotton / SSS skin".

[Zone F · Art notes & palette] right column, middle bar, 48% width × 20% high (Tier 3, stacked below Zone B), HSB palette (warm black hair H=25 S=38 B=20 #33251F, warm pink skin H=20 S=18 B=96 #F5D5C4, misty-gray knit H=35 S=7 B=78 #C7C1B7, milky-tea inner H=30 S=16 B=86 #DBCCB8, fatigue blue-gray H=215 S=12 B=58 #828A94) + material keywords "wool-blend / cotton / 925 silver / porcelain luminous skin" + personality keywords "restrained / forbearing / weary-tender / habitually swallowing her needs" + style direction "cinematic stylized realism".

Unified lighting: soft cinematic beauty lighting 5200-5600K, large softbox butterfly/loop key from upper right at 45° giving gentle cheekbone and nose-side dimensionality, low-intensity cool fill from left (about 3:1 ratio, dimensional not a flat wash), a low-intensity hair rim light separating hair from the background, bright catchlight in both eyes at 10-11 o'clock; PBR skin with SSS, soft specular on nose bridge and lower lip, joint warm pink flush, ultra-soft shadow transitions; knit shows fabric fibers / weave / wrinkles in three layers, silver shows matte reflection, cotton fibers visible. AXIS top-tier character CG quality, 2.5D anime-CG hybrid rendering, realistic 3D material rendering, cinematic game CG, next-gen AAA quality, hyper-realistic PBR material rendering + AO + SSS + Octane Render + Unreal Engine 5, 4K ultra-detailed, soft cinematic lighting (low-intensity rim light + hair light + soft-focus diffusion) + shallow depth of field, hair-strand detail, moist eye reflection, actor presence not catalog model.

Strictly forbidden: pure white / pure black background, colored bokeh, lens flare, floating particles, noise, film grain; no rough pores, no skin blemishes, no plastic wax-doll look, no cold-white mannequin face, no idol-like sugary makeup, no influencer skin smoothing, no childish flat anime; no text watermark logo (annotation layer excluded); no facial drift, no age drift, no garment swap, no wedding-ring drift across views; no rigid 9-grid symmetry; never all macro tiles upright; never include bedroom / office / hospital scene elements in background.

#### 【画面洁净负面约束】

不要耀斑、不要镜头 flare、不要散景光斑、不要漂浮粒子、不要火星碎点、不要发光碎点、不要空气中的小色点、不要灰尘亮点、不要噪点、不要胶片颗粒、不要随机微高光、不要表面随机脏纹理、不要人物身上密集噪声、不要场景背景、不要文字水印 logo（标注区除外）、不要机械对称网格、不要全部微距小图正放、不要塑料蜡像感、不要冷白假人脸、不要偶像化糖果浓妆。

#### T0 自检清单

**版面区块完整性**
- [ ] 顶部细条标题区（角色名+年龄+身高+风格方向+性格关键词）
- [ ] 区块 A 主视觉立像 + 金色身高刻度尺
- [ ] 区块 B 全身 5 视图（正/3-4正侧/纯侧/3-4背/背），底线允许错位
- [ ] 区块 C 头部 6 视图（正/3-4正侧/纯侧/低头/抬头/动态扭头），扭头略大偏出网格
- [ ] 区块 D 电影感情绪肖像（50mm 中近景，偏左对齐）
- [ ] 区块 E 5 张材质微距（针织袖口/素银婚戒/米白内搭领口/眼部微表情/指尖皮肤）±3° 旋转
- [ ] 区块 F HSB 色板 5 色 + HEX

**一致性核对**
- [ ] 鹅蛋脸+柔和尖下巴在 A/B/C/D 一致
- [ ] 水润杏眼+眼尾下压+眼下淡青灰在 A/B/C/D 一致
- [ ] 暖黑中长发垂落锁骨在 A/B/C/D 一致
- [ ] 雾灰针织开衫+米白内搭+深灰长裤+白色家居拖鞋在 A/B 一致
- [ ] 素银婚戒位置（左手无名指）在 A/B 一致
- [ ] 攥衣角手部动作在 A/B 一致

**材质真实性**
- [ ] 皮肤 PBR + SSS 透粉 + 鼻梁下唇柔光 + 关节偷暖粉红
- [ ] 针织 fabric fibers / weave / wrinkle 可见
- [ ] 素银哑光反射不过亮
- [ ] 棉布纤维清晰

**背景与画面洁净**
- [ ] 中性灰提案板背景（#BEC1C4~#C7CACD）非纯白/纯黑
- [ ] 极轻微亚麻布纹/纸纹存在
- [ ] 无卧室/办公室/医院等场景元素
- [ ] 无耀斑/散景/漂浮粒子/噪点/水印

**美术指导气质**
- [ ] 整张图略带不对称感、有手作贴板感
- [ ] 微距小图非全部正放
- [ ] 头部研究"动态扭头"略大偏出网格
- [ ] 五视图底线非完全平齐
- [ ] 演员气质（呼吸/重心/肌肉张力）

---

### 3.2 变体 A：职场"没事"状态

**变体说明**：来源剧本镜号 01-08（餐厅、电梯、办公室蒙太奇与工位删除消息段）。与基础形象**共享同一基底人物**（脸型/眼型/发型/婚戒/身高比例/微表情底色完全不变），仅服装与情绪强度变化。

**与基础形象差异**：
- 服装：雾灰家居针织衫 → 深灰职场针织衫；米白棉质内搭保持；深灰家居长裤 → 深灰直筒西装裤；白色家居拖鞋 → 低调通勤平底鞋
- 道具：左手持文件夹贴在身侧，右手攥住针织衫下摆
- 情绪：从"家居疲惫"换成"职场克制"——眉间微收、嘴角微敛、肩膀更收一档

**HSB 色板调整**：
- 🎨 暖黑发色：H=25, S=38, B=20，`#33251F`（不变）
- 🎨 暖粉底肌肤色：H=20, S=18, B=96，`#F5D5C4`（不变）
- 🎨 深灰职场针织衫：H=220, S=8, B=38，`#595D62`（替换雾灰家居款）
- 🎨 米白内搭：H=38, S=6, B=92，`#EBE6DD`（不变）
- 🎨 眼下淡青灰：H=215, S=12, B=58，`#828A94`（不变）

#### 【中文描述段】

电影级角色设定板（变体A·职场"没事"状态），横版大画幅 16:9，中性灰提案板背景，6 区块固定布局，与基础形象为同一人——精致鹅蛋脸+柔和尖下巴、水润杏眼+纤长睫毛+眼尾轻微下压+眼下淡青灰疲惫影、高挑鼻梁、暖黑中长发自然垂落锁骨、暖粉底瓷白光泽肌肤、165cm 身高、纤细匀称体型、素银婚戒位置严格不变。

【顶部细条】「成年女主·变体A 职场"没事"状态 · 28-32岁 · 身高 165cm · 电影级风格化写实 · 克制／职场抑制／嘴角微敛」。

【区块A 主视觉】左列·全高 24% 宽 × 94% 高（第一梯队·双主块之一·竖向贯通全高），85mm 全身正面演员气质立像，穿深灰职场针织衫 + 米白棉质内搭 + 深灰直筒西装裤 + 低调通勤平底鞋，左手持深灰薄文件夹贴在身侧、右手攥住针织衫下摆形成浅褶，肩膀微收、姿态在人前保持正常但眼底疲惫；金色细线身高刻度尺贴左缘。

【区块B 五视图】右列·上 48%×54%（第一梯队·画面最大主块），正/3·4正侧/纯侧/3·4背/背 5 视图横排，服装与道具持握严格一致，底线错位 ±2-4%。

【区块C 头部六视图】中列·下 28%×44%（第二梯队），正/3·4正侧/纯侧/低头/抬头/动态扭头 2×3，"动态扭头"放大 1.15× 偏出网格——抓"工位上被叫名字时职业化但短暂走神的回头"。

【区块D 情绪肖像】中列·上 28%×50%，50mm 中近景，眼神是"职场式'没事'微笑但眼底疲惫"——嘴角微敛却已习惯抬起、眉间未皱却紧绷、电梯灯下的克制疲倦。

【区块E 服装拆解】5 张 100mm 微距：① 深灰职场针织衫袖口（羊毛混纺、低反差织纹、袖口有轻微通勤起球感）；② 素银婚戒（细窄银圈、轻微划痕）；③ 深灰文件夹边缘（薄硬卡纸、被手指捏出浅压痕）；④ 攥紧针织衫下摆褶皱；⑤ 指关节偷暖粉红 SSS 透光的指尖；±3° 旋转拍立得感。

【区块F 色板】HSB：暖黑发 #33251F、暖粉底肌 #F5D5C4、深灰职场针织 #595D62、米白内搭 #EBE6DD、眼下淡青灰 #828A94 + 材质关键词「羊毛混纺/棉/卡纸/925银」+ 性格关键词「克制／职场抑制／嘴角微敛」+ 风格定位「电影级风格化写实」。

整张光源、皮肤 SSS、布料纤维、PBR/AO/Octane/UE5/8K 渲染参数与基础形象完全一致。

绝对禁止：办公室/电梯/电脑屏幕等场景背景出现，禁止任何脸型/年龄/婚戒/发型/身高漂移，禁止纯白纯黑、彩色光斑、散景、漂浮粒子、噪点、文字水印、塑料蜡像感、冷白假人脸。

#### 【English description block】

Cinematic character pitch board (Variant A · Workplace "I'm Fine" State), horizontal large-format 16:9, neutral gray pitch-board background, 6-zone fixed layout. Same character as base: identical refined oval face with soft pointed chin, watery almond eyes with slightly drooping outer corners and subtle blue-gray under-eye shadow, high nose bridge, warm black medium-long hair falling to collarbone, warm pink-undertone porcelain luminous skin, 165cm height, slim balanced body, plain silver wedding ring placement strictly unchanged.

[Top band] "Adult Female Lead · Variant A Workplace I'm Fine State · Age 28-32 · Height 165cm · Cinematic stylized realism · restrained / workplace suppression / corners-tight smile".

[Zone A] left column full height 24%×94% (Tier 1, main block · vertical full-height), 85mm full-body front portrait with actor presence, wearing dark gray workplace knit top + off-white cotton inner + dark gray straight suit trousers + understated commuter flats, left hand holding a thin dark gray folder against her side, right hand clutching the knit hem with shallow creases, shoulders slightly withdrawn, posture publicly composed but tiredness shows in the eyes; gold height ruler flush to left.

[Zone B] right column top 48%×54% (Tier 1, largest block), five 50mm full-body views in horizontal row (front / 3/4 front-side / pure side / 3/4 back / back), garment and folder identical, baseline staggered ±2-4%.

[Zone C] middle column lower 28%×44% (Tier 2), six head studies (front / 3/4 front-side / pure side / head down / head up / dynamic over-shoulder glance) 2×3, "over-shoulder" scaled 1.15× overflowing grid—captures the brief composed glance when called by name at the workstation.

[Zone D] middle column upper 28%×50%, 50mm mid-close portrait, eyes carry the workplace "I'm fine" micro-smile with fatigue beneath—corners habitually lifting but tight, brow tense without furrowing, restrained tiredness under elevator light.

[Zone E] five 100mm macro tiles: ① dark gray workplace knit cuff (wool blend, low-contrast weave, slight commuter pilling); ② plain silver wedding ring; ③ dark gray folder edge (thin cardstock with shallow finger press); ④ clutched knit hem creases; ⑤ fingertip with warm pink joint SSS translucency; rotated ±3° as if pinned.

[Zone F] HSB palette (warm black hair #33251F, warm pink skin #F5D5C4, dark gray workplace knit #595D62, off-white inner #EBE6DD, fatigue blue-gray #828A94) + material keywords + personality keywords "restrained / workplace suppression / corners-tight smile" + style direction.

Unified lighting, PBR skin with SSS, fabric fibers, PBR/AO/Octane/UE5/8K rendering identical to base.

Strictly forbidden: any office / elevator / computer screen scene background, any facial / age / wedding-ring / hair / height drift, no pure white or pure black background, no colored bokeh, no noise, no text watermark, no plastic wax-doll look, no cold-white mannequin face.

#### 【画面洁净负面约束】

不要耀斑、不要镜头 flare、不要散景光斑、不要漂浮粒子、不要噪点、不要胶片颗粒、不要场景背景、不要文字水印 logo、不要机械对称网格、不要全部微距小图正放、不要塑料蜡像感、不要冷白假人脸、不要任何角度脸型/年龄/服装/婚戒/发型漂移。

---

### 3.3 变体 B：夜晚胃疼睡衣状态

**变体说明**：来源剧本镜号 22-41（夜晚卧室/书房门缝核心高潮）。与基础形象**共享同一基底人物**，仅服装与情绪状态变化——隐忍式胃疼，不是夸张病弱。

**与基础形象差异**：
- 服装：雾灰针织开衫 → 奶茶色长袖棉质睡衣套装；下装也换为同色棉质睡裤
- 配件：素银婚戒保留
- 道具：右手攥睡衣下摆形成细褶，左手轻按腹部（不做夸张蜷缩）
- 情绪：克制痛感、嘴唇轻抿、眼眶湿润但不大哭

**HSB 色板调整**：
- 🎨 暖黑发色：H=25, S=38, B=20，`#33251F`（不变）
- 🎨 暖粉底肌肤色：H=20, S=18, B=96，`#F5D5C4`（不变）
- 🎨 奶茶棉质睡衣：H=30, S=16, B=86，`#DBCCB8`（替换针织衫）
- 🎨 睡衣暗褶影：H=28, S=18, B=48，`#7A675A`（新增）
- 🎨 手指泛白冷调：H=210, S=8, B=82，`#C2C9D1`（新增）

#### 【中文描述段】

电影级角色设定板（变体B·夜晚胃疼睡衣状态），横版大画幅 16:9，中性灰提案板背景，6 区块固定布局，与基础形象为同一人——精致鹅蛋脸+柔和尖下巴、水润杏眼+纤长睫毛+眼尾轻微下压+眼下淡青灰、高挑鼻梁、暖黑中长发垂落锁骨、暖粉底瓷白光泽肌肤、165cm、纤细匀称、素银婚戒严格不变。

【顶部细条】「成年女主·变体B 夜晚胃疼睡衣状态 · 28-32岁 · 身高 165cm · 电影级风格化写实 · 克制痛感／隐忍／不愿喊出"难受"」。

【区块A 主视觉】左列·全高 24%×94%（第一梯队·双主块之一·竖向贯通全高），85mm 全身正面演员气质立像，穿奶茶色长袖棉质睡衣上衣 + 同色棉质睡裤，赤脚或穿低调家居棉袜，右手攥睡衣下摆形成细密折痕，左手轻按腹部但姿态保持站立、不做夸张蜷缩；金色身高刻度尺贴左缘；微表情是"疼痛中仍想说'没事'的克制"——嘴唇轻抿、眼眶湿润但不落泪。

【区块B 五视图】右列·上 48%×54%（第一梯队·画面最大主块），正/3·4正侧/纯侧/3·4背/背 5 视图横排，睡衣套装与攥下摆动作严格一致，底线错位 ±2-4%。

【区块C 头部六视图】中列·下 28%×44%（第二梯队），正/3·4正侧/纯侧/低头/抬头/动态扭头 2×3，"动态扭头"放大 1.15× 偏出网格——抓"听到丈夫起身脚步声时的下意识扭头"。

【区块D 情绪肖像】中列·上 28%×50%，50mm 中近景，电影色调，眼神是"克制痛感的瞬间"——眉头微锁不展、嘴唇极轻抿、眼眶湿润反光、太阳穴几不可见的紧绷；与基础形象同光源同色温但情绪强度提升一档。

【区块E 服装拆解】5 张 100mm 微距：① 奶茶睡衣布料（薄棉、纤维清晰、走线规整）；② 素银婚戒；③ 攥紧睡衣下摆形成的细密折痕；④ 发白指节（指关节偷暖粉红 SSS 透光、按压腹部时指腹冷调泛白）；⑤ 湿润眼球反光特写；±3° 旋转拍立得感。

【区块F 色板】HSB：暖黑发 #33251F、暖粉底肌 #F5D5C4、奶茶睡衣 #DBCCB8、睡衣暗褶影 #7A675A、手指泛白冷调 #C2C9D1 + 材质关键词「薄棉/925银/SSS皮肤」+ 性格关键词「克制痛感／隐忍／不愿喊出难受」+ 风格定位「电影级风格化写实」。

整张光源、皮肤 SSS、PBR/AO/Octane/UE5/8K 渲染参数与基础形象一致。

绝对禁止：医院感、病床、绷带、伤口、血液、夸张痛苦表情、卧室/书房门缝/夜景背景、纯白纯黑、彩色光斑、散景、漂浮粒子、噪点、文字水印、塑料蜡像感、冷白假人脸、任何脸型/年龄/婚戒/发型/身高漂移。

#### 【English description block】

Cinematic character pitch board (Variant B · Night Stomach Pain Sleepwear State), horizontal large-format 16:9, neutral gray pitch-board background, 6-zone fixed layout. Same character as base: identical refined oval face, watery almond eyes with drooping outer corners and blue-gray under-eye shadow, high nose bridge, warm black medium-long hair to collarbone, warm pink-undertone porcelain luminous skin, 165cm height, plain silver wedding ring strictly unchanged.

[Top band] "Adult Female Lead · Variant B Night Stomach Pain Sleepwear State · Age 28-32 · Height 165cm · Cinematic stylized realism · restrained pain / forbearing / unwilling to cry out".

[Zone A] left column full height 24%×94% (Tier 1, main block · vertical full-height), 85mm full-body front portrait with actor presence, wearing beige milky-tea long-sleeve cotton pajama top + matching pajama trousers, bare feet or simple home cotton socks, right hand clutching pajama hem with fine creases, left hand lightly pressing abdomen but standing posture maintained without exaggerated curling; gold height ruler flush left; micro-expression is "restrained pain still wanting to say I'm fine"—lips lightly pressed, eyes moist but not crying.

[Zone B] right column top 48%×54% (Tier 1, largest block), five 50mm full-body views, pajama set and clutched-hem hand pose identical, baseline staggered ±2-4%.

[Zone C] middle column lower 28%×44% (Tier 2), six head studies 2×3, "over-shoulder glance" 1.15× overflowing grid—captures her instinctive turn when hearing her husband's footsteps.

[Zone D] middle column upper 28%×50%, 50mm mid-close portrait, cinematic tone; eyes capture the "moment of restrained pain"—brow lightly knit but not furrowed, lips faintly pressed, moist eye reflection, almost-imperceptible tension at the temple.

[Zone E] five 100mm macro tiles: ① milky-tea pajama fabric (thin cotton, visible fibers, neat stitching); ② plain silver wedding ring; ③ clutched hem fine creases; ④ pale knuckles (warm pink joint SSS translucency, fingertips cooling toward white when pressing abdomen); ⑤ moist eye reflection close-up; rotated ±3° as if pinned.

[Zone F] HSB palette (warm black hair #33251F, warm pink skin #F5D5C4, milky-tea pajama #DBCCB8, dark fold shadow #7A675A, cool-pale fingers #C2C9D1) + material keywords "thin cotton / 925 silver / SSS skin" + personality keywords "restrained pain / forbearing / unwilling to cry out" + style direction.

Unified lighting, PBR skin with SSS, PBR/AO/Octane/UE5/8K rendering identical to base.

Strictly forbidden: hospital feel, bed, bandage, wound, blood, exaggerated pain expression, bedroom / doorway / night scene background; no pure white / pure black, no colored bokeh, no floating particles, no noise, no text watermark, no plastic wax-doll look, no cold-white mannequin face, no facial / age / wedding-ring / hair / height drift.

#### 【画面洁净负面约束】

不要耀斑、不要镜头 flare、不要散景光斑、不要漂浮粒子、不要噪点、不要胶片颗粒、不要医院/病床/绷带/伤口/血液、不要夸张痛苦、不要场景背景、不要文字水印 logo、不要机械对称网格、不要全部微距小图正放、不要塑料蜡像感、不要冷白假人脸、不要任何角度脸型/年龄/婚戒/发型漂移。

---

## 四、角色 2：小女孩｜不敢说难受的童年女主

### 4.1 基础形象

#### 角色信息卡

```yaml
角色名称: 小女孩｜不敢说难受的童年女主
年龄: 7-9 岁
身高: 125cm（小学一二年级）
体型: 纤瘦、儿童正常发育、肩窄
风格方向: 电影级风格化写实（儿童年龄准确、不成人化、不低幼夸张）

性格关键词: 早熟懂事 / 怯生生 / 隐忍 / 不敢说难受 / 习惯性把话咽回去

外貌特征:
  脸型: 精致圆润童颜（婴儿肥未褪、柔和下巴）
  眼睛: 大而清澈的圆眼 + 纤长但稀疏的儿童睫毛 + 含水但不大哭、瞳孔反光小
  发型: 暖黑短中发略乱（齐耳到肩之间），额前有细碎汗湿发丝
  肤色: 暖粉底瓷白光泽肌肤，因发热脸颊轻微泛红，耳尖透粉 SSS 可见
  独特记忆点: 两只手捧着对她而言偏大的水杯 + 习惯性低头（把"妈妈我难受"咽回去）

服装设定:
  上装: 旧棉睡衣上衣（淡米粉色、洗旧褪色不均、领口轻微起毛）
  下装: 同色棉睡裤（衣摆略大）
  外层: 无（家中夜间）
  鞋子: 赤脚（脚部干净）
  配件: 无
  道具: 透明厚玻璃水杯（对她偏大、双手捧握、杯壁折射冷灰蓝高光）

场景气质: 被忽视的童年女主，深夜独自捧水杯走出房间寻求关注，过早懂事
```

#### HSB 色板（≥4 色）

- 🎨 童年暖黑发：H=24, S=42, B=18，`#2E211B`
- 🎨 暖粉底发热微红肤色：H=16, S=24, B=94，`#F0C4B0`
- 🎨 旧棉睡衣淡米粉：H=18, S=18, B=88，`#E0BDB4`
- 🎨 冷水杯透明灰蓝：H=205, S=15, B=88，`#BFD2E0`
- 🎨 眼眶轻红：H=355, S=20, B=80，`#CC9FA5`

#### 配饰/材质微距清单（5 件）

- 📌 旧棉睡衣领口：软棉布起毛，洗旧边缘，粉米色褪色不均
- 📌 小女孩指尖：暖粉底肌通透皮肤，指关节偷暖粉红，握杯用力指节微微泛白，指甲短圆，SSS 透光感可见
- 📌 透明厚玻璃水杯：杯壁折射，边缘冷灰蓝高光，无文字
- 📌 额前碎发：汗湿后贴近额角，发丝不结块、能看到根根分明
- 📌 眼眶微红特写：含水但未大哭，瞳孔反光小、下睫毛湿润但未挂泪

#### 【中文描述段】

电影级角色设定板，横版大画幅 16:9，中性灰提案板背景（#BEC1C4 至 #C7CACD 渐变，极轻微亚麻布纹/纸面纹理，无纯白无纯黑，禁止彩色光斑/散景虚化/场景元素）。整张画面被切为 6 个固定功能区块，构图被美术指导设计过、略带手作感、避免机械对称网格。

【顶部细条·标题区】横跨整张顶部 6% 高度，文字左对齐至主视觉右缘：「小女孩｜不敢说难受的童年女主 · 7-9岁 · 身高 125cm · 电影级风格化写实 · 早熟懂事／怯生生／隐忍／不敢说难受」，印刷标注统一用 Inter（西文/数字）+ 思源黑体（中文），手写注释统一用 Caveat（极少量），严禁第三种字体。

【区块A·主视觉角色立像】左列·全高 24% 宽 × 94% 高（第一梯队·双主块之一·竖向贯通全高），85mm 全身正面演员气质立像，自然站姿、肩膀轻收、头微低，重心一边略低一边略高带儿童正常摆动；7-9 岁亚洲小女孩，身高 125cm，纤瘦但儿童正常发育，头身比 5.5（儿童比例）；精致圆润童颜，婴儿肥未褪柔和下巴，大而清澈的圆眼+稀疏纤细儿童睫毛，含水但不大哭、瞳孔反光小，眼眶轻微泛红，小巧鼻梁鼻尖微翘+柔光高光，粉嫩自然唇色微张又闭回去；暖黑短中发略乱、额前有细碎汗湿发丝；暖粉底瓷白光泽肌肤，因发热脸颊轻微泛红，耳尖肩颈透粉 SSS 可见；穿洗旧淡米粉色棉质长袖睡衣套装（衣摆略大）、赤脚但脚部干净；两只手捧着一个对她而言偏大的透明厚玻璃水杯，肩膀轻收，头微低，动作像把"妈妈我难受"咽回去——这是她最具记忆点的姿态。立像左侧紧贴金色细线竖向身高刻度尺（2% 宽），标头/肩/腰/膝/脚踝高度与 cm 数字（顶端约 125cm）。

【区块B·全身多角度转面图】右列·上 48%×54%（第一梯队·画面最大主块），正面 → 3/4 正侧 → 纯侧面 → 3/4 背 → 背面 5 视图横排，每个 50mm 全身像，儿童圆润五官/头身比/暖黑短中发/旧棉睡衣/双手捧水杯/赤脚动作严格一致；底线允许 ±2-4% 错位（中间纯侧面下沉 3-4%，两侧上浮 2%）。

【区块C·头部研究图】中列·下 28%×44%（第二梯队），6 张头部研究：正面 / 3/4 正侧 / 纯侧面 / 低头 / 抬头 / 动态扭头（被叫到名字时下意识抬头），2 行 × 3 列，每张 85-105mm 头部特写；圆润童颜/大圆眼/小巧鼻梁/汗湿额前碎发/眼眶轻红与主视觉严格一致；其中"动态扭头"放大 1.15× 偏出网格 8%——抓"被妈妈不耐烦回应后下意识缩回去的转脸瞬间"。

【区块D·电影感情绪肖像】中列·上 28%×50%（第二梯队·定情绪脸），50mm 中近景肖像（半身或捧杯特写），偏左对齐留右呼吸；电影色调克制、保留 SSS 透粉肤感+脸颊发热轻微泛红；眼神是"说出'妈妈我难受'前最后一秒的迟疑"——嘴唇微张、眼眶湿润、瞳孔反光小、下颌轻微紧绷；与主视觉同光源同色温但情绪强度提升一档。

【区块E·服装与配件拆解】右列·下横条 48%×20%（第三梯队·堆叠于 B 之下），5 张 100mm 微距细节拍立得感小图：① 旧棉睡衣领口（软棉布起毛、洗旧边缘、粉米色褪色不均）；② 小女孩指尖捧杯（暖粉底通透皮肤、指关节偷暖粉红、握杯指节泛白、指甲短圆、SSS 透光）；③ 透明厚玻璃水杯（杯壁折射、边缘冷灰蓝高光、无文字、水面微动）；④ 额前汗湿碎发（发丝根根分明、贴近额角、不结块）；⑤ 眼眶微红特写（含水但未大哭、下睫毛湿润、瞳孔反光小）；±3° 旋转拍立得感，用 Caveat 手写体细线标注材质名（旧棉/玻璃/儿童肌肤/发丝）。

【区块F·美术备注与色板】右列·中横条 48%×20%（第三梯队·堆叠于 B 之下），HSB 色板（童年暖黑发 H=24 S=42 B=18 `#2E211B`、暖粉底发热微红肤色 H=16 S=24 B=94 `#F0C4B0`、旧棉睡衣淡米粉 H=18 S=18 B=88 `#E0BDB4`、冷水杯透明灰蓝 H=205 S=15 B=88 `#BFD2E0`、眼眶轻红 H=355 S=20 B=80 `#CC9FA5`）+ 材质关键词「旧棉/厚玻璃/SSS儿童肌肤/汗湿发丝」+ 性格关键词「早熟懂事／怯生生／隐忍／不敢说难受」+ 风格定位「电影级风格化写实·儿童年龄准确」。

整张光源统一：电影级柔光美人布光 5200-5600K，大柔光箱蝶形/环形主光从右上 45° 制造颧骨与鼻翼柔和立体，左侧低强度冷色补光（光比约 3:1、保留立体而非平光洗白），一道低强度发丝轮廓光把发缘与背景分离，双眼 10–11 点钟方向明亮 catchlight 眼神光；皮肤 PBR + SSS（耳尖肩颈透粉、指关节偷暖粉红、鼻尖柔光、明暗极柔过渡），棉布纤维清晰，玻璃真实折射但不过亮高光；AXIS 顶级人物 CG 质感，2.5D 动漫-CG 融合渲染，影视级游戏CG·次世代3A质感·超写实PBR材质渲染 + AO + SSS + Octane Render + Unreal Engine 5 + 4K极致细节，柔光电影打光（低强度轮廓光勾边 + 发丝光透发 + 柔光镜柔化）+ 浅景深小景深焦外柔化，发丝级细节，儿童头身比与年龄特征严格保留。

绝对禁止：成人化、网红化、低幼夸张可爱化、夸张病态、卧室/厨房/医院/体温计等场景元素、纯白纯黑背景、彩色光斑、散景、漂浮粒子、噪点、文字水印、塑料蜡像感、冷白假人脸、任何角度年龄/比例/服装漂移。

#### 【English description block】

Cinematic character pitch board, horizontal large-format 16:9, neutral gray pitch-board background gradient #BEC1C4 to #C7CACD with subtle linen weave / paper grain texture, no pure white, no pure black, no colored bokeh, no scene elements; art-directed slightly hand-laid composition.

[Top band] full top width 6% high, text left-aligned to right edge of main visual: "Little Girl | The Childhood Female Lead Who Doesn't Dare Say She Feels Unwell · Age 7-9 · Height 125cm · Cinematic stylized realism · precocious / timid / forbearing / dares not voice discomfort", printed labels strictly in Inter (Latin/numerals) + Source Han Sans (CJK), handwritten notes strictly in Caveat (minimal), no third typeface.

[Zone A · Hero portrait] left column full height 24%×94% (Tier 1, main block · vertical full-height), 85mm full-body front portrait with actor presence, natural stance, shoulders slightly withdrawn, head slightly lowered, weight subtly uneven with normal childlike sway; 7-9 year old Asian girl, height 125cm, slim but normally developed, head-to-body ratio ~5.5 (child proportion); refined round child face with unfaded baby fat and soft chin, large clear round eyes with sparse delicate child eyelashes, moist but not crying, small pupil reflection, slight rim redness, small upturned nose bridge with soft tip highlight, naturally pink moist child lips parted then closed; warm black slightly messy short-medium hair with subtle damp bangs near forehead; warm pink-undertone porcelain luminous skin with lightly flushed feverish cheeks, visible SSS pink translucency on ear tips and shoulders; old pale beige-pink long-sleeve cotton pajamas with slightly oversized hem, clean bare feet; both hands holding an oversized transparent thick-glass water cup, shoulders slightly withdrawn, head lowered as if swallowing back the words "Mommy I feel unwell"—her most memorable signature pose. Gold thin vertical height ruler (2% width) flush to left edge marking head/shoulder/waist/knee/ankle heights, top reading ~125cm.

[Zone B · Turnaround] right column top 48%×54% (Tier 1, largest block), five 50mm full-body views in horizontal row (front / 3/4 front-side / pure side / 3/4 back / back); round child features, head-to-body ratio, warm black short hair, old cotton pajamas, cup-holding pose, bare feet identical to Zone A; baseline staggered ±2-4%.

[Zone C · Head studies] middle column lower 28%×44% (Tier 2), six head studies (front / 3/4 front-side / pure side / head down / head up / dynamic head-turn—the instinctive look-up when called by name) 2×3, all features identical to Zone A; "head-turn" portrait scaled 1.15× and overflowing grid 8%—captures the moment she shrinks back after her mother's impatient response.

[Zone D · Emotional portrait] middle column upper 28%×50% (Tier 2, the emotion face), 50mm mid-close portrait (chest-up or cup-holding closeup), breathing space on right, cinematic restrained tone, preserved SSS skin with feverish cheek pink; eyes capture "the last second of hesitation before saying Mommy I feel unwell"—lips parting, eyes moist, small pupil reflection, jaw subtly tight; same lighting as main visual, emotional intensity escalated one notch.

[Zone E · Wardrobe & accessory breakdown] right column, lower bar, 48%×20% (Tier 3, stacked below Zone B), five 100mm macro Polaroid tiles: ① old cotton pajama collar (softened cotton with edge fuzz, worn-out faded edge, uneven pale pink); ② child fingertips holding cup (warm pink-undertone translucent skin, joint warm pink flush, knuckles whitening from grip, short rounded nails, SSS); ③ transparent thick-glass water cup (refractive walls, cool gray-blue rim highlights, no text, slightly moving water); ④ damp forehead bangs (individual hair strands visible, sticking to temples, not clumped); ⑤ red-rimmed eye closeup (moist but not crying, lower lashes wet, small pupil reflection); each rotated ±3° as if pinned, handwritten labels "old cotton / glass / child skin / damp hair".

[Zone F · Art notes] right column, middle bar, 48%×20% (Tier 3, stacked below Zone B), HSB palette (warm black hair H=24 S=42 B=18 #2E211B, feverish warm pink skin H=16 S=24 B=94 #F0C4B0, old pajama pale pink H=18 S=18 B=88 #E0BDB4, cool glass H=205 S=15 B=88 #BFD2E0, eye-rim red H=355 S=20 B=80 #CC9FA5) + material keywords "old cotton / thick glass / SSS child skin / damp hair" + personality keywords "precocious / timid / forbearing / dares not voice discomfort" + style direction "cinematic stylized realism · age-accurate child".

Unified lighting: soft cinematic beauty lighting 5200-5600K, large softbox butterfly/loop key from upper right at 45° giving gentle cheekbone and nose-side dimensionality, low-intensity cool fill from left (about 3:1 ratio, dimensional not a flat wash), a low-intensity hair rim light separating hair from the background, bright catchlight in both eyes at 10-11 o'clock; PBR skin with SSS, soft nose tip highlight, joint warm pink flush, ultra-soft shadow transitions; cotton fibers visible, glass shows real refraction without blown highlights; AXIS top-tier character CG quality, 2.5D anime-CG hybrid rendering, cinematic game CG, next-gen AAA quality, hyper-realistic PBR material rendering + AO + SSS + Octane Render + Unreal Engine 5, 4K ultra-detailed, soft cinematic lighting (low-intensity rim light + hair light + soft-focus diffusion) + shallow depth of field, hair-strand detail, age-accurate child proportions strictly preserved.

Strictly forbidden: adult-like rendering, glamour, infantile exaggerated cuteness, severe illness, bedroom / kitchen / hospital / thermometer scene elements, pure white / pure black background, colored bokeh, floating particles, noise, text watermark, plastic wax-doll look, cold-white mannequin face, any age / proportion / clothing drift.

#### 【画面洁净负面约束】

不要耀斑、不要镜头 flare、不要散景光斑、不要漂浮粒子、不要噪点、不要胶片颗粒、不要卧室/厨房/医院/体温计场景背景、不要严重病态/夸张可爱化/成人化、不要文字水印 logo、不要机械对称网格、不要全部微距小图正放、不要塑料蜡像感、不要冷白假人脸、不要任何角度年龄/比例/服装漂移。

#### T0 自检清单

**版面区块完整性**
- [ ] 顶部细条标题区
- [ ] 区块 A 主视觉立像 + 金色身高刻度尺（顶端 125cm）
- [ ] 区块 B 全身 5 视图（含双手捧杯姿态一致）
- [ ] 区块 C 头部 6 视图（含动态扭头略大偏出网格）
- [ ] 区块 D 电影感情绪肖像（捧杯特写或半身）
- [ ] 区块 E 5 张材质微距（旧棉领口/捧杯指尖/玻璃水杯/汗湿碎发/眼眶微红）
- [ ] 区块 F HSB 色板 5 色 + HEX

**一致性核对**
- [ ] 圆润童颜+婴儿肥未褪在 A/B/C/D 一致
- [ ] 大圆眼+稀疏儿童睫毛+眼眶轻红在 A/B/C/D 一致
- [ ] 暖黑短中发+额前汗湿碎发在 A/B/C/D 一致
- [ ] 旧棉淡米粉睡衣套装在 A/B 一致
- [ ] 双手捧大水杯姿态在 A/B 一致
- [ ] 头身比 5.5（儿童比例）严格保留、不成人化

**材质真实性**
- [ ] 皮肤 PBR + SSS + 脸颊发热轻微泛红 + 耳尖肩颈透粉
- [ ] 旧棉布纤维 / 起毛领口 / 褪色不均三层细节可见
- [ ] 厚玻璃真实折射、冷灰蓝边缘高光不过亮
- [ ] 汗湿发丝根根分明、不结块

**背景与画面洁净**
- [ ] 中性灰提案板背景非纯白/纯黑
- [ ] 极轻微亚麻布纹/纸纹存在
- [ ] 无卧室/厨房/医院/体温计场景元素
- [ ] 无耀斑/散景/漂浮粒子/噪点/水印

**美术指导气质**
- [ ] 整张图略带不对称感、有手作贴板感
- [ ] 微距小图非全部正放
- [ ] 头部研究"动态扭头"略大偏出网格
- [ ] 五视图底线非完全平齐
- [ ] 演员气质（儿童真实呼吸/重心）非摆拍模特

---

## 五、角色 3：母亲｜疲惫不耐烦的房门内侧母亲

### 5.1 基础形象

#### 角色信息卡

```yaml
角色名称: 母亲｜疲惫不耐烦的房门内侧母亲
年龄: 约 40 岁
身高: 162cm
体型: 普通中年女性、肩膀略前倾、腰腹自然
风格方向: 电影级风格化写实（中年生活感、保留年龄特征、不反派化）

性格关键词: 疲惫 / 不耐烦 / 半夜被打扰的烦躁 / 无意识伤人 / 不是恶毒只是普通

外貌特征:
  脸型: 柔和鹅蛋脸 + 眼尾微下垂（年龄感）
  眼睛: 杏眼但睫毛不浓密 + 眼下灰褐色疲惫阴影 + 眉间有轻微浅纹
  发型: 深棕短发略乱（齐耳短发，洗后未打理）
  肤色: 暖粉底瓷白光泽肌肤带轻微疲惫暗沉，保留轻微年龄细线
  独特记忆点: 半夜被打扰的疲惫皱眉 + 无意识伤人的门缝距离感

服装设定:
  上装: 米白棉质内搭（洗旧、领口轻微松弛）
  下装: 深灰家居棉裤
  外层: 暗灰宽松家居外套（旧棉混纺、肩部轻微塌陷、袖口无装饰）
  鞋子: 简单家居拖鞋（低调）
  配件: 无（不戴婚戒首饰）
  道具: 无

场景气质: 现实普通中年母亲，半夜被打扰后的疲惫皱眉，不是反派只是没耐心
```

#### HSB 色板（≥4 色）

- 🎨 深棕短发：H=24, S=48, B=22，`#38271D`
- 🎨 暖粉底疲惫肤色：H=22, S=18, B=90，`#E6C8B6`
- 🎨 暗灰家居外套：H=220, S=5, B=36，`#56585C`
- 🎨 米白内搭：H=38, S=8, B=90，`#E6E0D3`
- 🎨 眼下阴影灰褐：H=30, S=12, B=48，`#7A7067`

#### 配饰/材质微距清单（5 件）

- 📌 暗灰家居外套：旧棉混纺，肩部轻微塌陷，袖口无装饰、纤维起毛感
- 📌 米白内搭领口：洗旧棉布，领口轻微松弛、走线自然
- 📌 眼下疲惫色影：轻微黑眼圈与眉间浅皱，精致五官结构保持清晰
- 📌 手背皮肤：暖粉底肌通透皮肤，指关节偷暖粉红，保留轻微年龄细线，短指甲，无精致美甲
- 📌 嘴角与下颌线：嘴唇偏干燥自然偏暗，下颌线柔和但有轻微年龄松弛感

#### 【中文描述段】

电影级角色设定板，横版大画幅 16:9，中性灰提案板背景（#BEC1C4 至 #C7CACD 渐变，极轻微亚麻布纹/纸面纹理，无纯白无纯黑，禁止彩色光斑/散景虚化/场景元素）。整张画面被切为 6 个固定功能区块，构图被美术指导设计过、略带手作感、避免机械对称网格。

【顶部细条·标题区】横跨整张顶部 6% 高度，文字左对齐至主视觉右缘：「母亲｜疲惫不耐烦的房门内侧母亲 · 约40岁 · 身高 162cm · 电影级风格化写实 · 疲惫／不耐烦／半夜被打扰的烦躁／无意识伤人」，印刷标注统一用 Inter（西文/数字）+ 思源黑体（中文），手写注释统一用 Caveat（极少量），严禁第三种字体。

【区块A·主视觉角色立像】左列·全高 24% 宽 × 94% 高（第一梯队·双主块之一·竖向贯通全高），85mm 全身正面演员气质立像，姿态略疲惫、肩膀前倾、手臂自然垂下、不做反派姿势；约 40 岁现实普通中年女性，身高 162cm，体型普通中年女性、腰腹自然、肩膀略前倾、头身比 7（中年比例）；柔和鹅蛋脸+眼尾微下垂带年龄感，杏眼但睫毛不浓密+眼下灰褐色疲惫阴影+眉间轻微浅纹，鼻梁挺秀+鼻尖柔和高光，唇色偏干燥自然偏暗；深棕短发略乱（齐耳，洗后未打理）；暖粉底瓷白光泽肌肤带轻微疲惫暗沉，保留轻微年龄细线但仍有 SSS 透光（耳尖肩颈淡粉）；穿暗灰宽松家居外套（旧棉混纺、肩部轻微塌陷、袖口无装饰）+ 米白棉质内搭（洗旧、领口轻微松弛）+ 深灰家居棉裤 + 简单家居拖鞋；表情不是恶毒而是"半夜被打扰后的疲惫皱眉"——眉间微锁、嘴角无笑、眼神涣散无攻击性。立像左侧紧贴金色细线竖向身高刻度尺（2% 宽），标头/肩/腰/膝/脚踝高度与 cm 数字（顶端约 162cm）。

【区块B·全身多角度转面图】右列·上 48%×54%（第一梯队·画面最大主块），正面 → 3/4 正侧 → 纯侧面 → 3/4 背 → 背面 5 视图横排，每个 50mm 全身像，柔和鹅蛋脸+眼尾下垂/杏眼+眼下阴影/深棕短发/暗灰家居外套+米白内搭+深灰棉裤+家居拖鞋/略前倾肩膀严格一致；底线允许 ±2-4% 错位。

【区块C·头部研究图】中列·下 28%×44%（第二梯队），6 张头部研究：正面 / 3/4 正侧 / 纯侧面 / 低头 / 抬头 / 动态扭头（半夜被叫醒后的下意识皱眉转脸），2 行 × 3 列，每张 85-105mm 头部特写；柔和鹅蛋脸/眼尾下垂/杏眼+稀疏睫毛/眼下灰褐疲惫影/眉间浅纹/深棕短发与主视觉严格一致；其中"动态扭头"放大 1.15× 偏出网格 8%——抓"被孩子敲门后第一反应的不耐烦皱眉"。

【区块D·电影感情绪肖像】中列·上 28%×50%（第二梯队·定情绪脸），50mm 中近景肖像（半身），偏左对齐留右呼吸；电影色调克制、保留 SSS 透粉肤感+疲惫暗沉对比；眼神是"半夜被打扰后的疲惫不耐烦但不恶毒"——眉间微锁、嘴角无笑、眼神涣散、太阳穴轻微紧绷；与主视觉同光源同色温但情绪强度提升一档。

【区块E·服装与配件拆解】右列·下横条 48%×20%（第三梯队·堆叠于 B 之下），5 张 100mm 微距细节拍立得感小图：① 暗灰家居外套袖口（旧棉混纺、纤维起毛、肩部塌陷感）；② 米白内搭领口（洗旧棉布、领口轻微松弛、走线自然）；③ 眼下灰褐疲惫色影（轻微黑眼圈+眉间浅皱、五官结构清晰）；④ 手背皮肤（暖粉底通透、指关节偷暖粉红、轻微年龄细线、短指甲无美甲）；⑤ 嘴角与下颌线（嘴唇偏干燥偏暗、下颌线柔和但有年龄松弛感）；±3° 旋转拍立得感，用 Caveat 手写体细线标注材质名（旧棉混纺/洗旧棉布/中年皮肤/年龄细线）。

【区块F·美术备注与色板】右列·中横条 48%×20%（第三梯队·堆叠于 B 之下），HSB 色板（深棕短发 H=24 S=48 B=22 `#38271D`、暖粉底疲惫肤色 H=22 S=18 B=90 `#E6C8B6`、暗灰家居外套 H=220 S=5 B=36 `#56585C`、米白内搭 H=38 S=8 B=90 `#E6E0D3`、眼下阴影灰褐 H=30 S=12 B=48 `#7A7067`）+ 材质关键词「旧棉混纺/洗旧棉布/中年 SSS 皮肤/年龄细线」+ 性格关键词「疲惫／不耐烦／半夜被打扰／无意识伤人」+ 风格定位「电影级风格化写实·中年生活感·保留年龄特征」。

整张光源统一：电影级柔光美人布光 5200-5600K，大柔光箱蝶形/环形主光从右上 45° 制造颧骨与鼻翼柔和立体，左侧低强度冷色补光（光比约 3:1、保留立体而非平光洗白），一道低强度发丝轮廓光把发缘与背景分离，双眼 10–11 点钟方向明亮 catchlight 眼神光；皮肤 PBR + SSS（耳尖肩颈淡粉、关节偷暖粉红、鼻梁柔光、明暗极柔过渡），保留中年皮肤特征但仍真实通透；旧棉混纺纤维清晰；AXIS 顶级人物 CG 质感，2.5D 动漫-CG 融合渲染，影视级游戏CG·次世代3A质感·超写实PBR材质渲染 + AO + SSS + Octane Render + Unreal Engine 5 + 4K极致细节，柔光电影打光（低强度轮廓光勾边 + 发丝光透发 + 柔光镜柔化）+ 浅景深小景深焦外柔化，发丝级细节，中年女性年龄特征严格保留但精致五官结构清晰。

绝对禁止：反派化、恶毒感、恐怖脸、过度美化年轻化、卧室门口/夜景戏剧性阴影/家庭场景背景、纯白纯黑、彩色光斑、散景、漂浮粒子、噪点、文字水印、塑料蜡像感、冷白假人脸、任何角度年龄/比例/发型/服装漂移。

#### 【English description block】

Cinematic character pitch board, horizontal large-format 16:9, neutral gray pitch-board background gradient #BEC1C4 to #C7CACD with subtle linen weave / paper grain texture, no pure white, no pure black, no colored bokeh, no scene elements; art-directed slightly hand-laid composition.

[Top band] full top width 6% high, text left-aligned to right edge of main visual: "Mother | The Tired Impatient Mother Behind the Bedroom Door · Around 40 · Height 162cm · Cinematic stylized realism · weary / impatient / midnight-disturbance irritability / unintentionally hurtful", printed labels strictly in Inter (Latin/numerals) + Source Han Sans (CJK), handwritten notes strictly in Caveat (minimal), no third typeface.

[Zone A · Hero portrait] left column full height 24%×94% (Tier 1, main block · vertical full-height), 85mm full-body front portrait with actor presence, slightly tired posture, shoulders forward, arms naturally hanging, no villain pose; realistic ordinary mother around 40, height 162cm, normal middle-aged body with natural waist, slightly forward shoulders, head-to-body ratio ~7; gentle oval face with slightly drooping eye corners showing age, almond eyes with sparse mature lashes, gray-brown under-eye fatigue shadow, subtle brow frown line, straight nose bridge with soft tip highlight, naturally muted dry-toned lip color; dark brown slightly messy short hair (bob length, post-shower un-styled); warm pink-undertone porcelain luminous skin with subtle fatigue darkening, preserved subtle age lines but still with SSS translucency (ear tips and shoulders pink); wearing dark gray loose home jacket (worn cotton blend with slight shoulder slump, undecorated cuffs) + off-white cotton inner top (worn-soft with slightly loose collar) + dark gray home cotton trousers + simple home slippers; expression is not malicious but "tired frown after being awakened at night"—brow lightly knit, mouth without smile, eyes vacant without aggression. Gold thin vertical height ruler (2% width) flush to left, top reading ~162cm.

[Zone B · Turnaround] right column top 48%×54% (Tier 1, largest block), five 50mm full-body views (front / 3/4 front-side / pure side / 3/4 back / back), gentle oval face with drooping eye corners, dark brown short hair, dark gray home jacket + off-white inner + dark gray cotton trousers + slippers, slightly forward shoulders all identical to Zone A; baseline staggered ±2-4%.

[Zone C · Head studies] middle column lower 28%×44% (Tier 2), six head studies (front / 3/4 front-side / pure side / head down / head up / dynamic head-turn—the instinctive irritated frown when knocked at night) 2×3, all features identical to Zone A; "head-turn" portrait scaled 1.15× and overflowing grid 8%—captures the first-reaction impatient frown when her child knocks.

[Zone D · Emotional portrait] middle column upper 28%×50% (Tier 2, the emotion face), 50mm mid-close portrait, breathing space on right, cinematic restrained tone with preserved SSS pink and fatigue darkening contrast; eyes capture "tired impatience after midnight disturbance, not malicious"—brow lightly knit, mouth without smile, eyes vacant, temple subtly tense; same lighting as main visual, emotional intensity escalated one notch.

[Zone E · Wardrobe & accessory breakdown] right column, lower bar, 48%×20% (Tier 3, stacked below Zone B), five 100mm macro Polaroid tiles: ① dark gray home jacket cuff (worn cotton blend, fiber fuzz, shoulder slump); ② off-white inner collar (worn cotton, slightly loose collar, natural stitching); ③ gray-brown under-eye fatigue shadow (subtle dark circles + brow line, refined features still clear); ④ hand back skin (warm pink translucent, joint warm pink flush, subtle age lines, short nails no manicure); ⑤ mouth corner and jawline (dry muted lips, soft jaw with subtle age looseness); rotated ±3° as if pinned, handwritten labels "worn cotton blend / worn cotton / mid-age skin / age lines".

[Zone F · Art notes] right column, middle bar, 48%×20% (Tier 3, stacked below Zone B), HSB palette (dark brown hair H=24 S=48 B=22 #38271D, fatigue warm pink skin H=22 S=18 B=90 #E6C8B6, dark gray home jacket H=220 S=5 B=36 #56585C, off-white inner H=38 S=8 B=90 #E6E0D3, under-eye gray-brown H=30 S=12 B=48 #7A7067) + material keywords "worn cotton blend / worn cotton / mid-age SSS skin / age lines" + personality keywords "weary / impatient / midnight-disturbance irritability / unintentionally hurtful" + style direction "cinematic stylized realism · mid-age life feel · age features preserved".

Unified lighting: soft cinematic beauty lighting 5200-5600K, large softbox butterfly/loop key from upper right at 45° giving gentle cheekbone and nose-side dimensionality, low-intensity cool fill from left (about 3:1 ratio, dimensional not a flat wash), a low-intensity hair rim light separating hair from the background, bright catchlight in both eyes at 10-11 o'clock; PBR skin with SSS preserving mid-age characteristics but still realistically translucent; worn cotton blend fibers visible; AXIS top-tier character CG quality, 2.5D anime-CG hybrid rendering, cinematic game CG, next-gen AAA quality, hyper-realistic PBR material rendering + AO + SSS + Octane Render + Unreal Engine 5, 4K ultra-detailed, soft cinematic lighting (low-intensity rim light + hair light + soft-focus diffusion) + shallow depth of field, hair-strand detail, mid-age female age features strictly preserved with refined facial structure clear.

Strictly forbidden: villainization, malicious appearance, horror face, over-beautified youthification, bedroom doorway / dramatic night shadow / family scene background, pure white / pure black, colored bokeh, floating particles, noise, text watermark, plastic wax-doll look, cold-white mannequin face, any age / proportion / hair / clothing drift.

#### 【画面洁净负面约束】

不要耀斑、不要镜头 flare、不要散景光斑、不要漂浮粒子、不要噪点、不要胶片颗粒、不要反派化/恶毒感/恐怖脸/过度美化年轻化、不要卧室门口/夜景戏剧性阴影/家庭场景背景、不要文字水印 logo、不要机械对称网格、不要全部微距小图正放、不要塑料蜡像感、不要冷白假人脸、不要任何角度年龄/比例/发型/服装漂移。

#### T0 自检清单

**版面区块完整性**
- [ ] 顶部细条标题区
- [ ] 区块 A 主视觉立像 + 金色身高刻度尺（顶端 162cm）
- [ ] 区块 B 全身 5 视图（含略前倾肩膀疲惫姿态一致）
- [ ] 区块 C 头部 6 视图（含动态扭头略大偏出网格）
- [ ] 区块 D 电影感情绪肖像（不耐烦但不恶毒）
- [ ] 区块 E 5 张材质微距（外套袖口/内搭领口/眼下疲惫影/手背年龄细线/嘴角下颌）
- [ ] 区块 F HSB 色板 5 色 + HEX

**一致性核对**
- [ ] 柔和鹅蛋脸+眼尾下垂在 A/B/C/D 一致
- [ ] 杏眼+稀疏睫毛+眼下灰褐疲惫影+眉间浅纹在 A/B/C/D 一致
- [ ] 深棕齐耳短发略乱在 A/B/C/D 一致
- [ ] 暗灰家居外套+米白内搭+深灰棉裤+家居拖鞋在 A/B 一致
- [ ] 略前倾肩膀的疲惫姿态在 A/B 一致
- [ ] 中年比例（头身比 7）严格保留、不年轻化、不反派化

**材质真实性**
- [ ] 皮肤 PBR + SSS + 中年特征保留 + 年龄细线轻微但精致五官清晰
- [ ] 旧棉混纺纤维清晰、肩部塌陷感真实
- [ ] 米白棉布洗旧领口松弛感真实
- [ ] 短指甲无美甲、手背年龄细线轻微

**背景与画面洁净**
- [ ] 中性灰提案板背景非纯白/纯黑
- [ ] 极轻微亚麻布纹/纸纹存在
- [ ] 无卧室门口/夜景/家庭场景元素
- [ ] 无耀斑/散景/漂浮粒子/噪点/水印

**美术指导气质**
- [ ] 整张图略带不对称感、有手作贴板感
- [ ] 微距小图非全部正放
- [ ] 头部研究"动态扭头"略大偏出网格
- [ ] 五视图底线非完全平齐
- [ ] 演员气质（疲惫真实呼吸/重心）非摆拍模特、非反派化

---

## 六、角色 4：丈夫｜先做事后说话的现实伴侣

### 6.1 基础形象

#### 角色信息卡

```yaml
角色名称: 丈夫｜先做事后说话的现实伴侣
年龄: 30 岁左右
身高: 178cm
体型: 普通偏瘦、肩宽适中、不夸张
风格方向: 电影级风格化写实（现实伴侣感、不霸总、不偶像化）

性格关键词: 温厚 / 坚定 / 关切 / 沉稳 / 不善辞令但行动稳定

外貌特征:
  脸型: 窄长脸型 + 清晰下颌线
  眼睛: 温厚坚定眼型 + 眉型利落 + 眼神有一点红来自着急和心疼（不煽情）
  发型: 自然黑短发，精神剪裁
  肤色: 暖粉底瓷白光泽肌肤健康通透
  独特记忆点: 稳定的手部动作（拧瓶盖、摸杯壁、不抖）+ 不是霸总而是生活里能接住人的伴侣

服装设定:
  上装: 深蓝灰棉麻家居衬衫（细纱织纹、袖口可自然卷起）
  下装: 暖灰居家长裤（家居棉质）
  外层: 普通家居外套（金属拉链、边缘有细微使用痕迹）/ 无
  鞋子: 深色拖鞋
  配件: 无（不戴婚戒首饰，与女主形成手部动作呼应）
  道具: 透明水杯（温水浅琥珀高光）/ 拧水瓶盖动作

场景气质: 现实伴侣，30 岁左右普通丈夫，不是霸道总裁也不是浪漫海报型
```

#### HSB 色板（≥4 色）

- 🎨 自然黑发：H=28, S=35, B=16，`#29201B`
- 🎨 暖粉底健康肤色：H=20, S=15, B=95，`#F2D8CC`
- 🎨 深蓝灰家居衬衫：H=215, S=25, B=32，`#3D4952`
- 🎨 暖灰居家长裤：H=35, S=8, B=48，`#7A756D`
- 🎨 温水高光琥珀：H=38, S=30, B=86，`#DBBC82`

#### 配饰/材质微距清单（5 件）

- 📌 深蓝灰棉麻衬衫：细纱织纹，袖口自然卷起，非商务西装质感
- 📌 手部拧瓶动作参考：手背筋线自然，指节清楚，动作稳定不抖
- 📌 透明水杯边缘：杯壁折射，温水浅琥珀高光
- 📌 外套拉链：普通家居外套金属拉链，边缘有细微使用痕迹（不闪亮）
- 📌 眼部表情：眼睛有一点红来自着急和心疼，不做煽情泪眼

#### 【中文描述段】

电影级角色设定板，横版大画幅 16:9，中性灰提案板背景（#BEC1C4 至 #C7CACD 渐变，极轻微亚麻布纹/纸面纹理，无纯白无纯黑，禁止彩色光斑/散景虚化/场景元素）。整张画面被切为 6 个固定功能区块，构图被美术指导设计过、略带手作感、避免机械对称网格。

【顶部细条·标题区】横跨整张顶部 6% 高度，文字左对齐至主视觉右缘：「丈夫｜先做事后说话的现实伴侣 · 30岁左右 · 身高 178cm · 电影级风格化写实 · 温厚／坚定／关切／沉稳／不善辞令但行动稳定」，印刷标注统一用 Inter（西文/数字）+ 思源黑体（中文），手写注释统一用 Caveat（极少量），严禁第三种字体。

【区块A·主视觉角色立像】左列·全高 24% 宽 × 94% 高（第一梯队·双主块之一·竖向贯通全高），85mm 全身正面演员气质立像，自然站姿、重心略偏一侧、肩颈带真实呼吸感与肌肉张力，不做偶像站姿；30 岁左右现实普通丈夫，身高 178cm，普通偏瘦、肩宽适中、头身比 7.8（成年男性比例）；窄长脸型+清晰下颌线，温厚坚定眼型+眉型利落+眼神有一点着急的心疼但不泪眼，高挑鼻梁+鼻尖柔和高光，薄唇自然血色；自然黑短发精神剪裁；暖粉底瓷白光泽肌肤健康通透，肩颈耳尖 SSS 透粉；穿深蓝灰棉麻家居衬衫（袖口自然卷起到小臂）+ 暖灰居家长裤 + 深色拖鞋；左手自然垂下，右手习惯性摸过水杯（或手中握一只温水杯），姿态自然不偶像。立像左侧紧贴金色细线竖向身高刻度尺（2% 宽），标头/肩/腰/膝/脚踝高度与 cm 数字（顶端约 178cm）。

【区块B·全身多角度转面图】右列·上 48%×54%（第一梯队·画面最大主块），正面 → 3/4 正侧 → 纯侧面 → 3/4 背 → 背面 5 视图横排，每个 50mm 全身像，窄长脸型+清晰下颌线/温厚眼型/自然黑短发/深蓝灰棉麻衬衫袖口卷起+暖灰长裤+深色拖鞋/水杯持握严格一致；底线允许 ±2-4% 错位。

【区块C·头部研究图】中列·下 28%×44%（第二梯队），6 张头部研究：正面 / 3/4 正侧 / 纯侧面 / 低头 / 抬头 / 动态扭头（听到女主胃疼后的迅速转头），2 行 × 3 列，每张 85-105mm 头部特写；窄长脸型/温厚坚定眼神/眉型利落/薄唇/自然黑短发与主视觉严格一致；其中"动态扭头"放大 1.15× 偏出网格 8%——抓"听到声音第一时间转头看的关切但稳定的反应"。

【区块D·电影感情绪肖像】中列·上 28%×50%（第二梯队·定情绪脸），50mm 中近景肖像（半身），偏左对齐留右呼吸；电影色调克制、保留 SSS 透粉肤感+健康通透；眼神是"温厚坚定中带一点着急心疼"——眉间未皱却紧绷、嘴角无笑但坚定、眼睛有一点红但不落泪；与主视觉同光源同色温但情绪强度提升一档。

【区块E·服装与配件拆解】右列·下横条 48%×20%（第三梯队·堆叠于 B 之下），5 张 100mm 微距细节拍立得感小图：① 深蓝灰棉麻衬衫袖口（细纱织纹、自然卷起的折痕、非商务西装质感）；② 手部拧瓶动作（手背筋线自然、指节清楚、动作稳定不抖、指关节偷暖粉红 SSS 透光）；③ 透明水杯边缘（杯壁折射、温水浅琥珀高光）；④ 外套金属拉链（普通家居外套质感、边缘细微使用痕迹、不闪亮）；⑤ 眼部表情（眼睛有一点红来自着急和心疼，不煽情泪眼）；±3° 旋转拍立得感，用 Caveat 手写体细线标注材质名（棉麻/玻璃/金属拉链/SSS皮肤）。

【区块F·美术备注与色板】右列·中横条 48%×20%（第三梯队·堆叠于 B 之下），HSB 色板（自然黑发 H=28 S=35 B=16 `#29201B`、暖粉底健康肤色 H=20 S=15 B=95 `#F2D8CC`、深蓝灰家居衬衫 H=215 S=25 B=32 `#3D4952`、暖灰居家长裤 H=35 S=8 B=48 `#7A756D`、温水高光琥珀 H=38 S=30 B=86 `#DBBC82`）+ 材质关键词「棉麻/家居棉/玻璃/金属拉链/健康男性 SSS 皮肤」+ 性格关键词「温厚／坚定／关切／沉稳／不善辞令但行动稳定」+ 风格定位「电影级风格化写实·现实伴侣感」。

整张光源统一：电影级柔光美人布光 5200-5600K，大柔光箱蝶形/环形主光从右上 45° 制造颧骨与鼻翼柔和立体，左侧低强度冷色补光（光比约 3:1、保留立体而非平光洗白），一道低强度发丝轮廓光把发缘与背景分离，双眼 10–11 点钟方向明亮 catchlight 眼神光；皮肤 PBR + SSS（耳尖肩颈透粉、指关节偷暖粉红、鼻梁柔光、明暗极柔过渡），男性皮肤通透不过亮；棉麻衬衫纤维清晰、卷起袖口折痕真实；玻璃水杯真实折射；金属拉链哑光不过亮；AXIS 顶级人物 CG 质感，2.5D 动漫-CG 融合渲染，影视级游戏CG·次世代3A质感·超写实PBR材质渲染 + AO + SSS + Octane Render + Unreal Engine 5 + 4K极致细节，柔光电影打光（低强度轮廓光勾边 + 发丝光透发 + 柔光镜柔化）+ 浅景深小景深焦外柔化，发丝级细节，男性年龄特征严格保留。

绝对禁止：霸道总裁感、奢华西装、戏剧灯光、浪漫海报姿势、过度肌肉化、卧室/办公室/家庭场景背景、纯白纯黑、彩色光斑、散景、漂浮粒子、噪点、文字水印、塑料蜡像感、冷白假人脸、任何角度脸型/年龄/发型/服装漂移。

#### 【English description block】

Cinematic character pitch board, horizontal large-format 16:9, neutral gray pitch-board background gradient #BEC1C4 to #C7CACD with subtle linen weave / paper grain texture, no pure white, no pure black, no colored bokeh, no scene elements; art-directed slightly hand-laid composition.

[Top band] full top width 6% high, text left-aligned to right edge of main visual: "Husband | The Realistic Partner Who Acts Before He Speaks · Around 30 · Height 178cm · Cinematic stylized realism · warm-grounded / steady / caring / composed / not eloquent but reliable in action", printed labels strictly in Inter (Latin/numerals) + Source Han Sans (CJK), handwritten notes strictly in Caveat (minimal), no third typeface.

[Zone A · Hero portrait] left column full height 24%×94% (Tier 1, main block · vertical full-height), 85mm full-body front portrait with actor presence, natural stance with subtly uneven weight distribution, shoulders carrying real breathing tension, no idol pose; realistic ordinary husband around 30, height 178cm, slim build with moderate shoulders, head-to-body ratio ~7.8 (adult male); narrow long face with clean jawline, warm steady gaze with neat brows, eyes carrying a hint of worried concern without tears, high straight nose bridge with soft tip highlight, thin naturally-colored lips; natural black neatly-cut short hair; warm pink-undertone porcelain luminous healthy skin with SSS pink translucency on shoulders, collarbones, ear tips; wearing dark blue-gray cotton-linen home shirt with sleeves naturally rolled up to forearm + warm gray home trousers + dark slippers; left arm hanging naturally, right hand habitually touching a water glass (or holding a warm water glass), posture natural not idol-like. Gold thin vertical height ruler (2% width) flush left, top reading ~178cm.

[Zone B · Turnaround] right column top 48%×54% (Tier 1, largest block), five 50mm full-body views (front / 3/4 front-side / pure side / 3/4 back / back), narrow long face with clean jawline, warm steady eyes, natural black short hair, dark blue-gray rolled-sleeve shirt + warm gray trousers + dark slippers, water glass handling all identical to Zone A; baseline staggered ±2-4%.

[Zone C · Head studies] middle column lower 28%×44% (Tier 2), six head studies (front / 3/4 front-side / pure side / head down / head up / dynamic head-turn—the swift turn upon hearing his wife's stomach pain) 2×3, all features identical to Zone A; "head-turn" portrait scaled 1.15× and overflowing grid 8%—captures the immediate but composed concerned reaction when he hears something.

[Zone D · Emotional portrait] middle column upper 28%×50% (Tier 2, the emotion face), 50mm mid-close portrait, breathing space on right, cinematic restrained tone with preserved SSS pink translucency on healthy skin; eyes capture "warmly steady with a hint of worried concern"—brow tense without furrowing, mouth without smile but firm, eyes slightly reddened without tears; same lighting as main visual, emotional intensity escalated one notch.

[Zone E · Wardrobe & accessory breakdown] right column, lower bar, 48%×20% (Tier 3, stacked below Zone B), five 100mm macro Polaroid tiles: ① dark blue-gray cotton-linen shirt cuff (fine weave, natural rolled-up creases, not business suit feel); ② hand opening a bottle cap (natural dorsal tendons, clear knuckles, steady action without tremor, joint warm pink SSS translucency); ③ transparent water glass rim (refractive walls, warm water amber highlights); ④ casual jacket metal zipper (ordinary home jacket feel, subtle wear at edges, not shiny); ⑤ eye expression (slight redness from worry and concern, no melodramatic tears); rotated ±3° as if pinned, handwritten labels "cotton-linen / glass / metal zipper / male SSS skin".

[Zone F · Art notes] right column, middle bar, 48%×20% (Tier 3, stacked below Zone B), HSB palette (natural black hair H=28 S=35 B=16 #29201B, warm pink healthy skin H=20 S=15 B=95 #F2D8CC, dark blue-gray shirt H=215 S=25 B=32 #3D4952, warm gray trousers H=35 S=8 B=48 #7A756D, warm water amber H=38 S=30 B=86 #DBBC82) + material keywords "cotton-linen / home cotton / glass / metal zipper / healthy male SSS skin" + personality keywords "warm-grounded / steady / caring / composed / not eloquent but reliable in action" + style direction "cinematic stylized realism · realistic partner".

Unified lighting: soft cinematic beauty lighting 5200-5600K, large softbox butterfly/loop key from upper right at 45° giving gentle cheekbone and nose-side dimensionality, low-intensity cool fill from left (about 3:1 ratio, dimensional not a flat wash), a low-intensity hair rim light separating hair from the background, bright catchlight in both eyes at 10-11 o'clock; PBR skin with SSS, soft nose highlight, joint warm pink flush, ultra-soft shadow transitions, male skin translucent without blowing out; cotton-linen shirt fibers visible, rolled-sleeve creases natural; glass shows real refraction; metal zipper matte without blown highlights; AXIS top-tier character CG quality, 2.5D anime-CG hybrid rendering, cinematic game CG, next-gen AAA quality, hyper-realistic PBR material rendering + AO + SSS + Octane Render + Unreal Engine 5, 4K ultra-detailed, soft cinematic lighting (low-intensity rim light + hair light + soft-focus diffusion) + shallow depth of field, hair-strand detail, male age characteristics strictly preserved.

Strictly forbidden: CEO-tycoon look, luxury suit, dramatic lighting, romantic poster pose, over-muscular body, bedroom / office / family scene background, pure white / pure black, colored bokeh, floating particles, noise, text watermark, plastic wax-doll look, cold-white mannequin face, any face / age / hair / clothing drift.

#### 【画面洁净负面约束】

不要耀斑、不要镜头 flare、不要散景光斑、不要漂浮粒子、不要噪点、不要胶片颗粒、不要霸道总裁感/奢华西装/戏剧灯光/浪漫海报姿势/过度肌肉化、不要卧室/办公室/家庭场景背景、不要文字水印 logo、不要机械对称网格、不要全部微距小图正放、不要塑料蜡像感、不要冷白假人脸、不要任何角度脸型/年龄/发型/服装漂移。

#### T0 自检清单

**版面区块完整性**
- [ ] 顶部细条标题区
- [ ] 区块 A 主视觉立像 + 金色身高刻度尺（顶端 178cm）
- [ ] 区块 B 全身 5 视图（含袖口卷起+水杯持握姿态一致）
- [ ] 区块 C 头部 6 视图（含动态扭头略大偏出网格）
- [ ] 区块 D 电影感情绪肖像（温厚关切但不煽情）
- [ ] 区块 E 5 张材质微距（衬衫袖口/拧瓶手部/水杯边缘/外套拉链/眼部表情）
- [ ] 区块 F HSB 色板 5 色 + HEX

**一致性核对**
- [ ] 窄长脸型+清晰下颌线在 A/B/C/D 一致
- [ ] 温厚坚定眼型+眉型利落在 A/B/C/D 一致
- [ ] 自然黑短发精神剪裁在 A/B/C/D 一致
- [ ] 深蓝灰棉麻衬衫袖口卷起+暖灰长裤+深色拖鞋在 A/B 一致
- [ ] 水杯持握姿态在 A/B 一致
- [ ] 成年男性比例（头身比 7.8）严格保留、不偶像化、不霸总化

**材质真实性**
- [ ] 皮肤 PBR + SSS + 男性健康通透不过亮 + 鼻梁柔光 + 关节偷暖粉红
- [ ] 棉麻衬衫纤维清晰、卷起袖口折痕真实
- [ ] 玻璃水杯真实折射、温水浅琥珀高光不过亮
- [ ] 金属拉链哑光不过亮、有细微使用痕迹

**背景与画面洁净**
- [ ] 中性灰提案板背景非纯白/纯黑
- [ ] 极轻微亚麻布纹/纸纹存在
- [ ] 无卧室/办公室/家庭场景元素
- [ ] 无耀斑/散景/漂浮粒子/噪点/水印

**美术指导气质**
- [ ] 整张图略带不对称感、有手作贴板感
- [ ] 微距小图非全部正放
- [ ] 头部研究"动态扭头"略大偏出网格
- [ ] 五视图底线非完全平齐
- [ ] 演员气质（自然真实呼吸/重心）非摆拍模特、非霸总化、非偶像化

---

### 6.2 变体 A：夜晚照顾状态

**变体说明**：来源剧本镜号 31-39（夜晚照顾女主段）。与基础形象**共享同一基底人物**，仅情绪强度与道具动作变化——卷袖蹲下做拧药瓶与摸杯壁的稳定手部动作。

**与基础形象差异**：
- 服装：深蓝灰棉麻衬衫袖口从"自然卷起"变为"卷到小臂、更明显"；其余服装不变
- 道具：右手做拧瓶盖动作（明确特征）+ 左手稳定端水杯；不把女主画入
- 情绪：从"温厚关切"换成"着急但压住"——眉心轻收、嘴角不笑、薄唇微抿、眼神着急但手部稳定
- 姿态：可呈现蹲下/微前倾的照顾姿态，不直立站姿

**HSB 色板**（沿用基础形象，无变化）：
- 🎨 自然黑发：H=28, S=35, B=16，`#29201B`
- 🎨 暖粉底健康肤色：H=20, S=15, B=95，`#F2D8CC`
- 🎨 深蓝灰家居衬衫：H=215, S=25, B=32，`#3D4952`
- 🎨 暖灰居家长裤：H=35, S=8, B=48，`#7A756D`
- 🎨 温水高光琥珀：H=38, S=30, B=86，`#DBBC82`

#### 【中文描述段】

电影级角色设定板（变体A·夜晚照顾状态），横版大画幅 16:9，中性灰提案板背景，6 区块固定布局，与基础形象为同一人——窄长脸型+清晰下颌线、温厚坚定眼型、高挑鼻梁、自然黑短发、暖粉底健康肌肤、178cm 身高严格不变。

【顶部细条】「丈夫·变体A 夜晚照顾状态 · 30岁左右 · 身高 178cm · 电影级风格化写实 · 着急但压住／眉心轻收／薄唇微抿／手部稳定」。

【区块A 主视觉】左列·全高 24%×94%（第一梯队·双主块之一·竖向贯通全高），85mm 全身正面演员气质立像（也可呈蹲下/微前倾的照顾姿态），袖口卷到小臂更明显，右手做拧瓶盖动作（拇指食指关节明确发力但稳定不抖），左手稳定端一只温水杯——不把女主画入，仅丈夫单人；金色身高刻度尺贴左缘（蹲姿时刻度尺标注的是直立换算高度并标注"shown squatting"小注释）；微表情是"着急但压住"——眉心轻收、嘴角不笑、薄唇微抿、眼神着急但手部稳定。

【区块B 五视图】右列·上 48%×54%（第一梯队·画面最大主块），5 视图横排，袖口卷起到小臂+拧瓶盖+端水杯姿态严格一致，底线错位 ±2-4%。

【区块C 头部六视图】中列·下 28%×44%（第二梯队），正/3·4正侧/纯侧/低头（看手中瓶盖）/抬头（看向女主方向但女主不入画）/动态扭头（被女主声音叫住时下意识回头）2×3，"动态扭头"放大 1.15× 偏出网格——抓"被女主一句'没事'打断时的瞬间停顿"。

【区块D 情绪肖像】中列·上 28%×50%，50mm 中近景，眼神是"着急但压住"——薄唇微抿、眉心轻收、太阳穴轻微紧绷、眼睛有一点红但不落泪、电影色调克制。

【区块E 服装拆解】5 张 100mm 微距：① 拧瓶盖手指（指关节偷暖粉红 SSS 透光、动作稳定不抖、指甲短而干净）；② 杯壁温水高光（玻璃折射、浅琥珀高光、不过亮）；③ 卷起袖口折痕（棉麻细纱织纹、卷边自然不僵硬）；④ 眼部微红（着急和心疼但不煽情、瞳孔反光稳定）；⑤ 手背筋线（自然男性手部筋骨、暖粉底通透 SSS 透光）；±3° 旋转拍立得感。

【区块F 色板】HSB 沿用基础形象 5 色 + 材质关键词「棉麻/玻璃/SSS皮肤」+ 性格关键词「着急但压住／手部稳定／不煽情」+ 风格定位「电影级风格化写实·夜晚照顾状态」。

整张光源、皮肤 SSS、PBR/AO/Octane/UE5/8K 渲染参数与基础形象完全一致。

绝对禁止：女主入画、夸张拥抱、霸总姿态、戏剧性夜景灯光、卧室/书房门缝场景背景、纯白纯黑、彩色光斑、散景、漂浮粒子、噪点、文字水印、塑料蜡像感、冷白假人脸、任何脸型/年龄/发型/服装漂移。

#### 【English description block】

Cinematic character pitch board (Variant A · Night Caregiving State), horizontal large-format 16:9, neutral gray pitch-board background, 6-zone fixed layout. Same character as base: identical narrow long face with clean jawline, warm steady eyes, high nose bridge, natural black short hair, warm pink-undertone healthy skin, 178cm height strictly unchanged.

[Top band] "Husband · Variant A Night Caregiving State · Around 30 · Height 178cm · Cinematic stylized realism · anxious but composed / brow lightly knit / lips faintly pressed / hands steady".

[Zone A] left column full height 24%×94% (Tier 1, main block · vertical full-height), 85mm full-body front portrait with actor presence (may show squatting / slightly forward caring posture), sleeves rolled higher to forearm, right hand opening a bottle cap (thumb-index joint exerting clear but steady force without tremor), left hand steadily holding a warm water glass—female lead is NOT in frame, husband alone; gold height ruler flush left (when squatting, ruler shows standing-height conversion with small annotation "shown squatting"); micro-expression is "anxious but composed"—brow lightly knit, mouth without smile, lips faintly pressed, eyes anxious but hands steady.

[Zone B] right column top 48%×54% (Tier 1, largest block), five views, rolled sleeves + bottle-cap-opening + water-glass-holding identical, baseline staggered ±2-4%.

[Zone C] middle column lower 28%×44% (Tier 2), six head studies (front / 3/4 front-side / pure side / head down looking at bottle cap / head up looking toward but not at female lead / dynamic head-turn—instinctive look back when interrupted by her voice) 2×3, "head-turn" 1.15× overflowing grid—captures the brief pause when she says "I'm fine".

[Zone D] middle column upper 28%×50%, 50mm mid-close portrait, eyes carry "anxious but composed"—lips faintly pressed, brow lightly knit, temple subtly tense, eyes slightly reddened without tears, cinematic restrained tone.

[Zone E] five 100mm macro tiles: ① bottle-cap-opening fingers (joint warm pink SSS translucency, steady action without tremor, short clean nails); ② warm water glass highlight (glass refraction, soft amber highlight without blowing out); ③ rolled-sleeve creases (cotton-linen weave, natural rolled edge not stiff); ④ slightly reddened eyes (anxious and concerned but not melodramatic, steady pupil reflection); ⑤ hand back tendons (natural male hand structure, warm pink translucent SSS); rotated ±3° as if pinned.

[Zone F] HSB palette inherited from base 5 colors + material keywords "cotton-linen / glass / SSS skin" + personality keywords "anxious but composed / steady hands / not melodramatic" + style direction "cinematic stylized realism · night caregiving".

Unified lighting and rendering identical to base.

Strictly forbidden: female lead appearing in frame, exaggerated hug, CEO pose, dramatic night lighting, bedroom / doorway scene background, pure white / pure black, colored bokeh, floating particles, noise, text watermark, plastic wax-doll look, cold-white mannequin face, any face / age / hair / clothing drift.

#### 【画面洁净负面约束】

不要耀斑、不要镜头 flare、不要散景光斑、不要漂浮粒子、不要噪点、不要胶片颗粒、不要女主入画、不要夸张拥抱/霸总姿态/戏剧性夜景灯光、不要卧室/书房门缝场景背景、不要文字水印 logo、不要机械对称网格、不要全部微距小图正放、不要塑料蜡像感、不要冷白假人脸、不要任何角度脸型/年龄/发型/服装漂移。

---

## 七、复用流程（推荐）

1. **出图模型选择**：Nano Banana Pro 用中文描述段；Midjourney v6 / Flux Pro 用英文描述段；推荐输出尺寸 3840×2160 或 4096×2304（16:9）。
2. **每角色出 1 张提案板**：基础形象优先出，导演确认后再出变体。
3. **变体保持基底人物完全一致**：变体 A/B 与基础形象**共享同一基底**——脸型、五官、发型、身高、配饰位置严格不变；仅 D 情绪肖像 + E 服装拆解 + 顶部细条情绪关键词允许调整。
4. **出图后用各角色 T0 自检清单逐项核对**，未达项重出。
5. **跨角色一致性比对**：4 个角色提案板必须**共享同一中性灰背景规格、同一光源方向与色温、同一渲染参数**，确保整套提案板视觉统一。
6. **提案板通过后 → 走 AXIS 工业资产**：用同目录 `character-prompts.md`（三栏式纯白）出工业资产，**两份资产的脸型/眼型/发型/服装/配饰必须完全一致**——这是后续 Seedance/Kling 视频生成正确引用的前提。

---

## 八、与同目录 `character-prompts.md`（三栏式工业资产）的对照关系

| 角色 | 本文件提案板版本 | 同目录工业资产版本 | 视觉基底必须一致的核心字段 |
| --- | --- | --- | --- |
| 成年女主 | §三（基础+变体A职场+变体B睡衣） | `character-prompts.md` §[ep01]角色1 | 鹅蛋脸/水润杏眼/暖黑中长发/雾灰针织/素银婚戒/攥衣角动作 |
| 小女孩 | §四 | `character-prompts.md` §[ep01]角色2 | 圆润童颜/大圆眼/暖黑短中发/旧棉淡米粉睡衣/双手捧大水杯 |
| 母亲 | §五 | `character-prompts.md` §[ep01]角色3 | 柔和鹅蛋脸+眼尾下垂/深棕短发/暗灰家居外套/略前倾肩膀 |
| 丈夫 | §六（基础+变体A夜晚照顾） | `character-prompts.md` §[ep01]角色4 | 窄长脸型+清晰下颌/温厚眼型/自然黑短发/深蓝灰棉麻衬衫/水杯持握 |

> **铁律**：本文件（提案板）与同目录 `character-prompts.md`（三栏式工业资产）**必须共享同一基底人物**，仅版面/背景/标注层不同。任何角色的核心字段在两份文件之间必须严格一致，否则后续 Seedance/Kling 视频生成会出现"提案板看到的角色"与"视频里的角色"对不上的问题。
