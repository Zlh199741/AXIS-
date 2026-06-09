"""
预算检查模块
检查单条提示词的素材引用是否超出平台限制：
  图片 ≤ 9, 视频 ≤ 3, 音频 ≤ 3, 总文件 ≤ 12
"""

import re


class BudgetLimit:
    """平台素材引用上限配置"""

    def __init__(self, max_images: int = 9, max_videos: int = 3,
                 max_audios: int = 3, max_total: int = 12):
        self.max_images = max_images
        self.max_videos = max_videos
        self.max_audios = max_audios
        self.max_total = max_total


class BudgetChecker:
    """单条提示词预算检查器"""

    def __init__(self, limits: BudgetLimit = None):
        self.limits = limits or BudgetLimit()

    def calculate_budget(self, prompt: str) -> dict:
        images = len(re.findall(r"@图片\d+", prompt))
        videos = len(re.findall(r"@视频\d+", prompt))
        audios = len(re.findall(r"@音频\d+", prompt))
        return {
            "images": images,
            "videos": videos,
            "audios": audios,
            "total": images + videos + audios,
        }

    def check(self, prompt: str) -> dict:
        budget = self.calculate_budget(prompt)
        lim = self.limits

        if budget["images"] > lim.max_images:
            return {"pass": False, "reason": f"图片引用超限：{budget['images']} > {lim.max_images}", "budget": budget}
        if budget["videos"] > lim.max_videos:
            return {"pass": False, "reason": f"视频引用超限：{budget['videos']} > {lim.max_videos}", "budget": budget}
        if budget["audios"] > lim.max_audios:
            return {"pass": False, "reason": f"音频引用超限：{budget['audios']} > {lim.max_audios}", "budget": budget}
        if budget["total"] > lim.max_total:
            return {"pass": False, "reason": f"总引用超限：{budget['total']} > {lim.max_total}", "budget": budget}

        return {"pass": True, "reason": "", "budget": budget}
