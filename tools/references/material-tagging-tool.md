---
name: material-tagging-system
description: 素材标签系统。提供多维度标签检索能力，支持对人物、场景、道具等素材进行精细化分类和快速查找。
---

# 素材标签系统

## 概述

素材标签系统是一个用于对项目中的素材（人物、场景、道具等）进行多维度标注和检索的工具。通过多维度标签，可以实现：

- 快速查找符合条件的素材
- 跨集素材复用推荐
- 素材一致性检查
- 素材版本追踪

---

## 标签维度定义

### 1. 基础维度

| 维度 | 标签示例 | 说明 |
|------|---------|------|
| **类型** | `人物`, `场景`, `道具`, `服装`, `特效` | 素材的基本类型 |
| **集数** | `ep01`, `ep02`, `ep03` | 素材出现的集数 |
| **状态** | `待生成`, `生成中`, `已生成`, `已使用`, `已废弃` | 素材的当前状态 |

### 2. 人物维度

| 维度 | 标签示例 | 说明 |
|------|---------|------|
| **角色类型** | `主角`, `配角`, `反派`, `客串`, `群演` | 角色在剧中的重要性 |
| **性别** | `男`, `女`, `中性` | 角色性别 |
| **年龄** | `少年`, `青年`, `中年`, `老年` | 角色年龄段 |
| **身份** | `贵族`, `平民`, `侠客`, `商人`, `官员` | 社会身份 |
| **性格** | `沉稳`, `活泼`, `阴险`, `正直`, `复杂` | 性格特征 |
| **朝代** | `现代`, `唐`, `宋`, `明`, `清` | 穿着朝代 |

### 3. 场景维度

| 维度 | 标签示例 | 说明 |
|------|---------|------|
| **场景类型** | `内景`, `外景`, `内外结合` | 室内/室外 |
| **时间** | `白天`, `夜晚`, `清晨`, `黄昏` | 时间段 |
| **季节** | `春`, `夏`, `秋`, `冬` | 季节 |
| **地点类型** | `府邸`, `街道`, `山林`, `战场` | 地点分类 |
| **氛围** | `温馨`, `紧张`, `恐怖`, `浪漫` | 场景氛围 |
| **光线** | `自然光`, `烛光`, `灯光`, `月光` | 主要光源 |

### 4. 道具维度

| 维度 | 标签示例 | 说明 |
|------|---------|------|
| **道具类型** | `武器`, `服饰`, `首饰`, `家具`, `书信` | 道具分类 |
| **价值** | `普通`, `珍贵`, `稀世` | 价值等级 |
| **材质** | `金属`, `木质`, `玉质`, `丝绸` | 材质 |
| **时代特征** | `古代`, `现代`, `架空` | 时代特征 |

### 5. 视听维度

| 维度 | 标签示例 | 说明 |
|------|---------|------|
| **镜头类型** | `特写`, `近景`, `中景`, `全景`, `远景` | 镜头景别 |
| **运镜** | `推`, `拉`, `摇`, `移`, `跟` | 镜头运动 |
| **色调** | `暖色`, `冷色`, `复古`, `高饱和` | 整体色调 |
| **情绪` | `欢快`, `紧张`, `悲伤`, `恐怖` | 场景情绪 |

---

## 标签格式规范

### 标准标签格式

```
[类型]:[集数]:[状态]:[维度1-值1]:[维度2-值2]:...
```

### 示例

```
# 人物标签
[character]:[ep01]:[已生成]:[主角]:[男]:[青年]:[贵族]:[沉稳]:[唐]

# 场景标签
[scene]:[ep01]:[已使用]:[内景]:[夜晚]:[府邸]:[温馨]:[烛光]

