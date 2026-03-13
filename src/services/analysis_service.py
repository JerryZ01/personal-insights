"""分析服务"""
from typing import List, Dict
from src.analyzers.domain_analyzer import DomainAnalyzer
from src.analyzers.skill_analyzer import SkillAnalyzer
from src.analyzers.timeline_analyzer import TimelineAnalyzer
from src.analyzers.health_analyzer import HealthAnalyzer


class AnalysisService:
    """分析服务 - 统一入口"""
    
    def __init__(self) -> None:
        self.domain_analyzer = DomainAnalyzer()
        self.skill_analyzer = SkillAnalyzer()
        self.timeline_analyzer = TimelineAnalyzer()
        self.health_analyzer = HealthAnalyzer()
    
    def analyze_all(self, bookmarks: List[Dict]) -> Dict:
        """执行完整分析"""
        return {
            'domains': self.domain_analyzer.analyze(bookmarks),
            'skills': self.skill_analyzer.analyze(bookmarks),
            'timeline': self.timeline_analyzer.analyze(bookmarks),
            'health': self.health_analyzer.analyze(bookmarks),
        }
    
    def analyze_skills(self, bookmarks: List[Dict]) -> Dict:
        """只分析技能"""
        return self.skill_analyzer.analyze(bookmarks)
    
    def analyze_timeline(self, bookmarks: List[Dict]) -> Dict:
        """只分析时间线"""
        return self.timeline_analyzer.analyze(bookmarks)
    
    def analyze_health(self, bookmarks: List[Dict]) -> Dict:
        """只分析健康"""
        return self.health_analyzer.analyze(bookmarks)
