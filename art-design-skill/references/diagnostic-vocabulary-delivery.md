# 避坑红线·诊断指南·质感词库·输出交付标准

> 📖 本文件从 art-design-skill/SKILL.md 提取，包含设计创作/技术实现避坑红线、常见问题Q&A诊断指南、
> T0级核心质感词库（渲染/光学/角色视觉资产/材质描述/特殊效果）、输出交付标准与模板。

---

## 五、避坑红线（工业级标准）

### 设计创作避坑红线

| 红线 | 禁止行为 | 正确做法 |
|------|----------|----------|
| **同质化** | 输出通用化、模板化的角色设计 | 提炼核心记忆点，打造专属辨识度 |
| **无逻辑** | 无功能支撑的造型堆砌 | 遵循「功能→结构→造型」推导逻辑 |
| **脱离场景** | 不考虑应用场景的纯自嗨设计 | 匹配短剧/动画/游戏的具体规范 |
| **过度堆砌** | 为了炫技添加无意义细节 | 所有细节服务人设、情绪、叙事 |
| **多记忆点** | 试图在一个角色上实现多个亮点 | 单点极致，1个核心记忆点 |
| **生物生硬** | 简单拼接动物元素，无融合逻辑 | 遵循生物设计四步法，保留核心辨识度 |

### 技术实现避坑红线

| 红线 | 禁止行为 | 正确做法 |
|------|----------|----------|
| **忽视拓扑** | 设计无法合理布线的结构 | 考虑四边面流向与极点位置 |
| **材质冲突** | 同一区域多种复杂材质 | 控制材质数量，确保PBR可实现 |
| **比例失衡** | 头身比与风格定位不符 | 参考风格标准（写实7-8头/风格化2-4头） |
| **绑定灾难** | 设计无法绑定的结构 | 考虑骨骼放置与变形需求 |

---

## 六、诊断指南

### 常见问题Q&A

**Q: 生成的多视图角色不一致？**
A: 
1. 确保使用了统一的锚点图作为参考
2. 在提示词中添加`consistent character across all views`
3. 分步生成：先出正面锚点，再用锚点作为参考生成其他视图
4. 检查角色描述中的关键特征是否足够具体

**Q: 材质看起来有塑料感/AI味？**
A:
1. 添加PBR相关关键词：`physically based rendering`, `ambient occlusion`
2. 增加微观细节：`intricate texture`, `surface imperfections`
3. 指定具体材质类型而非泛化描述
4. 添加磨损细节：`tactical wear`, `subtle scratches`

**Q: 背景不够纯白，影响抠图？**
A:
1. 将`clean pure white background`放在提示词最前面
2. 添加`isolated on white`, `neutral studio backdrop`
3. 避免在背景描述中使用任何环境词汇
4. 使用`no shadows on background`确保背景干净

**Q: 面部缺乏真实感？**
A:
1. 添加微观皮肤细节：`visible pores`, `peach fuzz`, `subtle skin texture`
2. 使用次表面散射：`subsurface scattering on skin`
3. 指定眼睛细节：`realistic eye reflection`, `detailed iris`
4. 添加摄影参数：`shot on 85mm lens`, `f/1.4 aperture`

**Q: 角色缺乏辨识度，容易与其他角色混淆？**
A:
1. 重新提炼核心记忆点（形状/元素/生物特征）
2. 检查剪影识别度：3米外能否通过轮廓识别？
3. 确保有且仅有1个核心记忆点，避免多元素混乱
4. 使用反差设计：打破刻板印象，创造独特性

**Q: 设计缺乏灵魂，像模板化角色？**
A:
1. 检查是否遵循「功能→结构→造型」逻辑
2. 确保所有细节服务于角色人设与叙事
3. 添加叙事性细节：磨损痕迹、个人物品、职业特征
4. 强化情绪表达：通过形状语言、动态、表情传递情绪

**Q: 生物元素融合生硬，像元素堆砌？**
A:
1. 检查是否保留了物种的核心辨识度特征
2. 确保生物特征与角色整体形状语言统一
3. 基于生物功能设计功能性结构，而非仅装饰
4. 参考「生物设计四步法」重新梳理融合逻辑

**Q: 造型语言混乱，缺乏统一性？**
A:
1. 确定核心形状语言（圆/方/三角/S曲线/锯齿）
2. 检查直曲线分布是否符合解剖/机械结构
3. 确保动态线与角色情绪一致
4. 统一材质语言：有机vs硬表面的比例协调

**Q: 与导演/客户需求有偏差？**
A:
1. 重新核对需求文档中的所有视觉关键词
2. 建立关键词覆盖检查表，确保每个需求点都有对应描述
3. 与参考图对比，标注差异点
4. 使用情绪板（Mood Board）对齐视觉方向

---

## 七、T0级核心质感词库

### 渲染与光学参数库

**物理渲染参数**：
```
• physically based rendering (PBR)      - 基于物理的渲染
• ambient occlusion (AO)                - 环境光遮蔽
• subsurface scattering (SSS)           - 次表面散射
• ray tracing                           - 光线追踪
• global illumination                   - 全局光照
• Unreal Engine 5                       - 虚幻引擎5
• Octane Render                         - Octane渲染器
• Redshift Render                       - Redshift渲染器
```

