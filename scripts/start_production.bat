@echo off
chcp 65001 >nul
echo ================================
echo 启动生产环境服务器
echo ================================
echo.

echo 🚀 使用 Gunicorn 启动服务器...
echo 📍 访问地址: http://localhost:5000
echo ⚠️  按 Ctrl+C 停止服务
echo.

py -m gunicorn -c gunicorn_config.py app:app
pause
