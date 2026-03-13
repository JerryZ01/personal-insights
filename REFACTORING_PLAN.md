# 🔧 Personal Insights - 重构计划

**版本**: v0.3.0  
**优先级**: P0  
**预计工时**: 3 人天  
**状态**: 待执行

---

## 📋 重构目标

### 当前问题

1. **单文件过大**: `bookmark_analyzer.py` 707 行，难以维护
2. **缺少模块化**: 所有分析逻辑在一个类中
3. **缺少类型注解**: 代码可读性差，容易出错
4. **缺少测试**: 无单元测试，重构风险高
5. **配置硬编码**: 路径、参数等硬编码在代码中

### 重构目标

1. ✅ 拆分为多个模块，每个模块 < 300 行
2. ✅ 添加完整类型注解
3. ✅ 单元测试覆盖率 > 60%
4. ✅ 配置外部化
5. ✅ 保持向后兼容

---

## 📦 新目录结构

```
personal-insights/
├── src/
│   ├── __init__.py
│   │
│   ├── core/                    # 核心模块
│   │   ├── __init__.py
│   │   ├── models.py            # 数据模型 (新建)
│   │   ├── config.py            # 配置管理 (新建)
│   │   └── exceptions.py        # 自定义异常 (新建)
│   │
│   ├── analyzers/               # 分析器模块 (拆分)
│   │   ├── __init__.py
│   │   ├── base.py              # 分析器基类 (新建)
│   │   ├── domain_analyzer.py   # 从 bookmark_analyzer.py 拆分
│   │   ├── skill_analyzer.py    # 从 bookmark_analyzer.py 拆分
│   │   ├── timeline_analyzer.py # 从 bookmark_analyzer.py 拆分
│   │   ├── health_analyzer.py   # 从 bookmark_analyzer.py 拆分
│   │   └── content_analyzer.py  # 从 bookmark_analyzer.py 拆分
│   │
│   ├── sources/                 # 数据源模块
│   │   ├── __init__.py
│   │   ├── base.py              # 数据源基类 (新建)
│   │   ├── browser.py           # 浏览器书签 (保持不变)
│   │   └── github.py            # GitHub Stars (保持不变)
│   │
│   ├── services/                # 服务层 (新建)
│   │   ├── __init__.py
│   │   ├── import_service.py
│   │   ├── analysis_service.py
│   │   └── merge_service.py
│   │
│   └── utils/                   # 工具函数
│       ├── __init__.py
│       ├── logger.py            # 日志配置 (新建)
│       └── helpers.py           # 辅助函数 (新建)
│
├── cli/                         # CLI 模块 (新建)
│   ├── __init__.py
│   ├── main.py                  # CLI 入口
│   └── commands/                # 命令实现
│       ├── stats.py
│       ├── skills.py
│       ├── timeline.py
│       ├── health.py
│       ├── report.py
│       ├── import.py
│       └── merge.py
│
├── tests/                       # 测试 (新建)
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   └── integration/
│
├── cli.py                       # 保留，兼容旧版本
├── requirements.txt
└── pyproject.toml               # 新建
```

---

## 🔄 重构步骤

### Step 1: 准备工作 (2h)

```bash
# 1. 创建新目录结构
mkdir -p src/{core,analyzers,sources,services,utils}
mkdir -p cli/commands
mkdir -p tests/{unit,integration}

# 2. 创建 __init__.py 文件
touch src/__init__.py
touch src/core/__init__.py
touch src/analyzers/__init__.py
touch src/sources/__init__.py
touch src/services/__init__.py
touch src/utils/__init__.py
touch cli/__init__.py
touch cli/commands/__init__.py
touch tests/__init__.py

# 3. 备份当前代码
git checkout -b refactor/prepare
```

### Step 2: 创建核心模块 (4h)

#### 2.1 创建数据模型 (`src/core/models.py`)

```python
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
    skills: Dict[str, List[SkillMatch]]
    timeline: Dict[str, Any]
    health: Dict[str, Any]
    generated_at: datetime = field(default_factory=datetime.now)
```

