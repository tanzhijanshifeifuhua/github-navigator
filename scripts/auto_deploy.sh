#!/bin/bash
# GitHub 项目中文分类导航 - 云服务器一键部署脚本

set -e

echo "================================"
echo "GitHub 项目中文分类导航"
echo "云服务器一键部署脚本"
echo "================================"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查是否为 root 用户
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}请使用 root 用户运行此脚本${NC}"
    echo "使用命令: sudo bash auto_deploy.sh"
    exit 1
fi

echo -e "${GREEN}✓ Root 权限检查通过${NC}"

# 检测操作系统
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
    VERSION=$VERSION_ID
else
    echo -e "${RED}无法检测操作系统${NC}"
    exit 1
fi

echo -e "${GREEN}✓ 检测到操作系统: $OS $VERSION${NC}"

# 选择部署方式
echo ""
echo "请选择部署方式:"
echo "1. Docker 部署（推荐）"
echo "2. 传统部署"
read -p "请输入选项 (1-2): " deploy_method

if [ "$deploy_method" == "1" ]; then
    echo ""
    echo "================================"
    echo "开始 Docker 部署"
    echo "================================"
    
    # 安装 Docker
    echo -e "${YELLOW}正在安装 Docker...${NC}"
    if ! command -v docker &> /dev/null; then
        curl -fsSL https://get.docker.com | sh
        systemctl start docker
        systemctl enable docker
        echo -e "${GREEN}✓ Docker 安装完成${NC}"
    else
        echo -e "${GREEN}✓ Docker 已安装${NC}"
    fi
    
    # 安装 Docker Compose
    echo -e "${YELLOW}正在安装 Docker Compose...${NC}"
    if ! command -v docker-compose &> /dev/null; then
        curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        chmod +x /usr/local/bin/docker-compose
        echo -e "${GREEN}✓ Docker Compose 安装完成${NC}"
    else
        echo -e "${GREEN}✓ Docker Compose 已安装${NC}"
    fi
    
    # 克隆项目
    echo -e "${YELLOW}正在克隆项目...${NC}"
    if [ ! -d "/opt/github-navigator" ]; then
        cd /opt
        git clone https://github.com/tanzhijanshifeifuhua/github-navigator.git
        echo -e "${GREEN}✓ 项目克隆完成${NC}"
    else
        echo -e "${YELLOW}项目已存在，正在更新...${NC}"
        cd /opt/github-navigator
        git pull
        echo -e "${GREEN}✓ 项目更新完成${NC}"
    fi
    
    # 启动服务
    echo -e "${YELLOW}正在启动服务...${NC}"
    cd /opt/github-navigator
    docker-compose -f config/docker-compose.yml up -d
    
    echo ""
    echo -e "${GREEN}================================${NC}"
    echo -e "${GREEN}✓ 部署完成！${NC}"
    echo -e "${GREEN}================================${NC}"
    echo ""
    echo "访问地址: http://$(curl -s ifconfig.me):5000"
    echo ""
    echo "常用命令:"
    echo "  查看日志: docker-compose -f /opt/github-navigator/config/docker-compose.yml logs -f"
    echo "  停止服务: docker-compose -f /opt/github-navigator/config/docker-compose.yml down"
    echo "  重启服务: docker-compose -f /opt/github-navigator/config/docker-compose.yml restart"
    
elif [ "$deploy_method" == "2" ]; then
    echo ""
    echo "================================"
    echo "开始传统部署"
    echo "================================"
    
    # 更新系统
    echo -e "${YELLOW}正在更新系统...${NC}"
    if [ "$OS" == "ubuntu" ] || [ "$OS" == "debian" ]; then
        apt update && apt upgrade -y
        apt install python3 python3-pip python3-venv nginx git -y
    elif [ "$OS" == "centos" ] || [ "$OS" == "rhel" ]; then
        yum update -y
        yum install python3 python3-pip nginx git -y
    fi
    echo -e "${GREEN}✓ 系统更新完成${NC}"
    
    # 克隆项目
    echo -e "${YELLOW}正在克隆项目...${NC}"
    if [ ! -d "/var/www/github-navigator" ]; then
        mkdir -p /var/www
        cd /var/www
        git clone https://github.com/tanzhijanshifeifuhua/github-navigator.git
        echo -e "${GREEN}✓ 项目克隆完成${NC}"
    else
        echo -e "${YELLOW}项目已存在，正在更新...${NC}"
        cd /var/www/github-navigator
        git pull
        echo -e "${GREEN}✓ 项目更新完成${NC}"
    fi
    
    # 创建虚拟环境
    echo -e "${YELLOW}正在创建虚拟环境...${NC}"
    cd /var/www/github-navigator
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    echo -e "${GREEN}✓ 虚拟环境创建完成${NC}"
    
    # 配置 Systemd 服务
    echo -e "${YELLOW}正在配置系统服务...${NC}"
    cp config/github-navigator.service /etc/systemd/system/
    systemctl daemon-reload
    systemctl start github-navigator
    systemctl enable github-navigator
    echo -e "${GREEN}✓ 系统服务配置完成${NC}"
    
    # 配置 Nginx
    echo -e "${YELLOW}正在配置 Nginx...${NC}"
    cp config/nginx.conf /etc/nginx/sites-available/github-navigator
    
    # 获取服务器 IP
    SERVER_IP=$(curl -s ifconfig.me)
    sed -i "s/your-domain.com/$SERVER_IP/g" /etc/nginx/sites-available/github-navigator
    
    ln -sf /etc/nginx/sites-available/github-navigator /etc/nginx/sites-enabled/
    nginx -t && systemctl restart nginx
    echo -e "${GREEN}✓ Nginx 配置完成${NC}"
    
    # 配置防火墙
    echo -e "${YELLOW}正在配置防火墙...${NC}"
    if command -v ufw &> /dev/null; then
        ufw allow 80
        ufw allow 443
        ufw allow 5000
        echo -e "${GREEN}✓ 防火墙配置完成 (UFW)${NC}"
    elif command -v firewall-cmd &> /dev/null; then
        firewall-cmd --permanent --add-port=80/tcp
        firewall-cmd --permanent --add-port=443/tcp
        firewall-cmd --permanent --add-port=5000/tcp
        firewall-cmd --reload
        echo -e "${GREEN}✓ 防火墙配置完成 (Firewalld)${NC}"
    fi
    
    echo ""
    echo -e "${GREEN}================================${NC}"
    echo -e "${GREEN}✓ 部署完成！${NC}"
    echo -e "${GREEN}================================${NC}"
    echo ""
    echo "访问地址: http://$SERVER_IP"
    echo ""
    echo "常用命令:"
    echo "  查看日志: journalctl -u github-navigator -f"
    echo "  停止服务: systemctl stop github-navigator"
    echo "  重启服务: systemctl restart github-navigator"
    echo "  查看状态: systemctl status github-navigator"
    
else
    echo -e "${RED}无效的选项${NC}"
    exit 1
fi

echo ""
echo -e "${YELLOW}提示: 如果需要配置域名和 SSL，请查看文档${NC}"
echo ""
