# 智能眼镜 · 目视检查原型

640×400 智能眼镜 UI 原型，含基础版（拍照留底）与增强版（AI 辅助）两套流程。

## 在线访问

启用 [Gitee Pages](https://gitee.com/help/articles/4136) 后，访问：

```
https://sf_0423.gitee.io/g520-demo/
```

即打开 `index.html` 流程总览页。

**Pages 开启步骤：** 仓库 → 服务 → Gitee Pages → 部署分支 `master`、目录 `/` → 启动。

请将仓库设为**公开**，以便所有人无需登录即可访问。

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
