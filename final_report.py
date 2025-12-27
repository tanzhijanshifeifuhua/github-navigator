# -*- coding: utf-8 -*-
import json

with open("github_projects.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("="*70)
print("GitHub 项目中文分类导航系统 - 最终报告")
print("="*70)
print(f"\n📊 总体统计:")
print(f"  - 项目总数: {data['total_projects']}")
print(f"  - 最后更新: {data['updated_at'][:19]}")

print(f"\n📂 分类统计:")
sorted_categories = sorted(data['categories'].items(), key=lambda x: len(x[1]), reverse=True)
for category, projects in sorted_categories:
    print(f"  - {category}: {len(projects)} 个项目")

print(f"\n✅ 中文描述覆盖率:")
total = 0
with_cn = 0
for category, projects in data['categories'].items():
    for project in projects:
        total += 1
        if project.get('description_cn'):
            with_cn += 1

coverage = (with_cn / total * 100) if total > 0 else 0
print(f"  - 已添加中文描述: {with_cn}/{total} ({coverage:.1f}%)")

print(f"\n🌟 热门项目示例（前10个）:")
all_projects = []
for projects in data['categories'].values():
    all_projects.extend(projects)

# 按星标排序
all_projects.sort(key=lambda x: x.get('stars', 0), reverse=True)

for i, project in enumerate(all_projects[:10], 1):
    print(f"\n  {i}. {project['name']} ⭐ {project['stars']:,}")
    print(f"     {project.get('description_cn', '无描述')}")

print("\n" + "="*70)
print("🎉 系统已就绪！访问 http://localhost:5000 查看完整列表")
print("="*70)
