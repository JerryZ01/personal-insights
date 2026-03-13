#!/usr/bin/env python3
"""
GitHub Stars 数据源适配器
从 GitHub API 获取用户的 starred repositories
"""

import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class GitHubStarsSource:
    """GitHub Stars 数据源"""
    
    def __init__(self, token: str, username: str):
        """
        初始化 GitHub 数据源
        
        Args:
            token: GitHub Personal Access Token
            username: GitHub 用户名
        """
        self.token = token
        self.username = username
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": f"{username}-personal-insights"
        }
        self.stars = []
    
    def fetch_stars(self, per_page: int = 100, max_pages: int = 10) -> List[Dict]:
        """
        获取用户的 starred repositories
        
        Args:
            per_page: 每页数量 (最大 100)
            max_pages: 最大页数
            
        Returns:
            starred repos 列表
        """
        all_stars = []
        page = 1
        
        while page <= max_pages:
            url = f"{self.base_url}/users/{self.username}/starred"
            params = {
                "per_page": min(per_page, 100),
                "page": page,
                "sort": "created",
                "direction": "desc"
            }
            
            try:
                response = requests.get(url, headers=self.headers, params=params, timeout=30)
                response.raise_for_status()
                
                stars = response.json()
                if not stars:
                    break
                
                all_stars.extend(stars)
                
                # 检查是否有下一页
                if len(stars) < per_page:
                    break
                
                page += 1
                
                # 小延迟避免触发速率限制
                import time
                time.sleep(0.5)
                
            except requests.exceptions.RequestException as e:
                print(f"⚠️  获取 GitHub Stars 失败：{e}")
                break
        
        self.stars = all_stars
        return all_stars
    
    def fetch_detailed_stars(self) -> List[Dict]:
        """
        获取详细的 star 信息（包括 star 时间）
        使用 /user/starred 端点需要认证
        
        Returns:
            包含 star 时间的详细信息
        """
        detailed_stars = []
        page = 1
        
        while True:
            url = f"{self.base_url}/user/starred"
            params = {
                "per_page": 100,
                "page": page,
                "sort": "created",
                "direction": "desc"
            }
            
            try:
                response = requests.get(url, headers=self.headers, params=params, timeout=30)
                response.raise_for_status()
                
                # 检查 Link header 判断是否有更多页面
                stars = response.json()
                if not stars:
                    break
                
                detailed_stars.extend(stars)
                
                # 解析 Link header
                link_header = response.headers.get('Link', '')
                if 'rel="next"' not in link_header:
                    break
                
                page += 1
                
            except requests.exceptions.RequestException as e:
                print(f"⚠️  获取详细信息失败：{e}")
                break
        
        return detailed_stars
    
    def to_bookmark_format(self) -> List[Dict]:
        """
        转换为书签格式，方便统一分析
        
        Returns:
            统一格式的书签列表
        """
        bookmarks = []
        
        for repo in self.stars:
            # 提取 star 时间
            starred_at = repo.get('starred_at', repo.get('created_at', ''))
            
            # 转换时间为 Chrome 格式时间戳（微秒，从 1601-01-01 开始）
            chrome_timestamp = ""
            if starred_at:
                try:
                    # ISO 8601 格式：2024-01-15T10:30:00Z
                    dt = datetime.fromisoformat(starred_at.replace('Z', '+00:00'))
                    # 转换为 Unix 时间戳（秒）
                    unix_timestamp = dt.timestamp()
                    # 转换为 Chrome 时间戳（微秒，从 1601-01-01 开始）
                    chrome_timestamp = str(int((unix_timestamp + 11644473600) * 1000000))
                except Exception as e:
                    pass
            
            bookmark = {
                'name': repo.get('full_name', ''),
                'url': repo.get('html_url', ''),
                'description': repo.get('description', ''),
                'language': repo.get('language', ''),
                'topics': repo.get('topics', []),
                'stargazers_count': repo.get('stargazers_count', 0),
                'forks_count': repo.get('forks_count', 0),
                'domain': 'github.com',
                'date_added': chrome_timestamp,
                'source': 'github_stars',
                'path': ['GitHub Stars', repo.get('owner', {}).get('login', ''), repo.get('name', '')]
            }
            bookmarks.append(bookmark)
        
        return bookmarks
    
    def save_to_json(self, output_path: str):
        """
        保存 stars 到 JSON 文件
        
        Args:
            output_path: 输出文件路径
        """
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            'username': self.username,
            'fetched_at': datetime.now().isoformat(),
            'total_stars': len(self.stars),
            'stars': self.stars
        }
        
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ GitHub Stars 已保存：{output}")
    
    def get_language_stats(self) -> Dict[str, int]:
        """统计编程语言分布"""
        from collections import Counter
        languages = [repo.get('language') for repo in self.stars if repo.get('language')]
        return dict(Counter(languages).most_common())
    
    def get_topic_stats(self) -> Dict[str, int]:
        """统计主题分布"""
        from collections import Counter
        topics = []
        for repo in self.stars:
            topics.extend(repo.get('topics', []))
        return dict(Counter(topics).most_common())


def main():
    """测试函数"""
    import os
    
    # 从环境变量或配置文件读取 token
    token = os.getenv('GITHUB_TOKEN', '')
    username = os.getenv('GITHUB_USERNAME', 'JerryZ01')
    
    if not token:
        print("❌ 请设置 GITHUB_TOKEN 环境变量")
        return
    
    print(f"🔗 连接 GitHub: {username}")
    
    source = GitHubStarsSource(token, username)
    
    # 获取 stars
    print("📥 获取 starred repositories...")
    stars = source.fetch_stars()
    print(f"✅ 找到 {len(stars)} 个 starred repos")
    
    # 统计
    lang_stats = source.get_language_stats()
    print(f"\n📊 编程语言分布:")
    for lang, count in list(lang_stats.items())[:10]:
        print(f"  {lang}: {count}")
    
    topic_stats = source.get_topic_stats()
    print(f"\n🏷️  热门主题:")
    for topic, count in list(topic_stats.items())[:10]:
        print(f"  {topic}: {count}")
    
    # 保存
    output_path = Path(__file__).parent.parent.parent / 'data' / 'input' / 'github_stars.json'
    source.save_to_json(str(output_path))
    
    # 转换为书签格式
    bookmarks = source.to_bookmark_format()
    bookmark_path = Path(__file__).parent.parent.parent / 'data' / 'input' / 'github_stars_bookmarks.json'
    
    with open(bookmark_path, 'w', encoding='utf-8') as f:
        json.dump({'roots': {'bookmark_bar': {'children': bookmarks}}, 'source': 'github_stars'}, 
                  f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ 书签格式已保存：{bookmark_path}")


if __name__ == '__main__':
    main()