#### 2.2 创建配置管理 (`src/core/config.py`)

```python
"""配置管理"""
from pathlib import Path
from typing import Optional
import os


class Config:
    """应用配置"""
    
    def __init__(self):
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
```

#### 2.3 创建异常类 (`src/core/exceptions.py`)

```python
"""自定义异常"""


class PersonalInsightsError(Exception):
    """基础异常类"""
    pass


class DataLoadError(PersonalInsightsError):
    """数据加载失败"""
    pass


class DataFormatError(PersonalInsightsError):
    """数据格式错误"""
    pass


class AnalysisError(PersonalInsightsError):
    """分析失败"""
    pass


class DataSourceError(PersonalInsightsError):
    """数据源错误"""
    pass
```

### Step 3: 拆分分析器 (8h)

#### 3.1 创建分析器基类 (`src/analyzers/base.py`)

```python
"""分析器基类"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseAnalyzer(ABC):
    """分析器基类"""
    
    @abstractmethod
    def analyze(self, bookmarks: List[Dict]) -> Dict[str, Any]:
        """执行分析"""
        pass
    
    @abstractmethod
    def get_summary(self) -> str:
        """获取分析摘要"""
        pass
```

#### 3.2 拆分域名分析器 (`src/analyzers/domain_analyzer.py`)

```python
"""域名分析器"""
from typing import List, Dict
from collections import Counter
from .base import BaseAnalyzer


class DomainAnalyzer(BaseAnalyzer):
    """域名分析器"""
    
    DOMAIN_CATEGORIES = {
        'blog.csdn.net': '技术博客',
        'zhuanlan.zhihu.com': '深度文章',
        'github.com': '开源项目',
        # ... 更多域名
    }
    
    def analyze(self, bookmarks: List[Dict]) -> Dict[str, Any]:
        """分析域名分布"""
        domains = Counter([b['domain'] for b in bookmarks if b.get('domain')])
        
        category_stats = {}
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
```

#### 3.3 拆分技能分析器 (`src/analyzers/skill_analyzer.py`)

```python
"""技能分析器"""
from typing import List, Dict
from collections import Counter
from .base import BaseAnalyzer


class SkillAnalyzer(BaseAnalyzer):
    """技能分析器"""
    
    SKILL_KEYWORDS = {
        'Python': '编程语言',
        'Java': '编程语言',
        'Transformer': '深度学习',
        # ... 更多技能
    }
    
    def analyze(self, bookmarks: List[Dict]) -> Dict[str, List[Dict]]:
        """提取技能"""
        skill_counts = {}
        
        for bookmark in bookmarks:
            text = f"{bookmark.get('name', '')} {bookmark.get('url', '')}"
            text += f" {bookmark.get('description', '')}"
            
            for skill, category in self.SKILL_KEYWORDS.items():
                if skill.lower() in text.lower():
                    skill_counts[skill] = skill_counts.get(skill, 0) + 1
        
        # 按类别组织
        category_skills = {}
        for skill, count in skill_counts.items():
            category = self.SKILL_KEYWORDS.get(skill, '其他')
            if category not in category_skills:
                category_skills[category] = []
            category_skills[category].append({
                'skill': skill,
                'count': count,
            })
        
        # 排序
        for category in category_skills:
            category_skills[category].sort(key=lambda x: -x['count'])
        
        return category_skills
    
    def get_summary(self) -> str:
        """获取摘要"""
        return "技能提取完成"
```

#### 3.4 其他分析器

类似地创建：
- `timeline_analyzer.py` - 时间线分析
- `health_analyzer.py` - 健康检查
- `content_analyzer.py` - 内容分类

### Step 4: 创建服务层 (4h)

```python
# src/services/analysis_service.py
"""分析服务"""
from typing import List, Dict
from src.analyzers.domain_analyzer import DomainAnalyzer
from src.analyzers.skill_analyzer import SkillAnalyzer
from src.analyzers.timeline_analyzer import TimelineAnalyzer
from src.analyzers.health_analyzer import HealthAnalyzer


class AnalysisService:
    """分析服务"""
    
    def __init__(self):
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
```

