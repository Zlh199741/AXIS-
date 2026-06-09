"""
文件解析模块
解析项目中的各类 Markdown 文件：剧本、资产、输出提示词。
"""

import re
from typing import List, Dict, Optional


class ScriptParser:
    """剧本文件解析器"""

    _EP_RE = re.compile(r"(?i)ep\s*0*([1-9]\d?)|第([一二三四五六七八九十零百]+|\d+)集")
    _ZH_DIGIT = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
                 "六": 6, "七": 7, "八": 8, "九": 9}

    @classmethod
    def _zh_to_int(cls, zh: str) -> int:
        """将中文数字转为整数，支持复合数字（十一=11、二十=20、二十一=21…），上限 99。"""
        if not zh:
            return 0
        if zh in cls._ZH_DIGIT:
            return cls._ZH_DIGIT[zh]
        if "十" not in zh:
            # 纯数字串（无十），逐位拼接
            total = 0
            for ch in zh:
                if ch not in cls._ZH_DIGIT:
                    return 0
                total = total * 10 + cls._ZH_DIGIT[ch]
            return total
        tens_part, _, units_part = zh.partition("十")
        tens = cls._ZH_DIGIT.get(tens_part, 1) if tens_part else 1
        units = cls._ZH_DIGIT.get(units_part, 0) if units_part else 0
        return tens * 10 + units

    def extract_episode_number(self, filename: str) -> Optional[str]:
        m = self._EP_RE.search(filename)
        if not m:
            return None
        if m.group(1):
            return f"ep{int(m.group(1)):02d}"
        zh = m.group(2)
        try:
            num = int(zh)
        except ValueError:
            num = self._zh_to_int(zh)
        return f"ep{num:02d}" if num else None

    def extract_scenes(self, content: str) -> List[str]:
        scenes = []
        for m in re.finditer(r"P\d+\s*场景[：:]\s*(.+)", content):
            scenes.append(m.group(1).strip())
        return scenes

    def extract_characters(self, content: str) -> List[Dict]:
        chars = []
        in_section = False
        for line in content.splitlines():
            line = line.strip()
            if re.search(r"人物清单|角色清单", line):
                in_section = True
                continue
            if in_section and re.match(r"\d+[.、]", line):
                name_part = re.sub(r"^\d+[.、]\s*", "", line)
                name = name_part.split("-")[0].split("—")[0].strip()
                chars.append({"name": name, "raw": line})
            elif in_section and line.startswith("#"):
                break
        return chars


class AssetParser:
    """资产文件解析器（character-prompts.md / scene-prompts.md）"""

    _HEADER_RE = re.compile(
        r"\[(?P<ep>ep\d+)\]\[(?P<type>character|scene|props|prop)\]\[(?P<action>[^\]]+)\]\s+(?P<name>.+)"
    )

    def _parse_sections(self, content: str, asset_type: str) -> Dict[str, Dict]:
        result: Dict[str, Dict] = {}
        current_ep = None
        current_name = None
        for line in content.splitlines():
            line = line.strip()
            if line.startswith("#"):
                m = self._HEADER_RE.search(line)
                if m and m.group("type") == asset_type:
                    current_ep = m.group("ep")
                    current_name = m.group("name").strip()
                    result.setdefault(current_ep, {})[current_name] = {}
        return result

    def parse_character_prompts(self, content: str) -> Dict[str, Dict]:
        return self._parse_sections(content, "character")

    def parse_scene_prompts(self, content: str) -> Dict[str, Dict]:
        return self._parse_sections(content, "scene")


class OutputParser:
    """输出文件解析器（02-seedance-prompts.md 等）"""

    def parse_seedance_prompts(self, content: str) -> Dict[str, str]:
        prompts: Dict[str, str] = {}
        current_key = None
        lines_buf: List[str] = []
        for line in content.splitlines():
            m = re.search(r"##\s+(P\d+)", line)
            if m:
                if current_key:
                    prompts[current_key] = "\n".join(lines_buf).strip()
                current_key = m.group(1)
                lines_buf = []
            elif current_key:
                lines_buf.append(line)
        if current_key:
            prompts[current_key] = "\n".join(lines_buf).strip()
        return prompts

    def parse_material_mapping(self, content: str) -> Dict[str, Dict]:
        mapping: Dict[str, Dict] = {}
        for line in content.splitlines():
            line = line.strip()
            m = re.match(r"\|\s*(@(?:图片|视频|音频)\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|", line)
            if m:
                mapping[m.group(1)] = {
                    "type": m.group(2).strip(),
                    "description": m.group(3).strip(),
                }
        return mapping
