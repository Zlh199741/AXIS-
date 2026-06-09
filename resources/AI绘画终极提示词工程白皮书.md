# AI绘画终极提示词 (Prompt) 工程白皮书

## T0级工业商用提示词规则

本白皮书定义 AXIS 系统中所有 AI 绘画提示词的 T0 级工业标准。所有服化道设计、分镜编写阶段的提示词必须严格遵循以下规范。

---

## 维度一：角色视觉资产

### 资产隔离原则（强制）

角色与道具维度强制使用**纯白背景 (White Background)** 控制：
- `pure white background, isolated character, studio lighting`
- 禁止在角色设定图中出现复杂背景
- 目的：确保角色资产可独立使用、可自由合成

### 角色提示词公式（T0级）

```
[纯白背景隔离] + [精美排版：多视图/表情集/服饰拆分] + [角色身份] + [材质引擎/AO/PBR] + [微观面部细节] + [T0级画质后缀]
```

#### 6项强制要求

| # | 要求 | 关键词示例 |
|---|------|-----------|
| 1 | 纯白背景 | `pure white background, isolated, studio lighting, no background elements` |
| 2 | 表情集 | `expression sheet, 4 key expressions (neutral, angry, happy, sad)` |
| 3 | 服饰拆分 | `costume breakdown, clothing details separated, accessories isolated` |
| 4 | 多视图 | `character turnaround, front view, back view, left side, right side` |
| 5 | 渲染参数 | `PBR material, subsurface scattering, ambient occlusion, 8K UHD` |
| 6 | 微观细节 | `extreme facial detail, skin texture, iris detail, hair strand rendering` |

### 角色提示词模板

**融合角色身份 + 视觉资产全维度的T0级完整模板**

```
[纯白背景]: pure white background, isolated character, professional studio lighting, no background elements,
[角色身份]: [name], [age], [gender], [role/occupation], [personality core traits], [body type and proportions],
[多视图]: character design sheet, full body turnaround (front view, back view, left side, right side), consistent proportions across all views,
[表情集]: expression sheet with 4 key expressions: [list 4 expressions matching character personality], micro-expression nuance,
[服饰拆分]: costume breakdown: [main outfit description], accessories isolated: [list each accessory], clothing layers separated showing inner/outer garments,
[材质渲染]: PBR material rendering, subsurface scattering on skin, ambient occlusion on clothing folds, [specific material types for costume], [specific material types for accessories],
[微观细节]: extreme facial detail: [skin type specifics], individual hair strands with [hair texture description], iris detail with [eye color and pattern], [unique identifying features: scars/tattoos/markings],
[画质后缀]: 8K UHD, masterpiece quality, professional character concept art, [visual style] official character design sheet
```

#### 增强版6项要素说明

| # | 要素 | 说明 | 示例 |
|---|------|------|------|
| 1 | **纯白背景** | 强制隔离背景，指定studio灯光，确保角色资产可独立合成 | `pure white background, isolated character, 3-point studio lighting (key + fill + rim), no environmental elements, shadow on ground plane only` |
| 2 | **角色身份** | 姓名、年龄、性别、职业/角色定位、性格核心特征、体型比例 | `Lin Yue, 28 years old, female, imperial sword cultivator, cold and calculating exterior hiding protective nature, tall athletic build 175cm, long limbs with dancer proportions` |
| 3 | **多视图** | 角色转面图4视图（正面/背面/左侧/右侧），所有视图比例一致，标注身高参考线 | `character turnaround with 4 views: front, back, left profile, right profile, consistent proportions across all views, height reference grid lines` |
| 4 | **表情集** | 4种核心表情覆盖角色关键情绪，包含微表情细节，匹配角色性格 | `expression sheet: cold neutral (default), suppressed rage (clenched jaw), rare genuine smile (eyes softening), battle determination` |
| 5 | **服饰拆分** | 主装备+所有配件逐一隔离展示，内外层分离，材质标注 | `costume breakdown: outer layer (black leather long coat with silver clasps), inner layer (dark silk shirt), belt system (dual-holster leather rig), boots (steel-toe combat, worn leather), accessories isolated: pendant necklace, fingerless gloves, ear cuff` |
| 6 | **微观细节** | 面部皮肤类型、发丝纹理、虹膜图案色彩、独特识别特征（疤痕/纹身/胎记） | `extreme facial detail: weathered tan skin with faint acne scarring on jawline, individual coarse black hair strands with grey streaks at temples, heterochromatic iris (left: amber gold, right: steel grey) with visible limbal ring, diagonal scar across left eyebrow` |

#### 使用建议

- **所有角色设定**：统一使用6要素完整模板，确保角色资产在后续分镜中可直接引用
- **写实/超写实角色**：强化微观细节的皮肤纹理和毛发渲染，材质渲染使用SSS和毛孔级精度
- **动漫/二次元角色**：弱化皮肤微观（改为强调眼睛高光层次），强化表情集的夸张表现力
- **暗黑/反派角色**：强化服饰拆分的战损/污渍细节，微观细节加入疤痕/异瞳等特征
- **古风/仙侠角色**：强化服饰拆分的多层叠穿结构和配饰，材质渲染强调丝绸/玉石/金属
- **机甲/科幻角色**：强化服饰拆分的机械部件爆炸视图，材质渲染强调金属/碳纤维/LED发光
- **非人类/奇幻种族**：强化多视图中独特体态特征，微观细节加入种族特有纹理（鳞片/羽毛/角质）

### 角色实战示例

#### 示例1：写实男主（都市·硬汉侦探）

```
pure white background, isolated character, 3-point studio lighting (warm key light 45° camera-left, cool fill 30° camera-right, subtle rim light from behind), clean shadow on ground plane only, no environmental elements,
Character Identity: Shen Wei, 38 years old, male, veteran homicide detective, outwardly cynical and world-weary but deeply principled, mesomorphic build 182cm with broad shoulders slightly hunched from desk work, strong jaw with permanent stubble shadow,
character design sheet, full body turnaround: front view (hands in coat pockets, weight on left leg), back view (revealing concealed shoulder holster), left profile (showing aquiline nose bridge), right profile (showing ear scar detail), consistent proportions across all 4 views with 182cm height reference grid,
expression sheet with 4 key expressions: default weary cynicism (heavy-lidded eyes, slight frown), cold interrogation stare (unblinking, jaw set), explosive anger (veins on temple, teeth bared), rare genuine warmth (slight softening around eyes, barely-there smile),
costume breakdown with every element isolated: OUTER — charcoal wool overcoat (worn at elbows, missing one button, coffee stain on left lapel); MIDDLE — rumpled navy suit jacket (off-the-rack fit, slightly too tight at shoulders); INNER — wrinkled white dress shirt (top button undone, yellowed collar); LOWER — dark grey trousers (crease long gone, pocket bulge from notebook); FEET — scuffed brown oxford shoes (unpolished, worn heel); ACCESSORIES isolated: shoulder holster (tan leather, molded to body), detective badge on belt clip, battered wristwatch (cracked crystal), reading glasses tucked in breast pocket, cigarette pack outline visible in coat pocket,
PBR material rendering: wool overcoat with fabric weave visible under studio light (roughness 0.7-0.8), leather holster with body-oil darkening at contact points, cotton shirt with micro-wrinkle displacement map, metal badge with scratched chrome finish (metallic 0.9, roughness 0.4), watch crystal with hairline crack refraction,
extreme facial detail: weathered olive skin with visible pores on nose and cheeks, enlarged pores around nasal folds, 5 o'clock shadow with individual follicle direction mapping, dark circles under eyes with purple-blue subcutaneous vein visibility (SSS), coarse black hair with premature grey concentration at temples (individual strand rendering with 3 grey strands per 10), dark brown iris with visible crypts and collarette ring, broken capillaries on nose bridge from cold exposure, horizontal forehead wrinkles (3 deep lines), diagonal scar through right eyebrow (healed, slightly raised, lighter pigmentation),
8K UHD, masterpiece quality, professional character concept art, photorealistic detective character design sheet, cinema-quality character reference
```

#### 示例2：仙侠女主（古风·剑修女帝）

```
pure white background, isolated character, soft diffused studio lighting with subtle warm key light to emulate jade-like skin glow, ethereal rim light creating hair silhouette, clean minimal shadow on ground plane,
Character Identity: Mu Qinglan, appears 25 (true age 3000+), female, supreme sword cultivator and fallen dynasty empress in hiding, ice-cold regal bearing masking millennia of loneliness, slender willowy build 170cm with impossibly elegant posture (straight spine, slightly raised chin), long neck accentuating authority,
character design sheet, full body turnaround: front view (standing with sword held vertically before face in salute), back view (revealing elaborate hair ornament and trailing ribbon details), left profile (showing jade hairpin and ear pendant), right profile (showing sword sheath on back), consistent proportions across 4 views with height reference grid including hair ornament height,
expression sheet with 4 key expressions: imperial cold neutral (default — eyes looking slightly downward at lesser beings, perfectly composed), restrained fury (only visible in slight nostril flare and intensified gaze, face otherwise unchanged), battle focus (narrow predatory eyes, faint killing intent aura implied in expression), warm smile for one person only (eyes completely transforming with gentle crinkle, soft lips, vulnerability visible),
costume breakdown — multi-layer traditional hanfu system, each layer isolated: INNERMOST — white silk inner robe with silver thread cloud patterns (visible at collar and wrist); SECOND — ice-blue silk middle robe with flowing water embroidery; OUTER — midnight-blue brocade outer robe with constellation map woven in metallic thread; SHOULDER — white fox fur half-cape (left shoulder only, clasped with jade dragon brooch); WAIST — triple-wrap silver-thread belt system with jade pendant, medicine pouch, and sword tassel; FEET — white silk boots with cloud-pattern sole; HAIR — elaborate upswept style with: jade crown (carved phoenix), silver chain veil (draping over left ear), dangling pearl hairpin, ice-blue silk ribbon (2 meters trailing); ACCESSORIES isolated: ancient jade pendant (cracked, heirloom), finger armor (right index and middle finger, silver filigree), sword (named Qingfeng — ice-blue blade, white jade pommel, silver guard with frost crystal),
PBR material rendering: silk robes with anisotropic SSS showing fabric translucency at edges and overlapping layers, jade accessories with volumetric SSS (internal green glow, waxy surface roughness 0.3), silver metalwork with tarnish variation (metallic 0.95, roughness 0.2-0.5), fox fur with multi-layer hair shader (guard hairs + underfur + SSS skin layer), brocade fabric with displacement-mapped embroidery catching light at different angles, sword blade as custom ice-metal shader (subtle blue emissive, mirror polish with frost-crystal normal map),
extreme facial detail: porcelain-smooth skin with jade-like translucency (heavy SSS on cheeks and nose bridge), no visible pores (cultivator perfection), but subtle expression lines at eye corners (3000 years of suppressed emotion), jet-black hair with blue-sheen highlights (each strand rendered with cuticle-level light scattering), inner-glow amber-gold iris with visible qi-circulation patterns replacing normal human crypts (faint golden luminescence in dark environments), thin scar across left palm (visible in hand close-up views only — self-inflicted blood oath mark), beauty mark below right eye,
8K UHD, masterpiece quality, professional character concept art, xianxia female lead official character design sheet, Chinese fantasy premium quality
```

#### 示例3：暗黑反派（魂系·堕落圣骑士）

```
pure white background, isolated character, dramatic chiaroscuro studio lighting (hard key light from above-right creating deep facial shadows, minimal fill, strong rim light from below-left suggesting infernal glow), sharp shadow on ground plane,
Character Identity: Aldric the Unforgiven, age unknown (decades of undeath), male, former paladin-commander corrupted by forbidden resurrection magic, tragic fury and self-loathing driving merciless crusade, massive imposing build 198cm with unnaturally broad frame, asymmetric posture (left shoulder dropped from old wound that never healed),
character design sheet, full body turnaround: front view (greatsword planted point-down, both hands on crossguard, head slightly bowed), back view (revealing shattered halo fused to skull and tattered sacred cape), left profile (showing corrupted arm detail), right profile (showing intact armor side for contrast), consistent proportions across 4 views, height reference showing 198cm at shoulder hunch (210cm if standing straight),
expression sheet with 4 key expressions: hollow default (sunken eyes staring through viewer, slack jaw behind helm), berserker rage (eyes blazing with golden corruption, mouth twisted in scream, veins of light cracking across face), moment of clarity (eyes suddenly lucid and human, horror at own existence, reaching out with one hand), weeping corruption (golden tears of corrupted energy streaming from eyes, expression blank),
costume breakdown — corrupted paladin full plate armor, each component isolated: HELM — open-face sallet with broken holy symbol welded to brow, golden corruption veins spreading from symbol; PAULDRONS — massive asymmetric (left: intact ornate sacred engravings, right: shattered and fused with crystallized dark energy); CUIRASS — cathedral-plate chest piece with shattered stained-glass inlay, golden corruption bleeding through cracks; GAUNTLETS — left hand encased in fully corrupted crystalline growth (fingers fused, glowing), right hand intact with worn leather under-glove; GREAVES — articulated plate with sacred text etched (half corroded, half legible); FEET — armored sabatons with ground-scoring spikes; CAPE — once-white sacred mantle now tattered and stained (70% destroyed), golden embroidery still visible on remaining fragments; WEAPON isolated: greatsword "Oathbreaker" (blade of black steel with golden corruption veins pulsing, crossguard shaped as broken angel wings, pommel containing cracked holy relic stone),
PBR material rendering: plate armor with extreme wear — base polished steel (metallic 0.95) covered in scratches, dents, and dried blood (roughness variation 0.1-0.9 creating story of every battle), golden corruption as custom emissive shader (pulsing 0.5Hz, SSS internal glow through metal cracks), crystallized corruption on left arm as refractive mineral shader with internal volumetric light scattering, tattered cape as cloth simulation with torn edges and fiber fraying, black steel blade with micro-etched runes (emissive when corruption pulses),
extreme facial detail: deathly pale skin with grey undertone (heavy SSS showing blue vein networks), sunken cheeks with visible cheekbone structure, deep eye sockets with permanent dark hollows, lips cracked and colorless, golden corruption veins spreading from temple like lightning fractals under skin (emissive subsurface), patchy remnant of once-noble beard (sparse, grey, unkempt), clouded pale blue iris with golden corruption bleeding in from pupil edge (heterochromatic corruption progression: left eye 70% gold, right eye 30% gold), massive burn scar across bridge of nose and both cheeks (old holy fire — self-inflicted failed purification attempt),
8K UHD, masterpiece quality, professional character concept art, dark fantasy villain official character design sheet, Soulsborne premium quality
```

#### 示例4：萌系少女（日漫·魔法少女）

```
pure white background, isolated character, bright even studio lighting with soft pink-tinted key light, sparkle catch-lights in eyes, minimal shadow (kawaii aesthetic prefers flat lighting),
Character Identity: Hoshino Sakura, 15 years old, female, second-year middle school student and secret guardian of dream realm, endlessly optimistic and clumsy but brave when it counts, petite build 152cm with soft rounded proportions (anime 6-head-tall ratio), big expressive eyes dominating face,
character design sheet with decorative star-and-heart border frame, full body turnaround: front view (cheerful V-sign pose), back view (showing wing accessory and ribbon tail details), left profile (showing star-shaped ear clip), right profile (showing magical compact on hip), consistent chibi-adjacent proportions across 4 views, height reference with manga-style height comparison to mascot creature,
expression sheet with 4 key expressions: sparkling excitement (huge starry eyes, open mouth smile, blush marks), determined battle face (small sharp eyes, puffed cheek, clenched fist), comedic shock (pure white eyes, dropped jaw, sweat drop), transformation resolve (eyes glowing pink, hair floating, serious determined expression),
costume breakdown — dual outfit system (school uniform + magical girl), each isolated: SCHOOL UNIFORM: white sailor blouse with pink collar and star-pattern tie, pink pleated skirt (above knee), white knee-high socks with star ankle embroidery, brown penny loafers, pink school bag with mascot keychain; MAGICAL GIRL OUTFIT: white-and-pink bodice with heart-shaped gem brooch (glowing), layered petal skirt (gradient white-to-pink, tulle underskirt), thigh-high white boots with pink star buckles, detachable wing accessory (small, decorative, back-mounted), elbow-length white gloves with pink ribbon trim, star-shaped hair clips (x2, glowing); WEAPON isolated: Dream Wand (pink shaft, rotating star head piece, trailing ribbon, heart gem core),
PBR with anime stylization: cel-shading on all fabric with 2-tone shadow (base + single shadow color, hard edge), hair rendered with thick highlight reflection band (anime specular), gem accessories as emissive with star-shaped internal light pattern, tulle skirt with transparency shader, glowing elements with soft bloom-friendly emissive values, skin with smooth anime SSS (no pore detail — porcelain anime skin),
extreme facial detail (anime-specific): flawless smooth skin with warm peach undertone and permanent soft blush on cheeks and nose tip, massive detailed eyes (iris taking up 40% of face): multi-layered iris rendering with 5 highlight layers (main catch-light, secondary sparkle, star-shaped accent, color gradient ring, pupil reflection), individual eyelashes (upper: 8 defined lash groups with curl, lower: 4 subtle lashes), eyebrows with soft gradient edges, pink-brown hair with chunky anime highlight band (wide, sharp-edged), two signature antenna-like ahoge strands with physics bounce, lips as simple soft line with pink tint (anime minimal mouth),
8K UHD, masterpiece quality, professional character concept art, magical girl anime official character design sheet, Kyoto Animation premium quality, anime key visual
```

#### 示例5：机甲驾驶员（科幻·战术指挥官）

