#!/usr/bin/env bash
# 触发 Gitee Pages 重新部署（需先在网页端首次「启动」Pages）
set -e
OWNER="${GITEE_OWNER:-sf_0423}"
REPO="${GITEE_REPO:-g520-demo}"
TOKEN="${GITEE_TOKEN:?请设置环境变量 GITEE_TOKEN（码云私人令牌）}"

echo "→ 请求部署 Pages: ${OWNER}/${REPO}"
curl -fsS -X POST "https://gitee.com/api/v5/repos/${OWNER}/${REPO}/pages/builds?access_token=${TOKEN}"
echo ""
echo "→ 部署已触发，约 1～3 分钟后访问:"
echo "   https://${OWNER}.gitee.io/${REPO}/"
