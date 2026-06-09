"""
标签解析模块
解析 assets/ 中的集数标记标签，如：
  ## [ep01][character][新增] 江辰
  ## [ep02][scene][变体] 江府房间-夜
"""

import re
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional


class LabelType(Enum):
    CHARACTER = "character"
    SCENE = "scene"
    PROPS = "props"
    UNKNOWN = "unknown"


@dataclass
class EpisodeLabel:
    episode: str
    type: LabelType
    action: str
    name: str

    def __eq__(self, other):
        if not isinstance(other, EpisodeLabel):
            return False
        return (self.episode == other.episode and self.type == other.type
                and self.action == other.action and self.name == other.name)

    def __str__(self):
        return f"[{self.episode}][{self.type.value}][{self.action}] {self.name}"


# Matches: [ep01][character][新增] 江辰
_LABEL_RE = re.compile(
    r"\[(?P<episode>ep\d+)\]\[(?P<type>[a-z]+)\]\[(?P<action>[^\]]+)\]\s*(?P<name>.+)"
)

_TYPE_MAP = {
    "character": LabelType.CHARACTER,
    "scene": LabelType.SCENE,
    "props": LabelType.PROPS,
    "prop": LabelType.PROPS,  # 兼容历史单数写法
}


class LabelParser:
    """集数标签解析器"""

    def parse(self, label: str) -> Optional[EpisodeLabel]:
        m = _LABEL_RE.search(label.strip())
        if not m:
            return None
        label_type = _TYPE_MAP.get(m.group("type"), LabelType.UNKNOWN)
        return EpisodeLabel(
            episode=m.group("episode"),
            type=label_type,
            action=m.group("action"),
            name=m.group("name").strip(),
        )

    def extract_all(self, content: str) -> List[EpisodeLabel]:
        results = []
        for line in content.splitlines():
            line = line.strip().lstrip("#").strip()
            parsed = self.parse(line)
            if parsed:
                results.append(parsed)
        return results

    def filter_by_episode(self, labels: List[EpisodeLabel], episode: str) -> List[EpisodeLabel]:
        return [l for l in labels if l.episode == episode]
