#!/usr/bin/env python3
"""
剧情忠实度校验工具单元测试
"""

import unittest
import sys
import importlib.util
from pathlib import Path

_project_root = Path(__file__).parent.parent.parent
_spec = importlib.util.spec_from_file_location(
    "plot_fidelity_checker",
    _project_root / "tools" / "validators" / "plot-fidelity-checker.py",
)
pfc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pfc)


class TestSplitIntoChapters(unittest.TestCase):
    """章节拆分测试"""

    def test_normal_chapters(self):
        text = "第1章\n内容一\n第2章\n内容二\n第3章\n内容三"
        chapters = pfc.split_into_chapters(text)
        self.assertEqual(len(chapters), 3)
        self.assertIn("第1章", chapters)
        self.assertIn("第2章", chapters)
        self.assertIn("第3章", chapters)

    def test_no_chapters(self):
        text = "这是一段没有章节标记的文本，直接作为全文处理。"
        chapters = pfc.split_into_chapters(text)
        self.assertEqual(len(chapters), 1)
        self.assertIn("全文", chapters)

    def test_chapter_content_boundaries(self):
        text = "第1章\nAAA\nBBB\n第2章\nCCC\nDDD"
        chapters = pfc.split_into_chapters(text)
        self.assertIn("AAA", chapters["第1章"])
        self.assertIn("BBB", chapters["第1章"])
        self.assertIn("CCC", chapters["第2章"])
        self.assertNotIn("CCC", chapters["第1章"])


class TestScoreParagraphImportance(unittest.TestCase):
    """段落重要性评分测试"""

    def test_high_intensity_paragraph(self):
        para = "洛小阳吓得尖叫起来，拼命往外跑，猛然发现真相竟然如此惊人！"
        score = pfc.score_paragraph_importance(para)
        self.assertGreater(score, 0.2)

    def test_low_intensity_paragraph(self):
        para = "天气很好，阳光明媚。"
        score = pfc.score_paragraph_importance(para)
        self.assertLess(score, 0.1)

    def test_dialogue_rich_paragraph(self):
        para = '\u201c你是谁？\u201d他问道。\u201c我是陈先生。\u201d对方回答。\u201c你来做什么？\u201d他又问。'
        score = pfc.score_paragraph_importance(para)
        self.assertGreater(score, 0.05)


class TestClassifyEventCategory(unittest.TestCase):
    """事件分类测试"""

    def test_turning_point(self):
        para = "没想到他居然是赶尸匠，这个发现让所有人震惊。原来真相是这样。"
        category = pfc.classify_event_category(para)
        self.assertIn(category, ("turning_point", "revelation"))

    def test_climax(self):
        para = "他尖叫着拼命往前冲，猛然跳起来，瞬间爆发出惊人的力量。"
        category = pfc.classify_event_category(para)
        self.assertEqual(category, "climax")

    def test_setup(self):
        para = "这是一段普普通通的描写，没有什么特别的事件发生。"
        category = pfc.classify_event_category(para)
        self.assertEqual(category, "setup")


class TestExtractKeywordsFromParagraph(unittest.TestCase):
    """关键词提取测试"""

    def test_extract_special_terms(self):
        para = "万鼠拜坟的异象爆发了，五体投地诅咒开始生效，陈先生拿出阴鞋。"
        keywords = pfc.extract_keywords_from_paragraph(para)
        found = " ".join(keywords)
        self.assertTrue(
            any(kw in found for kw in ["万鼠拜坟", "五体投地", "阴鞋"]),
            f"Expected special terms in keywords, got: {keywords}"
        )

    def test_extract_dialogue(self):
        para = '他说"万鼠拜坟，有死无生"，然后转身就跑。'
        keywords = pfc.extract_keywords_from_paragraph(para)
        found = " ".join(keywords)
        self.assertTrue(
            "万鼠拜坟" in found or "有死无生" in found,
            f"Expected dialogue keywords, got: {keywords}"
        )


class TestComputeKeywordOverlap(unittest.TestCase):
    """关键词覆盖率计算测试"""

    def test_full_overlap(self):
        event = pfc.NovelEvent(
            event_id="E01", summary="test", category="setup",
            importance="major", chapter="第1章",
            keywords=["万鼠拜坟", "陈先生", "赶尸匠"],
        )
        text = "万鼠拜坟的异象让陈先生震惊，赶尸匠的秘密终于揭开。"
        score = pfc.compute_keyword_overlap(event, text)
        self.assertEqual(score, 1.0)

    def test_partial_overlap(self):
        event = pfc.NovelEvent(
            event_id="E01", summary="test", category="setup",
            importance="major", chapter="第1章",
            keywords=["万鼠拜坟", "陈先生", "张哈子"],
        )
        text = "万鼠拜坟的异象让陈先生震惊。"
        score = pfc.compute_keyword_overlap(event, text)
        self.assertAlmostEqual(score, 2 / 3, places=2)

    def test_no_overlap(self):
        event = pfc.NovelEvent(
            event_id="E01", summary="test", category="setup",
            importance="major", chapter="第1章",
            keywords=["完全不相关的词"],
        )
        text = "这段文本里没有任何匹配的关键词。"
        score = pfc.compute_keyword_overlap(event, text)
        self.assertEqual(score, 0.0)

    def test_empty_keywords(self):
        event = pfc.NovelEvent(
            event_id="E01", summary="test", category="setup",
            importance="major", chapter="第1章",
            keywords=[],
        )
        text = "任何文本"
        score = pfc.compute_keyword_overlap(event, text)
        self.assertEqual(score, 0.0)


