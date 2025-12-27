# -*- coding: utf-8 -*-
"""
为项目添加中文描述 - 使用简单的关键词映射
"""

import json

# 常见项目类型的中文描述模板
description_templates = {
    # 编程语言
    "python": "Python 编程语言相关项目",
    "javascript": "JavaScript 编程语言相关项目",
    "typescript": "TypeScript 编程语言相关项目",
    "java": "Java 编程语言相关项目",
    "go": "Go 编程语言相关项目",
    "rust": "Rust 编程语言相关项目",
    
    # 框架
    "react": "React 前端框架",
    "vue": "Vue.js 前端框架",
    "angular": "Angular 前端框架",
    "django": "Django Web 框架",
    "flask": "Flask Web 框架",
    "spring": "Spring 框架",
    "express": "Express.js 后端框架",
    
    # 工具
    "docker": "Docker 容器化工具",
    "kubernetes": "Kubernetes 容器编排平台",
    "git": "Git 版本控制工具",
    
    # 关键词映射
    "algorithm": "算法",
    "tutorial": "教程",
    "learning": "学习资源",
    "awesome": "精选资源列表",
    "framework": "框架",
    "library": "库",
    "tool": "工具",
    "guide": "指南",
    "interview": "面试",
    "roadmap": "学习路线图",
    "course": "课程",
    "book": "书籍",
    "cheatsheet": "速查表",
    "machine learning": "机器学习",
    "deep learning": "深度学习",
    "artificial intelligence": "人工智能",
    "data science": "数据科学",
    "web development": "Web 开发",
    "mobile": "移动开发",
    "android": "Android 开发",
    "ios": "iOS 开发",
    "game": "游戏开发",
    "blockchain": "区块链",
    "devops": "DevOps",
    "database": "数据库",
}

