"""健康检查器"""
from typing import List, Dict, Any
from collections import Counter, defaultdict
from .base import BaseAnalyzer


class HealthAnalyzer(BaseAnalyzer):
    """健康检查器"""
    
    def analyze(self, bookmarks: List[Dict]) -> Dict[str, Any]:
        """健康检查"""
        # 重复检查
        url_counter = Counter([b['url'] for b in bookmarks if b.get('url')])
        duplicates = {url: count for url, count in url_counter.items() if count > 1}
        
        # 死链检查
        suspicious = []
        for b in bookmarks:
            name_lower = b.get('name', '').lower()
            if '404' in name_lower or 'not found' in name_lower:
                suspicious.append(b.get('url', ''))
        
        # 质量评估
        quality = self._assess_quality(bookmarks)
        
        # 平台分布
        platform_health = self._assess_platforms(bookmarks)
        
        return {
            'total': len(bookmarks),
            'unique_urls': len(set([b['url'] for b in bookmarks if b.get('url')])),
            'duplicates': len(duplicates),
            'duplicate_urls': list(duplicates.keys())[:10],
            'suspicious': len(suspicious),
            'suspicious_urls': suspicious[:10],
            'quality': quality,
            'platform_health': platform_health,
        }
    
    def _assess_quality(self, bookmarks: List[Dict]) -> Dict[str, Any]:
        """评估内容质量"""
        high_quality_domains = ['github.com', 'docs.python.org', 'developer.mozilla.org']
        medium_quality_domains = ['zhihu.com', 'cnblogs.com', 'juejin.cn']
        
        high_count = 0
        medium_count = 0
        low_count = 0
        
        for b in bookmarks:
            domain = b.get('domain', '').lower()
            if any(hq in domain for hq in high_quality_domains):
                high_count += 1
            elif any(mq in domain for mq in medium_quality_domains):
                medium_count += 1
            else:
                medium_count += 1
        
        total = len(bookmarks)
        return {
            'high_quality': high_count,
            'medium_quality': medium_count,
            'low_quality': low_count,
            'high_quality_ratio': round(high_count / total * 100, 1) if total > 0 else 0,
        }
    
    def _assess_platforms(self, bookmarks: List[Dict]) -> Dict[str, Any]:
        """评估平台分布"""
        platform_counts: Dict[str, int] = defaultdict(int)
        
        for b in bookmarks:
            domain = b.get('domain', '').lower()
            if 'github.com' in domain:
                platform_counts['GitHub'] += 1
            elif 'zhihu.com' in domain:
                platform_counts['知乎'] += 1
            elif 'csdn.net' in domain or 'cnblogs.com' in domain:
                platform_counts['技术博客'] += 1
            else:
                platform_counts['其他'] += 1
        
        return {
            'platforms': dict(platform_counts),
            'platform_count': len(platform_counts),
            'diversity': '丰富' if len(platform_counts) >= 5 else '中等',
        }
    
    def get_summary(self) -> str:
        """获取摘要"""
        return "健康检查完成"
