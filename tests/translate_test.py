# -*- coding: utf-8 -*-
"""
测试翻译功能 - 只翻译前 10 个项目
"""

import json
import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def translate_to_chinese(text):
    """使用免费翻译 API 将英文翻译成中文"""
    if not text or len(text.strip()) == 0:
        return ""
    
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            "client": "gtx",
            "sl": "en",
            "tl": "zh-CN",
            "dt": "t",
            "q": text
        }
        
        response = requests.get(url, params=params, timeout=5, verify=False)
        if response.status_code == 200:
            result = response.json()
            translated = ""
            for item in result[0]:
                if item[0]:
                    translated += item[0]
            return translated
        else:
            return text
    except Exception as e:
        print(f"翻译失败: {e}")
        return text

# 读取数据
with open("github_projects.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 测试翻译前 10 个项目
count = 0
for category, projects in data["categories"].items():
    for project in projects:
        if count >= 10:
            break
        
        if not project.get("description_cn") and project.get("description"):
            print(f"\n项目: {project['name']}")
            print(f"原文: {project['description']}")
            
            translated = translate_to_chinese(project["description"])
            print(f"译文: {translated}")
            
            project["description_cn"] = translated
            count += 1
            time.sleep(1)  # 避免请求过快
    
    if count >= 10:
        break

# 保存测试结果
with open("github_projects_test.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ 测试完成！已翻译 {count} 个项目")
print("结果保存在 github_projects_test.json")
