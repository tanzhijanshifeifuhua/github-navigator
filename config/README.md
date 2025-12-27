# 配置文件说明

## Docker 相关

- `Dockerfile` - Docker 镜像构建文件
- `docker-compose.yml` - Docker Compose 配置

## Web 服务器配置

- `gunicorn_config.py` - Gunicorn WSGI 服务器配置
- `nginx.conf` - Nginx 反向代理配置
- `github-navigator.service` - Systemd 服务配置

## 部署平台配置

- `vercel.json` - Vercel 部署配置

## 使用说明

### Docker 部署
```bash
cd config
docker-compose up -d
```

### Gunicorn 启动
```bash
gunicorn -c config/gunicorn_config.py app:app
```

### Nginx 配置
```bash
sudo cp config/nginx.conf /etc/nginx/sites-available/github-navigator
sudo ln -s /etc/nginx/sites-available/github-navigator /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```
