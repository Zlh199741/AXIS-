"""
共享 IO 工具模块
提供项目级的文件读写、JSON 加载、编码修复等通用函数，
避免各 tools/ 脚本重复实现。
"""

import io
import json
import sys
from pathlib import Path
from typing import Optional


def get_project_root() -> Path:
    """返回项目根目录（包含 CLAUDE.md 的那层）"""
    p = Path(__file__).resolve().parent.parent
    # 向上查找直到找到 CLAUDE.md
    while p != p.parent:
        if (p / "CLAUDE.md").exists():
            return p
        p = p.parent
    # fallback
    return Path(__file__).resolve().parent.parent


def setup_encoding() -> None:
    """修复 Windows 控制台编码问题"""
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(
            sys.stdout.buffer, encoding='utf-8', errors='replace'
        )


def load_json(path: Path) -> Optional[dict]:
    """安全加载 JSON 文件，文件不存在或格式错误时返回 None"""
    if not path.exists():
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def save_json(path: Path, data: dict, indent: int = 2) -> None:
    """写入 JSON 文件"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def check_project_consistency(root: Path):
    """校验 .stage-gate.json 与 .agent-state.json 的 projectName 是否一致。

    多个剧本项目共用同一对状态文件时，切换不彻底会残留脏数据。
    返回 (是否一致: bool, 提示信息: str)；不一致时调用方应告警（不阻断流程）。
    """
    gate = load_json(root / ".stage-gate.json") or {}
    agent = load_json(root / ".agent-state.json") or {}
    g_name = gate.get("projectName", "")
    a_name = agent.get("projectName", "")
    if g_name and a_name and g_name != a_name:
        return False, (
            f"⚠️  项目名不一致：.stage-gate.json=「{g_name}」 vs "
            f".agent-state.json=「{a_name}」；疑似项目切换不彻底的脏数据，请核对后再继续。"
        )
    g_id = gate.get("projectId", "")
    a_id = agent.get("projectId", "")
    if g_id and a_id and g_id != a_id:
        return False, (
            f"⚠️  项目 ID 不一致：.stage-gate.json=「{g_id}」 vs "
            f".agent-state.json=「{a_id}」；疑似项目切换不彻底的脏数据，请核对后再继续。"
        )
    return True, ""


def read_file(path: Path) -> Optional[str]:
    """安全读取文本文件，文件不存在时返回 None"""
    if not path.exists():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None
