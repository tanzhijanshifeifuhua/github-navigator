# Vercel 部署说明

## 当前状态

✅ 代码已推送到 GitHub
✅ vercel.json 配置已添加
✅ API 目录已创建

## 部署地址

https://github-navigator-ochre.vercel.app/

## 如果网站无法访问

### 方法 1：检查 Vercel 部署日志

1. 访问 https://vercel.com/dashboard
2. 找到 `github-navigator` 项目
3. 点击最新的部署
4. 查看 "Build Logs" 和 "Function Logs"
5. 如果有错误，会显示具体信息

### 方法 2：重新部署

1. 访问 https://vercel.com/dashboard
2. 找到 `github-navigator` 项目
3. 点击右上角的 "..." 菜单
4. 选择 "Redeploy"
5. 等待 1-2 分钟

### 方法 3：检查项目设置

在 Vercel 项目设置中确认：

1. **Framework Preset**: Other
2. **Root Directory**: ./
3. **Build Command**: (留空)
4. **Output Directory**: (留空)
5. **Install Command**: pip install -r requirements.txt

### 方法 4：使用其他部署平台

如果 Vercel 持续有问题，可以尝试：

#### Railway（推荐）
1. 访问 https://railway.app
2. 使用 GitHub 登录
3. 点击 "New Project" → "Deploy from GitHub repo"
4. 选择 `github-navigator`
5. 自动部署，获取访问地址

#### Render
1. 访问 https://render.com
2. 注册并登录
3. 点击 "New +" → "Web Service"
4. 连接 GitHub 仓库
5. 配置：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. 点击 "Create Web Service"

## 常见问题

### Q: 显示 404 Not Found
A: 检查 vercel.json 是否在根目录，并且 api/index.py 文件存在

### Q: 显示 500 Internal Server Error
A: 查看 Vercel 的 Function Logs，可能是 Python 依赖问题

### Q: 显示空白页面
A: 检查 github_projects.json 文件是否已提交到仓库

### Q: 部署成功但数据为空
A: 确认 github_projects.json 文件大小正常（应该约 2MB）

## 本地测试

如果想在本地测试 Vercel 配置：

```bash
# 安装 Vercel CLI
npm install -g vercel

# 在项目目录运行
vercel dev
```

## 需要帮助？

1. 查看 Vercel 部署日志
2. 检查 GitHub 仓库文件是否完整
3. 尝试重新部署
4. 考虑使用 Railway 或 Render

---

**提示**: Vercel 的 Serverless 函数有 50MB 大小限制和 10 秒执行时间限制。如果项目数据很大，建议使用 Railway 或传统服务器部署。