class TestCheckEventCoverage(unittest.TestCase):
    """事件覆盖率检查测试"""

    def test_all_covered(self):
        events = [
            pfc.NovelEvent(
                event_id="E01", summary="万鼠拜坟", category="climax",
                importance="critical", chapter="第4章",
                keywords=["万鼠拜坟", "老鼠", "跪拜"],
                characters=["陈先生"],
            ),
        ]
        text = "万鼠拜坟——成千上万只老鼠朝坟地跪拜。陈先生大喊快跑。"
        results, rate = pfc.check_event_coverage(events, text, "outline")
        self.assertTrue(results[0].covered)
        self.assertGreater(rate, 0.5)

    def test_none_covered(self):
        events = [
            pfc.NovelEvent(
                event_id="E01", summary="完全不存在的事件", category="setup",
                importance="minor", chapter="第1章",
                keywords=["完全不存在的关键词ABC"],
            ),
        ]
        text = "这是一段完全无关的文本内容。"
        results, rate = pfc.check_event_coverage(events, text, "outline")
        self.assertFalse(results[0].covered)
        self.assertEqual(rate, 0.0)


class TestExtractEventsFromAnalysis(unittest.TestCase):
    """融合报告事件提取测试"""

    def test_extract_arrow_chain(self):
        text = """
## 四、事件线结构

### 核心主线
```
偷天换日活埋 → 死后异象 → 万鼠拜坟 → 五体投地
```

---

## 五、ABC爽点分析

### 峰值章节
1. **万鼠拜坟 + 赶尸匠身份揭示**
"""
        events = pfc.extract_events_from_analysis(text)
        summaries = [e.summary for e in events]
        self.assertTrue(
            any("偷天换日" in s for s in summaries),
            f"Expected '偷天换日' in summaries, got: {summaries}"
        )
        self.assertTrue(
            any("万鼠拜坟" in s for s in summaries),
            f"Expected '万鼠拜坟' in summaries, got: {summaries}"
        )

    def test_no_event_section(self):
        text = "## 一、作品概况\n- 书名：三尸语\n- 总章节：419"
        events = pfc.extract_events_from_analysis(text)
        self.assertEqual(len(events), 0)

    def test_filters_noise(self):
        text = """
## 四、事件线结构

**书名**是一个无关词。**题材**也是。

偷天换日 → 万鼠拜坟

## 五、下一章
"""
        events = pfc.extract_events_from_analysis(text)
        summaries = [e.summary for e in events]
        self.assertFalse(any("书名" in s for s in summaries))
        self.assertFalse(any("题材" in s for s in summaries))


class TestParseOutline(unittest.TestCase):
    """集纲解析测试"""

    def test_parse_episodes(self):
        text = """### 第1集：回魂压棺
内容一
### 第2集：棺中换人
内容二"""
        episodes = pfc.parse_outline(text)
        self.assertEqual(len(episodes), 2)
        self.assertIn("第1集", episodes)
        self.assertIn("第2集", episodes)
        self.assertIn("回魂压棺", episodes["第1集"])


class TestParseScript(unittest.TestCase):
    """剧本解析测试"""

    def test_parse_episodes(self):
        text = """## [第1集] 回魂压棺
场景一内容
## [第2集] 棺中换人
场景二内容"""
        episodes = pfc.parse_script(text)
        self.assertEqual(len(episodes), 2)
        self.assertIn("第1集", episodes)
        self.assertIn("回魂压棺", episodes["第1集"])


class TestPlotFidelityIssueGeneration(unittest.TestCase):
    """忠实度问题生成测试"""

    def test_missing_critical_event(self):
        events = [
            pfc.NovelEvent(
                event_id="E01", summary="关键转折事件", category="turning_point",
                importance="critical", chapter="第1章",
                keywords=["完全不存在的关键词XYZ"],
            ),
        ]
        issues = pfc.check_plot_fidelity(events, "无关内容", "", "")
        self.assertTrue(len(issues) > 0)
        self.assertEqual(issues[0].severity, "critical")
        self.assertEqual(issues[0].category, "missing")

    def test_no_issues_when_covered(self):
        events = [
            pfc.NovelEvent(
                event_id="E01", summary="万鼠拜坟", category="climax",
                importance="critical", chapter="第4章",
                keywords=["万鼠拜坟", "老鼠"],
                characters=["陈先生"],
            ),
        ]
        text = "万鼠拜坟异象爆发，成千上万老鼠涌来。陈先生大喊快跑。"
        issues = pfc.check_plot_fidelity(events, text, text, text)
        critical = [i for i in issues if i.severity == "critical"]
        self.assertEqual(len(critical), 0)


if __name__ == "__main__":
    unittest.main()
