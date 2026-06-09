#!/usr/bin/env python3
"""
跨产物语义一致性校验工具单元测试 (semantic-consistency-validator.py)
覆盖：P块解析 / 动作提取 / 情绪提取 / 一致性比对
"""

import unittest
import sys
import importlib.util
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

TOOLS_DIR = Path(__file__).parent.parent.parent / "tools" / "validators"


def _load_module(name, filepath):
    spec = importlib.util.spec_from_file_location(name, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


scv = _load_module("semantic_consistency_validator", TOOLS_DIR / "semantic-consistency-validator.py")


# ============================================================
# 导演 P 块解析
# ============================================================

class TestParseDirectorPBlocks(unittest.TestCase):

    def test_basic_p_extraction(self):
        content = """\
## P01 — 蛆虫的日常
时长：15s
导演阐述内容...

## P02 — 觉醒
时长：10s
更多内容...
"""
        blocks = scv.parse_director_p_blocks(content)
        self.assertIn("P01", blocks)
        self.assertIn("P02", blocks)
        self.assertEqual(blocks["P01"]["title"], "蛆虫的日常")
        self.assertEqual(blocks["P01"]["duration"], "15s")

    def test_triple_hash_p(self):
        content = "### P03 - 逃亡\n时长：8s\n内容\n"
        blocks = scv.parse_director_p_blocks(content)
        self.assertIn("P03", blocks)

    def test_empty_returns_empty(self):
        blocks = scv.parse_director_p_blocks("")
        self.assertEqual(len(blocks), 0)

    def test_no_duration(self):
        content = "## P01 — 开场\n没有时长标注的内容\n"
        blocks = scv.parse_director_p_blocks(content)
        self.assertEqual(blocks["P01"]["duration"], "")


# ============================================================
# 视频 P 块解析
# ============================================================

class TestParseVideoPBlocks(unittest.TestCase):

    def test_basic_extraction(self):
        content = """\
## P01 开场 时长：15s
🎬 Seedance提示词
镜头缓缓推进...
@主体 洛小阳
参考@图片1

## P02 觉醒 时长：10s
另一段内容
"""
        blocks = scv.parse_video_p_blocks(content)
        self.assertIn("P01", blocks)
        self.assertIn("P02", blocks)
        self.assertEqual(blocks["P01"]["duration"], "15s")
        self.assertIn("洛小阳", blocks["P01"]["characters_referenced"])
        self.assertIn("图片1", blocks["P01"]["scene_references"])

    def test_sub_p_merging(self):
        """P02-2 应归并到 P02"""
        content = """\
## P02 场景A 时长：10s
第一段

## P02-2 场景A延续 时长：5s
第二段
"""
        blocks = scv.parse_video_p_blocks(content)
        self.assertIn("P02", blocks)
        self.assertIn("第二段", blocks["P02"]["full_text"])


# ============================================================
# 动作 / 情绪提取
# ============================================================

class TestExtractActionVerbs(unittest.TestCase):

    def test_extract_actions(self):
        text = "洛小阳扑向敌人，踹开大门，然后蹲在角落颤抖。"
        actions = scv.extract_action_verbs(text)
        self.assertIn("扑向", actions)
        self.assertIn("踹", actions)
        self.assertIn("蹲", actions)
        self.assertIn("颤抖", actions)

    def test_no_actions(self):
        text = "今天天气真好。"
        actions = scv.extract_action_verbs(text)
        self.assertEqual(len(actions), 0)

    def test_deduplicated(self):
        text = "他跑了又跑，跑得很快。"
        actions = scv.extract_action_verbs(text)
        self.assertEqual(actions.count("跑"), 1)


class TestExtractEmotionKeywords(unittest.TestCase):

    def test_extract_emotions(self):
        text = "她感到绝望和恐惧，内心充满悲伤。"
        emotions = scv.extract_emotion_keywords(text)
        self.assertIn("绝望", emotions)
        self.assertIn("恐惧", emotions)
        self.assertIn("悲伤", emotions)

    def test_no_emotions(self):
        text = "他走进了房间。"
        emotions = scv.extract_emotion_keywords(text)
        self.assertEqual(len(emotions), 0)


# ============================================================
# 角色名解析
# ============================================================

class TestParseCharacterNamesFromPrompts(unittest.TestCase):

    def test_ep_label_format(self):
        content = """\
## [ep01][character][新增] 洛小阳
提示词内容A
提示词内容B

## [ep01][character][新增] 崔云秀
另一段提示词
"""
        chars = scv.parse_character_names_from_prompts(content)
        self.assertIn("洛小阳", chars)
        self.assertIn("崔云秀", chars)

    def test_numbered_format(self):
        content = """\
## 1. 洛小阳（男主角）
内容

## 2. 江辰（配角）
内容
"""
        chars = scv.parse_character_names_from_prompts(content)
        self.assertIn("洛小阳", chars)
        self.assertIn("江辰", chars)


# ============================================================
# 一致性检查引擎
# ============================================================

class TestCheckDirectorVsVideo(unittest.TestCase):

    def test_missing_p_detected(self):
        dir_blocks = {
            "P01": {"full_text": "导演内容", "duration": "15s"},
            "P02": {"full_text": "导演内容2", "duration": "10s"},
        }
        vid_blocks = {
            "P01": {"full_text": "视频内容", "duration": "15s"},
        }
        issues = scv.check_director_vs_video(dir_blocks, vid_blocks)
        critical = [i for i in issues if i.severity == "critical"]
        self.assertTrue(len(critical) > 0)
        self.assertTrue(any("P02" in i.description for i in critical))

    def test_duration_mismatch(self):
        dir_blocks = {
            "P01": {"full_text": "内容", "duration": "15s"},
        }
        vid_blocks = {
            "P01": {"full_text": "内容", "duration": "10s"},
        }
        issues = scv.check_director_vs_video(dir_blocks, vid_blocks)
        warnings = [i for i in issues if i.severity == "warning"]
        self.assertTrue(any("时长" in i.description for i in warnings))

    def test_no_issues_when_matched(self):
        dir_blocks = {
            "P01": {"full_text": "洛小阳蹲在角落", "duration": "15s"},
        }
        vid_blocks = {
            "P01": {"full_text": "洛小阳蹲在角落颤抖", "duration": "15s"},
        }
        issues = scv.check_director_vs_video(dir_blocks, vid_blocks)
        critical = [i for i in issues if i.severity == "critical"]
        self.assertEqual(len(critical), 0)


if __name__ == "__main__":
    unittest.main()
