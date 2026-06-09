---
name: virtual-lighting-camera-library
description: 灯光与摄影机参数库。整合1000组虚拟制片灯光与摄影机运动逻辑，提供多维度检索和自动推荐功能。
---

# 灯光与摄影机参数库

## 概述

整合了 1000 组虚拟制片灯光与摄影机运动逻辑，分为三大模块：
- **光影逻辑** (354条)：光源类型、光质、光比
- **场景合成** (325条)：大气介质、镜头瑕疵
- **摄影机物理** (321条)：焦段、景深、动态模糊

> **互补资源**：电影摄影三件套（技法原理+代表作案例+AI提示词模板）— `resources/电影摄影-主文件(技法+设备+工作流程).md` · `resources/电影摄影-40+代表作视觉分析.md` · `resources/电影摄影-AI提示词库.md` · `resources/电影感精确词汇参考表.md`

---

## 数据结构

```python
# 灯光摄影机参数库数据
LIGHTING_CAMERA_LIBRARY = {
    "light_sources": {
        "钨丝灯": {
            "name": "钨丝灯（暖色调点光源）",
            "characteristics": "暖色调点光源，模拟烛光/火光效果",
            "color_temp": "暖色 (2700-3000K)",
            "suitable_for": ["古典场景", "温馨氛围", "烛光场景"]
        },
        "LED灯墙": {
            "name": "LED灯墙（柔和面光源）",
            "characteristics": "柔和面光源，现代/科幻风格",
            "color_temp": "可调",
            "suitable_for": ["现代场景", "科幻风格", "补光"]
        },
        "镝灯": {
            "name": "镝灯（日光模拟）",
            "characteristics": "模拟日光，专业影视灯",
            "color_temp": "日光 (5600K)",
            "suitable_for": ["日景", "阳光效果", "专业拍摄"]
        },
        # ... 更多光源
    },
    
    "light_qualities": {
        "硬光": {
            "name": "硬光（Sharp Shadow）",
            "effect": "用于表现刚硬、金属质感",
            "creates": "清晰硬边阴影"
        },
        "柔光": {
            "name": "柔光（Soft Shadow）",
            "effect": "用于表现皮肤/丝绸等柔软质感",
            "creates": "柔和渐变阴影"
        },
        "散光": {
            "name": "散光（Diffused Light）",
            "effect": "均匀照明",
            "creates": "无明显阴影"
        },
        "聚光": {
            "name": "聚光（Focused Light）",
            "effect": "突出主体",
            "creates": "聚焦高亮区域"
        },
        "轮廓光": {
            "name": "轮廓光（Rim Light）",
            "effect": "分离主体与背景",
            "creates": "边缘高光轮廓"
        }
    },
    
    "light_ratios": {
        "1:1": {"name": "平光", "effect": "无明显阴影，柔和"},
        "2:1": {"name": "柔和对比", "effect": "轻微阴影，柔和"},
        "3:1": {"name": "戏剧性", "effect": "明显阴影，戏剧感"},
        "4:1": {"name": "强烈对比", "effect": "强烈明暗对比"},
        "5:1": {"name": "极端对比", "effect": "最大明暗对比"}
    },
    
    "atmospheric_media": {
        "雨": {"name": "雨（Rain）", "effect": "增加画面层次，表现时间流逝"},
        "花粉": {"name": "花粉（Pollen）", "effect": "让光线产生体积感"},
        "雪": {"name": "雪（Snow）", "effect": "营造浪漫/梦幻效果"},
        "烟": {"name": "烟（Smoke）", "effect": "模拟电影质感"},
        "尘": {"name": "尘（Dust）", "effect": "创造梦幻/神秘氛围"},
        "蒸汽": {"name": "蒸汽（Steam）", "effect": "表现时间流逝"},
        "雾": {"name": "雾（Fog）", "effect": "营造神秘/分隔空间"},
        "露珠": {"name": "露珠（Dew）", "effect": "营造精致/清新氛围"}
    },
    
    "lens_flaws": {
        "柔焦": {"name": "柔焦（Soft Focus）", "effect": "增强画面真实感/梦幻感"},
        "色差": {"name": "色差（Chromatic Aberration）", "effect": "营造神秘/科幻氛围"},
        "镜头光晕": {"name": "镜头光晕（Lens Flare）", "effect": "增加画面真实感"},
        "渐晕": {"name": "渐晕（Vignette）", "effect": "突出主体/分隔空间"},
        "锐化过度": {"name": "锐化过度（Over Sharpening）", "effect": "创造梦幻效果"},
        "暗角": {"name": "暗角（Dark Corners）", "effect": "突出主体/增加层次"}
    },
    
    "lens_types": {
        "广角": {
            "name": "广角（Wide Angle）",
            "characteristics": "夸张透视，适合大场景",
            "focal_length": "14-35mm",
            "suitable_for": ["大场景", "建筑", "狭窄空间"]
        },
        "标准": {
            "name": "标准（Normal）",
            "characteristics": "自然视角",
            "focal_length": "35-70mm",
            "suitable_for": ["日常拍摄", "人文", "记录"]
        },
        "长焦": {
            "name": "长焦（Telephoto）",
            "characteristics": "压缩空间，适合特写",
            "focal_length": "70-200mm",
            "suitable_for": ["人像特写", "压缩感", "远摄"]
        },
        "鱼眼": {
            "name": "鱼眼（Fisheye）",
            "characteristics": "极端广角",
            "focal_length": "8-16mm",
            "suitable_for": ["特殊效果", "夸张透视", "创意"]
        },
        "微距": {
            "name": "微距（Macro）",
            "characteristics": "近距离细节",
            "focal_length": "50-100mm",
            "suitable_for": ["细节拍摄", "产品", "昆虫"]
        },
        "移轴": {
            "name": "移轴（Tilt-Shift）",
            "characteristics": "透视校正",
            "suitable_for": ["建筑", "风景", "微缩效果"]
        }
    },
    
    "aperture_presets": {
        "f/1.4": {"name": "极浅景深", "effect": "突出主体，极度虚化背景"},
        "f/1.8": {"name": "浅景深", "effect": "人像摄影，背景虚化"},
        "f/2.8": {"name": "中等景深", "effect": "兼顾主体与环境"},
        "f/4": {"name": "适中景深", "effect": "日常拍摄"},
        "f/8": {"name": "深景深", "effect": "风景/建筑"},
        "f/16": {"name": "极深景深", "effect": "全景/微距"}
    },
    
    "motion_blur": {
        "45度": {"name": "超清晰", "effect": "几乎无运动模糊"},
        "90度": {"name": "清晰运动", "effect": "轻微运动感"},
        "180度": {"name": "电影级", "effect": "标准电影运动模糊"},
        "270度": {"name": "强烈模糊", "effect": "强烈运动感"},
        "360度": {"name": "极端模糊", "effect": "极度动态效果"}
    },
    
    # 应用场景索引
    "scenarios": {
        "让光线产生体积感": {
            "light_source": "氙气灯/荧光灯",
            "atmosphere": "花粉/烟雾/雨",
            "lens_flaw": "柔焦/渐晕"
        },
        "表现人物孤立强大": {
            "lens_type": "长焦/鱼眼/标准",
            "aperture": "f/1.4",
            "motion_blur": "180度/270度"
        },
        "营造悬疑氛围": {
            "light_source": "荧光灯/激光/霓虹灯",
            "light_quality": "硬光",
            "light_ratio": "4:1-5:1"
        },
        # ... 更多场景
    }
}
```

