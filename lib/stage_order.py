# -*- coding: utf-8 -*-
"""
AXIS 全阶段列表 — 仅用于显示/遍历
====================================
⚠️ 此列表不隐含执行顺序！
   小说分析（路径一入口）和脑洞生成（路径二入口）是互斥的并行入口。
   需要判断"下一阶段"时，请使用 lib.workflow_paths.get_next_stage()。

用法：
  from lib.stage_order import STAGE_ORDER  # 向后兼容，等价于 ALL_STAGES
"""

from lib.workflow_paths import ALL_STAGES

# 向后兼容：display-only 工具（dashboard / progress reporter）仍可 import STAGE_ORDER
STAGE_ORDER = ALL_STAGES
