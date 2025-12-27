# -*- coding: utf-8 -*-
import json

with open("github_projects.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("前端开发项目示例（前5个）：\n")
for project in data["categories"]["前端开发"][:5]:
    print(f"项目: {project['name']}")
    print(f"中文描述: {project.get('description_cn', '无')}")
    print(f"原描述: {project.get('description', '无')}")
    print("-" * 60)