---

## 工具实现

### virtual_lighting_camera_tool.py

```python
#!/usr/bin/env python3
"""
灯光与摄影机参数库工具
用于从1000组逻辑库中检索和推荐参数组合
"""

import json
import random
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class LightingParams:
    """灯光参数"""
    source: str  # 光源类型
    quality: str  # 光质
    ratio: str  # 光比
    
    def to_prompt(self) -> str:
        return f"{self.source}，{self.quality}，{self.ratio}"


@dataclass
class AtmosphereParams:
    """氛围参数"""
    media: str  # 大气介质
    lens_flaw: str  # 镜头瑕疵
    
    def to_prompt(self) -> str:
        return f"{self.media}，{self.lens_flaw}"


@dataclass
class CameraParams:
    """摄影机参数"""
    lens: str  # 焦段
    aperture: str  # 景深
    motion_blur: str  # 动态模糊
    
    def to_prompt(self) -> str:
        return f"{self.lens}，{self.aperture}，{self.motion_blur}"


@dataclass
class CompleteVisualParams:
    """完整视觉参数组合"""
    lighting: Optional[LightingParams]
    atmosphere: Optional[AtmosphereParams]
    camera: Optional[CameraParams]
    scenario: str  # 应用场景
    
    def to_prompt(self) -> str:
        parts = []
        if self.lighting:
            parts.append(f"灯光：{self.lighting.to_prompt()}")
        if self.atmosphere:
            parts.append(f"氛围：{self.atmosphere.to_prompt()}")
        if self.camera:
            parts.append(f"摄影：{self.camera.to_prompt()}")
        return " | ".join(parts)


class VirtualLightingCameraLibrary:
    """灯光与摄影机参数库"""
    
    def __init__(self, data_file: str = None):
        self.data_file = data_file or "副本虚拟制片灯光与摄影机运动逻辑库_1000组(1).txt"
        self.records = []
        self.load_data()
    
    def load_data(self):
        """加载数据"""
        import codecs
        
        try:
            with codecs.open(self.data_file, 'r', encoding='utf-16') as f:
                lines = f.readlines()
            
            # 跳过标题行
            for line in lines[1:]:
                parts = line.strip().split('\t')
                if len(parts) >= 6:
                    record = {
                        'id': parts[0],
                        'module': parts[1],  # 模块分类
                        'type': parts[2],    # 类型
                        'params': parts[3],  # 具体参数
                        'scenario': parts[4],  # 应用场景
                        'prompt': parts[5]   # 视觉提示词
                    }
                    self.records.append(record)
        except FileNotFoundError:
            # 如果文件不存在，使用内存中的数据
            self.records = self._get_default_records()
    
    def _get_default_records(self) -> List[Dict]:
        """获取默认记录（备用数据）"""
        # 这里可以硬编码一些常用组合
        return []
    
    # ========== 检索方法 ==========
    
    def search_by_module(self, module: str) -> List[Dict]:
        """按模块检索"""
        return [r for r in self.records if r['module'] == module]
    
    def search_by_scenario(self, scenario: str) -> List[Dict]:
        """按应用场景检索"""
        return [r for r in self.records if scenario in r['scenario']]
    
    def search_light_sources(self, source: str) -> List[Dict]:
        """检索特定光源"""
        return [r for r in self.records 
                if '光影逻辑' in r['module'] and source in r['params']]
    
    def search_atmosphere(self, media: str) -> List[Dict]:
        """检索特定大气介质"""
        return [r for r in self.records 
                if '场景合成' in r['module'] and media in r['params']]
    
    def search_lens(self, lens_type: str) -> List[Dict]:
        """检索特定焦段"""
        return [r for r in self.records 
                if '摄影机物理' in r['module'] and lens_type in r['params']]
    
    # ========== 推荐方法 ==========
    
    def recommend_for_character(self, 
                               mood: str = "normal",
                               era: str = "古代") -> CompleteVisualParams:
        """为人物推荐参数"""
        records = []
        
        if mood == "强大/孤立":
            # 寻找表现孤立强大的参数
            records = self.search_by_scenario("孤立强大")
            if not records:
                records = self.search_by_module("摄影机物理")[:10]
        elif mood == "温馨":
            records = self.search_by_scenario("浪漫")
        elif mood == "紧张":
            records = self.search_by_scenario("悬疑")
        else:
            # 随机选择一些
            records = random.sample(self.records, min(3, len(self.records)))
        
        return self._extract_params_from_records(records, f"人物-{mood}")
    
    def recommend_for_scene(self,
                           scene_type: str = "室内",
                           time: str = "夜晚",
                           atmosphere: str = "神秘") -> CompleteVisualParams:
        """为场景推荐参数"""
        records = []
        
        # 根据氛围搜索
        if atmosphere == "神秘":
            records = self.search_by_scenario("神秘")
        elif atmosphere == "浪漫":
            records = self.search_by_scenario("浪漫")
        elif atmosphere == "紧张":
            records = self.search_by_scenario("悬疑")
        
        if not records:
            # 根据时间搜索
            if time == "夜晚":
                # 夜晚场景适合的氛围
                records = [r for r in self.records if '烛光' in r['params'] or '柔光' in r['params']]
        
        if not records:
            records = random.sample(self.records, min(3, len(self.records)))
        
        return self._extract_params_from_records(records, f"场景-{atmosphere}")
    
    def recommend_for_action(self,
                            action_type: str = "运动") -> CompleteVisualParams:
        """为动作场景推荐参数"""
        records = self.search_by_scenario("运动")
        
        if not records:
            # 运动场景适合的摄影机参数
            records = [r for r in self.records 
                      if '90度' in r['params'] or '清晰' in r['params']]
        
        if not records:
            records = random.sample(self.records, min(3, len(self.records)))
        
        return self._extract_params_from_records(records, f"动作-{action_type}")
    
    def recommend_volume_sense(self) -> CompleteVisualParams:
        """推荐产生体积感的参数"""
        records = self.search_by_scenario("体积感")
        return self._extract_params_from_records(records, "体积感")
    
    def get_random_combo(self) -> CompleteVisualParams:
        """获取随机组合"""
        # 分别从三个模块各取一个
        light_records = self.search_by_module("光影逻辑")
        atmos_records = self.search_by_module("场景合成")
        camera_records = self.search_by_module("摄影机物理")
        
        lighting = None
        atmosphere = None
        camera = None
        
        if light_records:
            r = random.choice(light_records)
            params = self._parse_light_params(r['params'])
            if params:
                lighting = params
        
        if atmos_records:
            r = random.choice(atmos_records)
            params = self._parse_atmos_params(r['params'])
            if params:
                atmosphere = params
        
        if camera_records:
            r = random.choice(camera_records)
            params = self._parse_camera_params(r['params'])
            if params:
                camera = params
        
        return CompleteVisualParams(
            lighting=lighting,
            atmosphere=atmosphere,
            camera=camera,
            scenario="随机组合"
        )
    
    # ========== 解析方法 ==========
    
    def _extract_params_from_records(self, 
                                     records: List[Dict],
                                     scenario: str) -> CompleteVisualParams:
        """从记录中提取参数"""
        lighting = None
        atmosphere = None
        camera = None
        
        for r in records:
            module = r['module']
            params = r['params']
            
            if '光影逻辑' in module and not lighting:
                lighting = self._parse_light_params(params)
            elif '场景合成' in module and not atmosphere:
                atmosphere = self._parse_atmos_params(params)
            elif '摄影机物理' in module and not camera:
                camera = self._parse_camera_params(params)
        
        return CompleteVisualParams(
            lighting=lighting,
            atmosphere=atmosphere,
            camera=camera,
            scenario=scenario
        )
    
    def _parse_light_params(self, params: str) -> Optional[LightingParams]:
        """解析灯光参数"""
        # 提取光源
        source = ""
        sources = ["钨丝灯", "LED灯墙", "镝灯", "氙气灯", "荧光灯", 
                  "激光", "HMI灯", "霓虹灯管", "烛光"]
        for s in sources:
            if s in params:
                source = s
                break
        
        # 提取光质
        quality = ""
        qualities = ["硬光", "柔光", "散光", "聚光", "轮廓光", "半硬光"]
        for q in qualities:
            if q in params:
                quality = q
                break
        
        # 提取光比
        ratio = ""
        ratios = ["1:1", "2:1", "3:1", "4:1", "5:1"]
        for r in ratios:
            if r in params:
                ratio = r
                break
        
        if source and quality and ratio:
            return LightingParams(source=source, quality=quality, ratio=ratio)
        return None
    
    def _parse_atmos_params(self, params: str) -> Optional[AtmosphereParams]:
        """解析氛围参数"""
        # 提取大气介质
        media = ""
        media_list = ["雨", "花粉", "雪", "烟", "尘", "蒸汽", "雾", "露珠"]
        for m in media_list:
            if m in params:
                media = m
                break
        
        # 提取镜头瑕疵
        flaw = ""
        flaws = ["柔焦", "色差", "镜头光晕", "渐晕", "锐化过度", "暗角"]
        for f in flaws:
            if f in params:
                flaw = f
                break
        
        if media and flaw:
            return AtmosphereParams(media=media, lens_flaw=flaw)
        return None
    
    def _parse_camera_params(self, params: str) -> Optional[CameraParams]:
        """解析摄影机参数"""
        # 提取焦段
        lens = ""
        lenses = ["广角", "标准", "长焦", "鱼眼", "微距", "移轴"]
        for l in lenses:
            if l in params:
                lens = l
                break
        
        # 提取光圈
        aperture = ""
        apertures = ["f/1.4", "f/1.8", "f/2.8", "f/4", "f/8", "f/16"]
        for a in apertures:
            if a in params:
                aperture = a
                break
        
        # 提取动态模糊
        motion = ""
        motions = ["45度", "90度", "180度", "270度", "360度"]
        for m in motions:
            if m in params:
                motion = m
                break
        
        if lens and aperture and motion:
            return CameraParams(lens=lens, aperture=aperture, motion_blur=motion)
        return None
    
    # ========== 导出方法 ==========
    
    def export_to_prompt_format(self, 
                                scenario: str,
                                count: int = 5) -> List[str]:
        """导出为提示词格式"""
        records = self.search_by_scenario(scenario)
        
        if not records:
            records = random.sample(self.records, min(count, len(self.records)))
        
        return [r['prompt'] for r in records[:count]]
    
    def get_statistics(self) -> Dict:
        """获取统计信息"""
        stats = {
            "total": len(self.records),
            "by_module": defaultdict(int),
            "scenarios": defaultdict(int)
        }
        
        for r in self.records:
            stats["by_module"][r['module']] += 1
            
            # 提取场景关键词
            scenario = r['scenario']
            for key in ["体积感", "自然光", "电影质感", "分离", "悬疑", 
                       "孤立", "表情", "太空站", "层次", "浪漫", "金属", "细腻"]:
                if key in scenario:
                    stats["scenarios"][key] += 1
        
        stats["by_module"] = dict(stats["by_module"])
        stats["scenarios"] = dict(stats["scenarios"])
        
        return stats


def main():
    """命令行入口"""
    import argparse
    
    parser = argparse.ArgumentParser(description="灯光与摄影机参数库工具")
    parser.add_argument("data_file", nargs='?', help="数据文件路径")
    parser.add_argument("--search", type=str, help="按场景搜索")
    parser.add_argument("--module", type=str, choices=["光影逻辑", "场景合成", "摄影机物理"],
                       help="按模块搜索")
    parser.add_argument("--recommend-character", action="store_true", help="为人物推荐")
    parser.add_argument("--recommend-scene", action="store_true", help="为场景推荐")
    parser.add_argument("--random", action="store_true", help="随机组合")
    parser.add_argument("--stats", action="store_true", help="统计信息")
    parser.add_argument("--export", type=str, help="导出提示词")
    
    args = parser.parse_args()
    
    library = VirtualLightingCameraLibrary(args.data_file)
    
    if args.stats:
        stats = library.get_statistics()
        print(json.dumps(stats, ensure_ascii=False, indent=2))
    
    elif args.search:
        results = library.search_by_scenario(args.search)
        print(f"找到 {len(results)} 条结果:")
        for r in results[:10]:
            print(f"  - {r['prompt']}")
    
    elif args.module:
        results = library.search_by_module(args.module)
        print(f"找到 {len(results)} 条结果:")
        for r in results[:10]:
            print(f"  - {r['prompt']}")
    
    elif args.recommend_character:
        result = library.recommend_for_character(mood="强大/孤立")
        print(f"推荐参数：{result.to_prompt()}")
    
    elif args.recommend_scene:
        result = library.recommend_for_scene(atmosphere="神秘")
        print(f"推荐参数：{result.to_prompt()}")
    
    elif args.random:
        result = library.get_random_combo()
        print(f"随机组合：{result.to_prompt()}")
    
    elif args.export:
        prompts = library.export_to_prompt_format(args.export)
        for p in prompts:
            print(p)


if __name__ == "__main__":
    main()
```

