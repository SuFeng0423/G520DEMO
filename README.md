# 智能眼镜 · 目视检查原型

640×400 智能眼镜 UI 原型，含基础版（拍照留底）与增强版（AI 辅助）两套流程。

## 在线访问

> **注意：** 码云 Raw 链接只会显示 HTML **源码**，无法渲染成页面（个人版已无 Gitee Pages）。

### 临时预览（免部署）

```
https://htmlpreview.github.io/?https://gitee.com/sf_0423/g520-demo/raw/master/index.html
```

### 正式访问（推荐 GitHub Pages）

将仓库同步到 GitHub 并开启 Pages 后：

```
https://你的用户名.github.io/g520-demo/
```

详细步骤见 **[docs/PAGES.md](docs/PAGES.md)**（含 GitHub Pages、国内托管备选）。

## 本地预览

直接用浏览器打开 `index.html`，或：

```bash
python3 -m http.server 8080
# 访问 http://localhost:8080
```

## 结构

- `index.html` — 流程总览与入口
- `screens/` — 基础版各屏
- `screens/ai/` — 增强版各屏
- `css/`、`js/` — 样式与流程导航
