# 公开访问说明

## 为什么没有 Gitee Pages？

码云 **个人版仓库已不再提供 Gitee Pages**（2024 年起下线），因此在仓库 **服务** 菜单里看不到 Pages 入口——这是平台政策，不是项目配置问题。

企业版仓库才可能有 Pages 类服务；当前 `g520-demo` 为个人公开仓库。

---

## 推荐：Raw 直链（已可用，无需额外配置）

仓库公开后，可直接分享以下地址，完整加载 HTML / CSS / JS / 流程串联：

```
https://gitee.com/sf_0423/g520-demo/raw/master/index.html
```

**特点：**
- 所有人可访问，无需登录
- 支持「进入流程体验」逐步浏览
- URL 较长，但稳定、免费

可将此链接写入 README、文档或发给客户。

---

## 可选：更短域名（需第三方托管）

若需要类似 `xxx.com` 的短链接，可将同一套静态文件部署到：

| 平台 | 说明 |
|------|------|
| [GitHub Pages](https://pages.github.com/) | 免费，国内访问可能较慢 |
| [腾讯云 EdgeOne Pages](https://pages.edgeone.ai/) | 国内访问较快，有免费额度 |
| [Upma 上码](https://www.upma.cn/) | 国内静态托管，适合 Demo |

代码仍在码云维护；托管平台可从 Gitee 拉取或手动上传 `DEOM` 目录（**不含 `zl/`**）。

---

## 码云「服务」菜单中的项

截图中的 SonarQube、Jenkins、腾讯云托管等均为 **第三方集成**，不是 Pages 替代品。静态 HTML 原型 **不需要** 开通这些服务。

---

## 本地预览

```bash
cd DEOM
python3 -m http.server 8080
# 浏览器打开 http://localhost:8080
```