```
pure white background, isolated character, industrial studio lighting (cool blue-white key light simulating cockpit ambient, warm orange secondary from holographic HUD reflection on face, sharp rim light delineating suit edges), technical shadow on ground plane,
Character Identity: Commander Reyes "Apex" Nakamura, 34 years old, female, elite mecha division commander and ace pilot, calm tactical genius under pressure with dry humor, athletic toned build 174cm (functional muscle, not bodybuilder), cybernetic left arm from combat injury,
character design sheet, full body turnaround: front view (at-ease stance, helmet tucked under right arm, cybernetic left arm visible), back view (showing spinal interface port and tactical data pack), left profile (showing cybernetic arm full articulation detail), right profile (showing rank insignia and comm unit), consistent proportions across 4 views, height reference with technical measurement annotations in military format,
expression sheet with 4 key expressions: tactical assessment default (calm focused eyes scanning, slight knowing half-smile), combat intensity (eyes wide and locked on target, jaw set, micro-sweat on brow), command authority (chin raised, eyes hard, voice-of-command expression), protective fury (teeth bared, eyes blazing, defending squad),
costume breakdown — pilot suit system with military precision, each component isolated: FLIGHT SUIT BASE — form-fitting graphene-weave pressure suit (matte dark grey with orange accent lines along muscle groups, built-in biometric sensors visible as subtle raised lines); ARMOR OVERLAY — modular tactical plates: chest plate (ablative ceramic-composite, unit insignia laser-etched), shoulder pauldrons (asymmetric: left smaller for cybernetic arm mobility, right larger with rank LED strip), forearm guards (right: integrated holographic wrist display, left: cybernetic arm needs no guard); HELMET — full-face tactical helm with retractable visor (gold-tinted, HUD projection visible), rear ventilation fins, antenna array on right side; CYBERNETIC LEFT ARM isolated in exploded view: titanium endoskeleton, artificial muscle bundles (myomer fiber, visible through semi-transparent housing panels), articulated finger joints with haptic sensor pads, elbow hydraulic actuator, shoulder mount with neural interface collar; ACCESSORIES isolated: sidearm pistol in thigh holster, data tablet on magnetic hip mount, dog tags (3 — 1 hers + 2 memorial), mission patch collection on right shoulder,
PBR material rendering: graphene-weave suit with carbon fiber anisotropic reflections (metallic 0, roughness 0.6 with directional variation), ceramic armor plates with matte military finish (roughness 0.8) and micro-scratch battle wear, cybernetic arm titanium with brushed metal finish (metallic 0.95, roughness 0.3), artificial muscle myomer with translucent silicone housing (SSS, subtle red-orange internal glow when flexing), visor as gold-tinted glass with holographic HUD overlay (emissive decal projection), LED rank indicator as sharp-edge emissive strip,
extreme facial detail: warm brown skin with visible pores and natural texture, thin scar from right ear to jawline (shrapnel, surgically treated but visible), combat tan (visor tan line visible when helmet removed), defined cheekbones with slight hollow beneath (military fitness), short-cropped black hair with precise military fade (individual stubble hairs at shaved sides), dark brown iris with subtle gold-fleck cybernetic enhancement (HUD integration micro-implant visible as faint circuit pattern in iris), calloused hands on organic right hand (trigger finger callus, knuckle scarring), neural interface port visible at base of skull (titanium ring with faint blue LED glow indicating active connection),
8K UHD, masterpiece quality, professional character concept art, military sci-fi character design sheet, AAA game cinematic quality, next-gen character reference
```

#### 示例6：古风将军（国漫·战神大将军）

```
pure white background, isolated character, dramatic studio lighting (warm tungsten key light simulating bonfire/torchlight ambiance, cool steel-blue fill suggesting moonlit battlefield, strong rim light emphasizing armor silhouette),
Character Identity: Zhao Wuji, 42 years old, male, legendary undefeated general of northern frontier, quiet stoic exterior with volcanic loyalty to his soldiers, massive powerful build 193cm with barrel chest and thick limbs (warrior who wields a 60-jin halberd one-handed), battle-scarred body telling 20 years of campaign history,
character design sheet, full body turnaround: front view (standing at attention with halberd held vertically at side, cape draped over left shoulder), back view (revealing massive tiger embroidery on cape back and twin sword rack), left profile (showing long beard detail and waist-mounted war horn), right profile (showing arm guard calligraphy and rank medallion), consistent proportions across 4 views with height reference including weapon length,
expression sheet with 4 key expressions: stoic commander default (level gaze, closed mouth behind thick beard, immovable mountain presence), battlefield roar (mouth open in war cry, veins on neck and forehead, eyes blazing with killing intent), cold fury at betrayal (eyes gone flat and dead, face completely still — the most terrifying expression), grief for fallen soldiers (jaw clenched hard enough to see muscle, eyes reddened but no tears — generals don't cry where soldiers can see),
costume breakdown — Tang dynasty military general full dress, each layer isolated: INNERMOST — cotton undershirt with sweat stains at collar and underarms (evidence of armor weight); PADDING — quilted silk armor padding (visible at joints and neck); MAIN ARMOR — mountain-pattern lamellar armor (hundreds of individually laced iron scales, black lacquer with gold edge), cuirass reinforced with bronze tiger-head central plate; PAULDRONS — articulated scale shoulder guards with red silk tassels; BRACERS — leather-and-iron forearm guards with calligraphy etching (excerpts from "Art of War"); WAIST — wide leather war belt with bronze buckle (tiger motif), sword frog (x2), medicine pouch, war horn hook; LEGS — iron-scale tassets over leather riding trousers; FEET — reinforced leather cavalry boots with iron heel plates; CAPE — heavy crimson wool cloak with massive gold-thread tiger embroidery (mouth open, one complete paw stroke), wolf-fur collar; WEAPON isolated — "Devourer" halberd: 2.4m black iron shaft wrapped in ray-skin grip, crescent blade with tiger-tooth serration, counter-weight pommel shaped as roaring tiger head (bronze, green patina); ACCESSORIES isolated: jade general's seal on waist cord, iron ring (soldier's memorial, never removed, worn groove in finger beneath), horse-tail war standard (personal banner, red field, gold character 趙),
PBR material rendering: lamellar armor with individually modeled iron scales each showing unique lacquer wear pattern (metallic 0.85, roughness 0.4-0.7 per scale), bronze tiger plates with centuries-old green patina in recesses and polished gold on raised surfaces, crimson cape wool with heavy woven texture and visible thread count (roughness 0.9), wolf fur collar with multi-layer hair shader (coarse guard hairs + soft underfur), leather components with body-oil darkening at grip points and sweat salt staining, halberd iron with sharpening marks along blade edge and impact notches on shaft,
extreme facial detail: deep bronze weathered skin from decades of frontier sun and wind, network of fine wrinkles radiating from eyes and across forehead (laughter lines hidden among worry lines), thick black beard with significant grey streaking (70/30 black-to-grey ratio), beard braided in two warrior plaits with iron rings, prominent nose once-broken and healed with slight leftward deviation, fierce dark eyes under heavy brow ridge with deep-set sockets, thick eyebrows with one bisected by vertical sword scar (right brow, white scar tissue), additional facial scar from left temple curving down to jawline (old, faded), calloused hands with enlarged knuckles and permanent weapon-grip callus pattern, individual hair strands in warrior topknot showing oil-treated sheen,
8K UHD, masterpiece quality, professional character concept art, Chinese historical military character design sheet, national-style premium quality
```

#### 示例7：赛博朋克刺客（科幻·街头改造人）

```
pure white background, isolated character, high-contrast studio lighting (cold neon-blue key light from left, warm neon-magenta fill from right creating color-split on face, harsh rim light from behind emphasizing cybernetic edge geometry),
Character Identity: V-Nix (birth name unknown), estimated 26, non-binary, freelance corporate assassin and black-market cyberware dealer, nihilistic survivor humor masking deep paranoia, lean wiry build 168cm (compact for infiltration, deceptively strong from synthetic muscle augmentation), heavily modified body (approximately 40% cybernetic replacement),
character design sheet, full body turnaround: front view (casual lean pose, arms crossed showing cybernetic asymmetry), back view (revealing spinal data-port array and concealed blade housing), left profile (showing organic side — remaining human elements), right profile (showing heavy cybernetic side — replaced eye/arm/leg), consistent proportions across 4 views with technical annotations marking organic/cybernetic boundaries,
expression sheet with 4 key expressions: street-smart smirk default (asymmetric — organic half smirks, cybernetic half remains neutral, one eye human squint + one eye aperture adjustment), kill-mode flat affect (all expression drops from face, eyes dead, purely mechanical efficiency), manic glee during chaos (wide organic eye, wider cybernetic aperture, showing teeth in feral grin), system crash vulnerability (cybernetic half goes dark/limp, organic half shows raw terror of helplessness),
costume breakdown — street tech aesthetic, each element isolated: BASE — sleeveless black compression bodysuit with exposed cybernetic interface ports (glowing faint blue at connection points); JACKET — cropped asymmetric leather jacket (right arm removed to showcase cybernetic arm, left arm intact with hidden blade pocket); LEGS — tactical cargo pants (matte black, multiple hidden pockets with magnetic closures, right leg armor panel over cybernetic knee joint); FEET — mag-lock combat boots with shock-absorbing soles (custom-fit to cybernetic right foot); CYBERNETIC RIGHT ARM isolated in exploded view: carbon-fiber endoskeleton, myomer muscle bundles in translucent silicone housing (red-tinted), articulated fingers with retractable mono-blade (index finger), haptic sensor array on palm, forearm data screen (flexible OLED embedded in housing), shoulder mount with exposed gear mechanism; CYBERNETIC RIGHT EYE isolated: military-grade optical implant (glowing red-orange aperture ring, visible micro-lens array, tactical data overlay projected), scarring around eye socket from installation; ACCESSORIES isolated: neural interface jack behind left ear (chrome ring, blue LED), throat-mounted voice modulator (visible as thin metal strip), data-chip bandolier across chest (6 chip slots, 3 occupied with glowing chips), fingerless glove on organic left hand (knuckle armor inserts),
PBR material rendering: organic skin with cyberpunk lifestyle damage (roughness variation 0.3-0.7, visible injection-site scarring near interface ports), cybernetic arm with carbon fiber composite (anisotropic reflection, roughness 0.15) and exposed myomer (translucent SSS silicone with red internal glow), chrome interface ports (metallic 1.0, roughness 0.05, mirror-finish), leather jacket with street-wear aging (roughness 0.6-0.9, scuff maps, laser-burn hole on back), retractable mono-blade as monomolecular edge shader (razor-thin emissive line), embedded OLED screen as animated emissive texture with scrolling code,
extreme facial detail: mixed-heritage face (East Asian and Latino features), organic left half: warm olive skin with visible pores around nose, faint acne scarring on cheek, natural dark brown eye with dilated pupil (street-drug side effect), dark circles from insomnia, soft organic eyebrow; cybernetic right half: skin transitions at mid-forehead with visible surgical boundary line (raised scar tissue where organic meets chrome), cybernetic eye socket with red-orange glowing aperture (iris is mechanical diaphragm, visible micro-lens layers), no eyebrow (replaced by subtle LED status strip), skin around implant slightly inflamed (chronic low-grade rejection, reddened), shaved head on right side revealing cranial data-port array (4 chrome ports in diamond pattern), remaining hair on left side: shoulder-length black with neon-blue dyed tips (asymmetric undercut), individual strands greasy and unkempt (street life aesthetic),
8K UHD, masterpiece quality, professional character concept art, cyberpunk character design sheet, next-gen game quality, Cyberpunk 2077 premium visual reference
```

#### 示例8：奇幻种族（非人类·龙裔战巫）

```
pure white background, isolated character, mystical studio lighting (warm amber key light simulating internal draconic heat glow, cool teal fill for arcane contrast, strong orange rim light from below suggesting volcanic heritage),
Character Identity: Vyrathanax (Vyra), equivalent human age 300 (young adult for dragonkin), female dragonborn, war-shaman of the Obsidian Brood serving as bridge between mortal and dragon civilizations, fierce maternal protector with ancient alien wisdom, powerful statuesque build 190cm with draconic proportions (broader shoulders, longer forearms, digitigrade leg stance adding 10cm), tail length 120cm,
character design sheet, full body turnaround: front view (shamanic staff in right hand, left hand raised with arcane flame hovering above palm, wings partially spread), back view (full wing span detail at 70% spread, tail position, spinal ridge detail), left profile (showing horn curvature, wing fold mechanism, digitigrade leg structure), right profile (showing facial scale pattern detail, arm fin, tail cross-section), consistent proportions across 4 views with anatomical reference notes for non-human features (wing joint, digitigrade ankle, tail base, horn growth direction),
expression sheet with 4 key expressions (adapted for draconic face structure): regal neutral default (vertical-slit pupils at medium dilation, jaw scales slightly flared, inner heat visible as faint amber glow from between scale gaps), protective fury (full scale flare on jaw and neck — threat display, teeth bared showing double row of fangs, pupils contracted to needlepoint slits, horns seeming to darken), arcane channeling (eyes fully glowing solid amber-gold, no visible pupil or iris, scales lifting to vent heat, mouth open with visible heat shimmer), deep grief (scales dimming to dark grey, pupils fully dilated creating almost-mammalian soft eye, jaw scales drawn tight against neck),
costume breakdown — war-shaman hybrid of primal and arcane, each element isolated: TORSO — open-front obsidian-scale half-vest (actual shed dragon scales sewn onto leather backing, leaving midriff exposed to show natural body scales), fastened with bone clasps; SHOULDERS — asymmetric arrangement: left shoulder has stacked ancestor-bone pauldron (carved with ancestral runes, faintly glowing), right shoulder bare (tattoo/brand space); WAIST — wide ceremonial belt of interlocked dragon teeth (each from a different Brood elder, willingly given), hanging bone-and-crystal charms; LEGS — wrapped leather leg bindings adapted for digitigrade stance (reinforced at reverse-knee joint), loose enough for combat mobility; FEET — bare (digitigrade taloned feet with 3 forward claws + 1 rear spur, no footwear fits); WINGS isolated: 3.2m total wingspan, bat-like membrane structure with visible internal vein network (warm amber bio-luminescence), bone struts with scale armor at joints, small clawed "thumb" at wing wrist; TAIL isolated: 120cm prehensile, scaled with ventral smooth plates underside, tip widening into flat ceremonial rudder shape (natural, not modified); WEAPON isolated — War-Shaman's Staff "Ancestor's Voice": 2m shaft of petrified dragonbone (internal crystalline structure visible at breaks), crowned with floating obsidian orb held in place by arcane energy tendrils, base mounted with iron spike; ACCESSORIES isolated: bone-piercing through nasal bridge (elder dragon rib fragment), copper ritual rings on all horn ridges (7 total, each representing a completed spirit journey), obsidian mirror pendant (scrying focus),
PBR material rendering: natural body scales with custom reptilian shader (individual scale geometry with roughness variation 0.2-0.5, iridescent color shift from deep obsidian to subtle dark amber depending on angle, heat-glow emissive in gaps between scales when emotionally activated), shed dragon-scale armor with larger heavier scale geometry (roughness 0.3, blue-black metallic sheen 0.7), wing membrane as translucent organic SSS (thin enough to see vein structure when backlit, warm amber glow), bone accessories with aged yellowed keratin material (roughness 0.8, subtle SSS showing internal density), petrified dragonbone staff with crystalline fracture surfaces (refractive with internal amber light), obsidian orb with glass-like refraction and internal arcane energy volumetric,
extreme facial detail (non-human anatomy): angular reptilian face structure with pronounced brow ridges and cheekbone scales, smooth scales on face transitioning from small (forehead, nose bridge) to large (jaw, neck) — each individually modeled with thickness and overlap, vertical-slit amber-gold iris with visible faceted crystalline structure (draconic eyes refract light differently than mammalian), double eyelid system (outer scaled lid + inner nictitating membrane visible mid-blink), no external ears (replaced by scaled tympanic membranes behind jaw hinge, visible as slightly recessed circles), flared nasal openings (no protruding nose, flat reptilian profile) with faint heat shimmer during emotion, twin horns sweeping backward from temples (30cm each, ridged growth rings visible like tree rings indicating age, dark obsidian color with amber translucency at tips when backlit), fine scale detail around eyes and mouth showing expression muscle articulation points, subtle bio-luminescent markings on forehead scales (ancestral clan pattern, faint amber glow),
8K UHD, masterpiece quality, professional character concept art, fantasy non-human race character design sheet, AAA game cinematic quality, next-gen creature design reference
```

#### 示例9：游戏CG角色设定（UE5·JRPG圣骑士）

> **本示例融合维度一（角色设定图）+ 维度六（游戏级CG引擎格式），展示游戏CG角色设定的完整T0写法**

```
Unreal Engine 5.4 with Nanite virtualized geometry and Lumen global illumination, real-time character viewer rendering with ray-traced SSS and hair strand rendering,
AAA JRPG character design aesthetic, Final Fantasy XVI / Granblue Fantasy Relink visual reference, stylized photorealism with ornate costume craftsmanship and idealized proportions,
pure white background, isolated character, 3-point studio lighting within UE5 virtual studio (warm key light 45° camera-left with area light softness, cool fill from right, subtle rim light for armor edge definition), shadow on ground plane only, no environmental elements,
Character Identity: Seraphina Auralis, 24 years old, female, elite holy knight-commander of the Golden Dawn order, outwardly noble and composed with hidden reckless battle hunger, tall athletic build 176cm with dancer-warrior proportions (long legs, defined shoulders, narrow waist), Nanite-resolution character model,
character design sheet, full body turnaround: front view (standing at attention with ceremonial lance held vertically, shield on left arm), back view (revealing ornate cape clasp mechanism and hair detail), left profile (showing pauldron articulation and lance cross-section), right profile (showing shield face design and belt pouch system), consistent proportions across 4 views with UE5 measurement grid overlay,
expression sheet with 4 key expressions: noble composed default (gentle authority, slight knowing smile, eyes radiating calm confidence), battle ecstasy (wild grin breaking noble facade, eyes blazing with excitement, hair wind-caught), solemn oath (eyes closed, head slightly bowed, hand on heart, absolute sincerity), grief-stricken rage (tears streaming but expression twisted in fury, composure shattered),
costume breakdown — holy knight ceremonial battle dress, each component isolated with UE5 material instance parameters: CUIRASS — white enamel-coated steel breastplate with gold filigree inlay (metallic 0.95, roughness 0.15 on polished surfaces, roughness 0.6 on enamel, emissive holy sigil at sternum); PAULDRONS — asymmetric (right: large ceremonial wing-shaped with gold leaf, left: smaller combat-functional with lance rest groove); UNDER-ARMOR — midnight-blue padded gambeson with gold thread quilting pattern visible at joints and collar; GAUNTLETS — articulated finger plates with prayer-bead chain wrapped around right wrist; TASSETS — segmented white-and-gold hip plates over midnight-blue combat skirt (split front and back for mobility); GREAVES — knee-high armored boots with winged knee guards; CAPE — floor-length white silk cape with gold-embroidered order insignia (Golden Dawn radiant sun), cape clasp as ornate winged brooch; WEAPON isolated — ceremonial lance "Dawnpiercer" (2.2m white shaft with gold spiral wrap, diamond-shaped blade with internal light channel emissive, cross-guard shaped as sunrise rays); SHIELD isolated — kite shield "Aegis of Dawn" (white enamel face with golden sun relief, interior leather grip with sweat wear); ACCESSORIES isolated: prayer-bead chain (pearl beads with gold spacers), hair ornament (golden circlet with single sapphire), commander's signet ring (right hand),
PBR metallic-roughness workflow in UE5 material editor: white enamel armor as multi-layer material (base steel metallic 0.95 → enamel coat roughness 0.6 with chip-reveal map exposing base metal at edges and impact points), gold filigree as separate material layer (metallic 1.0, roughness 0.1, displacement-mapped relief), midnight-blue fabric with anisotropic cloth shading (roughness 0.8, SSS 0.3 for light fabric translucency at edges), hair with UE5 strand-based hair system (individual strand rendering, anisotropic specular, warm honey-blonde with platinum highlights), skin with UE5 SSS profile (3-layer: epidermis, dermis with blood scatter, deep tissue), lance blade internal channel as translucent emissive material with scrolling energy pattern,
Lumen GI within virtual studio environment, area light key providing soft warm illumination with natural shadow falloff, HDRI studio dome for ambient fill, ray-traced contact shadows on armor panel overlaps, ray-traced SSS on skin and fabric edges, virtual shadow maps for ground plane,
subtle bloom on emissive holy sigils and lance energy channel, character-viewer DOF disabled (all views tack-sharp), neutral studio LUT preserving material accuracy, SSAO in armor crevices and fabric folds, TAA with temporal super-resolution for strand hair anti-aliasing, no motion blur (static character sheet),
AAA JRPG character design sheet, Unreal Engine 5 in-engine character viewer quality, next-gen real-time rendering, 8K UHD, Square Enix character art premium quality
```

