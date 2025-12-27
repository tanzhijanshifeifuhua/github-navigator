# -*- coding: utf-8 -*-
"""
Flask Web 应用 - 展示分类后的 GitHub 项目
"""

from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# 生产环境配置
if os.environ.get('FLASK_ENV') == 'production':
    app.config['DEBUG'] = False
else:
    app.config['DEBUG'] = True

def load_data():
    """加载项目数据"""
    if os.path.exists("github_projects.json"):
        with open("github_projects.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"categories": {}, "total_projects": 0, "updated_at": "未更新"}

@app.route("/")
def index():
    """主页"""
    data = load_data()
    return render_template("index.html", data=data)

@app.route("/api/projects")
def api_projects():
    """API接口 - 返回所有项目数据"""
    data = load_data()
    return jsonify(data)

@app.route("/api/category/<category_name>")
def api_category(category_name):
    """API接口 - 返回特定分类的项目"""
    data = load_data()
    category_data = data.get("categories", {}).get(category_name, [])
    return jsonify({"category": category_name, "projects": category_data})

@app.route("/health")
def health():
    """健康检查端点"""
    data = load_data()
    return jsonify({
        "status": "healthy",
        "total_projects": data.get("total_projects", 0),
        "updated_at": data.get("updated_at", "unknown")
    })

if __name__ == "__main__":
    # 获取端口（Railway 会设置 PORT 环境变量）
    port = int(os.environ.get("PORT", 5000))
    # 开发环境运行
    app.run(debug=True, host="0.0.0.0", port=port)
else:
    # 生产环境（被 Gunicorn 等 WSGI 服务器调用）
    pass
