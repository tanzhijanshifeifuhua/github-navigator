@echo off
chcp 65001 >nul
echo ========================================
echo   GitHub 项目爬虫
echo ========================================
echo.
echo 正在爬取 GitHub 项目数据...
echo.
py crawler.py
echo.
echo 爬取完成！按任意键退出...
pause >nul
