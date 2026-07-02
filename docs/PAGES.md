# 公开访问说明

## 为什么 Raw 链接只显示源码？

访问  
`https://gitee.com/sf_0423/g520-demo/raw/master/index.html`  
时，码云返回 **`Content-Type: text/plain`**，浏览器按「纯文本」展示 HTML 源码，**不会渲染成网页**。

这是码云 Raw 文件的默认行为；个人仓库 **已无 Gitee Pages**，无法像以前一样用 `用户名.gitee.io` 托管。

---

## 方案一：在线预览（免部署，立即可用）

通过 HTML Preview 服务加载码云上的文件（相对路径 CSS/JS 可正常加载）：

```
https://htmlpreview.github.io/?https://gitee.com/sf_0423/g520-demo/raw/master/index.html
```

> 国内访问该预览域名可能较慢或被墙，适合临时演示；正式对外建议用方案二。

---

## 方案二：GitHub Pages（推荐 · 免费 · 稳定）

代码仍在码云维护，同步一份到 GitHub 即可免费托管：

### 1. 在 GitHub 新建空仓库

名称建议：`g520-demo`（与码云一致）

### 2. 推送代码（不含 zl）

```bash
cd DEOM
git remote add github https://github.com/你的用户名/g520-demo.git
git push github master
```

### 3. 开启 Pages

GitHub 仓库 → **Settings** → **Pages** → Source 选 **Deploy from a branch** → Branch 选 `master`、目录 `/` → Save

### 4. 访问

约 1 分钟后：

```
https://你的用户名.github.io/g520-demo/
```

仓库已含 `.github/workflows/pages.yml`，推送到 GitHub 后也可自动部署 Pages。

---

## 方案三：国内静态托管（访问更快）

将 `DEOM` 目录（**不要包含 zl/**）上传到：

| 平台 | 说明 |
|------|------|
| [EdgeOne Pages](https://pages.edgeone.ai/) | 腾讯云，有免费额度 |
| [Upma 上码](https://www.upma.cn/) | 国内静态托管，适合 Demo |

---

## 码云仓库的作用

- **代码托管与版本管理**（主仓库）
- **Raw 链接**仅适合查看/下载文件，**不适合**直接给客户演示
- **服务**菜单中的 Jenkins、腾讯云等与本静态 HTML 无关，无需开通

---

## 本地预览

```bash
cd DEOM
python3 -m http.server 8080
# http://localhost:8080
```