---

## 使用示例

### 1. 检索应用场景

```python
from virtual_lighting_camera_tool import VirtualLightingCameraLibrary

library = VirtualLightingCameraLibrary()

# 搜索"表现人物孤立强大"的参数
results = library.search_by_scenario("孤立强大")
for r in results[:5]:
    print(r['prompt'])

# 输出示例：
# 鱼眼，f/8（深景深），45度（超清晰）
# 移轴，f/16（极深景深），180度（电影级运动模糊）
# 广角，f/1.4（极浅景深），90度（清晰运动）
```

### 2. 为人物推荐参数

```python
# 为表现"孤立强大"的人物推荐
result = library.recommend_for_character(mood="强大/孤立")
print(result.to_prompt())

# 输出示例：
# 灯光：标准，f/1.4（极浅景深），180度（电影级运动模糊）
```

### 3. 为场景推荐参数

```python
# 为夜晚神秘氛围的场景推荐
result = library.recommend_for_scene(
    scene_type="室内",
    time="夜晚",
    atmosphere="神秘"
)
print(result.to_prompt())

# 输出示例：
# 灯光：激光，散光，4:1（强烈对比） | 氛围：雾（Fog），色差
```

### 4. 获取随机组合

```python
# 获取随机参数组合
result = library.get_random_combo()
print(result.to_prompt())

# 输出示例：
# 灯光：氙气灯，轮廓光，2:1（柔和对比） | 氛围：烟（Smoke），柔焦 | 摄影：长焦，f/8（深景深），90度（清晰运动）
```

