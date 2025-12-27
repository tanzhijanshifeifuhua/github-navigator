#!/bin/bash

# GitHub 项目中文分类导航 - 快速部署脚本

echo "================================"
echo "GitHub 项目中文分类导航 - 部署工具"
echo "================================"
echo ""

# 检查是否在项目目录
if [ ! -f "app.py" ]; then
    echo "❌ 错误: 请在项目根目录运行此脚本"
    exit 1
fi

echo "请选择部署方式:"
echo "1. Docker 部署（推荐）"
echo "2. 本地测试运行"
echo "3. 生产环境部署（Linux 服务器）"
echo "4. 构建 Docker 镜像"
echo ""
read -p "请输入选项 (1-4): " choice

case $choice in
    1)
        echo ""
        echo "🐳 使用 Docker Compose 部署..."
        
        # 检查 Docker
        if ! command -v docker &> /dev/null; then
            echo "❌ Docker 未安装，请先安装 Docker"
            exit 1
        fi
        
        # 检查 Docker Compose
        if ! command -v docker-compose &> /dev/null; then
            echo "❌ Docker Compose 未安装，请先安装 Docker Compose"
            exit 1
        fi
        
        # 构建并启动
        echo "📦 构建镜像..."
        docker-compose build
        
        echo "🚀 启动服务..."
        docker-compose up -d
        
        echo ""
        echo "✅ 部署完成！"
        echo "📍 访问地址: http://localhost:5000"
        echo ""
        echo "常用命令:"
        echo "  查看日志: docker-compose logs -f"
        echo "  停止服务: docker-compose down"
        echo "  重启服务: docker-compose restart"
        ;;
        
    2)
        echo ""
        echo "🧪 本地测试运行..."
        
        # 检查 Python
        if ! command -v python3 &> /dev/null; then
            echo "❌ Python3 未安装"
            exit 1
        fi
        
        # 创建虚拟环境
        if [ ! -d "venv" ]; then
            echo "📦 创建虚拟环境..."
            python3 -m venv venv
        fi
        
        # 激活虚拟环境
        source venv/bin/activate
        
        # 安装依赖
        echo "📦 安装依赖..."
        pip install -r requirements.txt
        
        # 运行应用
        echo "🚀 启动应用..."
        echo ""
        echo "✅ 服务已启动！"
        echo "📍 访问地址: http://localhost:5000"
        echo "⚠️  按 Ctrl+C 停止服务"
        echo ""
        python3 app.py
        ;;
        
    3)
        echo ""
        echo "🖥️  生产环境部署..."
        echo ""
        echo "此选项将配置 Systemd 服务和 Nginx"
        read -p "确认继续? (y/n): " confirm
        
        if [ "$confirm" != "y" ]; then
            echo "已取消"
            exit 0
        fi
        
        # 检查是否为 root
        if [ "$EUID" -ne 0 ]; then
            echo "❌ 请使用 sudo 运行此脚本"
            exit 1
        fi
        
        # 安装依赖
        echo "📦 安装系统依赖..."
        apt update
        apt install -y python3 python3-pip python3-venv nginx
        
        # 创建虚拟环境
        echo "📦 创建虚拟环境..."
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        
        # 配置 Systemd
        echo "⚙️  配置 Systemd 服务..."
        cp github-navigator.service /etc/systemd/system/
        systemctl daemon-reload
        systemctl enable github-navigator
        systemctl start github-navigator
        
        # 配置 Nginx
        echo "⚙️  配置 Nginx..."
        read -p "请输入域名 (留空使用 localhost): " domain
        if [ -z "$domain" ]; then
            domain="localhost"
        fi
        
        sed "s/your-domain.com/$domain/g" nginx.conf > /etc/nginx/sites-available/github-navigator
        ln -sf /etc/nginx/sites-available/github-navigator /etc/nginx/sites-enabled/
        nginx -t && systemctl restart nginx
        
        echo ""
        echo "✅ 部署完成！"
        echo "📍 访问地址: http://$domain"
        echo ""
        echo "常用命令:"
        echo "  查看服务状态: systemctl status github-navigator"
        echo "  查看日志: journalctl -u github-navigator -f"
        echo "  重启服务: systemctl restart github-navigator"
        ;;
        
    4)
        echo ""
        echo "🐳 构建 Docker 镜像..."
        
        if ! command -v docker &> /dev/null; then
            echo "❌ Docker 未安装"
            exit 1
        fi
        
        read -p "请输入镜像名称 (默认: github-navigator): " image_name
        if [ -z "$image_name" ]; then
            image_name="github-navigator"
        fi
        
        echo "📦 构建镜像: $image_name"
        docker build -t $image_name .
        
        echo ""
        echo "✅ 镜像构建完成！"
        echo ""
        echo "运行容器:"
        echo "  docker run -d -p 5000:5000 --name github-nav $image_name"
        ;;
        
    *)
        echo "❌ 无效选项"
        exit 1
        ;;
esac
