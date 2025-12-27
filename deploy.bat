@echo off
chcp 65001 >nul
echo ================================
echo GitHub 项目中文分类导航 - 部署工具
echo ================================
echo.

REM 检查是否在项目目录
if not exist "app.py" (
    echo ❌ 错误: 请在项目根目录运行此脚本
    pause
    exit /b 1
)

echo 请选择部署方式:
echo 1. Docker 部署（推荐）
echo 2. 本地测试运行
echo 3. 构建 Docker 镜像
echo.
set /p choice="请输入选项 (1-3): "

if "%choice%"=="1" goto docker_deploy
if "%choice%"=="2" goto local_run
if "%choice%"=="3" goto docker_build
echo ❌ 无效选项
pause
exit /b 1

:docker_deploy
echo.
echo 🐳 使用 Docker Compose 部署...

REM 检查 Docker
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker 未安装，请先安装 Docker Desktop
    pause
    exit /b 1
)

REM 检查 Docker Compose
docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker Compose 未安装
    pause
    exit /b 1
)

echo 📦 构建镜像...
docker-compose build

echo 🚀 启动服务...
docker-compose up -d

echo.
echo ✅ 部署完成！
echo 📍 访问地址: http://localhost:5000
echo.
echo 常用命令:
echo   查看日志: docker-compose logs -f
echo   停止服务: docker-compose down
echo   重启服务: docker-compose restart
pause
exit /b 0

:local_run
echo.
echo 🧪 本地测试运行...

REM 检查 Python
py --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python 未安装
    pause
    exit /b 1
)

REM 创建虚拟环境
if not exist "venv" (
    echo 📦 创建虚拟环境...
    py -m venv venv
)

REM 激活虚拟环境并安装依赖
echo 📦 安装依赖...
call venv\Scripts\activate.bat
pip install -r requirements.txt

REM 运行应用
echo 🚀 启动应用...
echo.
echo ✅ 服务已启动！
echo 📍 访问地址: http://localhost:5000
echo ⚠️  按 Ctrl+C 停止服务
echo.
py app.py
pause
exit /b 0

:docker_build
echo.
echo 🐳 构建 Docker 镜像...

docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker 未安装
    pause
    exit /b 1
)

set /p image_name="请输入镜像名称 (默认: github-navigator): "
if "%image_name%"=="" set image_name=github-navigator

echo 📦 构建镜像: %image_name%
docker build -t %image_name% .

echo.
echo ✅ 镜像构建完成！
echo.
echo 运行容器:
echo   docker run -d -p 5000:5000 --name github-nav %image_name%
pause
exit /b 0
