# Gitee Pages 部署说明

访问 `https://sf_0423.gitee.io/g520-demo/` 出现 **404**，说明 **Pages 服务尚未启动**（代码已在仓库，但码云还未发布静态站点）。

## 一次性开启（必做）

按顺序操作：

### 1. 确认仓库公开

[仓库设置](https://gitee.com/sf_0423/g520-demo/settings#index) → **是否开源** → 选 **公开**

### 2. 设置个性地址（若未设置）

右上角头像 → **设置** → **个性地址** → 设为 `sf_0423`（与用户名一致）

### 3. 实名认证（若未完成）

头像 → **设置** → **账号管理** → 完成 **实名认证**（Pages 通常要求已认证）

### 4. 启动 Gitee Pages

打开：<https://gitee.com/sf_0423/g520-demo/pages>

或：仓库 → **服务** → **Gitee Pages**

| 配置项 | 填写 |
|--------|------|
| 部署分支 | `master` |
| 部署目录 | `/`（根目录，留空亦可） |

点击 **启动**（或 **更新**），等待 1～3 分钟。

### 5. 访问

```
https://sf_0423.gitee.io/g520-demo/
```

即为 `index.html` 流程总览。

---

## 临时预览（未开 Pages 时）

公开仓库可直接打开 raw 地址（功能完整，URL 较长）：

```
https://gitee.com/sf_0423/g520-demo/raw/master/index.html
```

---

## 后续更新

代码推送到 `master` 后，到 Pages 页面点 **更新**，或执行：

```bash
export GITEE_TOKEN=你的私人令牌   # 设置 → 私人令牌
./scripts/deploy-pages.sh
```

私人令牌：<https://gitee.com/profile/personal_access_tokens>

---

## 仍 404 时排查

| 现象 | 处理 |
|------|------|
| Pages 页无「启动」按钮 | 先完成实名认证 |
| 启动后仍 404 | 等 3～10 分钟，Ctrl+F5 强刷 |
| 页面空白、样式丢失 | 确认部署目录为 `/`，且根目录有 `index.html` |
| 免费 Pages 不可用 | 码云政策变更时可改用 raw 链接或企业版 Pages |
