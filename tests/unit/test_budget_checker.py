#!/usr/bin/env python3
"""
预算检查模块单元测试
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.budget_checker import BudgetChecker, BudgetLimit


class TestBudgetChecker(unittest.TestCase):
    """预算检查器测试"""

    def setUp(self):
        self.checker = BudgetChecker()

    def test_check_image_references(self):
        """测试图片引用检查"""
        prompt = "使用 @图片1 @图片2 @图片3"
        result = self.checker.check(prompt)
        self.assertTrue(result["pass"])

        prompt = "使用 " + " ".join([f"@图片{i}" for i in range(15)])
        result = self.checker.check(prompt)
        self.assertFalse(result["pass"])
        self.assertIn("图片", result["reason"])

    def test_check_video_references(self):
        """测试视频引用检查"""
        prompt = "使用 @视频1 @视频2 @视频3"
        result = self.checker.check(prompt)
        self.assertTrue(result["pass"])

        prompt = "使用 " + " ".join([f"@视频{i}" for i in range(5)])
        result = self.checker.check(prompt)
        self.assertFalse(result["pass"])
        self.assertIn("视频", result["reason"])

    def test_check_audio_references(self):
        """测试音频引用检查"""
        prompt = "使用 @音频1 @音频2"
        result = self.checker.check(prompt)
        self.assertTrue(result["pass"])

    def test_check_total_references(self):
        """测试总引用数检查（9+3+3=15 > 12）"""
        refs = [f"@图片{i}" for i in range(9)]
        refs += [f"@视频{i}" for i in range(3)]
        refs += [f"@音频{i}" for i in range(4)]
        prompt = "使用 " + " ".join(refs)
        result = self.checker.check(prompt)
        self.assertFalse(result["pass"])

    def test_calculate_budget(self):
        """测试预算计算"""
        prompt = "@图片1 @图片2 @视频1 @音频1"
        budget = self.checker.calculate_budget(prompt)
        self.assertEqual(budget["images"], 2)
        self.assertEqual(budget["videos"], 1)
        self.assertEqual(budget["audios"], 1)
        self.assertEqual(budget["total"], 4)


class TestBudgetLimit(unittest.TestCase):
    """预算限制测试"""

    def test_default_limits(self):
        """测试默认限制"""
        limits = BudgetLimit()
        self.assertEqual(limits.max_images, 9)
        self.assertEqual(limits.max_videos, 3)
        self.assertEqual(limits.max_audios, 3)
        self.assertEqual(limits.max_total, 12)

    def test_custom_limits(self):
        """测试自定义限制"""
        limits = BudgetLimit(max_images=5, max_videos=2, max_audios=2, max_total=8)
        self.assertEqual(limits.max_images, 5)
        self.assertEqual(limits.max_total, 8)


if __name__ == "__main__":
    unittest.main()
