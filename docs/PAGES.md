# 公开访问说明

## 码云 Raw 链接为何只显示源码？

`https://gitee.com/sf_0423/g520-demo/raw/master/index.html` 返回 `text/plain`，浏览器只展示 HTML 源码。个人版码云已无 Gitee Pages。

---

## 正式访问（GitHub Pages · 推荐）

**仓库：** [github.com/SuFeng0423/G520DEMO](https://github.com/SuFeng0423/G520DEMO)

**访问地址：**

```
https://sufeng0423.github.io/G520DEMO/
```

### 开启 Pages（一次性）

1. 打开 <https://github.com/SuFeng0423/G520DEMO/settings/pages>
2. **Build and deployment** → **Source** 选 **GitHub Actions**  
   （或选 **Deploy from a branch** → Branch `main`、Folder `/`）
3. 若用 GitHub Actions：到 **Actions** 页运行 **Deploy GitHub Pages** 工作流
4. 等待 1～2 分钟，访问上列地址

仓库已含 `.github/workflows/pages.yml`，推送 `main` 分支后会自动部署。

---

## 临时预览（免部署）

```
https://htmlpreview.github.io/?https://gitee.com/sf_0423/g520-demo/raw/master/index.html
```

国内可能较慢，仅作临时演示。

---

## 双远程同步

```bash
cd DEOM
git push origin master    # 码云
git push github main      # GitHub（本地 master 已映射为 main）
```

---

## 本地预览

```bash
cd DEOM
python3 -m http.server 8080
# http://localhost:8080
```