# 特定项目的中文描述（大幅扩展）
specific_descriptions = {
    # 学习资源
    "freeCodeCamp": "免费学习编程的开源平台，提供数学、编程和计算机科学的完整课程体系",
    "developer-roadmap": "开发者学习路线图，提供前端、后端、DevOps 等方向的交互式学习指南",
    "coding-interview-university": "编程面试大学 - 完整的计算机科学学习计划，涵盖算法、数据结构等核心知识",
    "system-design-primer": "系统设计入门指南，学习如何设计可扩展的大型分布式系统",
    "build-your-own-x": "通过从零构建技术来学习，包含数据库、编译器、游戏引擎等项目教程",
    "awesome": "各种精选资源列表的集合，涵盖编程、开发工具、学习资源等",
    "public-apis": "免费 API 集合，提供各类公共 API 接口用于开发和学习",
    "free-programming-books": "免费编程书籍大全，包含多种编程语言和技术的电子书资源",
    "project-based-learning": "基于项目的编程教程集合，通过实战项目学习各种编程语言",
    "You-Dont-Know-JS": "深入理解 JavaScript 系列书籍，详解 JS 语言核心机制",
    "CS-Notes": "技术面试必备基础知识，涵盖算法、操作系统、网络、数据库等",
    "Python-100-Days": "Python 100 天从新手到大师的完整学习路线",
    "the-art-of-command-line": "命令行的艺术 - Linux/Unix 命令行使用技巧和最佳实践",
    "tech-interview-handbook": "技术面试手册，包含算法题解、面试技巧和职业建议",
    "javascript-algorithms": "JavaScript 实现的算法和数据结构，附带详细解释和相关阅读",
    "fucking-algorithm": "labuladong 的算法小抄，用动画形式讲解算法原理",
    "hello-algo": "动画图解、一键运行的数据结构与算法教程",
    "interviews": "软件工程技术面试个人指南",
    "LeetCodeAnimation": "用动画的形式呈现解 LeetCode 题目的思路",
    "JavaGuide": "Java 学习和面试指南，涵盖 Java 核心知识点",
    "advanced-java": "互联网 Java 工程师进阶知识完全扫盲",
    
    # 前端框架
    "react": "Facebook 开发的用于构建用户界面的 JavaScript 库，采用组件化和虚拟 DOM",
    "vue": "渐进式 JavaScript 框架，易学易用，性能出色，适用于构建单页应用",
    "angular": "Google 开发的企业级前端框架，提供完整的开发解决方案",
    "svelte": "编译时框架，无虚拟 DOM，生成高效的原生 JavaScript 代码",
    "next.js": "React 服务端渲染框架，支持静态生成和服务端渲染，适合生产环境",
    "nuxt": "Vue.js 的服务端渲染框架，简化 Vue 应用的开发和部署",
    "gatsby": "基于 React 的静态站点生成器，性能优异，适合博客和文档站点",
    "astro": "现代静态站点构建工具，支持多框架组件，性能优先",
    "remix": "全栈 Web 框架，专注于 Web 标准和现代用户体验",
    
    # UI 组件库
    "bootstrap": "最流行的 HTML、CSS 和 JavaScript 框架，快速构建响应式网站",
    "material-ui": "React 的 Material Design 组件库，提供丰富的 UI 组件",
    "ant-design": "蚂蚁集团开发的企业级 UI 设计语言和 React 组件库",
    "tailwindcss": "实用优先的 CSS 框架，通过组合类名快速构建界面",
    "shadcn-ui": "基于 Radix UI 和 Tailwind CSS 的可复用组件集合",
    "Semantic-UI": "语义化的 UI 组件框架，使用友好的 HTML 语法",
    "Font-Awesome": "最流行的图标字体库，提供数千个矢量图标",
    
    # 后端框架
    "django": "Python 高级 Web 框架，快速开发、安全可靠，内置管理后台",
    "flask": "Python 轻量级 Web 框架，灵活简洁，适合小型应用和 API 开发",
    "fastapi": "现代、快速的 Python Web 框架，基于类型提示，自动生成 API 文档",
    "express": "Node.js 最流行的 Web 应用框架，简洁灵活",
    "spring-boot": "Spring 框架的快速开发脚手架，简化 Java Web 应用开发",
    "spring-framework": "Java 企业级应用开发框架，提供依赖注入和面向切面编程",
    "gin": "Go 语言高性能 Web 框架，API 简洁，性能出色",
    "fiber": "Go 语言 Web 框架，受 Express 启发，性能极高",
    "nest": "Node.js 渐进式框架，使用 TypeScript 构建高效可扩展的服务端应用",
    
    # 开发工具
    "vscode": "微软开发的免费开源代码编辑器，功能强大，插件丰富",
    "atom": "GitHub 开发的可定制文本编辑器",
    "vim": "高效的文本编辑器，支持丰富的插件和自定义",
    "neovim": "Vim 的现代化重构版本，性能更好，扩展性更强",
    "zed": "高性能的多人协作代码编辑器",
    "cursor": "AI 驱动的代码编辑器",
    
    # 构建工具
    "webpack": "模块打包工具，将各种资源打包成浏览器可用的文件",
    "vite": "下一代前端构建工具，开发时极速热更新",
    "esbuild": "极速 JavaScript 打包工具，使用 Go 编写",
    "rollup": "JavaScript 模块打包器，适合构建库",
    "turbo": "高性能构建系统，支持增量构建和远程缓存",
    "turborepo": "高性能的 Monorepo 构建系统",
    
    # AI/机器学习
    "tensorflow": "Google 开发的端到端开源机器学习平台",
    "pytorch": "Facebook 开发的深度学习框架，灵活易用，科研首选",
    "keras": "高层神经网络 API，简化深度学习模型的构建",
    "transformers": "Hugging Face 的预训练模型库，提供 BERT、GPT 等最先进的 NLP 模型",
    "langchain": "构建 LLM 应用的框架，简化大语言模型的集成和使用",
    "AutoGPT": "自主 AI 代理实验项目，让 GPT-4 自主完成任务",
    "gpt4free": "免费使用 GPT-4/3.5 的逆向工程项目",
    "ollama": "在本地运行大语言模型的工具，支持 Llama、Mistral 等模型",
    "llama.cpp": "C++ 实现的 LLaMA 模型推理引擎，可在 CPU 上运行",
    "whisper": "OpenAI 的自动语音识别模型，支持多语言转录和翻译",
    "stable-diffusion-webui": "Stable Diffusion 的 Web 用户界面，功能强大的 AI 绘画工具",
    "ComfyUI": "强大且模块化的 Stable Diffusion GUI，支持节点式工作流",
    "gpt_academic": "为 GPT/GLM 提供图形交互界面，特别优化学术场景",
    "MetaGPT": "多智能体框架，让 GPT 扮演不同角色协作完成复杂任务",
    "DeepSeek-V3": "DeepSeek 开源的大语言模型",
    "LLaMA-Factory": "易用的 LLM 微调框架，支持多种模型",
    "LocalAI": "本地运行的 OpenAI 兼容 API，支持多种开源模型",
    
    # 数据科学
    "scikit-learn": "Python 机器学习库，提供分类、回归、聚类等算法",
    "pandas": "Python 数据分析库，提供高性能的数据结构和分析工具",
    "numpy": "Python 科学计算基础库，提供多维数组和矩阵运算",
    "matplotlib": "Python 绘图库，创建静态、动态和交互式可视化",
    "jupyter": "交互式计算环境，支持多种编程语言",
    "streamlit": "快速构建数据应用的 Python 框架",
    "gradio": "快速创建机器学习模型演示界面的 Python 库",
    
    # DevOps
    "kubernetes": "容器编排平台，自动化部署、扩展和管理容器化应用",
    "docker": "容器化平台，将应用及其依赖打包成可移植的容器",
    "terraform": "基础设施即代码工具，声明式管理云资源",
    "ansible": "自动化运维工具，简化配置管理和应用部署",
    "jenkins": "开源持续集成工具，自动化构建、测试和部署",
    "gitlab": "完整的 DevOps 平台，集成代码托管、CI/CD 和项目管理",
    "prometheus": "开源监控和告警系统，专为云原生环境设计",
    "grafana": "开源数据可视化和监控平台",
    "traefik": "现代化的反向代理和负载均衡器，原生支持容器",
    "nginx": "高性能 Web 服务器和反向代理服务器",
    
    # 数据库
    "redis": "内存数据库，支持多种数据结构，常用于缓存和消息队列",
    "mongodb": "NoSQL 文档数据库，灵活的数据模型",
    "postgresql": "强大的开源关系型数据库",
    "mysql": "最流行的开源关系型数据库",
    "elasticsearch": "分布式搜索和分析引擎",
    "supabase": "开源的 Firebase 替代品，提供数据库、认证、存储等服务",
    "prisma": "下一代 ORM，类型安全的数据库访问",
    
    # 移动开发
    "flutter": "Google 的跨平台 UI 框架，一套代码构建 iOS、Android、Web 应用",
    "react-native": "Facebook 的跨平台移动应用框架，使用 React 开发原生应用",
    "ionic": "跨平台移动应用框架，基于 Web 技术",
    "expo": "React Native 开发平台，简化移动应用开发流程",
    
    # 工具库
    "lodash": "JavaScript 实用工具库，提供数组、对象、函数等操作方法",
    "axios": "基于 Promise 的 HTTP 客户端，支持浏览器和 Node.js",
    "moment": "JavaScript 日期处理库",
    "dayjs": "轻量级的日期处理库，兼容 Moment.js API",
    "three.js": "JavaScript 3D 图形库，简化 WebGL 开发",
    "chart.js": "简单灵活的 JavaScript 图表库",
    "d3": "数据驱动的文档操作库，创建动态交互式数据可视化",
    
    # 其他工具
    "git": "分布式版本控制系统",
    "github": "代码托管平台",
    "PowerToys": "微软 Windows 系统实用工具集，提升工作效率",
    "scrcpy": "Android 设备屏幕镜像和控制工具，低延迟高性能",
    "frp": "内网穿透工具，将内网服务暴露到公网",
    "v2ray": "网络代理工具",
    "clash": "多平台代理客户端",
    "uptime-kuma": "自托管的服务监控工具，界面美观",
    "n8n": "工作流自动化工具，可视化编排自动化任务",
    "appwrite": "开源的后端即服务平台，提供认证、数据库、存储等功能",
    "pocketbase": "单文件后端，提供实时数据库、认证、文件存储",
    "strapi": "开源的无头 CMS，快速构建 API",
    "ghost": "专业的开源博客平台",
    "wordpress": "最流行的内容管理系统",
    "hugo": "快速的静态网站生成器，使用 Go 编写",
    "hexo": "快速、简洁的博客框架",
    "docusaurus": "Facebook 开发的文档网站生成器",
    "vuepress": "Vue 驱动的静态网站生成器",
    "gitbook": "现代化的文档平台",
    "mkdocs": "快速、简单的项目文档工具",
    "docsify": "神奇的文档网站生成器",
    "slidev": "为开发者打造的演示文稿工具",
    "reveal.js": "HTML 演示文稿框架，创建精美的幻灯片",
    "impress.js": "基于 CSS3 的演示框架",
    "marp": "Markdown 演示文稿生态系统",
    "excalidraw": "虚拟白板工具，用于绘制手绘风格的图表",
    "drawio": "免费的在线图表绘制工具",
    "mermaid": "用文本生成图表和流程图",
    "marktext": "简洁优雅的 Markdown 编辑器",
    "typora": "极简的 Markdown 编辑器",
    "obsidian": "强大的知识管理工具",
    "notion": "一体化的工作空间",
    "joplin": "开源的笔记和待办事项应用",
    "logseq": "隐私优先的知识管理工具",
    "affine": "下一代知识库，融合笔记、白板和数据库",
    "anytype": "本地优先的知识管理工具",
    
    # 更多常见项目
    "ohmyzsh": "Oh My Zsh - 优雅的 Zsh 配置管理框架，提供丰富的插件和主题",
    "linux": "Linux 操作系统内核源代码",
    "rust": "Rust 编程语言官方仓库",
    "go": "Go 编程语言官方仓库",
    "cpython": "Python 编程语言的官方实现",
    "node": "Node.js JavaScript 运行时环境",
    "deno": "现代化的 JavaScript/TypeScript 运行时，安全且高效",
    "bun": "极速的 JavaScript 运行时和包管理器",
    
    # GitHub 相关
    "gitignore": "各种编程语言和框架的 .gitignore 文件模板集合",
    "github-readme-stats": "动态生成 GitHub 统计卡片，美化个人主页",
    "shields": "为项目生成徽章图标",
    
    # 算法和数据结构
    "TheAlgorithms": "各种编程语言实现的算法集合",
    "leetcode": "LeetCode 题解集合",
    "algorithm-visualizer": "算法可视化工具，动画展示算法执行过程",
    
    # 精选列表
    "awesome-python": "Python 精选资源列表，包含框架、库、软件等",
    "awesome-go": "Go 语言精选资源列表",
    "awesome-java": "Java 精选资源列表",
    "awesome-javascript": "JavaScript 精选资源列表",
    "awesome-mac": "macOS 优质软件精选列表",
    "awesome-selfhosted": "可自托管的开源软件列表",
    "awesome-chatgpt-prompts": "ChatGPT 提示词精选集合",
    "awesome-vue": "Vue.js 精选资源列表",
    "awesome-react": "React 精选资源列表",
    "awesome-flutter": "Flutter 精选资源列表",
    "awesome-nodejs": "Node.js 精选资源列表",
    "awesome-cpp": "C++ 精选资源列表",
    
    # 更多工具
    "thefuck": "命令行错误自动纠正工具，自动修正输入错误的命令",
    "fzf": "命令行模糊查找工具，快速搜索文件和历史命令",
    "ripgrep": "极速的文本搜索工具，比 grep 更快",
    "bat": "cat 命令的现代化替代品，支持语法高亮",
    "fd": "find 命令的现代化替代品，更快更友好",
    "exa": "ls 命令的现代化替代品",
    "zoxide": "更智能的 cd 命令，记住常用目录",
    "starship": "极简、快速的跨平台命令行提示符",
    "lazygit": "Git 的终端 UI 工具，简化 Git 操作",
    "lazydocker": "Docker 的终端 UI 工具，简化容器管理",
    "dive": "Docker 镜像分析工具，优化镜像大小",
    "act": "在本地运行 GitHub Actions",
    "mkcert": "本地 HTTPS 证书生成工具",
    
    # 更多 AI 项目
    "transformers": "Hugging Face 的预训练模型库，提供 BERT、GPT 等最先进的 NLP 模型",
    "huggingface": "Hugging Face 的预训练模型库",
    "gpt4all": "在本地运行 GPT 模型的工具",
    "text-generation-webui": "大语言模型的 Web UI，类似 ChatGPT 界面",
    "oobabooga": "大语言模型的 Web UI",
    "chatgpt-next-web": "一键部署的 ChatGPT 网页应用",
    "lobe-chat": "现代化的 ChatGPT/LLM 聊天框架",
    "open-interpreter": "让 LLM 在本地运行代码",
    "screenshot-to-code": "将截图转换为代码的 AI 工具",
    "gpt_academic": "为学术研究优化的 GPT 交互界面",
    "browser-use": "让 AI 使用浏览器完成任务",
    "Deep-Live-Cam": "实时深度学习换脸工具",
    "GFPGAN": "AI 人脸修复工具，提升照片质量",
    "Real-Time-Voice-Cloning": "实时语音克隆工具",
    "MockingBird": "中文语音克隆工具",
    "TTS": "文本转语音工具",
    "yolov5": "YOLOv5 目标检测模型",
    "ultralytics": "YOLO 系列目标检测工具",
    "PaddleOCR": "百度开源的 OCR 工具，支持多语言文字识别",
    "tesseract": "开源 OCR 引擎",
    "opencv": "计算机视觉库",
    "mediapipe": "Google 的跨平台机器学习解决方案",
    "faiss": "Facebook 的相似性搜索库",
    "ColossalAI": "大模型训练加速工具",
    "DeepSpeed": "微软的深度学习优化库",
    "vllm": "高性能 LLM 推理引擎",
    "ray": "分布式计算框架",
    
    # 更多数据库
    "clickhouse": "高性能列式数据库",
    "dragonfly": "现代化的内存数据库，兼容 Redis",
    "surrealdb": "多模型数据库",
    "tidb": "分布式 SQL 数据库",
    "yugabyte": "分布式 SQL 数据库",
    "cockroachdb": "分布式 SQL 数据库",
    "milvus": "向量数据库，用于 AI 应用",
    "qdrant": "向量搜索引擎",
    "weaviate": "向量数据库",
    
    # 更多 DevOps
    "portainer": "Docker 和 Kubernetes 的可视化管理工具",
    "rancher": "Kubernetes 管理平台",
    "k9s": "Kubernetes 终端 UI 工具",
    "lens": "Kubernetes IDE",
    "minikube": "本地 Kubernetes 环境",
    "k3s": "轻量级 Kubernetes 发行版",
    "helm": "Kubernetes 包管理器",
    "argocd": "Kubernetes 的 GitOps 持续交付工具",
    "flux": "GitOps 工具",
    "tekton": "Kubernetes 原生 CI/CD 框架",
    "drone": "容器原生的 CI/CD 平台",
    "woodpecker": "轻量级 CI/CD 引擎",
    "gitea": "轻量级的 Git 服务",
    "gogs": "轻量级的 Git 服务",
    "gitlab": "完整的 DevOps 平台",
    "harbor": "容器镜像仓库",
    "nexus": "制品仓库管理器",
    "artifactory": "通用制品仓库",
    "vault": "密钥管理工具",
    "consul": "服务发现和配置工具",
    "etcd": "分布式键值存储",
    "zookeeper": "分布式协调服务",
    "nacos": "动态服务发现和配置管理平台",
    "apollo": "配置中心",
    "seata": "分布式事务解决方案",
    "sentinel": "流量控制和熔断降级工具",
    "skywalking": "分布式追踪系统",
    "jaeger": "分布式追踪系统",
    "zipkin": "分布式追踪系统",
    "opentelemetry": "可观测性框架",
    "loki": "日志聚合系统",
    "fluentd": "日志收集工具",
    "logstash": "日志处理管道",
    "filebeat": "轻量级日志采集器",
    "vector": "高性能日志和指标路由器",
    "netdata": "实时性能监控工具",
    "zabbix": "企业级监控解决方案",
    "nagios": "IT 基础设施监控工具",
    "icinga": "监控系统",
    "checkmk": "IT 监控解决方案",
    "uptime-kuma": "自托管的服务监控工具，界面美观易用",
    "statping": "服务状态监控工具",
    "cachet": "状态页面系统",
    
    # 更多前端工具
    "prettier": "代码格式化工具，支持多种语言",
    "eslint": "JavaScript 代码检查工具",
    "stylelint": "CSS 代码检查工具",
    "husky": "Git hooks 工具",
    "lint-staged": "对暂存文件运行 linters",
    "commitlint": "Git commit 信息检查工具",
    "semantic-release": "自动化版本管理和发布",
    "changesets": "Monorepo 版本管理工具",
    "lerna": "Monorepo 管理工具",
    "nx": "智能 Monorepo 构建系统",
    "pnpm": "快速、节省磁盘空间的包管理器",
    "yarn": "快速、可靠的包管理器",
    "npm": "Node.js 包管理器",
    "bun": "极速的 JavaScript 运行时和包管理器",
    
    # 更多后端工具
    "redis": "高性能内存数据库，支持多种数据结构",
    "kafka": "分布式流处理平台",
    "rabbitmq": "消息队列中间件",
    "rocketmq": "分布式消息中间件",
    "pulsar": "分布式消息系统",
    "nats": "轻量级消息系统",
    "mqtt": "物联网消息协议",
    "grpc": "高性能 RPC 框架",
    "protobuf": "Protocol Buffers 数据序列化格式",
    "thrift": "跨语言服务开发框架",
    "dubbo": "高性能 RPC 框架",
    "netty": "异步事件驱动的网络应用框架",
    "vert.x": "响应式应用工具包",
    "quarkus": "Kubernetes 原生 Java 框架",
    "micronaut": "现代化的 JVM 框架",
    "helidon": "轻量级微服务框架",
    
    # 更多移动开发
    "expo": "React Native 开发平台",
    "ionic": "跨平台移动应用框架",
    "capacitor": "跨平台原生运行时",
    "cordova": "移动应用开发框架",
    "nativescript": "原生移动应用框架",
    "xamarin": "跨平台移动开发框架",
    "kotlin": "Kotlin 编程语言",
    "swift": "Swift 编程语言",
    "swiftui": "Swift UI 框架",
    "jetpack-compose": "Android 现代 UI 工具包",
    
    # 更多测试工具
    "jest": "JavaScript 测试框架",
    "vitest": "Vite 原生测试框架",
    "mocha": "JavaScript 测试框架",
    "chai": "断言库",
    "cypress": "端到端测试框架",
    "playwright": "浏览器自动化测试工具",
    "puppeteer": "Chrome 无头浏览器控制工具",
    "selenium": "Web 应用测试工具",
    "appium": "移动应用测试工具",
    "detox": "React Native 端到端测试框架",
    "junit": "Java 测试框架",
    "testng": "Java 测试框架",
    "pytest": "Python 测试框架",
    "unittest": "Python 单元测试框架",
    "rspec": "Ruby 测试框架",
    "phpunit": "PHP 测试框架",
    "go-test": "Go 测试工具",
    "cargo-test": "Rust 测试工具",
}

