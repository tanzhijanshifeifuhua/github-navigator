# GitHub 项目中文分类导航

一个爬取 GitHub 项目并按照中文模块分类展示的 Web 应用。

## ✨ 功能特点

- 🔍 自动爬取 GitHub 热门项目（1158+ 项目）
- 📂 按中文模块智能分类（前端、后端、移动开发、数据科学等）
- 🌐 美观的 Web 界面展示
- 🔎 实时搜索过滤功能（支持中英文）
- 📊 显示项目星标、Fork 数等信息
- 🇨🇳 100% 中文描述覆盖
- 📑 侧边导航栏快速跳转
- ▼ 分类折叠功能
- 📱 响应式设计，支持移动端

## 🚀 快速开始

### 方式一：在线部署（推荐）

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/你的用户名/你的仓库)

### 方式二：Docker 部署

```bash
# 克隆项目
git clone https://github.com/你的用户名/你的仓库.git
cd 你的仓库

# 使用 Docker Compose
docker-compose up -d

# 访问 http://localhost:5000
```

### 方式三：本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行爬虫（可选，已有数据可跳过）
python crawler.py

# 启动 Web 服务
python app.py

# 访问 http://localhost:5000
```

## 📖 详细文档

- [项目结构说明](项目结构说明.md) - 完整的项目结构
- [快速部署指南](docs/快速部署.md) - 5 分钟快速部署
- [完整部署指南](docs/部署指南.md) - 多种部署方式详解
- [功能说明](docs/功能说明.md) - 所有功能介绍
- [使用说明](docs/使用说明.txt) - 日常使用指南

## 🛠️ 安装步骤

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. （可选）设置 GitHub Token：
   - 访问 https://github.com/settings/tokens
   - 生成新的 Personal Access Token
   - 在 `crawler.py` 中设置 token

## 📝 使用方法

### 1. 爬取数据

运行爬虫脚本获取 GitHub 项目数据：

```bash
cd scripts
python crawler.py
```

这将生成 `github_projects.json` 文件，包含分类后的项目数据。

### 2. 添加中文描述

```bash
cd scripts
python add_chinese_descriptions.py
```

为所有项目生成详细的中文描述。

### 3. 启动 Web 服务

```bash
python app.py
```

或使用快速启动脚本：
```bash
# Windows
scripts\start.bat

# Linux/Mac
./scripts/start.sh
```

然后在浏览器访问：http://localhost:5000

## 🎨 界面预览

- **侧边导航栏**: 快速跳转到各个分类
- **分类折叠**: 点击标题折叠/展开分类
- **实时搜索**: 输入关键词即时过滤
- **项目卡片**: 显示详细信息和中文描述
- **响应式设计**: 完美支持桌面和移动设备

## 🔧 自定义配置

### 修改分类模块

编辑 `scripts/crawler.py` 中的 `categories` 字典：

```python
self.categories = {
    "前端开发": ["react", "vue", "angular", ...],
    "后端开发": ["python", "java", "golang", ...],
    # 添加更多分类...
}
```

### 修改搜索条件

在 `scripts/crawler.py` 的 `__main__` 部分修改查询条件：

```python
queries = [
    "stars:>10000",
    "language:python stars:>5000",
    # 添加更多查询...
]
```

### 自定义中文描述

编辑 `scripts/add_chinese_descriptions.py` 中的 `specific_descriptions` 字典。

## 📊 项目结构

```
github-navigator/
├── app.py                    # Flask 主应用
├── requirements.txt          # Python 依赖
├── github_projects.json      # 项目数据（1158个项目）
├── templates/               # HTML 模板
├── static/                  # 静态资源（CSS/JS）
├── scripts/                 # 脚本文件（爬虫、部署等）
├── config/                  # 配置文件（Docker、Nginx等）
├── docs/                    # 文档
├── tests/                   # 测试文件
└── .github/                 # GitHub Actions
```

详细结构请查看 [项目结构说明.md](项目结构说明.md)

## 🚀 部署选项

- **Vercel**: 一键部署，免费 HTTPS
- **Railway**: 简单部署，免费额度
- **Render**: 免费托管
- **Docker**: 容器化部署
- **Linux 服务器**: 传统部署

详见 [部署指南.md](docs/部署指南.md)

## ⚙️ 环境变量

```env
FLASK_ENV=production          # 生产环境
GITHUB_TOKEN=your_token_here  # GitHub API Token（可选）
```

## 📈 数据统计

- **总项目数**: 1158+
- **分类数**: 10 个
- **中文描述覆盖率**: 100%
- **最后更新**: 2025-12-27

## 🔄 自动更新

使用 GitHub Actions 自动更新数据（已配置）：

1. 在仓库设置中添加 Secret: `GH_TOKEN`
2. 每天自动运行爬虫更新数据
3. 自动提交更新

## ⚠️ 注意事项

- GitHub API 有速率限制，建议使用 Personal Access Token
- 不使用 Token 时：每小时 60 次请求
- 使用 Token 时：每小时 5000 次请求
- 爬虫会自动添加延迟避免触发限制

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 🙏 致谢

- GitHub API
- Flask
- 所有开源项目贡献者

---

**⭐ 如果这个项目对你有帮助，请给个 Star！**