**摄影机与焦段参数**：
```
• shot on 85mm lens                     - 85mm人像镜头
• 14mm ultra-wide angle                 - 14mm超广角
• 100mm macro lens                      - 100mm微距镜头
• f/1.2 aperture                        - f/1.2大光圈
• f/1.4 aperture                        - f/1.4大光圈
• IMAX 70mm format                      - IMAX 70mm格式
• anamorphic lens flare                 - 变形镜头光晕
• deep depth of field                   - 深景深
• shallow depth of field                - 浅景深
```

### 角色视觉资产词库

**排版与视图**：
```
• comprehensive 2D character concept art sheet    - 完整2D角色概念设定表
• beautifully organized layout                    - 精美排版
• full body turnaround (front, side, back)        - 全身转正图
• four-view character sheet                      - 四视图角色表
• orthographic projection                         - 正交投影
• isometric view                                  - 等距视角
```

**细节拆分**：
```
• facial expression sheet                         - 表情表
• separated clothing breakdown                    - 服饰拆分图
• exact RGB color palette diagram                 - 精准RGB色号表
• material swatch panel                           - 材质球面板
• detail callout                                  - 细节标注
```

**微观精雕**：
```
• intricate skin texture                          - 复杂皮肤纹理
• visible pores                                   - 可见毛孔
• peach fuzz                                      - 面部绒毛
• translucent skin                                - 半透皮肤
• realistic eye reflection                        - 真实眼睛反光
• detailed hair physics                           - 精细毛发物理效果
• micro-details                                   - 微观细节
• subsurface scattering on skin                   - 皮肤次表面散射
```

### 材质描述词库

**硬表面材质**：
```
• brushed metal                                   - 拉丝金属
• weathered steel                                 - 风化钢铁
• polished chrome                                 - 抛光铬
• gunmetal finish                                 - 枪金属质感
• carbon fiber weave                              - 碳纤维编织
• scratched aluminum                              - 划痕铝材
```

**有机材质**：
```
• worn leather                                    - 做旧皮革
• oiled leather                                   - 油皮
• tactical nylon                                  - 战术尼龙
• cotton twill                                    - 棉斜纹
• wool tweed                                      - 羊毛粗花呢
• silk charmeuse                                  - 丝绸查米尤斯
```

**特殊效果**：
```
• tactical wear and tear                          - 战术磨损
• battle damage                                   - 战损痕迹
• dust accumulation                               - 积尘效果
• rust oxidation                                  - 锈蚀氧化
• patina finish                                   - 铜绿包浆
```

---

## 八、输出交付标准

### 标准交付物清单

```markdown
### 角色定妆参考单交付包

1. **主设定图** (Master Sheet)
   - 文件名: [角色名]_ModelSheet_v01.png
   - 规格: 4K分辨率 (3840×2160)
   - 内容: 四视图 + 材质球 + 表情集 + 色号表

2. **分图层文件** (Layered Files)
   - 文件名: [角色名]_Layers_v01.psd
   - 内容: 各视图独立图层，便于调整

3. **材质规范表** (Material Spec)
   - 文件名: [角色名]_MaterialSpec_v01.md
   - 内容: 每种材质的PBR参数、参考图、制作说明

4. **技术约束文档** (Technical Spec)
   - 文件名: [角色名]_TechSpec_v01.md
   - 内容: 面数限制、拓扑要求、绑定需求、UV规范

5. **变体设计图** (Variants) [如有]
   - 文件名: [角色名]_Variant_[类型]_v01.png
   - 内容: 服装变体、表情变体、损伤变体等
```

### 材质规范表模板

```markdown
# [角色名] 材质规范表

## 材质1: [材质名称]
- **类型**: [布料/皮革/金属/皮肤/毛发]
- **基础色 (Albedo)**: RGB([R], [G], [B]) / Hex: #[HexCode]
- **粗糙度 (Roughness)**: [0.0-1.0]
- **金属度 (Metallic)**: [0.0-1.0]
- **法线强度 (Normal)**: [强度值]
- **次表面散射 (SSS)**: [是/否] | 强度: [值]
- **视觉描述**: [详细描述]
- **参考图**: [参考图路径]
- **制作备注**: [特殊制作要求]

## 材质2: [材质名称]
...
```

### 技术约束文档模板

```markdown
# [角色名] 技术约束文档

## 建模规范
- **面数限制**: [数值] 三角面
- **四边面比例**: ≥ [百分比]%
- **极点位置**: [限制说明]
- **布线方向**: [跟随肌肉/服装结构]

## 绑定需求
- **骨骼数量**: [数值] 根
- **脊柱段数**: [数值] 段
- **手指骨骼**: [是否独立]
- **表情Blendshape**: [数值] 个
- **变形要求**: [特殊变形需求]

## UV规范
- **UV利用率**: ≥ [百分比]%
- **Texel密度**: [数值] px/m
- **接缝位置**: [隐藏位置说明]
- **UDIM分块**: [数量] 块

## 材质规范
- **PBR贴图**: [基础色/法线/粗糙度/金属度/AO/自发光]
- **贴图分辨率**: [2K/4K/8K]
- **特殊材质**: [毛发/皮肤/透明材质说明]
```