#### 示例10：超写实摄影级角色设定（电影级·动作片定妆照）

> **本示例融合维度一（角色设定图）+ 维度七（超写实摄影格式），展示摄影级角色设定的完整T0写法**

```
Shot on Hasselblad X2D 100C medium format, XCD 90mm f/2.5 V lens at f/5.6 for optimal sharpness across full body, 100-megapixel 16-bit RAW capture, tethered studio shoot,
cinematic wardrobe test / costume fitting photography, Hollywood production still aesthetic, Annie Leibovitz character portrait meets Marvel Studios costume reveal shoot,
pure white cyclorama studio backdrop, isolated character, professional 4-light studio setup (Profoto D2 key with 4-foot octabox 45° camera-left, Profoto fill with 6-foot silk diffusion panel camera-right at -1.5 stops, Profoto strip box hair/rim light from behind-left, white bounce card below for under-chin fill), clean shadow on white floor,
Character Identity: Elena Vasquez, 32 years old, female, ex-special forces turned underground cage fighter, controlled intensity masking deep trauma, athletic muscular build 173cm (visible muscle definition in arms and shoulders, functional combat physique, not bodybuilder proportions), real human being — imperfect and lived-in,
character design sheet — wardrobe test format, full body turnaround: front view (neutral standing pose, arms slightly away from body to show costume silhouette, direct eye contact with camera), back view (showing jacket back detail and hair length), left profile (showing ear piercing detail and jaw structure), right profile (showing neck tattoo and shoulder holster), consistent proportions across 4 views, wardrobe department measurement card visible at frame edge,
expression sheet with 4 key expressions: neutral assessment default (evaluating the camera like sizing up an opponent, jaw relaxed but eyes sharp), cold predatory smile (mouth smiling but eyes dead — the expression before a fight), vulnerable unguarded moment (caught off-guard, real emotion breaking through, eyes soft and uncertain), explosive fury (teeth bared, tendons in neck taut, veins at temple, feral survival rage),
costume breakdown — underground fighter civilian kit, each element isolated with wardrobe department tags: JACKET — worn black leather motorcycle jacket (real lambskin, years of body-conforming wear, left elbow with road rash abrasion marks, collar permanently turned up on one side); SHIRT — faded army-green ribbed tank top (thin cotton, washed hundreds of times, slightly too small showing lower ab definition); PANTS — black tactical cargo pants (rip-stop nylon, right thigh pocket bulge from phone, left knee reinforced with canvas patch — hand-sewn); BOOTS — black combat boots (real leather, 3 years of daily wear, heel worn at outer edge indicating gait pattern, paracord lace replacement on left boot); HAND WRAPS — muay thai cotton hand wraps on both hands (off-white with faded blood stains that never fully washed out, wrapped in orthodox boxing style); ACCESSORIES isolated: left ear — 3 small silver hoop piercings; neck — tattooed script on right side ("Todavía estoy aquí" — I'm still here — in script font, slightly faded with age); right wrist — medical alert bracelet (stainless steel, engraved); left ankle — faded friendship bracelet (frayed thread, never removed),
visible skin pores on face and arms (no airbrushing — real skin), individual peach fuzz on cheeks and forearms catching rim light, scar tissue on knuckles (healed micro-fracture calluses, white and slightly raised), faded stretch marks on shoulders from rapid muscle development, individual eyebrow hairs with natural irregularity, dark brown iris with visible crypts and amber flecks near pupil, crow's feet beginning at eye corners (32 years of squinting in sunlight), nasolabial lines visible but not deep, chapped lower lip with visible texture, individual hair strands in messy ponytail with flyaways catching backlight (natural dark brown with sun-bleached ends), tattoo ink showing slight blur at edges from years of skin cell turnover,
Capture One Pro tethered capture with Hasselblad X2D color science, wardrobe test color accuracy (WhiBal grey card reference shot taken), minimal retouching — skin texture fully preserved, only sensor dust and stray hairs removed, natural contrast with open shadows (no crushed blacks), neutral color palette letting wardrobe and skin tones speak, output at full 100MP resolution for costume detail reference, dual output: full-res for wardrobe department + web-res for production deck,
RAW photo, photorealistic, 8K UHD, medium format studio photography quality, Hollywood wardrobe test production still, award-winning character portrait photography
```

---

## 维度二：场景环境

### 场景提示词公式（T0级）

```
[光学镜头指定] + [构图法则] + [核心环境] + [时间、天气与胶片色彩] + [全局光照/丁达尔效应] + [T0级渲染后缀]
```

#### 5项强制要求

| # | 要求 | 关键词示例 |
|---|------|-----------|
| 1 | 镜头指定 | `Shot on 14mm ultra-wide lens` / `85mm portrait lens` / `35mm cinematic lens` |
| 2 | 构图法则 | `rule of thirds` / `golden ratio` / `leading lines` / `symmetrical composition` |
| 3 | 全局光照 | `global illumination, volumetric lighting, Tyndall effect, god rays` |
| 4 | 色彩分级 | `teal and orange color grading` / `Kodak Portra 400 aesthetic` / `cinematic LUT` |
| 5 | T0级渲染后缀 | `Unreal Engine 5, ray tracing, photorealistic, 8K resolution, cinematic quality` |

### 场景提示词模板

**融合空境强调 + 材质细节的T0级完整模板**

```
[空境强调]: [spatial atmosphere], [environmental emotion], [acoustic ambiance],
[镜头]: Shot on [focal length] lens, [aperture],
[构图]: [composition rule], [camera angle], [framing emphasis],
[场景]: [core scene description], [architectural style], [spatial layout], [key elements],
[时间气候]: [time of day], [weather condition], [season], [atmospheric effects],
[光影]: global illumination, volumetric lighting, Tyndall effect, [specific light source], [shadow characteristics],
[材质]: [key materials with properties], [surface textures], [weathering details],
[风格]: [color grading style], [film stock aesthetic], [visual style reference],
[渲染]: Unreal Engine 5, ray tracing, photorealistic, 8K UHD, cinematic quality
```

#### 增强版8项要素说明

| # | 要素 | 说明 | 示例 |
|---|------|------|------|
| 1 | **空境强调** | 空间氛围、环境情绪、声音氛围 | `Oppressive claustrophobic atmosphere, eerie silence broken by distant echoes` |
| 2 | **镜头** | 焦段、光圈、镜头特性 | `Shot on 14mm ultra-wide lens, f/2.8 aperture, slight barrel distortion` |
| 3 | **构图** | 构图法则、机位角度、画面框架 | `rule of thirds, low angle shot, Dutch angle for unease` |
| 4 | **场景** | 核心描述、建筑风格、空间布局、关键元素 | `abandoned principal's office, Gothic architecture, scattered papers, overturned chair` |
| 5 | **时间气候** | 时间、天气、季节、大气效果 | `late night, dense fog seeping through windows, autumn, misty atmosphere` |
| 6 | **光影** | 全局光照、体积光、丁达尔效应、光源、阴影 | `global illumination, volumetric fog, eerie green light, harsh dramatic shadows` |
| 7 | **材质** | 关键材质及属性、表面纹理、磨损细节 | `worn wood texture, peeling paint, rusted metal fixtures, dust accumulation` |
| 8 | **风格** | 色彩分级、胶片美学、视觉风格参考 | `desaturated dark palette, cold blue shadows, horror film aesthetic` |

#### 使用建议

- **所有场景**：统一使用8要素完整模板
- **恐怖/悬疑题材**：重点强化空境强调要素
- **写实场景**：重点强化材质细节要素
- **商用项目**：必须包含完整8要素

### 场景提示词实战示例

#### 示例1：校长室（恐怖氛围）

```
Oppressive and claustrophobic atmosphere, eerie silence broken by distant water drips and creaking wood,
Shot on 14mm ultra-wide lens, f/2.8 aperture, slight barrel distortion emphasizing spatial depth,
rule of thirds composition, low angle shot emphasizing ceiling height, Dutch angle for psychological unease,
abandoned principal's office, Gothic Revival architecture, decaying mahogany furniture, scattered yellowed papers, overturned leather chair, broken clock frozen at 3:33,
late night around 2 AM, dense fog seeping through broken windows, late autumn, misty cold atmosphere,
global illumination with harsh shadows, volumetric fog catching moonlight, eerie cold green light from windows, Tyndall effect through dust particles, deep shadows in corners,
worn wood texture with visible grain, peeling dark green paint revealing layers beneath, rusted metal door hinges, dust accumulation on surfaces, water stains on ceiling,
desaturated dark palette with cold blue shadows, high contrast, teal and orange color grading, horror film aesthetic, The Conjuring visual reference,
Unreal Engine 5, ray tracing, photorealistic, 8K UHD, cinematic quality
```

#### 示例2：教室（日常场景）

```
Warm and inviting atmosphere, gentle ambient sounds of distant birds chirping, peaceful quietness,
Shot on 35mm cinematic lens, f/1.4 aperture, shallow depth of field,
golden ratio composition, eye-level shot, leading lines from desk rows to windows,
modern high school classroom, minimalist Scandinavian design, clean wooden desks arranged in rows, potted plants on windowsill, whiteboard with colorful markers,
afternoon around 3 PM, soft golden hour sunlight streaming through large windows, spring season, clear sky with few clouds,
global illumination, Tyndall effect through window light creating visible light beams, natural ambient light, soft shadows, warm backlight,
smooth wooden desk surfaces with natural grain, matte white walls, polished linoleum floor reflecting light, fabric curtains with subtle texture,
soft pastel color palette, warm gentle lighting, Kodak Portra 400 aesthetic, overexposed highlights, dreamy atmosphere,
Unreal Engine 5, ray tracing, photorealistic, 8K UHD, cinematic quality
```

#### 示例3：废弃医院走廊（惊悚氛围）

```
Suffocating dread and isolation, oppressive silence punctuated by flickering fluorescent lights buzzing, distant metallic clangs,
Shot on 24mm wide lens, f/2.0 aperture, handheld camera slight shake for documentary realism,
symmetrical composition with vanishing point, eye-level tracking shot, centered framing emphasizing endless corridor,
abandoned hospital corridor, 1970s brutalist architecture, peeling institutional green walls, scattered medical equipment, overturned gurneys, broken ceiling tiles,
twilight around 6 PM, dim natural light fading through dirty windows, winter, cold sterile atmosphere,
global illumination with failing fluorescent lights creating intermittent harsh shadows, volumetric dust in air, cold blue-green light, deep shadows pooling in doorways,
cracked linoleum floor with visible wear patterns, peeling paint revealing concrete beneath, rusted metal bed frames, grimy glass windows, mold growth in corners,
desaturated cold palette, sickly green tint, high contrast shadows, Silent Hill visual aesthetic, found footage horror style,
Unreal Engine 5, ray tracing, photorealistic, 8K UHD, cinematic quality
```

#### 示例4：赛博朋克都市（科幻·雨夜街巷）

```
Overwhelming sensory immersion and technological alienation, cacophony of electronic advertisements, distant sirens, rain hissing on hot neon pipes,
Shot on 50mm anamorphic lens, f/1.4 aperture, anamorphic horizontal lens flare on every neon light source, shallow depth of field isolating foreground,
rule of thirds composition, low angle shot looking upward through narrow alley, leading lines from neon signs converging toward vanishing point in rain-soaked sky,
narrow cyberpunk back alley between mega-skyscrapers, exposed utility pipes and fiber optic cables lining walls, holographic advertisements floating mid-air, street-level ramen stall with steam rising, puddles reflecting neon everywhere,
late night around 11 PM, heavy acid rain pouring through gaps between buildings, perpetual urban twilight from light pollution, humid tropical heat in winter megacity,
global illumination dominated by competing neon sources (magenta from left, cyan from right), volumetric rain catching colored light as millions of streaks, holographic billboard casting animated light patterns on wet surfaces, deep black shadows between neon pools, Tyndall effect through steam vents,
wet concrete with iridescent oil slick reflections, rusted corrugated metal shop shutters, holographic film peeling from walls, chrome pipes with condensation droplets, cracked asphalt with glowing circuit-board-like cracks,
cyberpunk neon palette, magenta and cyan dominance, Blade Runner 2049 visual reference, high saturation neon against desaturated dark base,
Unreal Engine 5, ray tracing, photorealistic, 8K UHD, cinematic quality
```

#### 示例5：仙侠古风（古风·云海仙宫）

```
Transcendent ethereal grandeur and celestial serenity, vast silence of cloud ocean broken only by wind chimes and distant crane calls,
Shot on 16mm ultra-wide lens, f/8 aperture for maximum depth of field capturing infinite scale, slight upward tilt emphasizing vertical majesty,
golden ratio composition, extreme low angle shot from cloud level looking up at floating palace, symmetrical framing of central palace gate with flanking waterfalls,
floating celestial palace above cloud ocean, Tang Dynasty architecture with jade-green glazed roof tiles, white marble carved railings with dragon motifs, cascading waterfalls pouring from floating rock islands into cloud void below, ancient pine trees growing from impossible cliff edges,
dawn around 5:30 AM, first golden light piercing through sea of clouds, spring equinox, crystal-clear atmosphere above cloud layer with infinite visibility,
global illumination from golden sunrise behind palace as primary backlight, Tyndall effect with god rays piercing through palace gate and between pillars, volumetric cloud layer below glowing warm gold on top and cool blue-grey underneath, jade-green architectural elements catching and scattering morning light, soft ambient skylight from vast open sky,
white marble with subtle jade-green veining and morning dew, aged bronze fittings with verdigris patina, glazed ceramic roof tiles with micro-crack crazing, weathered stone steps with moss in crevices, silk banners with gold embroidery catching wind,
traditional Chinese ink wash palette with golden dawn warmth, muted earth tones and jade accents, Crouching Tiger Hidden Dragon meets classical shan shui painting,
Unreal Engine 5, ray tracing, photorealistic, 8K UHD, cinematic quality
```

#### 示例6：史诗战场（战争·黄昏决战）

```
Overwhelming chaos and desperate valor, deafening clash of steel and war drums, earth trembling from cavalry charge, smoke choking battlefield,
Shot on 12mm ultra-wide lens, f/5.6 aperture, extreme wide establishing shot capturing entire battlefield scale, slight Dutch angle for instability,
epic panoramic composition, slightly elevated angle from hillside vantage point, foreground soldiers framing distant castle siege,
massive medieval battlefield on rolling plains before fortified castle, siege towers and trebuchets in mid-operation, cavalry charge colliding with pike formation, scattered banners and fallen standards, field littered with broken weapons and shields,
late afternoon golden hour before sunset, thick smoke columns from burning siege engines mixing with low clouds, late autumn with dead grass and bare trees, heavy atmosphere with ash particles falling like snow,
global illumination from low golden sunset behind castle silhouette creating massive backlight, volumetric smoke and dust clouds catching golden light, fire from burning structures as secondary warm light sources scattered across field, Tyndall effect through smoke gaps creating dramatic god ray columns, long dramatic shadows stretching toward camera,
churned mud and trampled earth with hoof prints and boot marks, dented and scratched steel armor with blood spatter, torn fabric banners with embroidered heraldry, splintered wooden siege equipment, blood-stained grass flattened by combat,
teal and orange color grading with golden hour warmth, Ridley Scott / Kingdom of Heaven visual reference, desaturated midtones with saturated fire highlights,
Unreal Engine 5, ray tracing, photorealistic, 8K UHD, cinematic quality
```

#### 示例7：治愈田园（日常·夏日乡间小路）

```
Gentle nostalgia and peaceful contentment, layered ambience of cicadas and distant wind through grass, rustling leaves and babbling stream,
Shot on 85mm portrait lens, f/1.8 aperture, beautiful bokeh rendering background into dreamy circles of light, shallow depth focusing on foreground wildflowers,
golden ratio composition, eye-level shot along winding country path, leading lines from dirt road disappearing into sunlit distance,
Japanese countryside summer path between rice paddies, wooden utility poles with sagging power lines, small Jizo stone statue at path fork, weathered wooden bus stop with rusted tin roof, wildflowers (cosmos and sunflowers) lining both sides of dirt road,
mid-afternoon around 2 PM, bright summer sun with scattered cumulus clouds creating moving shadow patches on fields, peak summer July, hot and humid with visible heat shimmer on distant road,
global illumination from overhead summer sun, Tyndall effect through scattered cloud edges, soft fill light bouncing from bright green rice paddies, gentle lens flare from direct sunlight, minimal shadows due to high sun angle but soft ground shadows from cumulus clouds drifting across landscape,
packed dirt road with embedded small stones and dried tire tracks, weathered grey wood on bus stop with peeling paint, lush green rice paddy water reflecting sky, rust patina on tin roof, sun-bleached fabric on Jizo statue bib,
Kodak Portra 400 aesthetic with warm golden highlights, soft pastel overexposed quality, Ghibli-meets-photography Japanese countryside nostalgia,
Unreal Engine 5, ray tracing, photorealistic, 8K UHD, cinematic quality
```

