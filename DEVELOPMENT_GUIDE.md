# 👨‍💻 Personal Insights - 开发指南

**版本**: v0.3.0  
**最后更新**: 2026-03-13  
**目标读者**: 贡献者、开发者

---

## 📋 目录

1. [开发环境搭建](#开发环境搭建)
2. [代码规范](#代码规范)
3. [测试指南](#测试指南)
4. [调试技巧](#调试技巧)
5. [性能优化](#性能优化)
6. [常见问题](#常见问题)

---

## 🛠️ 开发环境搭建

### 1. 克隆项目

```bash
git clone https://github.com/JerryZ01/personal-insights.git
cd personal-insights
```

### 2. 创建虚拟环境

```bash
# 使用 conda (推荐)
conda create -n personal-insights python=3.10
conda activate personal-insights

# 或使用 venv
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 安装依赖

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 或手动安装
pip install requests cryptography python-dateutil rich click
pip install pytest pytest-cov mypy black flake8 pre-commit
```

### 4. 配置 pre-commit

```bash
# 安装 pre-commit hooks
pre-commit install

# 验证安装
pre-commit --version
```

### 5. 验证安装

```bash
# 运行测试
pytest tests/

# 类型检查
mypy src/

# 代码检查
flake8 src/

# 运行 CLI
python cli.py --help
```

---

## 📏 代码规范

### Python 风格指南

遵循 [PEP 8](https://peps.python.org/pep-0008/) 规范。

#### 代码格式

```python
# ✅ 好的格式
def analyze_bookmarks(
    bookmarks: List[Dict],
    include_skills: bool = True,
    include_timeline: bool = True,
) -> Dict[str, Any]:
    """分析书签数据"""
    pass

# ❌ 坏的格式
def analyze_bookmarks(bookmarks,include_skills=True,include_timeline=True):
    pass
```

#### 类型注解

```python
# ✅ 必须添加类型注解
from typing import List, Dict, Optional, Any

class BookmarkAnalyzer:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.bookmarks: List[Dict] = []
    
    def load(self) -> List[Dict]:
        pass
    
    def analyze(self, options: Optional[Dict] = None) -> Dict[str, Any]:
        pass

# ❌ 不要这样
class BookmarkAnalyzer:
    def __init__(self, path):
        self.path = path
        self.bookmarks = []
```

#### 文档字符串

```python
# ✅ 完整的文档字符串
def extract_skills(
    text: str,
    min_confidence: float = 0.5,
) -> List[SkillMatch]:
    """
    从文本中提取技能关键词
    
    Args:
        text: 要分析的文本（标题、描述等）
        min_confidence: 最小置信度，0-1 之间，默认 0.5
    
    Returns:
        匹配的技能列表，按置信度降序排列
    
    Raises:
        ValueError: 当 text 为空或 min_confidence 超出范围时
    
    Example:
        >>> analyzer = SkillAnalyzer()
        >>> skills = analyzer.extract_skills("Python 机器学习教程")
        >>> len(skills)
        2
    """
    pass
```

#### 错误处理

```python
# ✅ 好的错误处理
from pathlib import Path
from typing import Optional

class DataLoadError(Exception):
    """数据加载失败"""
    pass

def load_bookmarks(path: Path) -> List[Dict]:
    """
    加载书签数据
    
    Raises:
        DataLoadError: 当文件不存在或格式错误时
    """
    if not path.exists():
        raise DataLoadError(f"文件不存在：{path}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise DataLoadError(f"JSON 格式错误：{e}")
    except Exception as e:
        raise DataLoadError(f"未知错误：{e}")

# ❌ 坏的错误处理
def load_bookmarks(path):
    with open(path) as f:  # 没有 encoding，没有异常处理
        return json.load(f)
```

#### 日志记录

```python
# ✅ 使用日志
import logging

logger = logging.getLogger(__name__)

def analyze_bookmarks(bookmarks: List[Dict]) -> Dict:
    logger.info(f"开始分析 {len(bookmarks)} 个书签")
    
    if not bookmarks:
        logger.warning("书签列表为空")
        return {}
    
    try:
        result = _process(bookmarks)
        logger.info(f"分析完成，提取 {len(result['skills'])} 个技能")
        return result
    except Exception as e:
        logger.error(f"分析失败：{e}", exc_info=True)
        raise

# ❌ 使用 print
def analyze_bookmarks(bookmarks):
    print(f"开始分析 {len(bookmarks)} 个书签")  # 不要在生产代码中使用
    ...
```

---

## 🧪 测试指南

### 测试结构

```
tests/
├── __init__.py
├── conftest.py              # pytest 配置和 fixtures
├── unit/                    # 单元测试
│   ├── test_skill_analyzer.py
│   ├── test_timeline_analyzer.py
│   └── test_domain_analyzer.py
├── integration/             # 集成测试
│   ├── test_import_flow.py
│   └── test_merge_flow.py
└── e2e/                     # 端到端测试
    └── test_cli_commands.py
```

### 编写测试

```python
# tests/unit/test_skill_analyzer.py
import pytest
from src.analyzers.skill_analyzer import SkillAnalyzer, SkillMatch

class TestSkillAnalyzer:
    """技能分析器测试类"""
    
    @pytest.fixture
    def analyzer(self) -> SkillAnalyzer:
        """创建分析器实例"""
        return SkillAnalyzer()
    
    def test_extract_python_skill(self, analyzer: SkillAnalyzer) -> None:
        """测试提取 Python 技能"""
        text = "Python 编程从入门到精通"
        skills = analyzer.extract_from_text(text)
        
        assert any(s.name == "Python" for s in skills)
    
    def test_extract_multiple_skills(self, analyzer: SkillAnalyzer) -> None:
        """测试提取多个技能"""
        text = "使用 PyTorch 进行深度学习开发"
        skills = analyzer.extract_from_text(text)
        
        skill_names = [s.name for s in skills]
        assert "PyTorch" in skill_names
        assert "深度学习" in skill_names
    
    def test_no_skills_found(self, analyzer: SkillAnalyzer) -> None:
        """测试无技能匹配"""
        text = "今天天气真好"
        skills = analyzer.extract_from_text(text)
        
        assert len(skills) == 0
    
    def test_empty_text(self, analyzer: SkillAnalyzer) -> None:
        """测试空文本"""
        with pytest.raises(ValueError):
            analyzer.extract_from_text("")
    
    def test_skill_confidence_score(self, analyzer: SkillAnalyzer) -> None:
        """测试技能置信度"""
        text = "Python Python Python"
        skills = analyzer.extract_from_text(text)
        
        python_skill = next(s for s in skills if s.name == "Python")
        assert python_skill.confidence > 0.8
```

### 测试 Fixtures

```python
# tests/conftest.py
import pytest
from pathlib import Path
from typing import List, Dict

@pytest.fixture
def sample_bookmarks() -> List[Dict]:
    """示例书签数据"""
    return [
        {
            "name": "Python 教程",
            "url": "https://docs.python.org/3/tutorial/",
            "domain": "docs.python.org",
        },
        {
            "name": "PyTorch 文档",
            "url": "https://pytorch.org/docs/",
            "domain": "pytorch.org",
        },
    ]

@pytest.fixture
def temp_bookmark_file(tmp_path: Path, sample_bookmarks: List[Dict]) -> Path:
    """创建临时书签文件"""
    import json
    file_path = tmp_path / "bookmarks.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({"roots": {"bookmark_bar": {"children": sample_bookmarks}}}, f)
    return file_path
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/unit/test_skill_analyzer.py

# 运行特定测试类
pytest tests/unit/test_skill_analyzer.py::TestSkillAnalyzer

# 运行特定测试函数
pytest tests/unit/test_skill_analyzer.py::TestSkillAnalyzer::test_extract_python_skill

# 显示覆盖率
pytest --cov=src --cov-report=html

# 显示详细输出
pytest -v

# 失败后停止
pytest -x

# 重新运行失败的测试
pytest --lf
```

---

## 🐛 调试技巧

### 使用调试器

```python
# 使用 pdb
import pdb

def analyze(bookmarks):
    pdb.set_trace()  # 设置断点
    # 代码执行到这里会暂停
    ...

# Python 3.7+ 使用 breakpoint()
def analyze(bookmarks):
    breakpoint()  # 更简洁
    ...
```

### 使用日志调试

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def complex_function(data):
    logger.debug(f"输入数据：{data}")
    
    result = process(data)
    logger.debug(f"处理结果：{result}")
    
    return result
```

### 常见错误排查

#### 1. 导入错误

```bash
# 错误：ModuleNotFoundError
ModuleNotFoundError: No module named 'src'

# 解决：确保在正确的目录运行
cd personal-insights
python -m src.analyzers.skill_analyzer

# 或安装为可编辑包
pip install -e .
```

#### 2. 类型检查错误

```bash
# 错误：Argument type mismatch
error: Argument 1 to "analyze" has incompatible type "List[Dict]"; expected "List[Bookmark]"

# 解决：添加正确的类型注解或使用类型转换
from src.core.models import Bookmark

bookmarks = [Bookmark(**data) for data in raw_data]
analyzer.analyze(bookmarks)
```

#### 3. 测试失败

```bash
# 查看详细信息
pytest -v -s

# 使用 pytest 调试
pytest --pdb

# 查看日志
pytest --log-cli-level=DEBUG
```

---

## ⚡ 性能优化

### 性能分析

```python
# 使用 cProfile
import cProfile
import pstats

def benchmark():
    analyzer = BookmarkAnalyzer('data.json')
    analyzer.load()
    analyzer.analyze()

# 运行分析
cProfile.run('benchmark()', 'output.prof')

# 查看结果
stats = pstats.Stats('output.prof')
stats.sort_stats('cumulative')
stats.print_stats(10)
```

### 优化技巧

#### 1. 使用缓存

```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def extract_skills(text: str) -> List[str]:
    """技能提取（带缓存）"""
    # 实现代码
    pass
```

#### 2. 批量处理

```python
# ✅ 好的方式：批量处理
def analyze_bookmarks(bookmarks: List[Dict]) -> Dict:
    # 一次性处理所有书签
    all_skills = []
    for bookmark in bookmarks:
        skills = extract_skills(bookmark['name'])
        all_skills.extend(skills)
    return aggregate_skills(all_skills)

# ❌ 坏的方式：逐个处理并保存
def analyze_bookmarks_bad(bookmarks):
    for bookmark in bookmarks:
        skills = extract_skills(bookmark['name'])
        save_to_file(skills)  # 频繁的 IO 操作
```

#### 3. 惰性加载

```python
class LazyAnalyzer:
    def __init__(self, path: Path):
        self.path = path
        self._data: Optional[List[Dict]] = None
    
    @property
    def data(self) -> List[Dict]:
        """惰性加载数据"""
        if self._data is None:
            self._data = self._load_data()
        return self._data
    
    def analyze(self) -> Dict:
        # 只在需要时才加载
        return self._analyze(self.data)
```

---

## ❓ 常见问题

### Q1: 如何添加新的数据源？

```python
# 1. 创建新的数据源类
from src.sources.base import DataSource

class ZhihuFavorites(DataSource):
    """知乎收藏数据源"""
    
    def __init__(self, cookies: str):
        super().__init__(name="zhihu", privacy_level="medium")
        self.cookies = cookies
    
    def fetch(self) -> List[Dict]:
        """获取知乎收藏"""
        # 实现代码
        pass
    
    def to_unified_format(self, raw_data: Any) -> List[Dict]:
        """转换为统一格式"""
        # 实现代码
        pass

# 2. 在 CLI 中添加导入命令
# cli/commands/import.py
@click.command()
@click.option('--platform', type=click.Choice(['zhihu']))
def import_data(platform):
    if platform == 'zhihu':
        from src.sources.zhihu import ZhihuFavorites
        # 实现导入逻辑
```

### Q2: 如何添加新的分析器？

```python
# 1. 创建分析器类
from src.analyzers.base import BaseAnalyzer

class TrendAnalyzer(BaseAnalyzer):
    """趋势分析器"""
    
    def analyze(self, bookmarks: List[Dict]) -> Dict:
        """分析趋势"""
        # 实现代码
        return {
            'trending_skills': [...],
            'declining_skills': [...],
        }

# 2. 注册到引擎
# src/core/engine.py
from src.analyzers.trend_analyzer import TrendAnalyzer

class AnalysisEngine:
    def __init__(self):
        self.analyzers = {
            'domain': DomainAnalyzer(),
            'skill': SkillAnalyzer(),
            'trend': TrendAnalyzer(),  # 新增
        }
```

### Q3: 如何处理大数据集？

```python
# 使用生成器处理大数据
def process_large_dataset(file_path: Path) -> Generator[Dict, None, None]:
    """处理大型数据集"""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield json.loads(line)

# 分块处理
def analyze_in_chunks(
    bookmarks: List[Dict],
    chunk_size: int = 1000,
) -> Dict:
    """分块分析"""
    results = []
    for i in range(0, len(bookmarks), chunk_size):
        chunk = bookmarks[i:i + chunk_size]
        result = analyze_chunk(chunk)
        results.append(result)
    
    return merge_results(results)
```

### Q4: 如何调试 CLI 命令？

```bash
# 使用 verbose 模式
python cli.py stats -v

# 使用 Python 调试器
python -m pdb cli.py stats

# 添加断点
# cli.py
def cmd_stats(args):
    breakpoint()  # 在这里暂停
    ...
```

---

## 📚 学习资源

- [Python 官方文档](https://docs.python.org/3/)
- [pytest 文档](https://docs.pytest.org/)
- [类型注解指南](https://docs.python.org/3/library/typing.html)
- [Click CLI 框架](https://click.palletsprojects.com/)
- [FastAPI 文档](https://fastapi.tiangolo.com/)

---

**维护者**: @JerryZ01  
**贡献者**: 欢迎提交 PR！  
**最后更新**: 2026-03-13