### Step 5: 重构 CLI (4h)

```python
# cli/main.py
"""CLI 入口"""
import click
from .commands import stats, skills, timeline, health, report, merge


@click.group()
@click.version_option(version='0.3.0')
def cli():
    """Personal Insights - 个人洞察工具"""
    pass


cli.add_command(stats.cmd_stats)
cli.add_command(skills.cmd_skills)
cli.add_command(timeline.cmd_timeline)
cli.add_command(health.cmd_health)
cli.add_command(report.cmd_report)
cli.add_command(merge.cmd_merge)


if __name__ == '__main__':
    cli()
```

### Step 6: 保持向后兼容 (2h)

保留 `cli.py`，但内部调用新模块：

```python
# cli.py (兼容旧版本)
#!/usr/bin/env python3
"""兼容旧版本的 CLI 入口"""
import sys
from pathlib import Path

# 导入新 CLI
from cli.main import cli

if __name__ == '__main__':
    cli()
```

### Step 7: 编写测试 (8h)

```python
# tests/unit/test_skill_analyzer.py
import pytest
from src.analyzers.skill_analyzer import SkillAnalyzer


class TestSkillAnalyzer:
    def test_extract_python_skill(self):
        analyzer = SkillAnalyzer()
        bookmarks = [
            {'name': 'Python 教程', 'url': '...', 'domain': '...'}
        ]
        result = analyzer.analyze(bookmarks)
        assert '编程语言' in result
```

### Step 8: 测试和验证 (4h)

```bash
# 运行所有测试
pytest tests/ -v

# 类型检查
mypy src/

# 代码检查
flake8 src/

# 功能测试
python cli.py stats
python cli.py skills
python cli.py timeline
python cli.py health
```

---

## ✅ 验收标准

- [ ] 所有单元测试通过
- [ ] 类型检查通过 (mypy)
- [ ] 代码检查通过 (flake8)
- [ ] CLI 所有命令正常工作
- [ ] 向后兼容（旧命令仍可用）
- [ ] 代码覆盖率 > 60%
- [ ] 文档更新完成

---

## 📝 检查清单

### 代码质量

- [ ] 所有公共函数有类型注解
- [ ] 所有公共类有文档字符串
- [ ] 无重复代码 (DRY)
- [ ] 函数长度 < 50 行
- [ ] 类长度 < 300 行

### 测试

- [ ] 核心分析器有单元测试
- [ ] 数据源有集成测试
- [ ] CLI 命令有端到端测试
- [ ] 测试覆盖率报告生成

### 文档

- [ ] README 更新
- [ ] API 文档更新
- [ ] 迁移指南编写
- [ ] CHANGELOG 更新

---

## 🚨 风险控制

### 风险 1: 破坏向后兼容性

**缓解措施**:
- 保留旧 `cli.py` 作为兼容层
- 添加集成测试验证旧命令
- 发布前进行充分测试

### 风险 2: 引入新 Bug

**缓解措施**:
- 编写充分的单元测试
- 代码审查
- 灰度发布

### 风险 3: 重构时间超期

**缓解措施**:
- 分阶段重构
- 优先重构核心模块
- 保持功能可用

---

## 📅 时间表

| 阶段 | 任务 | 预计时间 | 完成标志 |
|------|------|---------|---------|
| 1 | 准备工作 | 2h | 目录结构创建完成 |
| 2 | 核心模块 | 4h | models/config/exceptions 完成 |
| 3 | 拆分分析器 | 8h | 5 个分析器模块完成 |
| 4 | 服务层 | 4h | 服务层完成 |
| 5 | CLI 重构 | 4h | 新 CLI 完成 |
| 6 | 向后兼容 | 2h | 兼容层完成 |
| 7 | 测试 | 8h | 测试覆盖率>60% |
| 8 | 验证 | 4h | 所有测试通过 |

**总计**: 36 小时 ≈ 4.5 人天

---

**负责人**: @JerryZ01  
**开始日期**: TBD  
**结束日期**: TBD  
**状态**: 待执行
