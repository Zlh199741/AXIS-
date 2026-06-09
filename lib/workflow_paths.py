# -*- coding: utf-8 -*-
"""
AXIS 工作流路径定义 — 唯一权威数据源
=====================================
3 条路径的阶段序列。小说分析（路径一）和脑洞生成（路径二）是互斥入口，
永远不会出现在同一条路径上。

🔴 阶段集合完整性约定（避免「孤儿阶段」）：
  - PATH_SEQUENCES 只收录**线性内容生产阶段**，三条路径都以「分镜编写」为终点
    （next-step-prompter 依赖此终点：分镜编写后返回 None → 触发系列收尾报告，
     故绝不可把收尾类阶段塞进 PATH_SEQUENCES）。
  - 「集间交接」是**每集分镜完成后执行的收尾型 housekeeping 阶段**
    （定义见 AXIS-workflow-stages.md「阶段十一：集间交接」、枚举见其
     「stageHistory / currentStage 标准枚举」），它紧跟「分镜编写」之后、不属于线性内容路径，
    因此单列在 POST_EPISODE_STAGES，使本文件仍是「系统所有阶段」的完整权威来源。

用法：
  from lib.workflow_paths import PATH_SEQUENCES, get_next_stage, POST_EPISODE_STAGES
"""

from typing import Dict, List, Optional


PATH_SEQUENCES: Dict[str, List[str]] = {
    "路径一": ["小说分析", "道具与金手指提取", "集纲生成", "剧本生成", "导演分析", "视觉风格选择", "服化道设计", "分镜编写"],
    "路径二": ["脑洞生成", "道具与金手指提取", "集纲生成", "剧本生成", "导演分析", "视觉风格选择", "服化道设计", "分镜编写"],
    "路径三": ["导演分析", "视觉风格选择", "服化道设计", "分镜编写"],
}

# 所有可能出现的线性内容阶段（去重、仅用于显示/遍历，不隐含执行顺序）
ALL_STAGES: List[str] = [
    "小说分析",
    "脑洞生成",
    "道具与金手指提取",
    "集纲生成",
    "剧本生成",
    "导演分析",
    "视觉风格选择",
    "服化道设计",
    "分镜编写",
]

# 集末收尾型阶段：每集「分镜编写」完成后执行，不属于线性内容路径，
# 故不进 PATH_SEQUENCES（保持「分镜编写」为内容终点），单列于此供状态机/校验完整识别。
# 详见 AXIS-workflow-stages.md「阶段十一：集间交接」。
POST_EPISODE_STAGES: List[str] = [
    "集间交接",
]


def get_next_stage(workflow_path: str, completed_stage: str) -> Optional[str]:
    """根据工作流路径和已完成阶段，返回下一个阶段名；末尾返回 None。"""
    seq = PATH_SEQUENCES.get(workflow_path)
    if not seq:
        return None
    try:
        idx = seq.index(completed_stage)
    except ValueError:
        return None
    if idx + 1 < len(seq):
        return seq[idx + 1]
    return None
