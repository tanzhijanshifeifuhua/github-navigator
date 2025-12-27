# 脚本说明

## 数据爬取和处理

- `crawler.py` - GitHub 项目爬虫脚本
- `add_chinese_descriptions.py` - 添加中文描述
- `check_descriptions.py` - 检查描述完整性
- `check_more_descriptions.py` - 深度检查描述
- `final_report.py` - 生成统计报告

## 部署脚本

- `deploy.bat` - Windows 部署脚本
- `deploy.sh` - Linux/Mac 部署脚本
- `start.bat` - 快速启动（开发环境）
- `start_production.bat` - 生产环境启动
- `crawl.bat` - 快速运行爬虫
- `push_to_github.bat` - 推送到 GitHub

## 使用方法

### 更新数据
```bash
# Windows
cd scripts
py crawler.py
py add_chinese_descriptions.py

# Linux/Mac
cd scripts
python3 crawler.py
python3 add_chinese_descriptions.py
```

### 部署
```bash
# Windows
scripts\deploy.bat

# Linux/Mac
./scripts/deploy.sh
```
