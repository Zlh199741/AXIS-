"""
提示词构建模块
构建 Seedance 2.0、角色设定、场景设定的提示词。
"""

from typing import List, Dict


class SeedancePromptBuilder:
    """Seedance 2.0 动态提示词构建器"""

    def build(self, scene: str, action: str, duration: int) -> str:
        return f"{scene}，{action}。时长：{duration}秒。1.视频画面禁止出现任何字幕、文字、标题或水印；2.视频不要有背景音乐，仅保留人声和动作音效；3.禁止出现任何文字气泡、对话气泡、聊天气泡或漫画式对白框。"

    def add_camera_movement(self, base: str, movement: str,
                            from_point: str, to_point: str) -> str:
        return f"{base}，镜头{movement}，从{from_point}到{to_point}。"

    def add_lighting(self, base: str, source: str, color: str, effect: str) -> str:
        return f"{base}，光源来自{source}，{color}光，{effect}。"

    def add_audio(self, base: str, bgm: str, sfx: str) -> str:
        return f"{base}，背景音乐：{bgm}，音效：{sfx}。"


class CharacterPromptBuilder:
    """角色设定提示词构建器"""

    def build(self, name: str, description: str, layout: str = "standard") -> str:
        if layout == "enhanced":
            layout_str = "8视图布局（正面/背面/左右侧面/特写×4）"
        else:
            layout_str = "标准布局（特写+三视图）"
        return (
            f"角色：{name}。"
            f"描述：{description}。"
            f"布局：{layout_str}。"
            "纯白背景隔离，PBR材质渲染，T0级画质。"
        )

    def add_material_details(self, base: str, materials: List[Dict]) -> str:
        detail_parts = []
        for m in materials:
            detail_parts.append(f"{m['name']}（{m['properties']}）")
        return base + "，材质细节：" + "、".join(detail_parts) + "。"


class ScenePromptBuilder:
    """场景设定提示词构建器"""

    def build_grid(self, scenes: List[str], size: str) -> str:
        rows, cols = (int(x) for x in size.lower().split("x"))
        display = f"{rows}×{cols}"
        preview = "、".join(scenes[:rows * cols])
        return f"{display}宫格场景图，包含：{preview}。"

    def add_lighting_specification(self, base: str, main_light: str,
                                   auxiliary: str, logic: str) -> str:
        return (
            f"{base}，主光源：{main_light}，"
            f"辅助光：{auxiliary}，"
            f"光影逻辑：{logic}。"
        )
