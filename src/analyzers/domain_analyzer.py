"""域名分析器"""
from typing import List, Dict, Any
from collections import Counter
from .base import BaseAnalyzer


class DomainAnalyzer(BaseAnalyzer):
    """域名分析器"""
    
    DOMAIN_CATEGORIES = {
        'blog.csdn.net': '技术博客',
        'zhuanlan.zhihu.com': '深度文章',
        'cnblogs.com': '技术博客',
        'jianshu.com': '技术博客',
        'github.com': '开源项目',
        'gitee.com': '开源项目',
        'cloud.tencent.com': '云厂商',
        'developer.aliyun.com': '云厂商',
        'huaweicloud.com': '云厂商',
        'stackoverflow.com': '社区论坛',
        'iwiki.woa.com': '内部文档',
    }
    
    def analyze(self, bookmarks: List[Dict]) -> Dict[str, Any]:
        """分析域名分布"""
        domains = Counter([b['domain'] for b in bookmarks if b.get('domain')])
        
        category_stats: Dict[str, int] = {}
        for domain, count in domains.items():
            category = self.DOMAIN_CATEGORIES.get(domain, '其他')
            category_stats[category] = category_stats.get(category, 0) + count
        
        return {
            'total_domains': len(domains),
            'top_domains': dict(domains.most_common(20)),
            'by_category': category_stats,
        }
    
    def get_summary(self) -> str:
        """获取摘要"""
        return "域名分析完成"
