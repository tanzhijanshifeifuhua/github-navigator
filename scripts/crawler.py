# -*- coding: utf-8 -*-
"""
GitHub 项目爬虫脚本
按照中文模块分类 GitHub 项目
"""

import requests
import json
import time
from datetime import datetime
import urllib3
from urllib.parse import quote

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class GitHubCrawler:
    def __init__(self, token=None):
        """
        初始化爬虫
        :param token: GitHub Personal Access Token (可选，但建议使用以提高API限制)
        """
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"
        
        # 中文分类模块
        self.categories = {
            "前端开发": ["react", "vue", "angular", "javascript", "typescript", "css", "html", "webpack"],
            "后端开发": ["python", "java", "golang", "nodejs", "spring", "django", "flask", "express"],
            "移动开发": ["android", "ios", "flutter", "react-native", "swift", "kotlin"],
            "数据科学": ["machine-learning", "deep-learning", "data-analysis", "pandas", "numpy", "tensorflow", "pytorch"],
            "DevOps": ["docker", "kubernetes", "ci-cd", "jenkins", "ansible", "terraform"],
            "数据库": ["mysql", "postgresql", "mongodb", "redis", "elasticsearch"],
            "工具库": ["cli", "utility", "library", "framework"],
            "游戏开发": ["game", "unity", "unreal", "godot"],
            "区块链": ["blockchain", "ethereum", "bitcoin", "web3"],
            "其他": []
        }
    
    def search_repos(self, query, max_results=30):
        """
        搜索 GitHub 仓库
        """
        url = f"{self.base_url}/search/repositories"
        params = {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": max_results
        }
        
        try:
            response = requests.get(url, headers=self.headers, params=params, verify=False)
            response.raise_for_status()
            return response.json().get("items", [])
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return []
    
    def categorize_repo(self, repo):
        """
        根据关键词将仓库分类
        """
        name = repo.get("name", "").lower()
        description = repo.get("description", "").lower() if repo.get("description") else ""
        topics = [t.lower() for t in repo.get("topics", [])]
        language = repo.get("language", "").lower() if repo.get("language") else ""
        
        search_text = f"{name} {description} {' '.join(topics)} {language}"
        
        matched_categories = []
        for category, keywords in self.categories.items():
            if category == "其他":
                continue
            for keyword in keywords:
                if keyword in search_text:
                    matched_categories.append(category)
                    break
        
        return matched_categories if matched_categories else ["其他"]
    
    def translate_to_chinese(self, text):
        """
        使用免费翻译 API 将英文翻译成中文
        """
        if not text or len(text.strip()) == 0:
            return ""
        
        try:
            # 使用 Google 翻译的免费接口
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
                # 提取翻译结果
                translated = ""
                for item in result[0]:
                    if item[0]:
                        translated += item[0]
                return translated
            else:
                return text  # 翻译失败返回原文
        except Exception as e:
            print(f"    翻译失败: {e}")
            return text  # 翻译失败返回原文
    
    def extract_repo_info(self, repo):
        """
        提取仓库关键信息
        """
        description = repo.get("description")
        description_cn = ""
        
        # 翻译描述
        if description:
            print(f"    正在翻译描述...")
            description_cn = self.translate_to_chinese(description)
            time.sleep(0.5)  # 避免翻译 API 限制
        
        return {
            "name": repo.get("name"),
            "full_name": repo.get("full_name"),
            "description": description,
            "description_cn": description_cn,  # 添加中文描述
            "url": repo.get("html_url"),
            "stars": repo.get("stargazers_count"),
            "forks": repo.get("forks_count"),
            "language": repo.get("language"),
            "topics": repo.get("topics", []),
            "updated_at": repo.get("updated_at")
        }
    
    def crawl_and_categorize(self, queries=None, max_per_query=30):
        """
        爬取并分类项目
        """
        if queries is None:
            queries = ["stars:>1000", "stars:>5000", "stars:>10000"]
        
        categorized_repos = {category: [] for category in self.categories.keys()}
        seen_repos = set()
        
        for query in queries:
            print(f"正在搜索: {query}")
            repos = self.search_repos(query, max_per_query)
            
            for repo in repos:
                repo_id = repo.get("id")
                if repo_id in seen_repos:
                    continue
                
                seen_repos.add(repo_id)
                repo_info = self.extract_repo_info(repo)
                categories = self.categorize_repo(repo)
                
                for category in categories:
                    categorized_repos[category].append(repo_info)
                
                print(f"  - {repo_info['full_name']} -> {', '.join(categories)}")
            
            time.sleep(2)  # 避免API限制
        
        return categorized_repos
    
    def save_to_json(self, data, filename="github_projects.json"):
        """
        保存数据到JSON文件
        """
        output = {
            "updated_at": datetime.now().isoformat(),
            "total_projects": sum(len(repos) for repos in data.values()),
            "categories": data
        }
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        
        print(f"\n数据已保存到 {filename}")
        print(f"总共分类了 {output['total_projects']} 个项目")


if __name__ == "__main__":
    # 使用示例
    # 建议设置 GitHub Token: token = "your_github_token_here"
    crawler = GitHubCrawler(token=None)
    
    # 扩展搜索查询 - 大幅增加项目数量
    queries = [
        # 高星项目
        "stars:>10000",
        "stars:5000..10000",
        "stars:3000..5000",
        
        # 按语言分类
        "language:python stars:>3000",
        "language:javascript stars:>3000",
        "language:typescript stars:>3000",
        "language:java stars:>3000",
        "language:go stars:>2000",
        "language:rust stars:>2000",
        "language:cpp stars:>2000",
        "language:c stars:>2000",
        
        # 前端相关
        "react stars:>2000",
        "vue stars:>2000",
        "angular stars:>1000",
        
        # 后端相关
        "django stars:>1000",
        "flask stars:>1000",
        "spring stars:>1000",
        "nodejs stars:>2000",
        
        # 移动开发
        "android stars:>2000",
        "ios stars:>1000",
        "flutter stars:>1000",
        
        # 数据科学/AI
        "machine-learning stars:>2000",
        "deep-learning stars:>1000",
        "artificial-intelligence stars:>1000",
        
        # DevOps
        "docker stars:>2000",
        "kubernetes stars:>1000",
        
        # 工具类
        "cli stars:>1000",
        "awesome stars:>3000"
    ]
    
    # 爬取并分类 - 每个查询获取更多项目
    categorized_data = crawler.crawl_and_categorize(queries, max_per_query=50)
    
    # 保存结果
    crawler.save_to_json(categorized_data)
