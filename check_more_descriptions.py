# -*- coding: utf-8 -*-
import json

with open("github_projects.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 检查不同分类的项目
categories_to_check = ["后端开发", "数据科学", "DevOps", "移动开发"]

for category in categories_to_check:
    if category in data["categories"]:
        print(f"\n{'='*60}")
        print(f"{category} 项目示例（前3个）：")
        print(f"{'='*60}\n")
        
        for project in data["categories"][category][:3]:
            print(f"项目: {project['name']}")
            print(f"中文描述: {project.get('description_cn', '无')}")
            print(f"原描述: {project.get('description', '无')[:100]}...")
            print("-" * 60)
