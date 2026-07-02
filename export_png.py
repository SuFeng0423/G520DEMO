#!/usr/bin/env python3
"""将 DEOM 原型导出为 640×400 PNG 静态图。"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCREENS = ROOT / "screens"
PNG_DIR = ROOT / "png"

SCREEN_FILES = [
    ("01-login", "01-登录"),
    ("02-work-order-list", "02-选择工单"),
    ("03-work-order-confirm", "03-确认作业"),
    ("04-inspection-preview-on", "04-目视检查-预览开"),
    ("05-inspection-preview-off", "05-目视检查-预览关"),
    ("06-photo-review", "06-照片回看"),
    ("07-upload-match-success", "07-上传留底-匹配成功"),
    ("08-upload-match-fail", "08-上传留底-匹配失败"),
]


def export_with_playwright() -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False

    PNG_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 640, "height": 400})
        for stem, label in SCREEN_FILES:
            html_path = SCREENS / f"{stem}.html"
            out_path = PNG_DIR / f"{label}.png"
            page.goto(html_path.as_uri())
            page.locator(".glasses-screen").screenshot(path=str(out_path))
            print(f"✓ {out_path.name}")
        browser.close()
    return True


def export_with_pillow_fallback() -> None:
    """无 Playwright 时用 Pillow 绘制简化线框图。"""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("请安装 playwright 或 pillow：pip install playwright && playwright install chromium")
        sys.exit(1)

    PNG_DIR.mkdir(parents=True, exist_ok=True)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 16)
        font_sm = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 12)
        font_lg = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 20)
    except OSError:
        font = font_sm = font_lg = ImageFont.load_default()

    screens_meta = {
        "01-登录": ("登录", "工号 / 密码 · 滚轮切换 · 按钮/语音登录"),
        "02-选择工单": ("选择工单 / 作业", "滚轮浏览 · 按钮/语音选中"),
        "03-确认作业": ("确认作业信息", "核对后「开始检查」"),
        "04-目视检查-预览开": ("目视检查 · 预览开", "小窗预览 · 滚轮调位置 · 拍照"),
        "05-目视检查-预览关": ("目视检查 · 预览关", "无预览 · 角标待命 · 拍照"),
        "06-照片回看": ("照片回看", "放大/缩小/移动 · 切换照片"),
        "07-上传留底-匹配成功": ("上传留底 · 匹配成功", "自动匹配 · 确认上传"),
        "08-上传留底-匹配失败": ("上传留底 · 匹配失败", "候选选择 · 语音绑定"),
    }

    for _, label in SCREEN_FILES:
        title, desc = screens_meta[label]
        img = Image.new("RGB", (640, 400), (10, 14, 20))
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, 639, 27], fill=(20, 27, 36))
        draw.rectangle([0, 348, 639, 399], fill=(20, 27, 36))
        draw.line([(0, 27), (639, 27)], fill=(42, 58, 77))
        draw.line([(0, 348), (639, 348)], fill=(42, 58, 77))
        draw.text((16, 6), "目视检查系统", fill=(138, 155, 176), font=font_sm)
        draw.text((16, 40), title, fill=(0, 212, 170), font=font_lg)
        draw.text((16, 72), desc, fill=(138, 155, 176), font=font_sm)
        draw.rectangle([16, 100, 623, 330], outline=(42, 58, 77), width=1)
        draw.text((280, 190), "[ 640×400 原型 ]", fill=(42, 58, 77), font=font)
        draw.text((16, 358), "🎤语音  ⟳滚轮  ●按钮", fill=(138, 155, 176), font=font_sm)
        out = PNG_DIR / f"{label}.png"
        img.save(out)
        print(f"✓ {out.name} (Pillow 简化版)")


def main() -> None:
    if export_with_playwright():
        # 流程总览图
        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page(viewport={"width": 1280, "height": 900})
                page.goto((ROOT / "index.html").as_uri())
                page.wait_for_timeout(500)
                out = PNG_DIR / "00-流程总览.png"
                page.locator(".flow-overview").screenshot(path=str(out))
                print(f"✓ {out.name}")
                browser.close()
        except Exception as exc:
            print(f"流程总览导出跳过: {exc}")
        return

    print("Playwright 不可用，使用 Pillow 简化导出…")
    export_with_pillow_fallback()


if __name__ == "__main__":
    main()
