# 🚀 部署到 Vercel 详细步骤

## 第一步：创建 GitHub 仓库

1. 打开浏览器，访问：https://github.com/new
2. 使用你的账号登录：
   - 邮箱：2495059149@qq.com
   - 用户名：tanzhijianshifeifuhua
   - 密码：zhf200902

3. 创建新仓库：
   - Repository name（仓库名）：`github-navigator`（或其他你喜欢的名字）
   - Description（描述）：GitHub 项目中文分类导航
   - 选择 **Public**（公开）
   - **不要**勾选 "Add a README file"
   - **不要**勾选 "Add .gitignore"
   - 点击 **Create repository**（创建仓库）

4. 创建后，GitHub 会显示一个页面，复制仓库地址（类似这样）：
   ```
   https://github.com/tanzhijianshifeifuhua/github-navigator.git
   ```

## 第二步：推送代码到 GitHub

在你的项目目录（F:\project\github）打开命令行，运行：

```bash
# 添加远程仓库（替换成你的仓库地址）
git remote add origin https://github.com/tanzhijianshifeifuhua/github-navigator.git

# 推送代码
git branch -M main
git push -u origin main
```

如果提示输入用户名和密码：
- Username: tanzhijianshifeifuhua
- Password: 使用 Personal Access Token（不是密码）

### 如何获取 Personal Access Token：
1. 访问：https://github.com/settings/tokens
2. 点击 "Generate new token" → "Generate new token (classic)"
3. Note（备注）：填写 "Vercel Deploy"
4. Expiration（过期时间）：选择 "No expiration"（永不过期）
5. 勾选权限：
   - ✅ repo（所有）
6. 点击 "Generate token"
7. **复制生成的 token**（只显示一次，请保存好）
8. 在命令行输入密码时，粘贴这个 token

## 第三步：部署到 Vercel

1. 访问：https://vercel.com
2. 点击 "Sign Up"（注册）或 "Log In"（登录）
3. 选择 "Continue with GitHub"（使用 GitHub 登录）
4. 授权 Vercel 访问你的 GitHub 账号
5. 点击 "Import Project"（导入项目）
6. 选择你刚创建的仓库：`github-navigator`
7. 配置项目：
   - Framework Preset: 选择 **Other**
   - Root Directory: 保持默认（./）
   - Build Command: 留空
   - Output Directory: 留空
   - Install Command: 留空
8. 点击 **Deploy**（部署）

## 第四步：等待部署完成

- Vercel 会自动构建和部署你的项目
- 大约 1-2 分钟后完成
- 部署成功后，会显示访问地址，类似：
  ```
  https://github-navigator-xxx.vercel.app
  ```

## 第五步：访问你的网站

点击 Vercel 提供的链接，就能看到你的网站了！🎉

---

## 常见问题

### Q: 推送代码时提示 "Permission denied"？
A: 需要使用 Personal Access Token 而不是密码

### Q: Vercel 部署失败？
A: 检查 `requirements.txt` 和 `vercel.json` 是否正确

### Q: 网站显示 404？
A: 确保 `github_projects.json` 已经提交到仓库

### Q: 如何更新网站内容？
A: 修改代码后，运行：
```bash
git add .
git commit -m "更新内容"
git push
```
Vercel 会自动重新部署

---

## 需要帮助？

如果遇到问题，可以：
1. 检查 Vercel 的部署日志
2. 查看 GitHub 仓库是否有所有文件
3. 确认 `github_projects.json` 文件已上传

祝部署顺利！🚀
