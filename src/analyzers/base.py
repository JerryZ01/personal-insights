"""分析器基类"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseAnalyzer(ABC):
    """分析器抽象基类"""
    
    @abstractmethod
    def analyze(self, bookmarks: List[Dict]) -> Dict[str, Any]:
        """执行分析"""
        pass
    
    @abstractmethod
    def get_summary(self) -> str:
        """获取分析摘要"""
        pass
