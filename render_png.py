#!/usr/bin/env python3
"""将 DEOM 原型导出为 640×400 高清 PNG（2× 超采样抗锯齿）。"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
PNG_DIR = ROOT / "png"

SCREEN_W, SCREEN_H = 640, 400
SCALE = 2  # 2× 超采样，导出后缩放至目标尺寸，字体更清晰

# 色板
BG = (10, 14, 20)
PANEL = (20, 27, 36)
BORDER = (42, 58, 77)
ACCENT = (0, 212, 170)
TEXT = (232, 238, 244)
DIM = (138, 155, 176)
VOICE = (110, 181, 255)
WHEEL = (201, 160, 255)
BTN = (255, 159, 67)
WARN = (255, 176, 32)
DANGER = (255, 92, 92)

FOOTER_TOP = 348
INTERACTION_Y = 356


def _s(v: int | float) -> int:
    return int(v * SCALE)


def load_fonts():
    paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for p in paths:
        try:
            return (
                ImageFont.truetype(p, _s(18)),
                ImageFont.truetype(p, _s(14)),
                ImageFont.truetype(p, _s(12)),
                ImageFont.truetype(p, _s(11)),
                ImageFont.truetype(p, _s(10)),
                ImageFont.truetype(p, _s(9)),
                ImageFont.truetype(p, _s(42)),
            )
        except OSError:
            continue
    d = ImageFont.load_default()
    return d, d, d, d, d, d, d


F_LG, F_MD, F_SM, F_BODY, F_XS, F_XXS, F_HUGE = load_fonts()


def save_hd(img: Image.Image, path: Path) -> None:
    hd = img.resize((SCREEN_W, SCREEN_H), Image.Resampling.LANCZOS)
    hd.save(path, optimize=True)


def new_screen():
    w, h = _s(SCREEN_W), _s(SCREEN_H)
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, w - 1, _s(27)], fill=PANEL)
    draw.line([(0, _s(27)), (w - 1, _s(27))], fill=BORDER)
    draw.rectangle([0, _s(FOOTER_TOP), w - 1, h - 1], fill=PANEL)
    draw.line([(0, _s(FOOTER_TOP)), (w - 1, _s(FOOTER_TOP))], fill=BORDER)
    return img, draw


def draw_status(draw, left: str, right: str, dot_color=ACCENT):
    draw.ellipse([_s(10), _s(10), _s(16), _s(16)], fill=dot_color)
    draw.text((_s(20), _s(7)), left, fill=DIM, font=F_XS)
    tw = draw.textlength(right, font=F_XS)
    draw.text((_s(SCREEN_W - 10) - tw, _s(7)), right, fill=DIM, font=F_XS)


def draw_title(draw, title: str, subtitle: str = "", color=ACCENT):
    draw.text((_s(16), _s(36)), title, fill=color, font=F_LG)
    if subtitle:
        draw.text((_s(16), _s(58)), subtitle, fill=DIM, font=F_XS)


def draw_interaction_bar(draw, tags: list[tuple[str, tuple]]):
    x, y = _s(8), _s(INTERACTION_Y)
    for text, color in tags:
        tw = draw.textlength(text, font=F_XXS) + _s(12)
        if x + tw > _s(632):
            x, y = _s(8), y + _s(18)
        draw.rounded_rectangle([x, y, x + tw, y + _s(16)], radius=_s(2), outline=color)
        draw.text((x + _s(6), y + _s(2)), text, fill=color, font=F_XXS)
        x += tw + _s(6)


def draw_field(draw, y: int, label: str, value: str, focused: bool = False):
    draw.text((_s(16), _s(y)), label, fill=DIM, font=F_XS)
    color = ACCENT if focused else BORDER
    draw.rounded_rectangle([_s(16), _s(y + 14), _s(624), _s(y + 46)], radius=_s(2), outline=color)
    draw.text((_s(24), _s(y + 22)), value, fill=TEXT, font=F_MD)


def draw_list_item(draw, y: int, title: str, meta: str, badge: str, selected: bool):
    color = ACCENT if selected else BORDER
    bg = (0, 40, 32) if selected else PANEL
    draw.rounded_rectangle([_s(16), _s(y), _s(624), _s(y + 52)], radius=_s(2), outline=color, fill=bg)
    draw.text((_s(24), _s(y + 8)), title, fill=TEXT, font=F_SM)
    draw.text((_s(24), _s(y + 28)), meta, fill=DIM, font=F_XXS)
    bw = draw.textlength(badge, font=F_XXS) + _s(10)
    draw.rounded_rectangle([_s(616) - bw, _s(y + 16), _s(616), _s(y + 34)], radius=_s(2), outline=color)
    draw.text((_s(616) - bw + _s(5), _s(y + 18)), badge, fill=color, font=F_XXS)


def draw_detail_card(draw, rows: list[tuple[str, str, bool]]):
    draw.rounded_rectangle([_s(16), _s(72), _s(624), _s(248)], radius=_s(2), outline=BORDER, fill=PANEL)
    y = 82
    for label, value, hl in rows:
        draw.text((_s(28), _s(y)), label, fill=DIM, font=F_XS)
        draw.text((_s(100), _s(y)), value, fill=ACCENT if hl else TEXT, font=F_SM)
        y += 24


def draw_preview(draw, x: int, y: int, w: int, h: int):
    draw.rounded_rectangle([_s(x), _s(y), _s(x + w), _s(y + h)], radius=_s(2), outline=ACCENT, width=_s(2))
    draw.rectangle([_s(x + 2), _s(y + 2), _s(x + w - 2), _s(y + h - 2)], fill=(26, 37, 48))
    draw.text((_s(x + 6), _s(y + 4)), "LIVE", fill=ACCENT, font=F_XXS)
    draw.text((_s(x + w // 2 - 30), _s(y + h // 2 - 6)), "镜头预览", fill=DIM, font=F_XS)


# ── 标准版导出 ──

def export_login():
    img, d = new_screen()
    draw_status(d, "目视检查系统 v1.0", "09:32 · 在线")
    draw_title(d, "登录", "滚轮切换字段 · 按钮确认 · 可说「登录」")
    draw_field(d, 80, "工号", "QC00128", focused=True)
    draw_field(d, 138, "密码", "********")
    d.text((_s(200), _s(200)), "▲▼ 滚轮切换输入框", fill=DIM, font=F_XS)
    draw_interaction_bar(d, [
        ("滚轮: 切换工号/密码", WHEEL),
        ("按钮: 确认登录", BTN),
        ("语音: 登录", VOICE),
    ])
    save_hd(img, PNG_DIR / "01-登录.png")


def export_work_list():
    img, d = new_screen()
    draw_status(d, "QC00128 · 质检员", "待作业 3 单")
    draw_title(d, "选择工单 / 作业", "滚轮浏览 · 按钮选中 · 可说「打开第 N 个」")
    draw_list_item(d, 76, "SH20250702001 · 到货目视检查", "A区收货 · 12 项待检 · 今天 09:00", "当前", True)
    draw_list_item(d, 134, "SH20250701998 · 外观抽检", "B区收货 · 5 项待检 · 今天 08:30", "待检", False)
    draw_list_item(d, 192, "SH20250701995 · 标签核对", "C区收货 · 8 项待检 · 昨天", "待检", False)
    d.text((_s(260), _s(258)), "▲ 滚轮向上  ▼ 滚轮向下", fill=DIM, font=F_XS)
    draw_interaction_bar(d, [
        ("滚轮: 上下选择工单", WHEEL),
        ("按钮: 确认进入", BTN),
        ("语音: 打开第一个", VOICE),
    ])
    save_hd(img, PNG_DIR / "02-选择工单.png")


def export_confirm():
    img, d = new_screen()
    draw_status(d, "工单 SH20250702001", "目视检查")
    draw_title(d, "确认作业信息", "核对后进入目视检查流程")
    draw_detail_card(d, [
        ("收货单号", "SH20250702001", True),
        ("作业类型", "到货目视检查", False),
        ("作业区域", "A区收货台 · 3号位", False),
        ("待检项", "12 项(外观/标签/破损)", False),
        ("供应商", "华东零部件有限公司", False),
    ])
    d.text((_s(180), _s(268)), "纯拍照留底 · 无 OCR/计数/翻译", fill=ACCENT, font=F_XS)
    draw_interaction_bar(d, [
        ("滚轮: 返回/确认", WHEEL),
        ("按钮: 开始检查", BTN),
        ("语音: 开始检查", VOICE),
    ])
    save_hd(img, PNG_DIR / "03-确认作业.png")


def export_preview_on():
    img, d = new_screen()
    draw_status(d, "SH20250702001 · 已拍 0 张", "预览: 开 · 全彩")
    d.text((_s(16), _s(36)), "拍照留底 · 纯拍照(无AI)", fill=ACCENT, font=F_MD)
    draw_preview(d, 474, 40, 150, 112)
    d.rounded_rectangle([_s(16), _s(168), _s(624), _s(330)], radius=_s(2), outline=BORDER)
    d.text((_s(220), _s(230)), "仅采集全彩图像", fill=DIM, font=F_SM)
    d.text((_s(200), _s(252)), "无识别框 · 无置信度", fill=DIM, font=F_XS)
    draw_interaction_bar(d, [
        ("滚轮: 调整预览位置", WHEEL),
        ("短按: 拍照  长按: 关预览", BTN),
        ("语音: 拍照/关闭预览", VOICE),
    ])
    save_hd(img, PNG_DIR / "04-目视检查-预览开.png")


def export_preview_off():
    img, d = new_screen()
    draw_status(d, "SH20250702001 · 已拍 2 张", "预览: 关")
    d.text((_s(16), _s(36)), "目视检查 · 无预览模式", fill=ACCENT, font=F_MD)
    d.ellipse([_s(596), _s(44), _s(620), _s(68)], outline=WARN, width=_s(2))
    d.text((_s(602), _s(48)), "CAM", fill=WARN, font=F_XXS)
    d.text((_s(220), _s(180)), "预览已关闭，视野无遮挡", fill=DIM, font=F_SM)
    d.text((_s(200), _s(205)), "短按按钮 / 说「拍照」即可拍摄", fill=DIM, font=F_XS)
    d.text((_s(190), _s(228)), "滚轮上 / 说「打开预览」恢复预览窗", fill=DIM, font=F_XS)
    draw_interaction_bar(d, [
        ("滚轮上: 开预览  下: 看照片", WHEEL),
        ("短按: 拍照", BTN),
        ("语音: 拍照/打开预览", VOICE),
    ])
    save_hd(img, PNG_DIR / "05-目视检查-预览关.png")


def export_review():
    img, d = new_screen()
    draw_status(d, "照片检视", "SH20250702001")
    d.text((_s(16), _s(36)), "已拍照片 · 放大/移动检查", fill=ACCENT, font=F_MD)
    d.rounded_rectangle([_s(16), _s(58), _s(624), _s(330)], radius=_s(2), outline=BORDER, fill=(13, 18, 24))
    d.rounded_rectangle([_s(48), _s(78), _s(592), _s(300)], radius=_s(2), outline=BORDER, fill=PANEL)
    d.text((_s(240), _s(175)), "[ 外观检查照片 #2 ]", fill=DIM, font=F_SM)
    d.text((_s(520), _s(66)), "2 / 5", fill=DIM, font=F_XS)
    d.text((_s(200), _s(310)), "滚轮: 放大缩小 · 长按: 拖动", fill=DIM, font=F_XXS)
    draw_interaction_bar(d, [
        ("滚轮: 放大缩小/切换", WHEEL),
        ("短按: 下一张  长按: 拖动", BTN),
        ("语音: 放大/下一张/上传", VOICE),
    ])
    save_hd(img, PNG_DIR / "06-照片回看.png")


def export_match_ok():
    img, d = new_screen()
    draw_status(d, "上传留底", "待传 3 张")
    d.text((_s(16), _s(36)), "工单挂接留档(无AI)", fill=ACCENT, font=F_MD)
    d.rounded_rectangle([_s(16), _s(58), _s(156), _s(230)], radius=_s(2), outline=BORDER, fill=PANEL)
    d.text((_s(52), _s(135)), "缩略图 x3", fill=DIM, font=F_XS)
    d.rounded_rectangle([_s(168), _s(58), _s(624), _s(270)], radius=_s(2), outline=BORDER, fill=PANEL)
    d.rounded_rectangle([_s(180), _s(70), _s(310), _s(88)], radius=_s(2), outline=ACCENT)
    d.text((_s(188), _s(72)), "按工单挂接", fill=ACCENT, font=F_XXS)
    rows = [("收货单", "SH20250702001", True), ("挂接", "进入作业已绑定", False),
            ("照片", "全彩原图x3", False), ("识别", "无结构化字段", False)]
    y = 98
    for lb, val, hl in rows:
        d.text((_s(180), _s(y)), lb, fill=DIM, font=F_XXS)
        d.text((_s(240), _s(y)), val, fill=ACCENT if hl else TEXT, font=F_XS)
        y += 20
    d.text((_s(220), _s(290)), "请确认后上传至收货系统留底", fill=WARN, font=F_XS)
    draw_interaction_bar(d, [
        ("滚轮: 取消/确认", WHEEL),
        ("按钮: 确认上传", BTN),
        ("语音: 确认上传/取消", VOICE),
    ])
    save_hd(img, PNG_DIR / "07-上传留底-匹配成功.png")


def export_match_fail():
    img, d = new_screen()
    draw_status(d, "上传留底", "网络异常")
    d.text((_s(16), _s(36)), "上传失败 · 本地缓存", fill=ACCENT, font=F_MD)
    d.rounded_rectangle([_s(16), _s(58), _s(156), _s(230)], radius=_s(2), outline=BORDER, fill=PANEL)
    d.text((_s(52), _s(135)), "缩略图 x1", fill=DIM, font=F_XS)
    d.rounded_rectangle([_s(168), _s(58), _s(624), _s(310)], radius=_s(2), outline=BORDER, fill=PANEL)
    d.rounded_rectangle([_s(180), _s(70), _s(320), _s(88)], radius=_s(2), outline=DANGER)
    d.text((_s(188), _s(72)), "上传中断", fill=DANGER, font=F_XXS)
    d.text((_s(180), _s(96)), "网络不可用 · 恢复后自动补传", fill=DIM, font=F_XXS)
    d.text((_s(180), _s(120)), "挂接: SH20250702001(已绑定)", fill=TEXT, font=F_XXS)
    draw_interaction_bar(d, [
        ("滚轮: 选择候选", WHEEL),
        ("按钮: 确认绑定", BTN),
        ("语音: 选择第一个", VOICE),
    ])
    save_hd(img, PNG_DIR / "08-上传留底-匹配失败.png")


def export_flow_overview():
    w, h = _s(1200), _s(400)
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    d.text((_s(480), _s(16)), "正式操作前流程 + 目视检查主流程", fill=ACCENT, font=F_MD)
    boxes = [
        (20, 50, "登录", ACCENT), (140, 50, "选择工单", ACCENT),
        (280, 50, "确认作业", ACCENT), (420, 50, "预览开", VOICE),
        (560, 50, "预览关", VOICE), (700, 50, "照片回看", VOICE),
        (840, 50, "上传留底", BTN), (980, 50, "匹配确认", BTN),
    ]
    for i, (x, y, label, color) in enumerate(boxes):
        d.rounded_rectangle([_s(x), _s(y), _s(x + 100), _s(y + 40)], radius=_s(4), outline=color)
        tw = d.textlength(label, font=F_XS)
        d.text((_s(x) + (_s(100) - tw) / 2, _s(y + 14)), label, fill=TEXT, font=F_XS)
        if i < len(boxes) - 1:
            nx = boxes[i + 1][0]
            d.line([(_s(x + 100), _s(y + 20)), (_s(nx), _s(y + 20))], fill=DIM, width=_s(1))
    d.text((_s(40), _s(120)), "交互: 语音 + 滚轮 + 按钮", fill=DIM, font=F_XS)
    d.text((_s(40), _s(160)), "预览开 <=> 预览关", fill=DIM, font=F_XS)
    d.text((_s(40), _s(190)), "匹配失败 -> 选择候选 -> 重新上传", fill=DANGER, font=F_XS)
    d.text((_s(40), _s(220)), "上传完成 -> 继续检查", fill=ACCENT, font=F_XS)
    d.text((_s(40), _s(320)), "屏幕规格: 640 x 400", fill=TEXT, font=F_SM)
    save_hd(img, PNG_DIR / "00-流程总览.png")


def main():
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    export_login()
    export_work_list()
    export_confirm()
    export_preview_on()
    export_preview_off()
    export_review()
    export_match_ok()
    export_match_fail()
    export_flow_overview()
    print(f"已导出标准版 9 张 -> {PNG_DIR}")


if __name__ == "__main__":
    main()