# 道具标签
[prop]:[ep02]:[待生成]:[武器]:[珍贵]:[金属]:[古代]
```

---

## 工具实现

### material_tagging_tool.py

```python
#!/usr/bin/env python3
"""
素材标签工具
用于生成、查询和管理素材标签
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, asdict
from datetime import datetime
from collections import defaultdict


@dataclass
class MaterialTag:
    """素材标签数据类"""
    id: str
    name: str
    material_type: str  # character, scene, prop, costume, effect
    episode: str
    status: str  # pending, generating, generated, used, deprecated
    dimensions: Dict[str, str]  # 多维度标签
    file_path: str
    created_at: str
    updated_at: str
    references: List[str] = None  # 引用的集数
    
    def __post_init__(self):
        if self.references is None:
            self.references = []


class MaterialTaggingSystem:
    """素材标签系统"""
    
    # 标签维度定义
    DIMENSIONS = {
        "character": ["role_type", "gender", "age", "identity", "personality", "era"],
        "scene": ["scene_type", "time", "season", "location_type", "atmosphere", "lighting"],
        "prop": ["prop_type", "value", "material", "era_feature"],
        "costume": ["garment_type", "material", "color", "era"],
        "effect": ["effect_type", "intensity", "color"]
    }
    
    # 有效标签值
    VALID_VALUES = {
        "role_type": ["主角", "配角", "反派", "客串", "群演", "设定"],
        "gender": ["男", "女", "中性"],
        "age": ["少年", "青年", "中年", "老年"],
        "identity": ["贵族", "平民", "侠客", "商人", "官员", "医者", "文人"],
        "personality": ["沉稳", "活泼", "阴险", "正直", "复杂", "腹黑", "单纯"],
        "era": ["现代", "唐", "宋", "明", "清", "架空"],
        "scene_type": ["内景", "外景", "内外结合"],
        "time": ["白天", "夜晚", "清晨", "黄昏", "午夜"],
        "season": ["春", "夏", "秋", "冬"],
        "location_type": ["府邸", "街道", "山林", "战场", "客栈", "青楼", "牢房", "书房"],
        "atmosphere": ["温馨", "紧张", "恐怖", "浪漫", "悲伤", "诡异", "严肃"],
        "lighting": ["自然光", "烛光", "灯光", "月光", "闪电", "火光"],
        "prop_type": ["武器", "服饰", "首饰", "家具", "书信", "药材", "银两"],
        "value": ["普通", "珍贵", "稀世"],
        "material": ["金属", "木质", "玉质", "丝绸", "陶瓷", "纸张"],
        "era_feature": ["古代", "现代", "架空"],
    }
    
    def __init__(self, project_dir: str):
        self.project_dir = Path(project_dir)
        self.tags_file = self.project_dir / "assets" / "material-tags.json"
        self.tags: Dict[str, MaterialTag] = {}
        self.load_tags()
    
    def load_tags(self):
        """加载标签数据"""
        if self.tags_file.exists():
            with open(self.tags_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for tag_id, tag_data in data.items():
                    self.tags[tag_id] = MaterialTag(**tag_data)
    
    def save_tags(self):
        """保存标签数据"""
        self.tags_file.parent.mkdir(parents=True, exist_ok=True)
        data = {tag_id: asdict(tag) for tag_id, tag in self.tags.items()}
        with open(self.tags_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def generate_tag_id(self, material_type: str, name: str, episode: str) -> str:
        """生成标签 ID"""
        clean_name = re.sub(r'[^\w]', '', name)
        return f"{material_type}_{clean_name}_{episode}"
    
    def add_tag(self, name: str, material_type: str, episode: str,
                dimensions: Dict[str, str], file_path: str,
                status: str = "pending") -> MaterialTag:
        """添加新标签"""
        tag_id = self.generate_tag_id(material_type, name, episode)
        
        tag = MaterialTag(
            id=tag_id,
            name=name,
            material_type=material_type,
            episode=episode,
            status=status,
            dimensions=dimensions,
            file_path=file_path,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        
        self.tags[tag_id] = tag
        self.save_tags()
        
        return tag
    
    def update_tag(self, tag_id: str, **kwargs) -> Optional[MaterialTag]:
        """更新标签"""
        if tag_id not in self.tags:
            return None
        
        tag = self.tags[tag_id]
        for key, value in kwargs.items():
            if hasattr(tag, key):
                setattr(tag, key, value)
        
        tag.updated_at = datetime.now().isoformat()
        self.save_tags()
        
        return tag
    
    def delete_tag(self, tag_id: str) -> bool:
        """删除标签"""
        if tag_id in self.tags:
            del self.tags[tag_id]
            self.save_tags()
            return True
        return False
    
    def search(self, conditions: Dict[str, str]) -> List[MaterialTag]:
        """多维度检索"""
        results = []
        
        for tag in self.tags.values():
            match = True
            
            for key, value in conditions.items():
                if key == "material_type":
                    if tag.material_type != value:
                        match = False
                        break
                elif key == "episode":
                    if tag.episode != value and value not in tag.references:
                        match = False
                        break
                elif key == "status":
                    if tag.status != value:
                        match = False
                        break
                elif key in tag.dimensions:
                    if tag.dimensions[key] != value:
                        match = False
                        break
                elif key == "keyword":
                    # 关键词搜索
                    if value.lower() not in tag.name.lower():
                        match = False
                        break
            
            if match:
                results.append(tag)
        
        return results
    
    def fuzzy_search(self, keyword: str) -> List[MaterialTag]:
        """模糊搜索"""
        results = []
        keyword_lower = keyword.lower()
        
        for tag in self.tags.values():
            # 搜索名称
            if keyword_lower in tag.name.lower():
                results.append(tag)
                continue
            
            # 搜索维度值
            for dim_value in tag.dimensions.values():
                if keyword_lower in dim_value.lower():
                    results.append(tag)
                    break
        
        return results
    
    def get_by_material_type(self, material_type: str) -> List[MaterialTag]:
        """按素材类型获取"""
        return [t for t in self.tags.values() if t.material_type == material_type]
    
    def get_by_episode(self, episode: str) -> List[MaterialTag]:
        """按集数获取"""
        return [t for t in self.tags.values() 
                if t.episode == episode or episode in t.references]
    
    def get_by_status(self, status: str) -> List[MaterialTag]:
        """按状态获取"""
        return [t for t in self.tags.values() if t.status == status]
    
    def get_statistics(self) -> Dict:
        """获取统计信息"""
        stats = {
            "total": len(self.tags),
            "by_type": defaultdict(int),
            "by_status": defaultdict(int),
            "by_episode": defaultdict(int),
            "by_dimension": defaultdict(lambda: defaultdict(int))
        }
        
        for tag in self.tags.values():
            stats["by_type"][tag.material_type] += 1
            stats["by_status"][tag.status] += 1
            stats["by_episode"][tag.episode] += 1
            
            for dim, value in tag.dimensions.items():
                stats["by_dimension"][dim][value] += 1
        
        # 转换 defaultdict
        stats["by_type"] = dict(stats["by_type"])
        stats["by_status"] = dict(stats["by_status"])
        stats["by_episode"] = dict(stats["by_episode"])
        stats["by_dimension"] = dict(stats["by_dimension"])
        
        return stats
    
    def recommend_reuse(self, target_episode: str, 
                       dimensions: Dict[str, str]) -> List[MaterialTag]:
        """推荐可复用素材"""
        # 查找其他集数中相同维度的素材
        candidates = []
        
        for tag in self.tags.values():
            if tag.episode == target_episode:
                continue
            
            # 计算维度匹配度
            match_count = 0
            for dim, value in dimensions.items():
                if dim in tag.dimensions and tag.dimensions[dim] == value:
                    match_count += 1
            
            if match_count > 0:
                candidates.append((tag, match_count))
        
        # 按匹配度排序
        candidates.sort(key=lambda x: x[1], reverse=True)
        
        return [c[0] for c in candidates[:10]]
    
    def export_tags(self, format: str = "json") -> str:
        """导出标签"""
        if format == "json":
            return json.dumps(
                {k: asdict(v) for k, v in self.tags.items()},
                ensure_ascii=False,
                indent=2
            )
        elif format == "markdown":
            lines = ["# 素材标签汇总\n"]
            
            # 按类型分组
            by_type = defaultdict(list)
            for tag in self.tags.values():
                by_type[tag.material_type].append(tag)
            
            for mtype, tags in by_type.items():
                lines.append(f"## {mtype}\n")
                for tag in tags:
                    lines.append(f"### {tag.name} ({tag.episode})\n")
                    lines.append(f"- ID: {tag.id}\n")
                    lines.append(f"- 状态: {tag.status}\n")
                    for dim, value in tag.dimensions.items():
                        lines.append(f"- {dim}: {value}\n")
                    lines.append("\n")
            
            return "".join(lines)
        
        return ""


def main():
    """命令行入口"""
    import argparse
    
    parser = argparse.ArgumentParser(description="素材标签工具")
    parser.add_argument("project_dir", help="项目目录")
    parser.add_argument("--add", action="store_true", help="添加标签")
    parser.add_argument("--search", type=str, help="搜索标签")
    parser.add_argument("--list", action="store_true", help="列出所有标签")
    parser.add_argument("--stats", action="store_true", help="统计信息")
    parser.add_argument("--export", type=str, choices=["json", "markdown"], 
                       help="导出标签")
    
    args = parser.parse_args()
    
    system = MaterialTaggingSystem(args.project_dir)
    
    if args.list:
        for tag in system.tags.values():
            print(f"{tag.id}: {tag.name} [{tag.status}]")
    
    elif args.search:
        results = system.fuzzy_search(args.search)
        print(f"找到 {len(results)} 个结果:")
        for tag in results:
            print(f"  - {tag.name} ({tag.episode})")
    
    elif args.stats:
        stats = system.get_statistics()
        print(json.dumps(stats, ensure_ascii=False, indent=2))
    
    elif args.export:
        print(system.export_tags(args.export))


if __name__ == "__main__":
    main()
```

---

## 使用示例

### 1. 添加素材标签

```python
from material_tagging_tool import MaterialTaggingSystem

system = MaterialTaggingSystem("/path/to/project")

# 添加人物标签
system.add_tag(
    name="江辰",
    material_type="character",
    episode="ep01",
    dimensions={
        "role_type": "主角",
        "gender": "男",
        "age": "青年",
        "identity": "贵族",
        "personality": "沉稳",
        "era": "唐"
    },
    file_path="assets/character-江辰.png",
    status="已生成"
)

# 添加场景标签
system.add_tag(
    name="江府房间",
    material_type="scene",
    episode="ep01",
    dimensions={
        "scene_type": "内景",
        "time": "夜晚",
        "location_type": "府邸",
        "atmosphere": "温馨",
        "lighting": "烛光"
    },
    file_path="assets/scene-江府房间.png",
    status="已使用"
)
```

### 2. 多维度检索

```python
# 查找所有主角
results = system.search({"role_type": "主角"})

# 查找 ep01 中的男性角色
results = system.search({
    "episode": "ep01",
    "gender": "男"
})

# 查找夜晚内景
results = system.search({
    "scene_type": "内景",
    "time": "夜晚"
})

# 组合多个维度
results = system.search({
    "material_type": "character",
    "gender": "女",
    "era": "唐",
    "status": "已生成"
})
```

### 3. 素材复用推荐

```python
# 为新集数推荐可复用的古代贵族男性角色
recommendations = system.recommend_reuse(
    target_episode="ep03",
    dimensions={
        "gender": "男",
        "identity": "贵族",
        "era": "唐"
    }
)

for tag in recommendations:
    print(f"推荐: {tag.name} (来自 {tag.episode})")
```

### 4. 统计信息

```python
stats = system.get_statistics()

print(f"总素材数: {stats['total']}")
print(f"按类型: {stats['by_type']}")
print(f"按状态: {stats['by_status']}")
print(f"按集数: {stats['by_episode']}")
```

---

## 与现有系统集成

### 在导演分析阶段自动生成标签

```python
# 在 director-skill 中集成标签生成
def generate_character_tags(character_info: dict) -> dict:
    """从人物信息生成标签"""
    return {
        "role_type": character_info.get("角色类型", "配角"),
        "gender": character_info.get("性别", "男"),
        "age": character_info.get("年龄", "青年"),
        "identity": character_info.get("身份", "平民"),
        "personality": character_info.get("性格", "沉稳"),
        "era": character_info.get("朝代", "唐")
    }
```

### 在服化道阶段自动更新标签

```python
# 素材生成完成后更新状态
system.update_tag(
    tag_id="character_江辰_ep01",
    status="已生成",
    file_path="assets/character-江辰-v2.png"
)
```

---

## 命令行工具

```bash
# 列出所有标签
python material_tagging_tool.py /path/to/project --list

# 搜索标签
python material_tagging_tool.py /path/to/project --search "江辰"

# 查看统计
python material_tagging_tool.py /path/to/project --stats

# 导出为 Markdown
python material_tagging_tool.py /path/to/project --export markdown > tags.md
```

