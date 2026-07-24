# 智能眼镜 · 目视检查原型

640×400 智能眼镜 UI 原型（拍照留底流程）。

## 在线访问

> **注意：** 码云 Raw 链接只会显示 HTML **源码**，无法渲染成页面（个人版已无 Gitee Pages）。

### 临时预览（免部署）

> `htmlpreview.github.io` **只支持 GitHub / Bitbucket**，不支持 Gitee（会 CORS + 常 404）。请用下方 GitHub 地址：

```
https://htmlpreview.github.io/?https://github.com/SuFeng0423/G520DEMO/blob/main/index.html
```

### 正式访问（GitHub Pages）

```
https://sufeng0423.github.io/G520DEMO/
```

首次需在 GitHub 仓库开启 Pages：**Settings → Pages → Source 选 GitHub Actions**（或 Deploy from branch `main` / `/`）。

详细步骤见 **[docs/PAGES.md](docs/PAGES.md)**。

## 本地预览

直接用浏览器打开 `index.html`，或：

```bash
python3 -m http.server 8080
# 访问 http://localhost:8080
```

## 结构

- `index.html` — 流程总览与入口
- `screens/` — 各流程屏
- `css/`、`js/` — 样式与流程导航