#### 示例8：现代都市夜景（都市·摩天楼天台）

```
Exhilarating urban vertigo and metropolitan grandeur, distant traffic hum blending into white noise, high-altitude wind rushing past ears,
Shot on 35mm cinematic lens, f/2.0 aperture, medium depth of field keeping rooftop sharp while city lights become soft bokeh ocean, slight wide-angle for spatial drama,
rule of thirds composition with horizon on lower third, high angle looking down and outward from skyscraper rooftop edge, leading lines from rooftop railing converging toward distant skyline,
modern glass-and-steel skyscraper rooftop at 80th floor, minimalist rooftop garden with architectural lighting, infinity pool reflecting city lights, glass railing at building edge, panoramic view of sprawling metropolitan skyline with competing skyscrapers,
late evening around 9 PM, clear night sky with city light pollution creating warm amber dome, early autumn with crisp cool air, light high-altitude breeze,
global illumination from city light carpet below creating warm ambient uplight on cloud layer, architectural LED lighting on rooftop as local light source (warm white 3200K), thousands of building windows as individual warm point lights creating bokeh field, aircraft warning lights as red accent points, moon providing subtle cool fill light from above,
polished concrete rooftop surface with subtle wet sheen from evening condensation, brushed stainless steel railing with fingerprint smudges, tempered glass panels with city light reflections, infinity pool water surface with micro-ripples distorting reflected lights, potted ornamental grass rustling in wind,
teal and orange color grading, warm city lights against cool night sky, Michael Mann / Collateral visual reference, sophisticated urban elegance,
Unreal Engine 5, ray tracing, photorealistic, 8K UHD, cinematic quality
```

---

## 维度三：道具与硬表面

### 道具提示词公式（T0级）

```
[纯白背景隔离] + [道具身份与叙事] + [多视图/爆炸拆解视图] + [硬表面材质与战损层] + [微距材质特写面板] + [T0级产品渲染画质后缀]
```

#### 6项强制要求

| # | 要求 | 关键词示例 |
|---|------|-----------|
| 1 | 纯白背景隔离 | `pure white background, isolated object, professional product photography studio lighting, no environmental elements` |
| 2 | 道具身份与叙事 | `[weapon/prop name], [origin/lore], [functional purpose], [owner history], [age/era]` |
| 3 | 多视图/爆炸拆解 | `orthographic views (front, side, top, bottom), exploded view showing internal mechanism, cross-section cutaway` |
| 4 | 硬表面材质与战损 | `PBR metallic-roughness, [material type], battle damage layer, wear pattern, patina/oxidation, surface imperfections` |
| 5 | 微距材质特写面板 | `4 extreme macro detail panels: [material 1 micro-texture], [material 2 micro-texture], [joint/mechanism detail], [wear/damage close-up]` |
| 6 | T0级产品渲染后缀 | `8K UHD, product photography quality, professional concept art render, hard surface masterpiece, commercial catalog quality` |

### 道具提示词模板

**融合道具叙事 + 工业级材质细节的T0级完整模板**

```
[纯白背景]: pure white background, isolated object, professional product photography studio (3-point lighting: key light emphasizing surface texture, fill light opening shadow detail, rim light defining silhouette edges), no environmental elements, clean shadow on ground plane only,
[道具身份]: [prop/weapon name], [origin era and cultural context], [functional purpose and mechanism], [owner history and narrative significance], [current condition state],
[多视图]: orthographic prop design sheet: front view, side view (left), top-down view, bottom view, [additional view: 3/4 hero angle / cross-section cutaway / exploded assembly view showing internal components],
[材质战损]: hard surface concept art, PBR metallic-roughness workflow: [primary material with roughness/metallic values], [secondary material], [tertiary material], battle damage layer: [specific damage types], wear pattern: [usage-specific wear], aging: [patina/oxidation/corrosion details],
[微距面板]: 4 extreme macro material detail panels — Panel 1: [primary material micro-texture with PBR values], Panel 2: [secondary material micro-texture], Panel 3: [mechanism/joint/edge detail], Panel 4: [wear/damage/aging close-up with narrative context],
[画质后缀]: 8K UHD, professional hard surface concept art, product photography render quality, PBR material masterpiece, commercial catalog presentation
```

#### 增强版6项要素说明

| # | 要素 | 说明 | 示例 |
|---|------|------|------|
| 1 | **纯白背景** | 强制隔离背景，指定产品级studio布光，确保道具资产可独立使用和合成 | `pure white background, isolated object, 3-point product photography lighting (key at 45° emphasizing engraving depth, fill at -1.5 stops, rim light for edge separation), shadow on ground plane only` |
| 2 | **道具身份** | 道具名称、时代/文化背景、功能机制、所有者历史、当前状态——道具必须有叙事生命 | `"Oathkeeper" bastard sword, forged in 12th century Crusader forge, double-edged hand-and-a-half blade designed for mounted and dismounted combat, wielded by 7 generations of knight-commanders, current state: battle-worn but maintained with reverence` |
| 3 | **多视图** | 正交多视图（正/侧/顶/底）+ 英雄角度3/4视图 + 爆炸拆解或截面图展示内部结构 | `orthographic views: front showing full blade profile, left side showing fuller and edge geometry, top-down showing cross-guard symmetry, exploded view separating: blade, cross-guard, grip wrap, pommel, tang with pin holes` |
| 4 | **材质战损** | 主/次/辅材质各标PBR参数，战损层（砍痕/弹痕/烧灼），磨损层（握持磨光/使用痕迹），老化层（锈蚀/包浆/氧化） | `blade: folded Damascus steel (metallic 0.90, roughness 0.3-0.5 varied by fold pattern), guard: cast bronze with verdigris in recesses (metallic 0.75, roughness 0.6), grip: ray-skin wrapped with silk cord (roughness 0.8), battle damage: 3 visible blade-on-blade impact notches on edge, wear: grip cord compressed and darkened at palm contact` |
| 5 | **微距面板** | 4组极致微距材质特写，每组标注PBR参数+微观纹理描述+叙事含义 | `Panel 1: Damascus steel fold pattern at 10x magnification (visible carbon banding, etched surface revealing serpentine pattern, roughness variation 0.25-0.45 between hard/soft layers), Panel 2: bronze guard verdigris macro (green copper carbonate crystals in recessed engraving, polished gold on raised surfaces from hand contact), Panel 3: grip ray-skin macro (individual calcified denticles visible, centuries of palm oil darkening), Panel 4: blade edge impact notch extreme close-up (deformed steel curling, visible crystalline fracture surface, story of a specific parried blow)` |
| 6 | **画质后缀** | T0级产品渲染画质声明 + 道具设计专业术语 | `8K UHD, professional hard surface concept art, weapon design sheet, museum-quality product photography render, PBR material showcase, commercial catalog masterpiece` |

#### 使用建议

- **所有道具设定**：统一使用6要素完整模板，确保道具资产在后续分镜中可直接引用，每件道具必须有叙事身份
- **古代冷兵器**：强化材质战损的锻造纹理与历史磨损层，微距面板强调金属晶体结构与包浆
- **现代枪械/军事装备**：强化多视图的机械爆炸拆解，材质战损强调工业级表面处理与实战磨损
- **魔法/奇幻道具**：强化材质中的自发光/emissive元素，微距面板加入符文/宝石的内部光散射
- **机甲/载具**：强化爆炸拆解的模块化结构展示，材质战损强调多层装甲复合材料
- **写实日常道具**：强化微距面板的材质真实感，材质战损强调自然使用痕迹而非战斗损伤
- **赛博朋克科技**：强化材质中有机体与机械的交界过渡，微距面板加入电路/LED/生物接口细节

### 6大道具子类型速查表

| # | 子类型 | 风格关键词 |
|---|--------|-----------|
| 1 | 古代冷兵器 | `ancient weapon, forged steel, Damascus pattern, battle-worn, historical craftsmanship, patina, leather/silk wrap, gemstone pommel` |
| 2 | 现代军事装备 | `modern military hardware, mil-spec finish, Cerakote coating, Picatinny rail, modular attachments, field-worn, tactical precision` |
| 3 | 魔法/奇幻道具 | `enchanted artifact, arcane runes (emissive), gemstone with internal light scatter, ancient parchment, mystical materials, magical aura` |
| 4 | 机甲/载具 | `mecha/vehicle hard surface, modular armor plates, hydraulic joints, cockpit detail, battle damage with exposed internals, military markings` |
| 5 | 写实日常道具 | `everyday object, product photography, natural material aging, functional wear pattern, brand-accurate detail, lifestyle patina` |
| 6 | 赛博朋克科技 | `cyberpunk tech, chrome and carbon fiber, LED circuit traces, bio-mechanical interface, holographic display, street-modified aesthetic` |

### 道具实战示例

#### 示例1：仙侠古剑（古代冷兵器·传说级神剑）

```
pure white background, isolated object, professional product photography studio lighting (warm tungsten key light at 45° camera-left emphasizing blade surface Damascus pattern, cool fill from right to open shadow side, strong rim light from behind-left defining blade edge as razor-thin bright line), clean shadow on white ground plane only, no environmental elements,
Prop Identity: "Cangming" (苍冥 — Vast Darkness), legendary immortal-forged longsword, created 3000 years ago by the founder of the Qingxu Sword Sect using meteorite iron smelted in celestial fire, designed as both a cultivation focus and a battlefield weapon capable of channeling sword qi, passed through 47 sword masters (each leaving a faint spiritual imprint on the blade), current state: pristine condition maintained by spiritual energy — the sword appears ancient but uncorroded, with a permanent cold mist emanating from the blade edge,
orthographic prop design sheet: front view (full blade profile showing 90cm blade length, subtle curvature, and blade width tapering from 4cm at guard to 2cm before tip), left side view (showing blade thickness profile, fuller groove depth, and guard cross-section), top-down view (showing blade geometry symmetry, guard ornament detail, and pommel top design), 3/4 hero angle (dramatic presentation with cold mist effect visible along blade edge), exploded assembly view separating: blade (with visible tang extending through grip), jade guard (front and back plates), silk-wrapped grip cord (partially unwound to show ray-skin underlayer), pommel cap (hollow, containing sealed spirit pearl),
PBR metallic-roughness workflow — primary: meteorite Damascus steel blade with unique celestial fold pattern (metallic 0.92, roughness 0.2-0.5 varying along fold lines, subtle blue-silver color shift between hard and soft steel layers visible when etched by spiritual energy), secondary: nephrite jade guard carved as intertwined dragons (roughness 0.3, waxy SSS translucency with internal deep green glow, gold-filled engraved runes in jade surface), tertiary: silk grip cord over ray-skin base (roughness 0.75 for silk, 0.6 for calcified ray-skin denticles), pommel: white jade with silver cap (SSS showing internal luminescence); battle damage layer: blade edge has zero damage (supernaturally maintained) BUT guard shows micro-chips from deflecting lesser blades, silk grip shows 3000 years of hand-oil darkening compressed into permanent patina; aging layer: jade has deepened in color over millennia (dark imperial green versus original pale celadon), silver fittings show noble tarnish in recesses (intentionally unpolished as mark of lineage),
4 extreme macro material detail panels — Panel 1: meteorite Damascus steel fold pattern at 20x magnification (celestial iron creates unique serpentine pattern unlike earthly Damascus, with faint blue luminescence in fold valleys suggesting residual spiritual energy, individual carbon nano-banding visible, roughness variation mapping between hard martensite ridges 0.25 and soft pearlite valleys 0.45), Panel 2: nephrite jade guard dragon carving macro (individual chisel marks from immortal craftsman's jade-carving technique visible at micro level, gold-filled rune channels with meniscus surface tension of molten gold preserved, waxy jade surface with SSS internal glow strongest at thinnest carved areas), Panel 3: grip ray-skin and silk wrap intersection macro (calcified placoid scales of ray-skin visible as individual raised bumps beneath semi-transparent silk, silk thread individual fiber twist visible, centuries of palm oil creating dark amber lacquer-like finish on contact surfaces), Panel 4: blade edge extreme close-up (edge thickness measured in atoms — supernatural sharpness, faint cold mist condensation droplets forming on blade surface from temperature differential, micro-frost crystallization pattern at edge),
8K UHD, professional hard surface concept art, legendary weapon design sheet, museum-quality product photography render, xianxia immortal artifact, PBR material showcase masterpiece
```

#### 示例2：战术步枪（现代军事·特种作战定制枪）

```
pure white background, isolated object, professional product photography studio lighting (neutral daylight-balanced key light at 30° camera-right emphasizing Cerakote matte finish and rail system geometry, minimal fill to maintain tactical shadow depth, crisp rim light from behind defining every rail slot and accessory edge), technical shadow on white ground plane, no environmental elements,
Prop Identity: "SCAR-H Mk.20 SSR — Callsign 'Whisper'", highly customized FN SCAR-H platform converted to designated marksman role by Tier-1 JSOC unit armorer, 7.62×51mm NATO chambered for 800m precision engagement, this specific rifle has 2,847 confirmed rounds through barrel with detailed shot log, personal weapon of a senior operator with 6 combat deployments — every modification earned through specific mission requirements, current state: field-worn but meticulously maintained, Cerakote showing holster wear at grip points,
orthographic prop design sheet: left side view (full profile showing 20" heavy barrel, extended handguard, optic, suppressor, bipod in folded position), right side view (showing ejection port detail, fire selector markings, sling mount points, cheek riser adjustment), top-down view (showing Picatinny rail system full length, optic turret caps, laser/IR designator offset mount), exploded assembly view separating: upper receiver, lower receiver with trigger group, bolt carrier group, charging handle, barrel assembly with gas block, free-float handguard with M-LOK panels, buttstock assembly with adjustable cheek riser and length-of-pull spacers, all accessories dismounted and arranged: optic (Nightforce ATACR 4-16×42), suppressor (Surefire SOCOM762-RC2), bipod (Atlas BT47 V8), PEQ-15 laser/IR, Surefire M600V weapon light, Magpul MBUS Pro backup sights,
PBR metallic-roughness workflow — primary: 7075-T6 aluminum receivers with Cerakote Burnt Bronze finish (metallic 0.1, roughness 0.7 matte base, roughness 0.4-0.5 at holster wear points where base aluminum shows through), secondary: cold hammer-forged chrome-lined steel barrel with phosphate finish (metallic 0.85, roughness 0.6), tertiary: polymer furniture — Magpul FDE (roughness 0.8, zero metallic, subtle texture stippling pattern); battle damage layer: Cerakote wear at mag well entry from thousands of tactical reloads (base aluminum visible in crescent pattern), stock shows impact ding from specific mission (Operator chose not to refinish — "it earned that"), suppressor shows heat discoloration gradient (straw yellow to purple to blue from muzzle end); wear pattern: grip texture compressed and polished at habitual hand position, optic turret caps show fingernail marks from rapid field adjustment, sling swivel mount polished to mirror from constant friction,
4 extreme macro material detail panels — Panel 1: Cerakote surface finish macro (ceramic-polymer matrix visible at micro level, consistent stipple texture of spray application, wear-through zone showing smooth aluminum substrate underneath with machining marks, clear boundary between worn and coated areas revealing exact hand placement), Panel 2: bolt carrier group chrome surface macro (chrome bore lining with carbon fouling pattern from 2,847 rounds, extractor claw with brass transfer residue embedded in tool steel, gas key staking marks with Loctite residue), Panel 3: Nightforce optic lens macro (multi-layer anti-reflective coating showing purple-green color shift, dust cover O-ring seal with compression set, laser-etched serial number with fill paint), Panel 4: suppressor baffle stack cross-section (Inconel alloy baffles with carbon buildup gradient decreasing from blast chamber to end cap, weld seams between baffle cones, heat discoloration showing thermal history),
8K UHD, professional hard surface concept art, military weapon system design sheet, mil-spec product photography render, tactical equipment catalog masterpiece
```

#### 示例3：魔法典籍（奇幻·禁忌之书）

```
pure white background, isolated object, professional product photography studio lighting (warm amber key light at 60° camera-left creating dramatic shadow in page folds and carved cover relief, cool blue-tinted fill from right suggesting arcane cold, subtle green-tinted rim light from behind simulating internal magical glow bleeding through cover edges), clean shadow on white ground plane, no environmental elements,
Prop Identity: "Codex Abyssalis" (深渊法典), forbidden grimoire of void magic, created by an unnamed heretic archmage 800 years ago using materials harvested from three planes of existence — mortal realm leather, fey realm silver, and abyssal realm ink, the book is semi-sentient and resists opening by the unworthy (cover chains are self-locking), contains 666 pages of void incantations written in ink that shifts between languages, current state: the book has been sealed in a cathedral vault for 400 years — its malevolent aura has stained the surrounding white marble black in a 1-meter radius,
orthographic prop design sheet: front cover view (showing full leather-and-metal cover design with central eye motif, chain-lock system, corner reinforcements), back cover view (showing simpler design with drain-channels for leaked magical energy), spine view (showing 5 raised bands, metal spine reinforcements, title embossed in shifting script), open-book spread view (showing interior pages with self-illuminating void-ink text and animated margin illustrations), exploded assembly view separating: front cover (leather stretched over boards), chain-lock mechanism (9 interlocking chains with central padlock shaped as screaming face), metal corner guards (4, each different demon face), spine hardware, page block (showing deckle-edged pages with gilt — but gold is tarnished black), back cover,
PBR metallic-roughness workflow — primary: cover leather — human-realm origin but altered by 800 years of void energy exposure (roughness 0.8 base, but with areas of unnatural smoothness 0.3 where the leather has become semi-crystallized, color shifted from original brown to deep purple-black, subtle iridescent oil-slick sheen at certain angles); secondary: fey-silver metalwork — corner guards, spine bands, chain links, lock (metallic 0.95, roughness 0.1 for untouched surfaces BUT void-tarnish creating matte black areas roughness 0.9, the silver resists corruption unevenly creating dramatic contrast); tertiary: abyssal ink on pages (emissive shader — text glows faint purple-black, paradoxically darker than the surrounding parchment while still luminous, SSS through parchment pages showing text bleed-through); chain-lock mechanism: wrought iron with silver inlay (each chain link hand-forged with visible hammer marks, lock shaped as screaming face with gemstone eyes — garnets with internal dark emissive); aging layer: cover leather cracked along spine fold from hundreds of forced openings, void energy staining as black veining spreading from text-block edge into cover like capillary action, silver tarnish pattern reveals which chains have been most tested by would-be readers,
4 extreme macro material detail panels — Panel 1: cover leather surface macro (original grain pattern still visible but overlaid with void-crystallization — smooth glassy patches growing from within the leather like frost on a window, purple-black color with depth suggesting the leather is deeper than its physical thickness, micro-cracks at crystallization boundaries revealing original warm brown leather underneath), Panel 2: fey-silver corner guard demon face macro (exquisite micro-engraving detail of demon's expression — different emotion from each viewing angle due to fey metalworking, void-tarnish concentrated in expression lines creating enhanced relief, silver surface where fingers have touched remains bright from skin-oil contact breaking tarnish, individual chain-link forge-weld seam visible), Panel 3: abyssal ink on parchment page macro (ink appears to exist slightly above the page surface — visible shadow between text and parchment, characters shift slowly even in still image, ink has depth — looking into the text is like looking into a dark pool, surrounding parchment shows yellow aging except near text where void-bleaching creates white halos), Panel 4: chain-lock screaming face macro (garnet gemstone eyes with internal fractures creating star-pattern reflection, emissive dark glow from within stone suggesting trapped entity, silver inlay in iron chain link showing bi-metallic corrosion boundary, keyhole shaped as inverted cross with signs of attempted lock-picking scratches from centuries of curious archivists),
8K UHD, professional hard surface concept art, enchanted artifact design sheet, dark fantasy prop masterpiece, PBR material showcase with emissive magical elements
```