### 5. 导出提示词格式

```python
# 导出"体积感"场景的提示词
prompts = library.export_to_prompt_format("体积感", count=10)
for p in prompts:
    print(p)
```

---

## 命令行工具

```bash
# 按场景搜索
python virtual_lighting_camera_tool.py --search "孤立强大"

# 按模块搜索
python virtual_lighting_camera_tool.py --module "光影逻辑"

# 为人物推荐
python virtual_lighting_camera_tool.py --recommend-character

# 为场景推荐
python virtual_lighting_camera_tool.py --recommend-scene

# 随机组合
python virtual_lighting_camera_tool.py --random

# 统计信息
python virtual_lighting_camera_tool.py --stats

# 导出提示词
python virtual_lighting_camera_tool.py --export "体积感"
```

---

## 在项目中的集成位置

### 1. 集成到 `art-designer`

在生成人物/场景提示词时，自动添加推荐的灯光和摄影机参数：

```python
# 在 art-design-skill 中
from virtual_lighting_camera_tool import VirtualLightingCameraLibrary

def enhance_with_lighting_prompt(base_prompt: str, mood: str) -> str:
    library = VirtualLightingCameraLibrary()
    params = library.recommend_for_character(mood=mood)
    return f"{base_prompt}\n\n**视觉参数**：{params.to_prompt()}"
```

### 2. 集成到视听语言逻辑

作为视听语言的补充，提供精确的技术参数：

```markdown
## 视听语言设计
- 镜头关系：轴线/越轴
- 光影设计：{{params.lighting.to_prompt()}}
- 氛围营造：{{params.atmosphere.to_prompt()}}
```

### 3. 集成到 Seedance 提示词

在生成 Seedance 提示词时添加视觉参数：

```python
def add_visual_params_to_seedance(prompt: str, scene: str) -> str:
    library = VirtualLightingCameraLibrary()
    params = library.recommend_for_scene(atmosphere=scene)
    return f"{prompt}\n\n## 视觉参数\n{params.to_prompt()}"
```

