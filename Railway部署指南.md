# 🚂 Railway 部署指南（推荐）

Railway 比 Vercel 更适合 Flask 应用，部署更简单！

## 为什么选择 Railway？

✅ 自动识别 Python 项目
✅ 无需额外配置文件
✅ 免费 $5/月额度
✅ 自动 HTTPS
✅ 部署速度快
✅ 支持持久化存储

## 🚀 部署步骤（5分钟）

### 1. 访问 Railway
打开浏览器访问：https://railway.app

### 2. 登录
点击 "Login" → 选择 "Login with GitHub"

### 3. 创建新项目
- 点击 "New Project"
- 选择 "Deploy from GitHub repo"
- 找到并选择 `github-navigator`

### 4. 等待部署
Railway 会自动：
- 检测到 Python 项目
- 安装 requirements.txt 中的依赖
- 运行 app.py
- 生成访问地址

### 5. 获取访问地址
- 部署完成后，点击项目
- 点击 "Settings" → "Domains"
- 点击 "Generate Domain"
- 复制生成的地址（类似：xxx.railway.app）

## ✅ 完成！

访问你的网站：`https://你的项目名.railway.app`

## 🔧 可选配置

### 添加环境变量（如果需要）
1. 在项目页面点击 "Variables"
2. 添加：
   - `FLASK_ENV=production`
   - `PORT=5000`

### 查看日志
点击 "Deployments" → 选择最新部署 → 查看实时日志

### 重新部署
点击 "Deployments" → "Redeploy"

## 💰 费用说明

- 免费额度：$5/月
- 足够个人项目使用
- 超出后按使用量计费

## 🆚 Railway vs Vercel

| 特性 | Railway | Vercel |
|------|---------|--------|
| Python 支持 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 配置难度 | 简单 | 需要配置 |
| 部署速度 | 快 | 快 |
| 免费额度 | $5/月 | 100GB 带宽 |
| 持久化存储 | ✅ | ❌ |

## 🐛 故障排除

### 部署失败？
1. 检查 requirements.txt 是否正确
2. 查看部署日志中的错误信息
3. 确认 github_projects.json 已提交

### 网站无法访问？
1. 确认域名已生成
2. 等待 1-2 分钟让 DNS 生效
3. 检查部署状态是否为 "Active"

### 数据显示为空？
1. 确认 github_projects.json 文件存在
2. 检查文件大小是否正常（约 2MB）
3. 查看应用日志

## 📝 其他部署选项

如果 Railway 也有问题，还可以尝试：

### Render（免费）
https://render.com
- 类似 Railway
- 完全免费
- 有休眠机制（15分钟无访问会休眠）

### Fly.io（免费）
https://fly.io
- 支持 Docker
- 全球部署
- 免费额度充足

## 🎯 推荐流程

1. **首选**: Railway（最简单）
2. **备选**: Render（完全免费）
3. **高级**: 自己的服务器（完全控制）

---

**现在就去试试 Railway 吧！** 🚀

访问：https://railway.app