#### 示例4：战斗机甲（机甲/载具·重型突击单位）

```
pure white background, isolated object, professional product photography studio lighting (cool industrial key light at 35° camera-left simulating hangar bay overhead, warm secondary from lower-right simulating deck-level work lights, strong rim light from behind-left defining armor panel silhouette separation), mechanical shadow on white ground plane, no environmental elements,
Prop Identity: "GK-07 Ragnarök" heavy assault mecha, 12-meter bipedal weapons platform manufactured by Krieger Dynamics for planetary siege operations, unit serial GK-07-2241, this specific unit survived the Battle of Europa Station with 340+ hours of combat deployment, piloted by veteran operator "Hammerfall" who has personalized the cockpit and armor with kill-tally markings and unit insignia, current state: post-deployment maintenance bay — hull patched but not repainted, kill markings preserved by tradition,
orthographic mecha design sheet: front view (full 12m height, arms at rest with rotary cannon in right hand and tower shield mag-locked to left forearm), rear view (showing thruster array, ammunition drum access panels, exhaust venting system, power cable routing), left side view (showing cockpit hatch mechanism, hip joint hydraulics, leg actuator detail), right side view (showing shoulder missile pod in closed position, arm weapon hardpoints), top-down view (showing dorsal armor layout, sensor dome, and escape hatch); modular exploded assembly view separating major subsystems: HEAD unit (sensor dome with multi-spectrum array, communications antenna, targeting laser), TORSO (cockpit module with pilot seat visible, reactor housing with shielding, ammunition storage), RIGHT ARM assembly (rotary cannon "Fenrir" with barrel cluster, ammo feed mechanism, shoulder actuator), LEFT ARM assembly (tower shield "Aegis" with ablative facing, forearm housing, wrist joint), HIP/LEG assemblies (x2, showing hydraulic piston arrangement, armored knee joint, feet with magnetic clamp system), BACKPACK unit (thruster array, heat sink fins, missile pod magazine),
PBR metallic-roughness workflow — primary: hull armor plates — layered composite (outer: reactive armor tiles — matte dark grey Cerakote metallic 0.15, roughness 0.75, inner: titanium-carbide structural plate metallic 0.9, roughness 0.4 — visible where reactive tiles have been destroyed and replaced with mismatched field-repair patches); secondary: joint actuators and hydraulics — exposed machined steel with hydraulic fluid sheen (metallic 0.85, roughness 0.3, black rubber hydraulic line roughness 0.9); tertiary: cockpit canopy — laminated armored glass with spiderweb stress-fracture (refraction shader, roughness 0.05 clean areas, 0.7 at fracture lines); battle damage layer: LEFT TORSO — 3 penetration holes from railgun rounds (entry holes clean-edged, surrounding reactive armor tiles detonated and cratered, field-welded steel patch plates visible with rough bead), RIGHT LEG — gouged armor from melee combat (deep scoring revealing layered armor composition), SHIELD — ablative facing 60% consumed (underlayer ceramic honeycomb structure exposed); wear pattern: foot magnetic clamps polished bright from terrain contact, hand grip on rotary cannon worn smooth at habitual hold position, cockpit hatch seal edge worn from repeated entry/exit; personalization: 47 kill-tally marks hand-stenciled below cockpit (white paint, deliberately crude), unit patch "Hammerfall" painted on left shoulder, small lucky charm dangling from cockpit mirror mount,
4 extreme macro material detail panels — Panel 1: reactive armor tile surface macro (ceramic face with micro-crack network from thermal cycling, Cerakote matte finish with blast-residue embedded in surface texture, tile mounting bolt with safety wire still attached, gap between tiles showing structural plate underneath), Panel 2: hydraulic knee joint mechanism macro (precision-ground steel piston shaft with micro-scoring from particulate ingress, rubber seal with compression set and slight weeping of amber hydraulic fluid, hardened steel bearing race with individual ball bearings visible, grease nipple with fresh lubricant bead), Panel 3: cockpit canopy stress-fracture macro (laminated glass layers visible in cross-section at fracture: outer ballistic layer, energy-absorbing interlayer, inner anti-spall layer, fracture propagation pattern radiating from impact point, trapped air bubbles in interlayer near fracture), Panel 4: field-repair weld patch macro (rough MIG weld bead with spatter, heat-affected zone showing steel temper colors, mismatched paint where field-grey patch meets original dark grey hull, visible grinding marks where weld was dressed down to clear adjacent hatch),
8K UHD, professional hard surface concept art, military mecha design sheet, AAA game vehicle concept, industrial product photography render masterpiece
```

#### 示例5：复古相机（写实日常·徕卡M3胶片相机）

```
pure white background, isolated object, professional product photography studio lighting (soft warm key light at 50° camera-left through large silk diffusion panel — emulating gallery display lighting, minimal cool fill maintaining gentle shadow density, crisp rim light from behind emphasizing chrome and brass edge reflections), elegant shadow on white ground plane, no environmental elements,
Prop Identity: Leica M3 Double-Stroke rangefinder camera, serial number 700xxx (1954 first-batch production), original Wetzlar manufacture, paired with Leica Summicron 50mm f/2 collapsible lens (matching era), this specific camera was purchased new by a Life Magazine photojournalist in 1954 and used professionally for 30 years covering civil rights movement, Vietnam War, and Woodstock — every scratch and brass wear mark is a chapter of photographic history, current state: fully functional (recently CLA'd by authorized Leica technician), cosmetically honest — no re-covering or re-chroming, wearing its history proudly,
orthographic prop design sheet: front view (showing lens mounted and extended, rangefinder windows, self-timer lever, lens release button), rear view (showing film door with hinge, viewfinder eyepiece, film rewind knob), top view (showing top plate with shutter speed dial, film advance lever, accessory hot shoe, frame counter), bottom view (showing baseplate with tripod socket, serial number engraving, film door release), 3/4 hero angle (classic presentation angle showing front-top chrome and lens barrel); exploded assembly view: top plate (showing internal rangefinder prism assembly), lens mount and bayonet ring, shutter curtain assembly (visible through lens opening), body shell with vulcanite covering, baseplate with internal film pressure plate, lens separately: front element, aperture ring, focus helicoid, rear element, collapsible inner barrel,
PBR metallic-roughness workflow — primary: chrome top plate and body trim (metallic 0.95, roughness 0.08 in preserved areas — near mirror finish, roughness 0.3-0.6 at brassing wear points where chrome has worn through to brass substrate); secondary: black vulcanite body covering (roughness 0.85, zero metallic, pebbled texture with micro-relief diamond pattern, edges lifting slightly where adhesive has aged); tertiary: glass lens elements (refraction shader, multi-coating showing subtle amber-purple shift, roughness 0.02 optical surfaces); brass substrate (visible at wear points — warm golden color, metallic 0.85, roughness 0.4, fingerprint oil patterns visible on frequently touched brass); aging layer: chrome brassing concentrated at: film advance lever thumb contact, top plate corners, lens barrel grip zone, baseplate edges — following 30 years of professional daily handling; vulcanite shows slight shrinkage cracks at body corners; lens barrel has fine circumferential wear marks from thousands of focus pulls,
4 extreme macro material detail panels — Panel 1: top plate chrome-to-brass transition macro (gradual wear boundary visible — chrome thinning to reveal nickel intermediate layer before brass, individual micro-scratches in chrome surface each catching light differently, fingerprint oil residue on brass creating slightly darker oxidation patches, engraved "Leica" lettering with original black fill paint 80% worn away revealing bright engraving groove), Panel 2: vulcanite pebble texture macro (individual diamond-shaped pebble peaks with 70 years of hand-polishing creating subtle sheen on high points, valley areas retaining original matte texture, edge of vulcanite where it meets chrome body trim showing slight gap from shrinkage, adhesive residue visible in gap), Panel 3: Summicron front element macro (multi-coating showing Newton-ring-like color patterns in reflected studio light, single cleaning mark — fine swirl from improper 1970s lens tissue, brass focus ring knurling with individual diamond-cut grooves partially filled with decades of hand cream and dust), Panel 4: film pressure plate and internal mechanism macro (precision-ground stainless steel pressure plate with micro-polished surface (roughness 0.1), film guide rails with film-emulsion residue from thousands of rolls, shutter curtain textile with rubberized surface showing slight craze pattern from 70 years of elastic stress),
8K UHD, professional product photography, vintage camera collector reference, museum-quality catalog render, luxury heritage object masterpiece
```

#### 示例6：赛博朋克义体（赛博朋克科技·军用改造手臂）

```
pure white background, isolated object, professional product photography studio lighting (cold blue-white key light at 40° camera-right simulating clinical lab lighting, warm amber secondary from left suggesting street neon ambient, dual rim lights — cool blue from behind-right and magenta from behind-left creating cyberpunk color-split edge definition), technical shadow on white ground plane, no environmental elements,
Prop Identity: "Mantis Mk.IV" military-grade cybernetic right arm prosthesis, manufactured by Arasaka BioMech Division (black market unit — serial filed off), designed for covert-ops operatives requiring enhanced strength (3x human baseline), embedded weapon systems, and sensory augmentation, this specific unit has been street-modified by an underground ripperdoc — warranty voided, military firmware jailbroken, cosmetic panels partially removed to expose internals for faster field maintenance, current state: 14 months post-installation, showing mix of clinical precision engineering and crude street customization,
orthographic prop design sheet: front view (showing full arm from shoulder mount to fingertips, fingers slightly splayed revealing palm sensor array), rear view (showing posterior muscle bundle routing, elbow joint mechanism, dorsal data port array), medial view (showing inner arm with exposed myomer muscle bundles through removed panel, embedded forearm blade housing in retracted position), lateral view (showing outer arm with intact armor panels, shoulder joint ball-and-socket mechanism, wrist data-jack); cross-section cutaway view at mid-forearm (showing layer structure: outer armor shell, shock-absorbing gel layer, myomer muscle bundles, carbon-fiber endoskeleton, central wiring harness, embedded retractable blade in sheath); exploded assembly view separating: shoulder mount with neural interface collar, upper arm assembly (endoskeleton + muscle bundles + armor panels), elbow joint (hydraulic + servo hybrid mechanism), forearm assembly with embedded blade system, wrist joint with 360° rotation mechanism, hand with individual articulated finger assemblies (5 fingers, each with 3 phalanges and haptic sensor pads),
PBR metallic-roughness workflow — primary: titanium endoskeleton and structural frame (metallic 0.92, roughness 0.25 brushed finish, visible CNC machining marks on internal surfaces); secondary: myomer artificial muscle bundles in translucent silicone housing (roughness 0.4, SSS with deep red internal glow when under load — simulating biological muscle flush, silicone housing with micro-tear stress marks from 14 months of superhuman force output); tertiary: carbon fiber armor panels (anisotropic reflection, roughness 0.15, weave pattern visible at macro, panels showing street-customization: one panel replaced with raw brushed steel plate, another removed entirely and zip-tied open); chrome interface ports and data jacks (metallic 1.0, roughness 0.05 mirror finish on maintained ports, roughness 0.5 with oxidation on neglected ones); embedded blade: monomolecular-edged tungsten carbide (metallic 0.9, roughness 0.1, edge too thin to resolve — renders as bright emissive line); LED circuit traces on exposed internal surfaces (emissive cyan, 0.2Hz pulse animation); neural interface collar: bio-compatible polymer ring with embedded electrodes (roughness 0.6, subtle SSS showing internal wiring, surgical-grade steel electrode contacts with skin-residue patina); street modifications visible: aftermarket LED strips (cyan, hot-glued to endoskeleton), rewired power junction with exposed solder joints, black electrical tape on one hydraulic line,
4 extreme macro material detail panels — Panel 1: myomer muscle bundle through silicone housing macro (artificial muscle fibers visible as parallel strands within translucent housing, individual fiber contracts and relaxes visible as thickness variation, silicone housing micro-tears at high-stress points creating white stress marks against red-tinted base, nutrient/coolant fluid visible between fibers as amber liquid with micro-bubbles), Panel 2: neural interface collar skin-boundary macro (surgical boundary where organic skin meets polymer collar — visible scar tissue ring, skin growing slightly over collar edge indicating body's attempt to integrate, electrode contacts with subtle green patina from bio-electrical interaction, individual skin pores at boundary edge showing chronic mild inflammation — slight redness), Panel 3: embedded blade deployment mechanism macro (tungsten carbide blade edge at extreme magnification showing monomolecular sharpness — single-atom edge width rendered as razor-bright emissive line, blade housing channel with PTFE-coated guide rails showing blade travel wear marks, micro-hydraulic deployment piston with visible extension), Panel 4: street-modified power junction macro (original Arasaka-precision circuit board with surface-mount components visible, ripperdoc's crude solder joints adding aftermarket power tap — solder blobs with flux residue, black electrical tape wrap on bypass wire, LED strip hot-glue mount with visible adhesive squeeze-out, contrast between military precision engineering and street-level improvisation telling the story of this arm's journey from factory to black market to back-alley installation),
8K UHD, professional hard surface concept art, cybernetic prosthesis design sheet, cyberpunk tech showcase, bio-mechanical product photography masterpiece, next-gen game prop reference
```

---

## 维度四：色彩分级预设

### 色彩分级提示词公式（T0级）

```
[色彩预设风格] + [主色调与辅色调定义] + [高光/中间调/暗部色偏] + [胶片/LUT参考] + [饱和度与对比度控制] + [色彩情绪关键词]
```

#### 6项强制要求

| # | 要求 | 关键词示例 |
|---|------|-----------|
| 1 | 色彩预设指定 | `teal and orange color grading` / `cyberpunk neon palette` / `Kodak Portra 400 aesthetic` |
| 2 | 主辅色调定义 | `primary: warm amber, secondary: cool teal` / `dominant magenta with cyan accents` |
| 3 | 三区色偏 | `warm golden highlights, neutral midtones, cool blue shadows` |
| 4 | 胶片/LUT参考 | `Kodak Vision3 500T` / `Fujifilm Pro 400H` / `cinematic LUT reference` |
| 5 | 饱和度与对比度 | `high saturation, medium contrast` / `desaturated, high contrast` / `muted colors, low contrast` |
| 6 | 色彩情绪 | `warm and inviting` / `cold and clinical` / `dreamy and nostalgic` / `oppressive and suffocating` |

### 色彩分级提示词模板

**融合色彩情绪 + 技术参数的T0级完整模板**

```
[色彩预设]: [preset style name], [visual reference],
[主辅色调]: primary [dominant color tone], secondary [accent color tone], [color relationship],
[三区色偏]: highlights [highlight color shift], midtones [midtone character], shadows [shadow color cast],
[胶片参考]: [film stock / LUT reference], [grain characteristics], [color rendering intent],
[饱和对比]: [saturation level], [contrast level], [dynamic range preference],
[色彩情绪]: [emotional atmosphere], [psychological color association], [narrative color intent]
```

#### 增强版6项要素说明

| # | 要素 | 说明 | 示例 |
|---|------|------|------|
| 1 | **色彩预设** | 指定整体调色风格流派或参考作品 | `teal and orange cinematic color grading, Blade Runner 2049 visual reference` |
| 2 | **主辅色调** | 定义画面中占主导的色调及互补/点缀色 | `primary: deep teal (#008080), secondary: burnt orange (#CC5500), complementary split` |
| 3 | **三区色偏** | 分别控制高光、中间调、暗部的色彩倾向 | `warm golden highlights, slightly desaturated midtones, deep blue-purple shadows` |
| 4 | **胶片参考** | 指定胶片类型或数字LUT参考，含颗粒感特征 | `Kodak Vision3 500T tungsten film, fine grain, slightly warm color rendering` |
| 5 | **饱和对比** | 明确饱和度、对比度、动态范围的程度 | `moderately desaturated, high contrast, compressed dynamic range for cinematic look` |
| 6 | **色彩情绪** | 色彩传达的情绪氛围与叙事意图 | `melancholic nostalgia, faded memories, bittersweet warmth suggesting lost time` |

#### 使用建议

- **所有场景**：统一使用6要素完整模板，确保色彩分级与剧情情绪匹配
- **恐怖/悬疑题材**：优先使用暗黑冷调，强化三区色偏中暗部的色彩压迫感
- **商业/电影级**：优先使用青橙色调，搭配胶片参考增强质感
- **怀旧/文艺题材**：优先使用柯达胶片预设，强调颗粒感与暖色高光
- **科幻/赛博题材**：优先使用赛博朋克预设，强调霓虹色与高饱和度
- **古风/仙侠题材**：优先使用国风水墨预设，强调低饱和与水墨质感

### 可选色彩分级预设速查

| 预设名 | 关键词 | 适用场景 |
|--------|--------|----------|
| 青橙色调 | `teal and orange color grading, complementary colors` | 电影级、商业广告 |
| 赛博朋克 | `cyberpunk neon palette, magenta and cyan, neon glow` | 科幻、未来都市 |
| 柯达胶片 | `Kodak Portra 400 aesthetic, warm highlights, soft grain` | 怀旧、文艺 |
| 暗黑冷调 | `desaturated dark palette, cold blue shadows, high contrast` | 悬疑、恐怖 |
| 日系清新 | `soft pastel colors, overexposed highlights, dreamy atmosphere` | 治愈、校园 |
| 国风水墨 | `traditional Chinese ink wash palette, muted earth tones` | 古风、仙侠 |

