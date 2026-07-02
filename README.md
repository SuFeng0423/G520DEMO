# 智能眼镜 · 目视检查原型

640×400 智能眼镜 UI 原型，含基础版（拍照留底）与增强版（AI 辅助）两套流程。

## 在线访问

### 正式地址（需先开启 Pages）

```
https://sf_0423.gitee.io/g520-demo/
```

**若出现 404**：代码已上传，但 **Gitee Pages 尚未启动**。请按 **[docs/PAGES.md](docs/PAGES.md)** 操作（约 2 分钟）：

1. 仓库 → **服务** → **Gitee Pages**
2. 分支 `master`、目录 `/` → **启动**
3. 等待部署完成后访问上列地址

### 临时预览（Pages 未开时可用）

```
https://gitee.com/sf_0423/g520-demo/raw/master/index.html
```

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
