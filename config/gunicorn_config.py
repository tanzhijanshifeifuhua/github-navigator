# Gunicorn 配置文件

# 绑定地址和端口
bind = "0.0.0.0:5000"

# 工作进程数（建议：CPU 核心数 * 2 + 1）
workers = 4

# 工作模式
worker_class = "sync"

# 超时时间（秒）
timeout = 120

# 保持连接时间（秒）
keepalive = 5

# 最大请求数（防止内存泄漏）
max_requests = 1000
max_requests_jitter = 50

# 日志
accesslog = "-"  # 输出到 stdout
errorlog = "-"   # 输出到 stderr
loglevel = "info"

# 进程名称
proc_name = "github-navigator"

# 优雅重启
graceful_timeout = 30

# 预加载应用
preload_app = True