### 色彩分级实战示例

#### 示例1：青橙色调（动作电影·追逐场景）

```
teal and orange cinematic color grading, Michael Bay / Mad Max: Fury Road visual reference,
primary: warm burnt orange and amber skin tones, secondary: deep teal shadows and background, complementary color harmony,
highlights: warm golden-orange push (+15 warmth), midtones: neutral with slight amber shift, shadows: rich teal-cyan cast with deep blacks,
Kodak Vision3 500T tungsten film stock, medium grain texture, warm color rendering with teal crossprocessing,
high saturation on skin tones, strong contrast with crushed blacks, wide dynamic range preserving highlight detail,
intense adrenaline-fueled energy, heroic warmth against cold danger, visual tension through color opposition
```

#### 示例2：暗黑冷调（悬疑惊悚·犯罪现场）

```
desaturated dark palette, Se7en / Zodiac visual reference, neo-noir color grading,
primary: cold steel blue-grey, secondary: sickly pale yellow from artificial lighting, monochromatic with minimal accent color,
highlights: blown-out pale yellow-green from fluorescent lights, midtones: heavily desaturated grey-blue, shadows: near-black with subtle blue-purple shift,
Fujifilm Eterna 500T emulation, heavy grain in shadow areas, clinical cold color rendering,
heavily desaturated (−40 saturation), extreme high contrast, narrow dynamic range with crushed shadows,
suffocating dread and hopelessness, clinical detachment, moral decay visualized through color absence
```

#### 示例3：国风水墨（仙侠·山巅论剑）

```
traditional Chinese ink wash palette, Crouching Tiger Hidden Dragon visual reference, xianxia ink painting aesthetic,
primary: muted ink black and stone grey, secondary: subtle jade green and vermillion red accents, analogous earth tone harmony,
highlights: soft rice paper white with warm cream undertone, midtones: desaturated sage green and stone grey, shadows: deep ink black with subtle warm brown,
no specific film stock — emulate traditional Chinese scroll painting tonal range, no grain, smooth tonal gradations like ink wash on xuan paper,
low saturation (muted and restrained), low-medium contrast with smooth tonal transitions, extended midtone range mimicking ink wash gradients,
transcendent serenity and ancient gravitas, wu-wei philosophical calm, timeless elegance of Chinese literati aesthetic
```

#### 示例4：赛博朋克（科幻·未来都市夜巡）

```
cyberpunk neon palette, Blade Runner 2049 / Ghost in the Shell visual reference, neo-Tokyo dystopian color grading,
primary: electric magenta and hot pink, secondary: deep cyan and turquoise, triadic neon harmony with dark base,
highlights: blown-out neon white-pink and white-cyan from holographic signs, midtones: saturated magenta-purple and electric blue, shadows: near-black with deep purple undertone and subtle neon bleed,
no traditional film stock — digital sensor aesthetic with intentional chromatic aberration, no grain but digital noise artifacts in dark areas, hyper-saturated color rendering pushing beyond natural gamut,
extreme high saturation on neon elements (+60), high contrast with pitch-black base, narrow dynamic range — crushed blacks with blown-out neon highlights intentionally clipping,
sensory overload and technological sublime, alienation within hyper-connected society, seductive danger of neon-lit urban decay, cybernetic transcendence
```

#### 示例5：柯达胶片（怀旧文艺·夏日午后野餐）

```
Kodak Portra 400 aesthetic, Call Me By Your Name / Moonrise Kingdom visual reference, nostalgic golden hour film photography,
primary: warm golden amber and honey tones, secondary: soft sage green and muted lavender, analogous warm harmony with pastel accents,
highlights: creamy overexposed warm white with golden halo, midtones: rich warm amber with soft peach skin rendering, shadows: gentle brown-orange with lifted blacks (never true black),
Kodak Portra 400 daylight film stock, fine organic grain visible on skin and sky, characteristic warm color rendering with signature pastel highlight rolloff and forgiving skin tone latitude,
moderate saturation (naturally pleasing, not pushed), low-medium contrast with smooth tonal curve and lifted shadows, wide dynamic range with gentle highlight rolloff preserving cloud detail,
bittersweet nostalgia and sun-drenched innocence, fleeting summer beauty, warmth of cherished memories slowly fading, analog imperfection as emotional authenticity
```

#### 示例6：日系清新（治愈校园·樱花树下告白）

```
soft pastel colors, Your Lie in April / March Comes in Like a Lion visual reference, Japanese shoujou manga color aesthetic,
primary: soft cherry blossom pink and pearl white, secondary: pale sky blue and light lavender, pastel analogous harmony with high-key luminosity,
highlights: blown-out pure white with subtle warm pink bloom and lens flare, midtones: delicate pastel pink and soft cream with translucent quality, shadows: very light lavender-grey (almost no true shadows), lifted to maintain dreamy airiness,
Fujifilm Pro 400H emulation with deliberate +1.5 stop overexposure, minimal fine grain barely visible, characteristic cool-neutral rendering with ethereal pastel shift in overexposed areas,
low-moderate saturation (soft and muted pastels, never vivid), very low contrast with compressed tonal range skewed toward highlights, extreme high-key exposure with minimal shadow information,
innocent first-love flutter and emotional vulnerability, ephemeral beauty of cherry blossoms as metaphor for fleeting youth, gentle melancholy beneath surface sweetness, pure and uncomplicated tenderness
```

---

## 维度五：极致动漫美学

### 极致动漫提示词公式（T0级）

```
[顶级工作室画风指定] + [角色极度张力姿态] + [色彩与笔触美学] + [光影与VFX特效] + [背景环境] + [T0级二次元画质后缀]
```

#### 6项强制要求

| # | 要求 | 关键词示例 |
|---|------|-----------|
| 1 | 工作室画风指定 | `Ufotable style` / `Studio Trigger style` / `Kyoto Animation style` |
| 2 | 角色张力姿态 | `dynamic battle pose, mid-air slash` / `wind-blown hair, dramatic cape flutter` / `emotional breakdown, tears streaming` |
| 3 | 色彩与笔触美学 | `bold black outlines, cel-shading` / `soft watercolor gradients` / `high-contrast neon palette` |
| 4 | 光影与VFX特效 | `elemental aura, glowing particle effects` / `volumetric god rays` / `impact frame with speed lines` |
| 5 | 背景环境 | `detailed cityscape at twilight` / `lush greenery, hand-painted background` / `abstract dark void with energy wisps` |
| 6 | T0级二次元画质后缀 | `best quality, ultra-detailed, masterpiece, official art, sharp focus, vibrant colors` |

### 极致动漫提示词模板

**融合工作室风格 + 动态表现力的T0级完整模板**

```
[工作室画风]: [studio name] style, [specific visual traits of the studio], [art direction reference],
[角色姿态]: [character identity], [dynamic pose description], [motion state], [clothing/hair dynamics],
[色彩笔触]: [line art style], [coloring technique], [color palette characteristics], [brush stroke quality],
[光影VFX]: [primary light source], [VFX effects], [particle systems], [impact/speed effects], [aura/energy visualization],
[背景环境]: [environment description], [depth layers], [atmospheric effects], [background art style],
[画质后缀]: best quality, ultra-detailed, masterpiece, official art, sharp focus, vibrant colors, highly detailed eyes, detailed hair strands, dynamic lighting, [studio name] official artwork quality
```

#### 增强版6项要素说明

| # | 要素 | 说明 | 示例 |
|---|------|------|------|
| 1 | **工作室画风** | 指定具体工作室名称、视觉特征、参考作品 | `Ufotable style, Demon Slayer visual reference, hyper-realistic CGI blended with 2D cel animation` |
| 2 | **角色姿态** | 角色身份、动态姿态、运动状态、衣发飘动 | `male swordsman, mid-air horizontal slash, body rotating 270 degrees, haori fluttering in wind, intense focused expression` |
| 3 | **色彩笔触** | 线稿风格、上色技法、色板特征、笔触质感 | `clean sharp line art with variable thickness, digital cel-shading with gradient shadows, saturated warm-cool contrast palette` |
| 4 | **光影VFX** | 主光源、特效系统、粒子效果、冲击/速度线、能量可视化 | `blazing fire aura as primary light source, massive glowing ember particles, radial speed lines, impact frame with white flash` |
| 5 | **背景环境** | 环境描述、景深层次、大气效果、背景画风 | `moonlit bamboo forest, three-layer parallax depth (foreground bamboo silhouettes, midground clearing, background full moon), volumetric mist` |
| 6 | **画质后缀** | 标准二次元画质关键词组合 + 工作室品质声明 | `best quality, ultra-detailed, masterpiece, official art, Ufotable official artwork quality, anime key visual` |

#### 使用建议

- **所有动漫风格画面**：统一使用6要素完整模板，确保工作室风格一致性
- **战斗/动作场景**：优先选用扳机社、飞碟社、MAPPA，强化光影VFX与角色姿态要素
- **日常/治愈场景**：优先选用京阿尼、吉卜力，强化背景环境与色彩笔触要素
- **都市/风景壁纸级**：优先选用新海诚风格，强化背景环境层次与大气光效
- **暗黑/男频爽文**：优先选用韩漫风格，强化角色姿态的压迫感与暗色调VFX
- **怀旧/致敬经典**：优先选用90年代复古风格，强化色彩笔触的胶片质感与赛璐珞手感

### 8大工作室风格

| # | 工作室 | 风格关键词 |
|---|--------|-----------|
| 1 | 扳机社 / 赛博张力 | `Studio Trigger style, hyper-dynamic angle, high-contrast neon colors, visual explosion, bold black outlines, extreme perspective, impact frame` |
| 2 | 飞碟社 / 极致光污染 | `Ufotable style, hyper-realistic CGI VFX blending with 2D, massive glowing particle effects, elemental aura, flowing energy trails` |
| 3 | 顶级韩漫 / 暗黑大男主 | `Korean Webtoon style, Solo Leveling art style, sharp line art, dark shadowy aura, intimidating presence, vertical scroll format` |
| 4 | 90年代复古 / 蒸汽波 | `90s retro anime style, VHS filter, muted pastel colors, nostalgic atmosphere, CRT monitor scanlines, cel animation aesthetic` |
| 5 | MAPPA / 混沌暴力美学 | `MAPPA studio style, cinematic fisheye lens, sketchy line art, chaotic action, gritty texture, dynamic motion blur` |
| 6 | 京阿尼 / 极致微观光影 | `Kyoto Animation style, photographic lighting, hyper-detailed sparkling eyes, detailed water reflections, soft ambient light` |
| 7 | 吉卜力 / 治愈系手绘 | `Studio Ghibli style, hand-painted watercolor background, lush greenery, soft sunlight, warm earth tones, whimsical atmosphere` |
| 8 | 新海诚 / 极致环境壁纸 | `Makoto Shinkai style, breathtaking twilight, glowing cumulus clouds, gorgeous lens flare, Tyndall effect, hyper-detailed cityscape` |

### T0级二次元画质后缀

```
best quality, ultra-detailed, masterpiece, official art, 
sharp focus, vibrant colors, highly detailed eyes,
detailed hair strands, dynamic lighting,
[studio name] official artwork quality
```

### 极致动漫实战示例

#### 示例1：飞碟社风格（战斗·火焰剑击）

```
Ufotable style, Demon Slayer visual reference, hyper-realistic CGI VFX seamlessly blended with 2D cel animation, peak sakuga quality,
male swordsman in mid-air, executing Hinokami Kagura horizontal slash, body rotating with explosive momentum, black haori and checkered obi fluttering wildly, intense determined expression with glowing amber eyes,
clean sharp line art with variable brush thickness, digital cel-shading with rich gradient shadows, highly saturated warm-cool contrast palette (blazing orange-red versus deep midnight blue),
massive fire dragon VFX spiraling around blade as primary light source, thousands of glowing ember particles scattering outward, radial speed lines radiating from impact point, impact frame with white-hot flash, volumetric smoke and heat distortion,
moonlit mountain clearing, three-layer parallax depth: foreground scattered rock debris mid-explosion, midground scorched earth with cracks, background full moon partially obscured by smoke columns, volumetric mist at ground level,
best quality, ultra-detailed, masterpiece, official art, sharp focus, vibrant colors, highly detailed eyes with fire reflections, detailed individual hair strands, dynamic lighting from fire VFX, Ufotable official artwork quality, anime key visual
```

#### 示例2：京阿尼风格（日常·放学黄昏）

```
Kyoto Animation style, Violet Evergarden visual reference, photorealistic lighting with soft 2D character rendering, delicate emotional storytelling through visuals,
high school girl standing at classroom window, gentle side profile, one hand resting on glass, soft wind blowing hair across face, subtle melancholic smile, school uniform with slightly loosened ribbon, golden hour light casting long shadows,
refined thin line art with subtle color variation, soft gradient cel-shading with watercolor-like transparency in shadows, pastel warm palette dominated by amber gold and soft lavender,
golden hour sunlight streaming through tall windows as primary light source, Tyndall effect with visible dust particles dancing in light beams, soft lens flare on window edge, delicate rim lighting on hair creating translucent glow, no harsh shadows — everything bathed in gentle warmth,
detailed high school classroom interior, desks with subtle wood grain texture, potted plants on windowsill with individually rendered leaves, distant cityscape visible through window with evening haze, hand-painted cumulus clouds in gradient orange-pink sky,
best quality, ultra-detailed, masterpiece, official art, sharp focus, soft vibrant colors, hyper-detailed sparkling eyes with light reflections, individual hair strands catching golden light, ambient dynamic lighting, Kyoto Animation official artwork quality, anime key visual
```

#### 示例3：韩漫风格（暗黑·觉醒时刻）

```
Korean Webtoon style, Solo Leveling art reference, sharp high-contrast digital illustration, intimidating dark fantasy aesthetic,
male protagonist standing in center, awakening moment, dark shadow aura erupting violently from body, eyes glowing piercing electric blue, sharp jawline and cold expression, torn black coat billowing upward from energy shockwave, one hand extended forward with crackling dark energy,
ultra-sharp clean line art with heavy bold outlines on character, high-contrast digital coloring with deep blacks and selective vivid highlights, limited color palette: dominant black and dark purple with electric blue accent highlights,
dark shadow tendrils as ambient light-absorbing effect, electric blue energy crackling around hands and eyes as point light sources, ground-level shockwave ring expanding outward with dust debris, vertical energy column piercing upward, heavy vignette darkening edges,
abstract dark void background with subtle purple fog, shattered stone floor with glowing blue cracks radiating from character's feet, faint silhouettes of defeated enemies in background darkness, atmospheric purple-black gradient,
best quality, ultra-detailed, masterpiece, official art, sharp focus, high contrast vibrant accent colors against dark base, highly detailed glowing eyes, detailed hair strands with energy wisps, dramatic dynamic lighting, Solo Leveling official artwork quality, webtoon key visual
```

#### 示例4：扳机社风格（赛博张力·机甲暴走）

```
Studio Trigger style, Promare / Kill la Kill visual reference, hyper-dynamic maximalist animation, explosive visual energy with punk attitude,
female mecha pilot bursting out of cockpit in mid-transformation sequence, body arched backward with arms spread wide, mechanical armor plates separating and reassembling around her in radial explosion pattern, wild spiky hair defying gravity, manic grin with sharp canine teeth, eyes blazing with spiral energy symbol,
ultra-bold black outlines with extreme variable thickness (hair-thin to massive), flat cel-shading with hard shadow edges and NO gradients, hyper-saturated neon color palette: electric lime green and hot magenta as primary contrast pair against jet black,
massive radial energy explosion as primary light source emanating from character center, thick bold speed lines filling entire frame, impact frame with screen-shake effect and chromatic aberration, geometric VFX shapes (triangles and spirals) bursting outward, lens flare shaped as cross-stars,
abstract geometric background shattering into angular fragments, extreme fisheye perspective warping grid lines, neon grid floor dissolving into pure energy, no realistic environment — pure visual abstraction of velocity and power,
best quality, ultra-detailed, masterpiece, official art, sharp focus, hyper-saturated neon colors, bold graphic impact, highly detailed expressive eyes with spiral motif, wild dynamic hair, extreme dynamic lighting with hard neon edges, Studio Trigger official artwork quality, anime key visual
```

#### 示例5：90年代复古风格（蒸汽波·深夜便利店）

```
90s retro anime style, Cowboy Bebop / Serial Experiments Lain visual reference, nostalgic late-night cel animation aesthetic with VHS warmth,
young woman leaning against convenience store window at 2 AM, casual slouch with one hand in jacket pocket, other hand holding canned coffee, tired half-lidded eyes gazing at rain outside, oversized bomber jacket over tank top, headphones around neck, cigarette smoke curling upward,
traditional hand-drawn cel animation line art with slight wobble and inconsistency (charming imperfection), limited cel-shading with 2-3 shadow layers only, muted pastel color palette with warm amber and dusty rose against cool grey-blue,
warm fluorescent convenience store light spilling through window as primary source, neon sign glow (pink and blue) reflecting on wet pavement outside, CRT monitor scanline overlay across entire image, subtle VHS tracking distortion at frame edges, soft diffused light with no sharp shadows,
late-night urban convenience store interior: magazine racks, instant noodle shelves, buzzing fluorescent ceiling lights, rain-streaked glass window showing empty street with distant neon signs, wet asphalt reflections, lonely vending machine glowing outside,
best quality, ultra-detailed, masterpiece, official art, retro anime aesthetic, muted nostalgic colors, VHS filter grain, CRT scanline texture, hand-drawn cel animation quality, 90s anime official artwork quality, anime key visual
```

#### 示例6：MAPPA风格（混沌暴力美学·巨人突袭）

