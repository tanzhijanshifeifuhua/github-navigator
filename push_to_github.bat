@echo off
chcp 65001 >nul
echo ================================
echo 推送代码到 GitHub
echo ================================
echo.

echo 请先在 GitHub 创建仓库：https://github.com/new
echo.
echo 仓库信息：
echo - 用户名：tanzhijianshifeifuhua
echo - 建议仓库名：github-navigator
echo - 类型：Public（公开）
echo.
pause

echo.
set /p repo_url="请输入你的 GitHub 仓库地址（例如：https://github.com/tanzhijianshifeifuhua/github-navigator.git）: "

if "%repo_url%"=="" (
    echo ❌ 错误：仓库地址不能为空
    pause
    exit /b 1
)

echo.
echo 📦 添加远程仓库...
git remote add origin %repo_url% 2>nul
if errorlevel 1 (
    echo ⚠️  远程仓库已存在，更新地址...
    git remote set-url origin %repo_url%
)

echo.
echo 🔄 切换到 main 分支...
git branch -M main

echo.
echo 🚀 推送代码到 GitHub...
echo.
echo ⚠️  如果提示输入密码，请使用 Personal Access Token
echo    获取 Token：https://github.com/settings/tokens
echo.
git push -u origin main

if errorlevel 1 (
    echo.
    echo ❌ 推送失败！
    echo.
    echo 可能的原因：
    echo 1. 需要 Personal Access Token（不是密码）
    echo 2. 仓库地址错误
    echo 3. 网络问题
    echo.
    echo 获取 Token 步骤：
    echo 1. 访问：https://github.com/settings/tokens
    echo 2. 点击 "Generate new token (classic)"
    echo 3. 勾选 "repo" 权限
    echo 4. 生成并复制 token
    echo 5. 在提示输入密码时粘贴 token
    pause
    exit /b 1
)

echo.
echo ✅ 代码已成功推送到 GitHub！
echo.
echo 📍 仓库地址：%repo_url%
echo.
echo 下一步：部署到 Vercel
echo 1. 访问：https://vercel.com
echo 2. 使用 GitHub 登录
echo 3. 导入你的仓库
echo 4. 点击 Deploy
echo.
pause