def generate_chinese_description(project):
    """为项目生成中文描述"""
    name = project.get("name", "").lower()
    full_name = project.get("full_name", "").lower()
    description = project.get("description") or ""
    description_lower = description.lower()
    topics = [t.lower() for t in project.get("topics", [])]
    
    # 1. 检查是否有特定项目的描述（精确匹配项目名）
    if name in specific_descriptions:
        return specific_descriptions[name]
    
    # 2. 检查 full_name 中的组织名/项目名组合
    for key, value in specific_descriptions.items():
        if key.lower() in full_name:
            return value
    
    # 3. 检查项目名称中的关键词（部分匹配，按长度排序优先匹配长关键词）
    sorted_keys = sorted(specific_descriptions.keys(), key=len, reverse=True)
    for key in sorted_keys:
        if key.lower() in name:
            return specific_descriptions[key]
    
    # 3. 根据 topics 标签匹配
    topic_keywords = {
        "react": "React 相关项目",
        "vue": "Vue.js 相关项目",
        "angular": "Angular 相关项目",
        "python": "Python 相关项目",
        "javascript": "JavaScript 相关项目",
        "typescript": "TypeScript 相关项目",
        "machine-learning": "机器学习相关项目",
        "deep-learning": "深度学习相关项目",
        "artificial-intelligence": "人工智能相关项目",
        "docker": "Docker 容器化相关项目",
        "kubernetes": "Kubernetes 容器编排相关项目",
        "android": "Android 开发相关项目",
        "ios": "iOS 开发相关项目",
        "flutter": "Flutter 跨平台开发相关项目",
        "game": "游戏开发相关项目",
        "blockchain": "区块链相关项目",
        "devops": "DevOps 相关项目",
        "cli": "命令行工具",
        "api": "API 相关项目",
        "framework": "开发框架",
        "library": "开发库",
    }
    
    for topic in topics:
        if topic in topic_keywords:
            return topic_keywords[topic]
    
    # 4. 根据描述内容智能匹配
    description_patterns = {
        # 学习资源
        "tutorial": "编程教程和学习资源",
        "learning": "学习资源和教程",
        "course": "在线课程和学习材料",
        "book": "编程书籍和文档",
        "guide": "开发指南和最佳实践",
        "roadmap": "技术学习路线图",
        "interview": "技术面试准备资料",
        "cheatsheet": "技术速查表和参考手册",
        "awesome": "精选资源列表",
        "collection": "资源集合",
        
        # 框架和库
        "framework": "开发框架",
        "library": "开发库",
        "toolkit": "工具包",
        "boilerplate": "项目模板和脚手架",
        "starter": "项目启动模板",
        "template": "项目模板",
        
        # 工具
        "tool": "开发工具",
        "cli": "命令行工具",
        "editor": "代码编辑器",
        "ide": "集成开发环境",
        "extension": "扩展插件",
        "plugin": "插件",
        
        # 前端
        "ui component": "UI 组件库",
        "component library": "组件库",
        "css framework": "CSS 框架",
        "responsive": "响应式设计工具",
        "animation": "动画库",
        "visualization": "数据可视化工具",
        "chart": "图表库",
        "3d": "3D 图形库",
        
        # 后端
        "web framework": "Web 开发框架",
        "api": "API 开发工具",
        "rest": "RESTful API 工具",
        "graphql": "GraphQL 相关工具",
        "microservice": "微服务架构工具",
        "serverless": "无服务器架构工具",
        
        # 数据库
        "database": "数据库",
        "orm": "对象关系映射工具",
        "sql": "SQL 数据库工具",
        "nosql": "NoSQL 数据库",
        "cache": "缓存系统",
        
        # AI/ML
        "machine learning": "机器学习工具",
        "deep learning": "深度学习框架",
        "neural network": "神经网络工具",
        "nlp": "自然语言处理工具",
        "computer vision": "计算机视觉工具",
        "llm": "大语言模型相关工具",
        "gpt": "GPT 相关工具",
        "ai": "人工智能工具",
        "model": "AI 模型",
        
        # DevOps
        "container": "容器化工具",
        "orchestration": "容器编排工具",
        "ci/cd": "持续集成/持续部署工具",
        "deployment": "部署工具",
        "monitoring": "监控工具",
        "logging": "日志管理工具",
        "automation": "自动化工具",
        
        # 移动开发
        "mobile": "移动应用开发工具",
        "cross-platform": "跨平台开发工具",
        "native": "原生应用开发工具",
        
        # 游戏开发
        "game engine": "游戏引擎",
        "game development": "游戏开发工具",
        
        # 安全
        "security": "安全工具",
        "encryption": "加密工具",
        "authentication": "身份认证工具",
        
        # 测试
        "testing": "测试工具",
        "test": "测试框架",
        "automation testing": "自动化测试工具",
        
        # 文档
        "documentation": "文档工具",
        "static site": "静态网站生成器",
        "blog": "博客平台",
        "cms": "内容管理系统",
        
        # 其他
        "algorithm": "算法实现和教程",
        "data structure": "数据结构实现",
        "design pattern": "设计模式示例",
        "best practice": "最佳实践指南",
        "performance": "性能优化工具",
        "productivity": "生产力工具",
    }
    
    for pattern, desc in description_patterns.items():
        if pattern in description_lower:
            return desc
    
    # 5. 根据项目名称关键词匹配
    name_patterns = {
        "awesome": "精选资源列表",
        "tutorial": "教程项目",
        "learn": "学习资源",
        "guide": "指南文档",
        "example": "示例代码",
        "demo": "演示项目",
        "sample": "示例项目",
        "starter": "启动模板",
        "boilerplate": "项目模板",
        "template": "项目模板",
        "cli": "命令行工具",
        "api": "API 工具",
        "sdk": "软件开发工具包",
        "framework": "开发框架",
        "library": "开发库",
        "tool": "开发工具",
        "app": "应用程序",
        "ui": "用户界面工具",
        "admin": "管理后台",
        "dashboard": "数据面板",
        "monitor": "监控工具",
        "bot": "机器人程序",
        "crawler": "网络爬虫",
        "scraper": "数据抓取工具",
        "parser": "解析器",
        "generator": "生成器",
        "builder": "构建工具",
        "compiler": "编译器",
        "interpreter": "解释器",
        "debugger": "调试工具",
        "profiler": "性能分析工具",
        "linter": "代码检查工具",
        "formatter": "代码格式化工具",
    }
    
    for pattern, desc in name_patterns.items():
        if pattern in name:
            return desc
    
    # 6. 返回原描述或默认值
    if description and len(description) > 0:
        return description
    
    return "优质开源项目"

# 读取数据
print("正在读取项目数据...")
with open("github_projects.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 为所有项目添加中文描述
count = 0
updated = 0
for category, projects in data["categories"].items():
    for project in projects:
        # 重新生成所有描述（不管是否已存在）
        new_desc = generate_chinese_description(project)
        old_desc = project.get("description_cn", "")
        
        project["description_cn"] = new_desc
        count += 1
        
        if old_desc != new_desc:
            updated += 1

# 保存结果
print(f"正在保存数据...")
with open("github_projects.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ 完成！")
print(f"总项目数: {data['total_projects']}")
print(f"处理项目数: {count}")
print(f"更新描述数: {updated}")