```
MAPPA studio style, Attack on Titan Final Season / Jujutsu Kaisen visual reference, cinematic chaos with gritty realism and visceral impact,
male soldier in mid-air ODM gear maneuver, body twisted at extreme angle with dual blades drawn, rain and blood droplets frozen in motion around him, torn Survey Corps cloak whipping violently, face contorted in primal battle scream with veins visible on neck, extreme foreshortening with fist toward camera,
sketchy rough line art with visible construction lines left intentionally, aggressive crosshatching in shadow areas, digital painting with textured brush strokes mimicking oil paint, desaturated military palette: olive drab, dried blood red, storm grey, muted flesh tones,
overcast storm sky providing cold diffused primary lighting, lightning flash as dramatic secondary light source creating harsh split-second shadows, rain particles catching light as thousands of white streaks, motion blur on character limbs suggesting extreme velocity, dust and debris cloud with volumetric density,
collapsing medieval city in background, massive titan silhouette emerging through smoke and dust, crumbling stone buildings with dynamic debris trajectories, three-layer depth: foreground rain and blood droplets out of focus, midground character in sharp focus, background destruction in atmospheric haze,
best quality, ultra-detailed, masterpiece, official art, sharp focus, gritty desaturated palette, sketchy dynamic line art, motion blur, highly detailed strained expression, individual rain-soaked hair strands, visceral dramatic lighting, MAPPA official artwork quality, anime key visual
```

#### 示例7：吉卜力风格（治愈系手绘·山间面包店清晨）

```
Studio Ghibli style, Kiki's Delivery Service / Howl's Moving Castle visual reference, hand-painted warmth with whimsical wonder and gentle humanity,
young baker girl carrying fresh bread basket on her head, cheerful walking stride on cobblestone path, simple linen dress with flour-dusted apron, bare feet feeling morning dew, genuine warm smile with rosy cheeks, soft breeze lifting hair and apron hem gently, small cat companion trotting alongside,
soft hand-painted line art with warm brown ink lines (never pure black), traditional watercolor-style coloring with visible color bleeding at edges, warm earth tone palette: terracotta, warm cream, sage green, cornflower blue, sunflower yellow,
early morning golden sunlight filtering through oak trees as primary light source, Tyndall effect with golden light beams cutting through morning mist, soft ambient bounce light from warm stone buildings, gentle long shadows stretching across cobblestones, everything bathed in warm morning glow,
idyllic European countryside village on hillside: hand-painted stone cottages with flower boxes, winding cobblestone path through village center, lush green hillside with wildflowers, distant blue mountains with morning haze, puffy cumulus clouds in watercolor gradient sky, birds in V-formation,
best quality, ultra-detailed, masterpiece, official art, soft warm focus, hand-painted watercolor texture, warm earth tones, lush greenery detail, whimsical atmosphere, gentle ambient lighting, Studio Ghibli official artwork quality, anime key visual
```

#### 示例8：新海诚风格（极致环境壁纸·彗星黄昏）

```
Makoto Shinkai style, Your Name / Weathering with You visual reference, breathtaking photorealistic background art with emotionally resonant atmospheric beauty,
teenage girl standing on Tokyo rooftop observation deck, silhouetted against vast twilight sky, one hand reaching upward toward falling comet fragments, school uniform skirt and hair billowing in high-altitude wind, tears glistening on cheeks catching golden light, emotional expression between awe and longing,
ultra-clean precise line art for character with soft edges, hyper-detailed photorealistic background painting with individual cloud formations, signature Shinkai saturated color palette: deep azure and ultramarine sky transitioning through magenta-pink to golden amber at horizon,
spectacular twilight sky as overwhelming primary light source, comet tail fragments creating hundreds of golden light streaks across sky, gorgeous multi-layered lens flare (hexagonal bokeh), Tyndall effect through gaps in cumulus clouds, city lights below beginning to twinkle creating secondary warm glow carpet, god rays piercing cloud layer,
hyper-detailed Tokyo cityscape stretching to horizon: individual building windows reflecting sunset, elevated train crossing bridge with lit windows, Tokyo Tower silhouetted against sky, layered atmospheric perspective with five depth planes: foreground rooftop railing detail, near-ground building rooftops, mid-distance urban sprawl, far-distance city edge, sky with comet trail as backdrop,
best quality, ultra-detailed, masterpiece, official art, sharp focus, breathtaking vibrant sky colors, hyper-detailed cityscape, gorgeous lens flare and light effects, individual cloud detail, emotional atmospheric lighting, Makoto Shinkai official artwork quality, anime wallpaper key visual
```

---

## 维度六：游戏级CG美学

### 游戏级CG提示词公式（T0级）

```
[游戏引擎/渲染管线指定] + [CG子风格流派] + [角色/场景核心描述] + [材质与着色器系统] + [后处理特效栈] + [T0级游戏CG画质后缀]
```

#### 6项强制要求

| # | 要求 | 关键词示例 |
|---|------|-----------|
| 1 | 游戏引擎指定 | `Unreal Engine 5 Nanite and Lumen` / `Unity HDRP` / `CryEngine` |
| 2 | CG子风格流派 | `AAA JRPG cinematic` / `Soulsborne dark fantasy` / `open world RPG` / `fighting game key art` |
| 3 | 材质着色器系统 | `PBR metallic-roughness workflow, 4K texture maps, subsurface scattering, displacement mapping` |
| 4 | 后处理特效栈 | `bloom, chromatic aberration, depth of field, screen-space reflections, ambient occlusion, motion blur` |
| 5 | 全局光照系统 | `Lumen global illumination, ray-traced reflections, HDRI environment lighting, virtual shadow maps` |
| 6 | T0级游戏CG后缀 | `AAA game cinematic quality, in-engine cutscene render, 8K UHD, next-gen console graphics` |

### 游戏级CG提示词模板

**融合引擎技术 + 视觉风格的T0级完整模板**

```
[引擎渲染]: [game engine] with [rendering features], [real-time / pre-rendered], [technical pipeline],
[CG风格]: [game genre aesthetic], [specific game/studio visual reference], [art direction style],
[核心描述]: [character/scene identity], [pose/composition], [key visual elements], [narrative moment],
[材质系统]: [PBR workflow], [key material types with shader details], [texture resolution], [surface detail level],
[光照系统]: [global illumination method], [primary light source], [secondary fills], [volumetric effects], [shadow system],
[后处理]: [bloom intensity], [DOF settings], [color grading LUT], [screen effects], [anti-aliasing method],
[画质后缀]: AAA game cinematic quality, next-gen real-time rendering, 8K UHD, [engine name] in-engine quality
```

#### 增强版6项要素说明

| # | 要素 | 说明 | 示例 |
|---|------|------|------|
| 1 | **引擎渲染** | 指定游戏引擎、渲染管线、实时/预渲染模式 | `Unreal Engine 5.4 with Nanite virtualized geometry and Lumen global illumination, real-time ray tracing enabled` |
| 2 | **CG风格** | 游戏类型美学、参考作品、美术方向风格 | `Soulsborne dark fantasy aesthetic, Elden Ring visual reference, FromSoftware art direction with European Gothic influence` |
| 3 | **核心描述** | 角色/场景主体、姿态/构图、关键视觉元素、叙事瞬间 | `armored knight kneeling before colossal ancient dragon, fog-shrouded ruins, moment of confrontation before boss battle` |
| 4 | **材质系统** | PBR工作流、关键材质着色器细节、贴图精度、表面细节 | `PBR metallic-roughness, ornate silver armor with micro-scratch normal map, cloth physics on tattered cape, SSS on exposed skin` |
| 5 | **光照系统** | 全局光照方案、主光源、补光、体积效果、阴影系统 | `Lumen GI with infinite bounces, dying sunset as warm key light, cool ambient fill from overcast sky, volumetric fog, ray-traced contact shadows` |
| 6 | **后处理** | 泛光、景深、色彩分级LUT、屏幕特效、抗锯齿 | `subtle bloom on light sources, cinematic DOF f/2.8 with hexagonal bokeh, filmic tone mapping, TAA with sharpening pass` |

#### 使用建议

- **所有游戏CG风格**：统一使用6要素完整模板，必须指定具体引擎和渲染特性
- **暗黑魂系/ARPG**：强化材质系统的战损细节与光照系统的戏剧性暗调
- **JRPG/动作RPG**：强化CG风格的华丽感与后处理的bloom和色彩饱和度
- **开放世界**：强化光照系统的自然环境GI与大气散射
- **格斗/动作游戏**：强化后处理的运动模糊与核心描述的动态张力
- **恐怖生存**：强化光照系统的极端明暗对比与后处理的噪点/胶片颗粒

### 6大游戏CG子风格

| # | 子风格 | 风格关键词 |
|---|--------|-----------|
| 1 | UE5 写实CG电影 | `Unreal Engine 5 Nanite Lumen, cinematic in-engine cutscene, photogrammetry assets, ray-traced GI, film-quality rendering` |
| 2 | 魂系暗黑 | `Soulsborne dark fantasy, FromSoftware aesthetic, oppressive atmosphere, intricate armor design, Gothic architecture, fog and decay` |
| 3 | JRPG 华丽CG | `AAA JRPG cinematic, Final Fantasy XVI / Xenoblade visual reference, stylized realism, ornate costume design, magical particle VFX` |
| 4 | 开放世界史诗 | `Open world RPG, The Witcher 3 / Horizon visual reference, vast landscape, dynamic weather, natural lighting, exploration grandeur` |
| 5 | 格斗游戏Key Art | `Fighting game key art, Street Fighter 6 / Tekken visual reference, dynamic muscle anatomy, impact freeze frame, stylized shading` |
| 6 | 恐怖生存 | `Survival horror, Resident Evil / Silent Hill visual reference, found-footage grain, flashlight-only lighting, photorealistic decay` |

### 游戏级CG实战示例

#### 示例1：UE5写实CG电影（太空歌剧·飞船桥舱）

```
Unreal Engine 5.4 with Nanite virtualized geometry and Lumen global illumination, real-time cinematic in-engine cutscene, photogrammetry-scanned asset pipeline,
AAA sci-fi cinematic aesthetic, Star Citizen / Mass Effect Legendary visual reference, hard sci-fi industrial design with lived-in aesthetic,
spaceship bridge command center, female captain standing at holographic tactical display, one hand manipulating 3D star map, other hand gripping console edge, determined expression illuminated by hologram blue glow, flight suit with magnetic boots and mission patches,
PBR metallic-roughness workflow: brushed aluminum console panels with fingerprint smudges (roughness variation 0.3-0.6), tempered glass displays with anti-reflective coating, carbon fiber chair frame with leather seat showing wear, rubber grip surfaces with compression marks, holographic display as emissive shader with volumetric projection,
Lumen GI with multiple bounce lighting, holographic display as primary cool blue key light, secondary warm amber from corridor lighting behind, HDRI deep space environment visible through bridge windows, virtual shadow maps with contact shadow refinement, subtle caustics from glass panels,
subtle anamorphic bloom on holographic elements, cinematic DOF at f/2.0 with shallow focus on captain, teal and orange cinematic LUT, screen-space reflections on polished surfaces, film grain at 0.5% intensity, TAA with DLSS upscaling,
AAA game cinematic quality, next-gen real-time rendering, 8K UHD, Unreal Engine 5 in-engine showcase quality
```

#### 示例2：魂系暗黑（Boss战·腐朽王座）

```
Unreal Engine 5 with Lumen and hardware ray tracing, pre-rendered cinematic quality targeting 60fps real-time equivalent,
Soulsborne dark fantasy aesthetic, Elden Ring / Dark Souls III visual reference, FromSoftware art direction with Baroque and Gothic European architectural influence,
colossal corrupted king fused with his throne, amalgamation of rotting flesh and tarnished gold, crown melted into skull, one arm elongated into massive blade of crystallized dark energy, player character (small scale) approaching from foreground with greatsword and tattered shield, oppressive vertical composition emphasizing boss scale,
PBR metallic-roughness: corroded gold throne with verdigris and black tarnish (metallic 0.8, roughness 0.7), exposed bone with SSS and moisture shader, tattered royal robes with cloth simulation and moth-eaten holes, crystallized dark energy as custom emissive shader with internal refraction, player armor with deep battle scars revealing base metal,
Lumen GI with minimal bounce (dark oppressive mood), single shaft of dying amber light from cracked ceiling as dramatic key, boss's dark energy crystal providing sickly purple-green secondary illumination, deep volumetric fog at floor level, ray-traced shadows creating absolute blacks in recesses,
heavy bloom on dark energy crystals only, wide DOF keeping both player and boss in focus (f/8), heavily desaturated dark LUT with selective color on gold and crystal energy, SSAO cranked to maximum for deep crevice shadows, subtle chromatic aberration at frame edges,
AAA game cinematic quality, Soulsborne boss encounter key art, next-gen rendering, 8K UHD, FromSoftware official cinematic quality
```

#### 示例3：JRPG华丽CG（召唤术·水晶殿堂）

```
Unreal Engine 5 with Nanite and Lumen, Square Enix Visual Works pre-rendered cinematic quality,
AAA JRPG cinematic aesthetic, Final Fantasy XVI / Final Fantasy VII Rebirth visual reference, stylized photorealism with fantasy spectacle and emotional gravitas,
young summoner channeling ultimate spell in grand crystal cathedral, arms raised skyward with magical sigils orbiting wrists, hair and robes levitating from magical energy upwelling, eyes glowing pure white, massive translucent crystal summon beast materializing overhead from light particles, dramatic upward camera angle,
PBR with stylized enhancement: ornate white-and-gold ceremonial robes with silk SSS and embroidered magical circuits (emissive thread detail), crystal architecture with custom refraction and dispersion shader, skin with idealized SSS and porcelain smoothness, magical sigils as complex animated emissive decals, summon beast as translucent volumetric crystal with internal light scattering,
Lumen GI with maximum bounce count for crystal light diffusion, magical upwelling as intense white-blue primary light from below, warm amber stained-glass window light as fill, thousands of light-particle motes as individual emissive point lights, crystal architecture creating prismatic rainbow caustics throughout space,
intense bloom on all magical elements (intensity 2.0+), dramatic DOF with summoner sharp and background crystal architecture in soft bokeh, vibrant saturated LUT boosting blues and golds, heavy screen-space reflections on crystal floor, lens flare on magical convergence point, particle depth of field,
AAA JRPG cinematic quality, Square Enix pre-rendered CG quality, 8K UHD, next-gen fantasy spectacle rendering
```

#### 示例4：开放世界史诗（探索·黄昏草原）

```
Unreal Engine 5 with Nanite landscape, Lumen sky GI, and virtual shadow maps, real-time open world rendering,
Open world RPG aesthetic, The Witcher 3 Blood and Wine / Horizon Forbidden West visual reference, vast natural landscape with exploration grandeur and sense of discovery,
lone wanderer on horseback cresting hilltop overlooking endless golden grass plains, wind creating wave patterns in tall grass, ancient stone ruins with overgrown vines in middle distance, massive snow-capped mountain range on horizon, dramatic sky with towering cumulonimbus clouds catching sunset,
PBR landscape pipeline: procedural grass with individual blade geometry (Nanite), weathered stone ruins with photogrammetry-scanned textures, horse with multi-layer fur shader (base coat + guard hairs + SSS), leather saddle and gear with wear maps, character's travel-worn cloak with cloth physics and dirt accumulation,
Lumen sky-based GI with golden hour sunset as primary directional light, warm orange key light from low sun angle, cool blue-purple ambient fill from opposite sky, volumetric cloud shadows creating dramatic light-and-shadow patches moving across plains, atmospheric scattering with aerial perspective haze on mountains,
subtle natural bloom on sun and cloud edges, deep DOF at f/11 keeping everything sharp (landscape photography style), warm golden hour LUT with slight teal in shadows, atmospheric fog with exponential height falloff, SSAO on grass roots and stone crevices, minimal post-processing for natural clarity,
AAA open world game quality, real-time exploration vista, next-gen landscape rendering, 8K UHD, photo-mode screenshot quality
```

#### 示例5：格斗游戏Key Art（对决·冲击定格）

```
Unreal Engine 5 with real-time muscle deformation and cloth simulation, stylized PBR rendering pipeline,
Fighting game key art aesthetic, Street Fighter 6 / Tekken 8 visual reference, dynamic anatomical showcase with impact spectacle and competitive intensity,
two fighters in mid-clash freeze frame: attacker executing flying roundhouse kick connecting with defender's cross-arm block, impact shockwave distorting air between them, sweat and water droplets frozen in explosion pattern from impact point, attacker's face showing fierce kiai scream, defender gritting teeth absorbing force,
PBR with stylized muscle shader: hyper-detailed anatomical muscle definition with specular highlights on sweat-covered skin (roughness 0.2 for wet skin), fabric fight gloves with compression wrinkles at knuckle contact, torn gi fabric with dynamic rip physics, individual sweat droplets as refractive particle meshes,
dramatic three-point fighting game lighting: intense warm key light from above-left, cool blue rim light from right creating edge definition on muscles, ground-level orange fill light from arena floor, impact point generating white shockwave light burst, theatrical lighting with no attempt at naturalism,
heavy stylized bloom on impact shockwave, extreme motion blur on attacking leg (radial from hip pivot), frozen DOF with both fighters razor-sharp against blurred arena background, high-contrast saturated LUT boosting skin warmth and impact blue, speed lines composited as post-process, chromatic aberration burst at impact,
AAA fighting game key art quality, character select screen render, next-gen real-time graphics showcase, 8K UHD, competitive gaming visual spectacle
```

#### 示例6：恐怖生存（探索·废弃实验室）

```
Unreal Engine 5 with Lumen in complete darkness mode and hardware ray tracing for flashlight-only illumination,
Survival horror aesthetic, Resident Evil Village / Silent Hill 2 Remake visual reference, photorealistic environmental decay with psychological dread,
first-person perspective: player hand holding dim flashlight illuminating narrow cone of abandoned underground laboratory, beam revealing overturned chemical equipment, shattered specimen jars with unknown contents spilled on floor, bloody drag marks leading around corner into darkness, distorted shadow of unseen entity just at flashlight beam edge,
PBR photorealistic materials: cracked tile floor with biological contamination stains and moisture pooling, rusted stainless steel surgical equipment with dried biological residue, shattered glass with refraction and sharp edge detail, peeling institutional paint revealing damp concrete with mold growth, fluorescent ceiling light fixture hanging by wires (off/dead),
near-zero ambient lighting — Lumen GI disabled to simulate total darkness, flashlight as single harsh spotlight with realistic falloff (inverse-square law), faint bioluminescent glow from spilled specimen fluid as subtle secondary, ray-traced flashlight shadows creating hyper-sharp silhouettes of equipment on walls, absolute pitch black beyond flashlight range,
no bloom (realistic darkness), narrow DOF simulating human eye focus anxiety, heavily desaturated cold LUT with sickly green shift in flashlight cone, heavy film grain (3-5%) for found-footage unease, SSAO at maximum creating oppressive depth in every crack and corner, vignette darkening at frame edges, subtle VHS noise artifacts,
AAA survival horror quality, first-person exploration tension, next-gen photorealistic horror, 8K UHD, Capcom RE Engine cinematic quality
```

