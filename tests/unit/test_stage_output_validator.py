#!/usr/bin/env python3
"""
产物结构校验工具单元测试 (stage-output-validator.py)
覆盖：validate_file / STAGE_SCHEMAS / get_episode_prompt_paths
"""

import unittest
import sys
import json
import tempfile
import shutil
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# 直接导入被测模块中的核心函数和数据结构
import importlib.util

TOOLS_DIR = Path(__file__).parent.parent.parent / "tools" / "validators"

def _load_module(name, filepath):
    spec = importlib.util.spec_from_file_location(name, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

sov = _load_module("stage_output_validator", TOOLS_DIR / "stage-output-validator.py")


class TestValidateFileExists(unittest.TestCase):
    """文件存在性检查"""

    def test_missing_file_returns_fail(self):
        schema = {"display_name": "测试", "required_sections": [], "required_per_p": []}
        result = sov.validate_file(Path("/nonexistent/file.md"), schema, "ep01")
        self.assertFalse(result.pass_result)
        self.assertFalse(result.exists)
        self.assertTrue(any("不存在" in i["description"] for i in result.issues))

    def test_empty_file_returns_fail(self):
        with tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False, encoding="utf-8") as f:
            f.write("short")
            tmp = Path(f.name)
        try:
            schema = {"display_name": "测试", "required_sections": [], "required_per_p": []}
            result = sov.validate_file(tmp, schema, "ep01")
            self.assertFalse(result.pass_result)
            self.assertTrue(any("过少" in i["description"] for i in result.issues))
        finally:
            tmp.unlink()


class TestValidateRequiredSections(unittest.TestCase):
    """必需章节检查"""

    def _write_tmp(self, content):
        f = tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False, encoding="utf-8")
        f.write(content)
        f.close()
        return Path(f.name)

    def test_all_sections_present(self):
        content = "x" * 60 + "\n# 故事梗概\n# 人物清单\n# 场景清单\n"
        tmp = self._write_tmp(content)
        try:
            schema = {
                "display_name": "测试",
                "required_sections": [
                    {"name": "故事梗概", "patterns": [r"故事梗概"], "severity": "critical"},
                    {"name": "人物清单", "patterns": [r"人物清单"], "severity": "critical"},
                    {"name": "场景清单", "patterns": [r"场景清单"], "severity": "critical"},
                ],
                "required_per_p": [],
            }
            result = sov.validate_file(tmp, schema, "ep01")
            self.assertTrue(result.pass_result)
        finally:
            tmp.unlink()

    def test_missing_critical_section_fails(self):
        content = "x" * 60 + "\n# 故事梗概\n# 人物清单\n"
        tmp = self._write_tmp(content)
        try:
            schema = {
                "display_name": "测试",
                "required_sections": [
                    {"name": "故事梗概", "patterns": [r"故事梗概"], "severity": "critical"},
                    {"name": "场景清单", "patterns": [r"场景清单"], "severity": "critical"},
                ],
                "required_per_p": [],
            }
            result = sov.validate_file(tmp, schema, "ep01")
            self.assertFalse(result.pass_result)
            self.assertTrue(any("场景清单" in i["field"] for i in result.issues))
        finally:
            tmp.unlink()

    def test_missing_warning_section_still_passes(self):
        content = "x" * 60 + "\n# 故事梗概\n"
        tmp = self._write_tmp(content)
        try:
            schema = {
                "display_name": "测试",
                "required_sections": [
                    {"name": "故事梗概", "patterns": [r"故事梗概"], "severity": "critical"},
                    {"name": "光影设计", "patterns": [r"光影"], "severity": "warning"},
                ],
                "required_per_p": [],
            }
            result = sov.validate_file(tmp, schema, "ep01")
            self.assertTrue(result.pass_result)  # warning 不影响 pass
            self.assertTrue(any("光影设计" in i["field"] for i in result.issues))
        finally:
            tmp.unlink()


class TestValidatePerPBlock(unittest.TestCase):
    """P块字段校验"""

    def _write_tmp(self, content):
        f = tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False, encoding="utf-8")
        f.write(content)
        f.close()
        return Path(f.name)

    def test_p_block_field_present(self):
        content = "x" * 60 + "\n## P01 场景一\n时长：15s\n导演阐述内容\n"
        tmp = self._write_tmp(content)
        try:
            schema = {
                "display_name": "测试",
                "required_sections": [],
                "required_per_p": [
                    {"name": "时长标注", "patterns": [r"时长[：:]\s*\d+s"], "severity": "warning"},
                ],
            }
            result = sov.validate_file(tmp, schema, "ep01")
            # P01 有时长，不应报 warning
            time_issues = [i for i in result.issues if "时长" in i.get("field", "")]
            self.assertEqual(len(time_issues), 0)
        finally:
            tmp.unlink()

    def test_p_block_missing_critical_field(self):
        content = "x" * 60 + "\n## P01 场景一\n这段内容缺少必要字段\n"
        tmp = self._write_tmp(content)
        try:
            schema = {
                "display_name": "测试",
                "required_sections": [],
                "required_per_p": [
                    {"name": "导演阐述内容", "patterns": [r"导演阐述"], "severity": "critical"},
                ],
            }
            result = sov.validate_file(tmp, schema, "ep01")
            self.assertFalse(result.pass_result)
        finally:
            tmp.unlink()


class TestStageSchemas(unittest.TestCase):
    """验证 STAGE_SCHEMAS 结构完整性"""

    def test_all_stages_have_required_keys(self):
        for stage_name, schema in sov.STAGE_SCHEMAS.items():
            with self.subTest(stage=stage_name):
                self.assertIn("file", schema)
                self.assertIn("display_name", schema)
                self.assertIn("required_sections", schema)
                self.assertIn("required_per_p", schema)

    def test_director_schema_has_critical_sections(self):
        director = sov.STAGE_SCHEMAS["director"]
        critical_names = {s["name"] for s in director["required_sections"] if s["severity"] == "critical"}
        self.assertIn("人物清单", critical_names)
        self.assertIn("场景清单", critical_names)
        self.assertIn("导演讲戏本", critical_names)

    def test_storyboard_schema_checks_extra_files(self):
        sb = sov.STAGE_SCHEMAS["storyboard"]
        extra_names = {e["display_name"] for e in sb.get("extra_files", [])}
        self.assertIn("文字分镜稿（03-text-storyboard.md）", extra_names)


class TestGetEpisodePromptPaths(unittest.TestCase):
    """测试集数提示词路径读取"""

    def test_returns_defaults_when_no_gate_file(self):
        result = sov.get_episode_prompt_paths("ep01", Path("/nonexistent"))
        self.assertIn("characterPrompts", result)
        self.assertIn("scenePrompts", result)

    def test_reads_from_gate_file(self):
        tmpdir = Path(tempfile.mkdtemp())
        try:
            gate = {
                "episodeProgress": {
                    "ep01": {
                        "_characterPrompts": "custom/char.md",
                        "_scenePrompts": "custom/scene.md",
                    }
                }
            }
            (tmpdir / ".stage-gate.json").write_text(json.dumps(gate), encoding="utf-8")
            result = sov.get_episode_prompt_paths("ep01", tmpdir)
            self.assertEqual(result["characterPrompts"], "custom/char.md")
            self.assertEqual(result["scenePrompts"], "custom/scene.md")
        finally:
            shutil.rmtree(tmpdir)


if __name__ == "__main__":
    unittest.main()
