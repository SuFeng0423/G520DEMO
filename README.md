# 智能眼镜 · 目视检查原型

640×400 智能眼镜 + 手机 APK 协作原型。流程按三端划分：

| 端 | 层级 | 职责 |
|---|---|---|
| **服务端** | 数据层 | 云宏方提供工单 / 上传 / 提交接口 |
| **APK 端** | 预览层 | 收图、放大缩小与局部预览、删图、一键提交（进度条） |
| **眼镜端** | 操作层 | 登录取工单、执行检查；**每拍一张自动传 APK**（无需二次确认） |

## 在线访问

```
https://sufeng0423.github.io/G520DEMO/
```

临时预览：

```
https://htmlpreview.github.io/?https://github.com/SuFeng0423/G520DEMO/blob/main/index.html
```

## 本地预览

```bash
python3 -m http.server 8080
# 访问 http://localhost:8080
```

## 结构

- `index.html` — 三端架构与屏幕总览
- `screens/` — 眼镜端操作屏
- `screens/apk/` — APK 预览 / 提交屏
- `css/`、`js/` — 样式与流程导航