---

## 维度七：超写实摄影级

### 超写实摄影提示词公式（T0级）

```
[相机机身与镜头系统] + [摄影类型与流派] + [核心主体描述] + [自然光/人工光方案] + [胶片/数码后期风格] + [T0级超写实画质后缀]
```

#### 6项强制要求

| # | 要求 | 关键词示例 |
|---|------|-----------|
| 1 | 相机镜头系统 | `Shot on Canon EOS R5, RF 85mm f/1.2L USM` / `Hasselblad X2D 100C, XCD 90mm f/2.5` / `Sony A7R V, GM 135mm f/1.8` |
| 2 | 摄影类型指定 | `editorial fashion photography` / `National Geographic wildlife` / `architectural photography` / `street photography` |
| 3 | 光线方案 | `natural golden hour window light` / `Profoto B10 studio strobe with 5-foot octabox` / `practical lighting only` |
| 4 | 皮肤/材质微观 | `visible skin pores, peach fuzz, capillary detail` / `micro-fiber fabric texture` / `water droplet surface tension` |
| 5 | 后期风格 | `Capture One RAW processing, skin retouching preserving texture` / `Lightroom film emulation preset` |
| 6 | T0级超写实后缀 | `RAW photo, photorealistic, 8K UHD, DSLR quality, ultra-high-resolution, award-winning photography` |

### 超写实摄影提示词模板

**融合摄影技术 + 真实质感的T0级完整模板**

```
[相机系统]: Shot on [camera body], [lens model with focal length and aperture], [sensor format],
[摄影类型]: [photography genre], [specific photographer/magazine style reference], [editorial context],
[核心主体]: [subject description], [pose/action], [wardrobe/surface detail], [expression/state],
[光线方案]: [key light type and modifier], [fill light], [rim/hair light], [ambient/practical lights], [light quality and direction],
[材质微观]: [skin/surface micro-detail], [fabric/material texture at macro level], [environmental micro-texture],
[后期风格]: [RAW processing software], [color science], [retouching approach], [film emulation if applicable], [output sharpening],
[画质后缀]: RAW photo, photorealistic, 8K UHD, DSLR quality, [photography genre] award-winning quality
```

#### 增强版6项要素说明

| # | 要素 | 说明 | 示例 |
|---|------|------|------|
| 1 | **相机系统** | 指定机身型号、镜头型号（含焦段光圈）、传感器画幅 | `Shot on Hasselblad X2D 100C medium format, XCD 90mm f/2.5 V lens, 100MP sensor, 16-bit RAW` |
| 2 | **摄影类型** | 摄影流派、参考摄影师/杂志风格、编辑语境 | `editorial fashion photography, Vogue Italia aesthetic, Peter Lindbergh emotional naturalism` |
| 3 | **核心主体** | 主体描述、姿态/动作、服装/表面细节、表情/状态 | `female model mid-stride on wet Parisian cobblestone, oversized vintage Chanel tweed coat, wind-caught hair, candid unguarded expression` |
| 4 | **光线方案** | 主光类型与柔光器、补光、轮廓光、环境光、光线品质与方向 | `overcast sky as massive natural softbox key light, silver reflector fill from below, no rim light (flat editorial look), soft even directionless quality` |
| 5 | **材质微观** | 皮肤/表面微观细节、面料/材质纹理微距、环境微观纹理 | `visible skin pores on cheekbones, peach fuzz catching backlight, tweed fabric individual fiber weave pattern, wet cobblestone with reflected sky micro-detail` |
| 6 | **后期风格** | RAW处理软件、色彩科学、修图手法、胶片模拟、输出锐化 | `Capture One with medium format color science, minimal skin retouching preserving natural texture, muted editorial palette, output sharpened for print at 300dpi` |

#### 使用建议

- **所有超写实画面**：统一使用6要素完整模板，必须指定真实相机型号和镜头
- **人像/时尚**：强化材质微观的皮肤细节与光线方案的人工布光
- **风光/自然**：强化相机系统的广角镜头与光线方案的自然光变化
- **商业产品**：强化材质微观的产品表面细节与光线方案的studio布光
- **街拍/纪实**：强化摄影类型的纪实风格与后期风格的胶片模拟
- **建筑/室内**：强化相机系统的移轴镜头与光线方案的混合光源控制

### 6大超写实摄影子流派

| # | 子流派 | 风格关键词 |
|---|--------|-----------|
| 1 | 时尚编辑 | `editorial fashion, Vogue aesthetic, studio/location hybrid, dramatic lighting, haute couture detail, model casting quality` |
| 2 | 电影剧照 | `cinematic still photography, film set lighting, anamorphic lens character, production design detail, actor portrait quality` |
| 3 | 风光大片 | `landscape photography, National Geographic quality, golden hour, dramatic weather, vast scale, tack-sharp front-to-back` |
| 4 | 商业产品 | `commercial product photography, phase-one capture, focus stacking, controlled studio lighting, catalog quality` |
| 5 | 街头纪实 | `street photography, Magnum Photos aesthetic, decisive moment, available light, documentary authenticity, Leica rendering` |
| 6 | 肖像特写 | `portrait photography, large format rendering, extreme shallow DOF, catch light detail, emotional connection, Annie Leibovitz quality` |

### 超写实摄影实战示例

#### 示例1：时尚编辑（Vogue封面·雨中巴黎）

```
Shot on Hasselblad X2D 100C medium format, XCD 80mm f/1.9 lens wide open, 100-megapixel 16-bit RAW capture, handheld with IBIS,
editorial fashion photography, Vogue Paris cover story aesthetic, Peter Lindbergh meets Paolo Roversi — emotional naturalism with ethereal softness,
female model (mid-20s) standing in center of empty Place Vendôme at blue hour, wearing oversized vintage Dior New Look coat in dove grey, silk scarf caught mid-flutter by wind, one hand touching rain-wet cheek, expression of quiet defiance and vulnerability simultaneously, barefoot on wet cobblestone (deliberate creative choice),
overcast Parisian twilight sky as enormous natural softbox providing directionless cool key light, warm amber glow from Ritz hotel windows as secondary practical fill from frame left, reflections from wet cobblestone acting as natural reflector bouncing sky light upward onto face, no artificial lights — purely available environmental light,
visible skin pores and natural skin texture on face and hands (no airbrushing), individual water droplets on cheekbones catching ambient light, peach fuzz on jawline illuminated by warm practical light, Dior coat wool fiber texture at individual thread level, wet cobblestone with each stone's unique surface texture and micro-puddle reflections,
Capture One Pro with Hasselblad medium format color science, minimal skin retouching preserving all natural texture and imperfections, muted desaturated editorial palette with lifted blacks, subtle split-toning (cool shadows / neutral highlights), output sharpened for Vogue print at 300dpi,
RAW photo, photorealistic, 8K UHD, medium format DSLR quality, Vogue cover award-winning fashion photography
```

#### 示例2：电影剧照（黑色电影·侦探办公室）

```
Shot on ARRI ALEXA 65 large format cinema camera, Panavision Ultra Vista 40mm anamorphic lens at T/2.0, ARRIRAW open gate capture,
cinematic still photography, film noir production still aesthetic, Roger Deakins lighting philosophy meets Gordon Willis shadow work,
male detective (50s) sitting behind cluttered mahogany desk, face half-illuminated through venetian blind shadows, cigarette smoke curling from ashtray, one hand on rotary phone receiver, other hand resting on revolver on desk, weary eyes with decades of disillusionment, loosened tie and rolled sleeves revealing forearm,
single hard key light (2K tungsten Fresnel) positioned outside window creating sharp venetian blind shadow pattern across face and room, no fill light (intentional deep shadow on opposite face), practical desk lamp providing warm pool of light on desk surface only, cigarette smoke catching venetian blind light shafts creating volumetric layers,
five o'clock shadow stubble with individual hair follicle detail, crow's feet wrinkles with visible skin depth, nicotine-stained fingers with visible fingerprint ridges, mahogany desk surface with decades of ring stains and pen scratches, glass ashtray with cigarette ash micro-particle texture,
ARRI LogC to Rec.709 with custom noir LUT, heavy contrast with crushed blacks (zone 0-II absent), warm tungsten white balance (3200K), no digital noise reduction preserving sensor texture, anamorphic horizontal lens flare on practical lamp, 2.39:1 widescreen crop,
RAW photo, photorealistic, 8K UHD, ARRI cinema camera quality, film noir production still award-winning cinematography
```

#### 示例3：风光大片（National Geographic·冰岛火山）

```
Shot on Phase One IQ4 150MP medium format digital back, Schneider Kreuznach 28mm LS f/4.5 lens at f/11 for maximum sharpness, tripod-mounted 30-second exposure,
epic landscape photography, National Geographic cover feature quality, Ansel Adams zone system precision meets modern color landscape grandeur,
erupting Icelandic volcano at night, molten lava rivers snaking down black basalt slopes, massive eruption column of ash and fire illuminating low cloud layer from within, Northern Lights (aurora borealis) dancing in green and purple curtains above eruption, foreground of black volcanic sand with glowing lava cracks,
volcanic eruption as primary warm light source (intense orange-red illuminating clouds and terrain), aurora borealis as secondary cool green light source illuminating upper atmosphere, starlight providing minimal ambient fill, lava rivers as linear warm light sources creating orange glow corridors, no artificial lighting,
individual volcanic rock surface texture with glassy obsidian fragments catching lava glow, molten lava surface with visible convection cell patterns and cooling crust cracking, ash particles in air visible in lava light, black sand with individual grain detail, aurora curtain with visible ray structure,
Phase One Capture One with IQ4 color science, HDR merge of 5 bracketed exposures for extreme dynamic range (lava to stars), precise color temperature management (mixed lighting), no composite — single location single moment, output sharpened for large format print (40x60 inches at 300dpi),
RAW photo, photorealistic, 8K UHD, 150-megapixel medium format quality, National Geographic cover award-winning landscape photography
```

#### 示例4：商业产品（奢侈品·腕表特写）

```
Shot on Canon EOS R5, Canon RF 100mm f/2.8L Macro IS USM lens at f/8, focus stacking of 47 frames for infinite depth of field, tripod-mounted tethered to Capture One,
commercial luxury product photography, Hodinkee / Watches of Switzerland catalog quality, precision still-life with obsessive material detail,
Patek Philippe Nautilus 5711 watch face-up on polished black obsidian surface, bracelet partially draped off surface edge creating S-curve, crown at 3 o'clock catching key light, dial indices and hands casting micro-shadows on sunburst blue dial, exhibition caseback partially visible in obsidian reflection,
main key light: Profoto D2 1000 with strip softbox positioned at 10 o'clock creating gradient across dial and brushed steel bracelet, secondary fill: white V-flat reflector at 4 o'clock opening shadows without killing contrast, accent: fiber-optic light wand highlighting crown and logo, background: black acrylic surface with graduated reflection,
brushed stainless steel bracelet with directional satin finish visible at microscopic level (individual brush stroke lines), polished bezel with mirror reflection of studio environment, blue sunburst dial with radial pattern catching light at different angles, applied gold indices with chamfered edges catching accent light, sapphire crystal with anti-reflective coating showing subtle blue-purple tint,
Capture One tethered capture with live color verification, focus stack merged in Helicon Focus, micro-level sensor dust removal, obsessive color accuracy for brand Pantone matching, no compositing — single lighting setup with focus stacking only, output ICC profiled for luxury print on 100lb coated stock,
RAW photo, photorealistic, 8K UHD, medium format product photography quality, luxury brand catalog award-winning commercial photography
```

#### 示例5：街头纪实（Magnum级·东京十字路口）

```
Shot on Leica M11 rangefinder, Leica Summilux-M 35mm f/1.4 ASPH wide open, handheld with zone focusing at 3 meters hyperfocal, ISO 3200 for available light,
street photography, Magnum Photos agency aesthetic, Henri Cartier-Bresson decisive moment philosophy meets Daido Moriyama Tokyo grain,
Shibuya scramble crossing at night in rain, hundreds of pedestrians mid-stride creating motion choreography, central figure: elderly salaryman standing still in crosswalk center while crowd flows around him — umbrella lowered at side despite rain, staring upward at giant video billboard, frozen island of stillness in human river,
overhead Shibuya billboard screens as primary mixed-color light source raking down at crowd, wet asphalt reflecting all light sources creating mirror-world doubling of every neon sign, pedestrian smartphone screens as hundreds of individual blue-white point lights, rain catching neon as millions of colored streaks in slow-shutter capture,
rain droplets on salaryman's glasses with refracted billboard imagery, wet polyester suit fabric with visible weave pattern clinging to shoulders, umbrella fabric with individual raindrop impact craters, pedestrian shoes splashing through 2mm puddle layer, asphalt road surface with painted crosswalk lines worn by millions of footsteps,
Leica DNG RAW processed in Lightroom with custom high-contrast B&W preset converted back to selective desaturated color (only neon colors remain vivid), heavy grain from ISO 3200 embraced as aesthetic texture, no noise reduction, slight motion blur on crowd (1/30s shutter) with static central figure sharp, vignette from wide-open Summilux,
RAW photo, photorealistic, 8K UHD, Leica rangefinder quality, Magnum Photos award-winning street photography
```

#### 示例6：肖像特写（情感人像·祖母的双手）

```
Shot on Sony A7R V, Sony FE 90mm f/2.8 Macro G OSS at f/4, handheld with eye-detection AF, natural light only,
intimate portrait photography, Annie Leibovitz emotional intimacy meets Platon extreme close-up confrontation, LensCulture Portrait Awards finalist quality,
extreme close-up of elderly grandmother's hands (80+) resting on handmade lace tablecloth, hands cupped gently holding small wilted wildflower, wedding ring worn thin from 60 years of marriage embedded in finger, visible veins and liver spots telling lifetime of labor, natural hand pose without posing direction,
single north-facing window providing soft cool natural key light from camera-left, white lace tablecloth acting as natural fill reflector from below, no artificial light — honoring simplicity and authenticity, gentle shadow gradient from window-side to far-side of hands creating dimensional modeling,
individual skin wrinkles with visible depth and shadow, age spots with color variation from light tan to deep brown, protruding veins with visible blue-green subcutaneous color and skin translucency (SSS), wedding ring with decades of micro-scratches creating matte gold surface, individual lace thread pattern with slight yellowing from age, wildflower petals with cellular structure visible at macro distance,
Sony ARW RAW processed in Lightroom, gentle highlight recovery preserving window light quality, no skin smoothing or retouching — every wrinkle and mark preserved as essential story element, warm color shift +5 to honor nostalgic warmth, subtle vignette drawing focus to hands, output at full 61MP resolution,
RAW photo, photorealistic, 8K UHD, full-frame mirrorless quality, intimate portrait award-winning photography, emotional storytelling through detail
```

---

## 防崩坏指令（强制包含）

所有角色提示词必须包含以下防崩坏指令：

```
Negative prompt: lowres, bad anatomy, bad hands, text, error, 
missing fingers, extra digit, fewer digits, cropped, worst quality, 
low quality, normal quality, jpeg artifacts, signature, watermark, 
username, blurry, deformed, distorted, disfigured, mutation, 
mutated, ugly, poorly drawn face, extra limbs, missing limbs,
floating limbs, disconnected limbs, malformed hands, 
long neck, long body
```

---

## 通用风格预设

| 风格 | 关键词 | 详见维度 |
|------|--------|----------|
| 真人写实 | `Photorealistic style, cinema-grade lighting, high detail, 8K UHD, RAW photo` | 维度七 |
| 超写实摄影 | `Shot on [camera body + lens], RAW photo, visible skin pores, DSLR quality, award-winning photography` | 维度七 |
| 游戏级CG | `Unreal Engine 5, Nanite, Lumen GI, PBR materials, AAA game cinematic quality, next-gen rendering` | 维度六 |
| 魂系暗黑CG | `Soulsborne dark fantasy, FromSoftware aesthetic, oppressive atmosphere, intricate armor, Gothic decay` | 维度六 |
| 国漫 | `Chinese anime style, elegant brush strokes, traditional architecture, mythic elements, ink wash influence` | 维度五 |
| 日漫 | `Japanese anime style, vibrant colors, expressive characters, detailed eyes, dynamic poses` | 维度五 |
| 3D CG / 皮克斯 | `3D CGI Pixar style, clean geometry, soft shadows, subsurface scattering, cartoon proportions` | — |
| 迪士尼 | `Disney style, whimsical, colorful, family-friendly, rounded proportions, expressive eyes` | — |

---

## 校验清单

### 角色提示词校验（6项）
- [ ] 纯白背景隔离
- [ ] 表情集（至少4种表情）
- [ ] 服饰拆分
- [ ] 多视图（至少4个角度）
- [ ] 渲染参数（PBR/AO/8K）
- [ ] 微观面部细节

### 场景提示词校验（5项）
- [ ] 光学镜头指定（焦段）
- [ ] 构图法则
- [ ] 全局光照 / 丁达尔效应
- [ ] 色彩分级
- [ ] T0级渲染后缀

### 道具提示词校验（6项）
- [ ] 纯白背景隔离
- [ ] 道具身份与叙事（名称/时代/功能/所有者/状态）
- [ ] 多视图/爆炸拆解（正交视图+爆炸分解/截面图）
- [ ] 硬表面材质与战损（PBR参数+战损层+磨损层+老化层）
- [ ] 微距材质特写面板（4组极致微距+PBR参数）
- [ ] T0级产品渲染画质后缀

### 极致动漫校验（3项）
- [ ] 8大工作室风格指定
- [ ] T0级二次元画质后缀
- [ ] 防崩坏指令包含

### 游戏级CG校验（6项）
- [ ] 游戏引擎指定（UE5/Unity HDRP/CryEngine）
- [ ] CG子风格流派指定
- [ ] 材质着色器系统（PBR工作流+贴图精度）
- [ ] 全局光照系统（Lumen/ray tracing）
- [ ] 后处理特效栈（bloom/DOF/LUT/SSAO）
- [ ] T0级游戏CG画质后缀

### 超写实摄影校验（6项）
- [ ] 相机机身+镜头型号指定
- [ ] 摄影类型与流派指定
- [ ] 光线方案（主光/补光/轮廓光）
- [ ] 皮肤/材质微观细节
- [ ] 后期风格（RAW处理+色彩科学）
- [ ] T0级超写实画质后缀
