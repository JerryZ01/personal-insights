"""时间线分析器"""
from typing import List, Dict, Any
from collections import defaultdict
from datetime import datetime
from .base import BaseAnalyzer


class TimelineAnalyzer(BaseAnalyzer):
    """时间线分析器"""
    
    TECH_TAXONOMY = {
        'AI/大模型': ['Transformer', 'LLM', '大模型', 'PyTorch', 'RAG', 'LangChain'],
        '云计算': ['Kubernetes', 'K8s', 'Docker', 'OpenStack', 'CVM'],
        '编程语言': ['Python', 'Java', 'C++', 'Go', 'JavaScript'],
        '大数据': ['Hadoop', 'Spark', 'Flink', 'Hive', 'Hudi', '大数据'],
        'AI 芯片': ['昇腾', 'Ascend', 'CANN', 'NPU'],
    }
    
    def analyze(self, bookmarks: List[Dict]) -> Dict[str, Any]:
        """分析时间线"""
        timeline: Dict[str, List[Dict]] = defaultdict(list)
        
        # 按月份分组
        for bookmark in bookmarks:
            date_added = bookmark.get('date_added', '')
            if date_added:
                month = self._chrome_date_to_month(date_added)
                if month:
                    timeline[month].append(bookmark)
        
        # 分析每个月
        monthly_stats: Dict[str, Dict] = {}
        for month, items in sorted(timeline.items()):
            tech_counter: Dict[str, int] = defaultdict(int)
            for item in items:
                text = f"{item.get('name', '')} {item.get('url', '')}".lower()
                for category, keywords in self.TECH_TAXONOMY.items():
                    for keyword in keywords:
                        if keyword.lower() in text:
                            tech_counter[category] += 1
            
            top_category = max(tech_counter.items(), key=lambda x: x[1])[0] if tech_counter else '其他'
            
            intensity = '低'
            count = len(items)
            if count >= 20:
                intensity = '高'
            elif count >= 10:
                intensity = '中'
            
            monthly_stats[month] = {
                'count': count,
                'top_category': top_category,
                'categories': dict(tech_counter),
                'intensity': intensity,
            }
        
        # 识别学习阶段
        phases = self._identify_phases(monthly_stats)
        
        return {
            'monthly': monthly_stats,
            'phases': phases,
            'stats': {
                'total_months': len(monthly_stats),
                'total_bookmarks': sum(len(items) for items in timeline.values()),
            }
        }
    
    def _chrome_date_to_month(self, chrome_date: str) -> str:
        """转换 Chrome 时间戳到月份"""
        try:
            timestamp = int(chrome_date) / 1000000 - 11644473600
            dt = datetime.fromtimestamp(timestamp)
            return dt.strftime('%Y-%m')
        except Exception:
            return ''
    
    def _identify_phases(self, monthly_stats: Dict[str, Dict]) -> List[Dict]:
        """识别学习阶段"""
        if not monthly_stats:
            return []
        
        phases = []
        phase_start = None
        phase_category = None
        phase_count = 0
        
        for month, stats in sorted(monthly_stats.items()):
            category = stats['top_category']
            count = stats['count']
            
            if phase_start is None:
                phase_start = month
                phase_category = category
                phase_count = count
            elif category == phase_category:
                phase_count += count
            else:
                if phase_count >= 5:
                    phases.append({
                        'period': f"{phase_start} - {month}",
                        'category': phase_category,
                        'count': phase_count,
                    })
                phase_start = month
                phase_category = category
                phase_count = count
        
        # 保存最后一个阶段
        if phase_count >= 5 and phase_category:
            last_month = list(monthly_stats.keys())[-1]
            phases.append({
                'period': f"{phase_start} - {last_month}",
                'category': phase_category,
                'count': phase_count,
            })
        
        return phases
    
    def get_summary(self) -> str:
        """获取摘要"""
        return "时间线分析完成"
