"""
集数映射读取助手
================
统一读取 `assets/chapter-episode-map.json`（由
tools/generators/chapter-episode-map-generator.py 生成），
给各工具提供 ep → 章节 / 对应小说章节 的解析，避免每个脚本各自硬编码或靠 --chapter 传参。

设计：纯读取，map 不存在或缺该集时返回 None / 空列表（fail-soft），调用方自行兜底。
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Optional


def _default_map_path(root: Path) -> Path:
    return root / "assets" / "chapter-episode-map.json"


def normalize_ep(raw: str) -> Optional[str]:
    """ep2 / EP02 / ep0201 → ep02（取前两位集号）。无法识别返回 None。"""
    if not raw:
        return None
    m = re.search(r"(?i)ep\s*0*(\d{1,2})", raw)
    return f"ep{int(m.group(1)):02d}" if m else None


def load_episode_map(root: Path) -> Optional[dict]:
    """读取映射 JSON；不存在或损坏返回 None。"""
    p = _default_map_path(root)
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def get_episode_entry(root: Path, ep: str) -> Optional[dict]:
    data = load_episode_map(root)
    ep_id = normalize_ep(ep)
    if not data or not ep_id:
        return None
    return data.get("episodes", {}).get(ep_id)


def resolve_chapter(root: Path, ep: str) -> Optional[str]:
    """返回该集对应的集纲章节标识，如 'ch02'；无映射返回 None。"""
    entry = get_episode_entry(root, ep)
    return entry.get("chapter") if entry else None


def resolve_novel_chapters(root: Path, ep: str) -> list[str]:
    """返回该集改编自的小说章节列表，如 ['第3章','第4章']；无映射返回 []。"""
    entry = get_episode_entry(root, ep)
    return list(entry.get("novelChapters", [])) if entry else []
