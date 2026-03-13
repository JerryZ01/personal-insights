"""配置管理"""
from pathlib import Path
from typing import Optional
import os


class Config:
    """应用配置"""
    
    def __init__(self) -> None:
        # 路径配置
        self.base_dir = Path(__file__).parent.parent.parent
        self.data_dir = self.base_dir / "data"
        self.input_dir = self.data_dir / "input"
        self.output_dir = self.data_dir / "output"
        
        # GitHub 配置
        self.github_token: Optional[str] = os.getenv("GITHUB_TOKEN")
        self.github_username: str = os.getenv("GITHUB_USERNAME", "JerryZ01")
        
        # 分析配置
        self.max_timeline_months: int = 12
        self.min_skill_confidence: float = 0.5
        
        # 确保目录存在
        self.input_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def from_env(cls) -> "Config":
        """从环境变量加载配置"""
        return cls()


# 全局配置实例
config = Config()
