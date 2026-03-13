"""数据模型定义"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime


@dataclass
class Bookmark:
    """书签数据模型"""
    name: str
    url: str
    domain: str
    date_added: Optional[str] = None
    path: List[str] = field(default_factory=list)
    description: Optional[str] = None
    language: Optional[str] = None
    topics: List[str] = field(default_factory=list)
    source: str = "bookmark"
    
    def is_valid(self) -> bool:
        """检查书签是否有效"""
        return bool(self.name and self.url)


@dataclass
class SkillMatch:
    """技能匹配结果"""
    name: str
    category: str
    count: int
    confidence: float = 1.0


@dataclass
class AnalysisResult:
    """分析结果"""
    total_bookmarks: int
    unique_domains: int
    skills: Dict[str, List[Dict]]
    timeline: Dict[str, Any]
    health: Dict[str, Any]
    domains: Dict[str, Any]
    generated_at: datetime = field(default_factory=datetime.now)
