#!/usr/bin/env python3
"""
运行所有测试
用法：python tests/run_all.py
"""

import unittest
import sys
from pathlib import Path

# 确保项目根目录在 sys.path 中
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

# 自动发现并运行所有测试
loader = unittest.TestLoader()
suite = unittest.TestSuite()

unit_dir = ROOT / "tests" / "unit"
unit_suite = loader.discover(str(unit_dir), pattern="test_*.py")
suite.addTests(unit_suite)

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
sys.exit(0 if result.wasSuccessful() else 1)
