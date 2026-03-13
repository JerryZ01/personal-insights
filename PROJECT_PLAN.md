# 📋 Personal Insights - 项目总体规划

**版本**: v0.3.0  
**最后更新**: 2026-03-13  
**状态**: 规划中  
**架构师**: @JerryZ01

---

## 🎯 项目愿景

**做成一个比自己更懂自己的开源项目**

基于全平台收藏数据，构建隐私优先的个人画像系统，帮助用户：
- 📊 了解知识技能结构
- 📈 追踪成长轨迹
- 💡 发现盲点和潜力
- 🔮 预测发展趋势

**核心承诺**: 数据不出设备，隐私绝不泄露！

---

## 📊 当前状态 (v0.2.0)

### ✅ 已完成功能

| 模块 | 功能 | 状态 | 完成度 |
|------|------|------|--------|
| **数据源** | 浏览器书签导入 | ✅ | 100% |
| **数据源** | GitHub Stars 导入 | ✅ | 100% |
| **数据源** | 多平台合并 | ✅ | 100% |
| **分析引擎** | 域名分析 | ✅ | 100% |
| **分析引擎** | 内容分类 | ✅ | 100% |
| **分析引擎** | 技能提取 | ✅ | 90% |
| **分析引擎** | 时间线分析 | ✅ | 90% |
| **分析引擎** | 健康检查 | ✅ | 90% |
| **CLI 工具** | stats 命令 | ✅ | 100% |
| **CLI 工具** | skills 命令 | ✅ | 100% |
| **CLI 工具** | timeline 命令 | ✅ | 90% |
| **CLI 工具** | health 命令 | ✅ | 90% |
| **CLI 工具** | report 命令 | ✅ | 90% |
| **CLI 工具** | github 命令 | ✅ | 100% |
| **CLI 工具** | merge 命令 | ✅ | 100% |
| **文档** | README | ✅ | 100% |
| **文档** | ARCHITECTURE | ✅ | 100% |
| **文档** | ROADMAP | ✅ | 80% |
| **文档** | PHILOSOPHY | ✅ | 100% |

### ⚠️ 技术债务

| 问题 | 影响 | 优先级 | 预计工时 |
|------|------|--------|----------|
| 缺少类型注解 | 代码可维护性 | P1 | 4h |
| 缺少单元测试 | 代码质量 | P1 | 8h |
| 配置硬编码 | 灵活性 | P2 | 2h |
| 缺少日志系统 | 调试困难 | P2 | 3h |
| 错误处理不完善 | 用户体验 | P1 | 3h |
| 代码重复 | 可维护性 | P2 | 4h |

---

## 🏗️ 目标架构 (v1.0.0)

### 完整架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                        用户界面层 (UI Layer)                     │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   CLI 工具    │  │   Web UI     │  │  Desktop App │          │
│  │   (Python)   │  │  (Vue3+TS)   │  │  (Electron)  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                      API 网关层 (API Gateway)                     │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              REST API / FastAPI                          │  │
│  │  /api/v1/analyze  /api/v1/import  /api/v1/report        │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    应用服务层 (Service Layer)                    │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  ImportSvc   │  │  AnalysisSvc │  │  ReportSvc   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  MergerSvc   │  │  InsightSvc  │  │  PredictSvc  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    分析引擎层 (Engine Layer)                     │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ DomainAnalyzer│ │ SkillAnalyzer│ │TimelineAnalyzer│         │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │HealthAnalyzer│ │TrendAnalyzer │ │StyleAnalyzer  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                   数据适配层 (DataSource Layer)                  │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Browser    │  │   GitHub     │  │   Zhihu      │          │
│  │  Bookmarks   │  │   Stars      │ │  Favorites   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Bilibili    │  │   Douban     │  │   WeChat     │          │
│  │  Favorites   │  │  Favorites   │  │   Read       │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    数据存储层 (Storage Layer)                    │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  JSON Files  │  │   SQLite     │  │  Encrypted   │          │
│  │  (Input)     │  │  (Metadata)  │  │  Storage     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

### 核心设计原则

1. **本地优先 (Local-First)**
   - 所有数据处理在本地完成
   - 离线可用
   - 低延迟

2. **隐私优先 (Privacy-First)**
   - 数据不出设备
   - 可选加密存储
   - 用户完全控制

3. **模块化 (Modular)**
   - 数据源可插拔
   - 分析器可扩展
   - 界面可替换

4. **类型安全 (Type-Safe)**
   - Python 类型注解
   - TypeScript 严格模式
   - 编译时检查

5. **测试驱动 (Test-Driven)**
   - 单元测试覆盖率 > 80%
   - 集成测试覆盖核心流程
   - E2E 测试关键用户路径

---

## 📦 项目结构规划

### 当前结构 (v0.2.0)

```
personal-insights/
├── cli.py                          # CLI 入口 (437 行)
├── requirements.txt
├── README.md
├── ARCHITECTURE.md
├── data/
│   ├── input/
│   └── output/
└── src/
    ├── analyzer/
    │   └── bookmark_analyzer.py   # 707 行，过于臃肿
    └── sources/
        └── github.py              # 257 行
```

### 目标结构 (v1.0.0)

```
personal-insights/
├── 📁 .github/                     # GitHub 配置
│   ├── workflows/                  # CI/CD
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
│
├── 📁 src/                         # 源代码
│   ├── 📁 core/                    # 核心引擎
│   │   ├── __init__.py
│   │   ├── analyzer.py             # 分析器基类
│   │   ├── engine.py               # 分析引擎
│   │   └── models.py               # 数据模型
│   │
│   ├── 📁 analyzers/               # 具体分析器
│   │   ├── __init__.py
│   │   ├── domain_analyzer.py
│   │   ├── skill_analyzer.py
│   │   ├── timeline_analyzer.py
│   │   ├── health_analyzer.py
│   │   └── trend_analyzer.py
│   │
│   ├── 📁 sources/                 # 数据源适配器
│   │   ├── __init__.py
│   │   ├── base.py                 # 数据源基类
│   │   ├── browser.py
│   │   ├── github.py
│   │   ├── zhihu.py               # TODO
│   │   └── bilibili.py            # TODO
│   │
│   ├── 📁 services/                # 应用服务
│   │   ├── __init__.py
│   │   ├── import_service.py
│   │   ├── analysis_service.py
│   │   ├── report_service.py
│   │   └── merge_service.py
│   │
│   ├── 📁 api/                     # API 层 (Web UI 用)
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   └── 📁 utils/                   # 工具函数
│       ├── __init__.py
│       ├── config.py
│       ├── logger.py
│       └── crypto.py
│
├── 📁 cli/                         # CLI 工具
│   ├── __init__.py
│   ├── main.py                     # CLI 入口
│   ├── commands/                   # 命令实现
│   │   ├── stats.py
│   │   ├── skills.py
│   │   ├── timeline.py
│   │   ├── health.py
│   │   ├── report.py
│   │   ├── import.py
│   │   └── merge.py
│   └── formatters/                 # 输出格式化
│       ├── table.py
│       └── json.py
│
├── 📁 web/                         # Web UI (Vue 3 + TypeScript)
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── stores/
│   │   └── api/
│   ├── package.json
│   └── vite.config.ts
│
├── 📁 tests/                       # 测试
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── 📁 docs/                        # 文档
│   ├── api/
│   ├── guides/
│   └── architecture/
│
├── 📄 pyproject.toml               # 项目配置 (替代 requirements.txt)
├── 📄 setup.py                     # 安装配置
├── 📄 pytest.ini                   # 测试配置
├── 📄 mypy.ini                     # 类型检查配置
├── 📄 .pre-commit-config.yaml      # Git 钩子
├── 📄 .gitignore
├── 📄 LICENSE
├── 📄 README.md
├── 📄 CHANGELOG.md
└── 📄 CONTRIBUTING.md
```

---

## 🚀 版本规划

### v0.3.0 (2026-04) - 代码质量提升

**目标**: 解决技术债务，提升代码质量

**功能**:
- [ ] 添加完整类型注解
- [ ] 配置 pre-commit hooks
- [ ] 添加日志系统
- [ ] 完善错误处理
- [ ] 配置管理外部化

**质量**:
- [ ] 单元测试覆盖率 > 60%
- [ ] 通过 mypy 严格检查
- [ ] 通过 flake8 代码检查
- [ ] 代码格式化 (black)

**预计工时**: 3 人天

---

### v0.4.0 (2026-05) - 分析增强

**目标**: 增强分析能力，提供更深洞察

**功能**:
- [ ] 学习风格分析
- [ ] 知识缺口分析
- [ ] 趋势预测 (基于历史模式)
- [ ] 智能推荐系统
- [ ] 人格特质分析 (基于收藏行为)

**预计工时**: 5 人天

---

### v0.5.0 (2026-06) - 多平台扩展

**目标**: 支持更多数据源

**功能**:
- [ ] 知乎收藏接入
- [ ] B 站收藏接入
- [ ] 豆瓣书影音接入
- [ ] 微信读书导入 (手动导出)
- [ ] 跨平台分析

**预计工时**: 8 人天

---

### v0.6.0 (2026-07) - Web UI

**目标**: 提供可视化界面

**功能**:
- [ ] 基础 Web UI (Vue 3 + TypeScript)
- [ ] 交互式知识图谱 (D3.js)
- [ ] 时间线可视化
- [ ] 能力雷达图
- [ ] 技能树可视化
- [ ] 数据导入向导

**技术栈**:
- Frontend: Vue 3 + TypeScript + Vite
- UI: Element Plus / Naive UI
- Charts: ECharts / D3.js
- Backend: FastAPI (可选，用于提供 API)

**预计工时**: 10 人天

---

### v0.7.0 (2026-08) - 隐私增强

**目标**: 增强隐私保护

**功能**:
- [ ] AES-256 加密存储
- [ ] 密钥管理 (密码短语)
- [ ] 安全删除
- [ ] 隐私审计报告
- [ ] 数据导出/导入

**预计工时**: 5 人天

---

### v1.0.0 (2026-09) - 稳定版本

**目标**: 发布第一个稳定版本

**功能**:
- [ ] 完整功能集成
- [ ] 性能优化
- [ ] 文档完善
- [ ] 用户测试
- [ ] Bug 修复

**发布**:
- [ ] PyPI 发布
- [ ] GitHub Release
- [ ] 产品 Hunt 发布
- [ ] 技术博客宣传

**预计工时**: 8 人天

---

### v2.0.0 (2027-Q1) - AI 驱动

**目标**: 引入 AI 能力

**功能**:
- [ ] AI 驱动的学习建议
- [ ] 智能学习路径规划
- [ ] 职业发展建议
- [ ] 桌面应用 (Electron)
- [ ] 多设备同步 (端到端加密)

**预计工时**: 20 人天

---

## 📏 开发规范

### 代码规范

#### Python 代码

```python
# ✅ 好的示例
from typing import List, Dict, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Bookmark:
    """书签数据模型"""
    name: str
    url: str
    domain: str
    date_added: Optional[str] = None
    
    def is_valid(self) -> bool:
        """检查书签是否有效"""
        return bool(self.name and self.url)


class BookmarkAnalyzer:
    """书签分析器"""
    
    def __init__(self, bookmarks_path: Path):
        self.bookmarks_path = bookmarks_path
        self.bookmarks: List[Bookmark] = []
    
    def load(self) -> List[Bookmark]:
        """加载书签数据"""
        # 实现代码
        pass
    
    def analyze(self) -> Dict[str, any]:
        """执行分析"""
        # 实现代码
        pass
```

```python
# ❌ 坏的示例
class bookmarkAnalyzer:  # 类名应该大写
    def __init__(self,path):  # 缺少类型注解，空格
        self.path=path  # 缺少空格
        self.data=[]
    
    def load(self):  # 缺少返回类型
        with open(self.path) as f:  # 没有 encoding
            data=json.load(f)  # 缺少异常处理
        return data
```

#### 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| 类名 | PascalCase | `BookmarkAnalyzer`, `DataSource` |
| 函数/方法 | snake_case | `analyze_domains`, `extract_skills` |
| 变量 | snake_case | `bookmark_count`, `user_name` |
| 常量 | UPPER_SNAKE_CASE | `MAX_RETRIES`, `API_VERSION` |
| 私有方法 | `_snake_case` | `_parse_folder`, `_extract_domain` |

#### 文档字符串

```python
def analyze_timeline(self, months: int = 12) -> Dict[str, any]:
    """
    分析学习时间线
    
    Args:
        months: 分析的月份数量，默认 12 个月
    
    Returns:
        包含以下字段的字典:
        - monthly: 每月统计数据
        - phases: 学习阶段列表
        - stats: 总体统计信息
    
    Raises:
        ValueError: 当 months 小于 1 时
    
    Example:
        >>> analyzer = BookmarkAnalyzer('data.json')
        >>> analyzer.load()
        >>> timeline = analyzer.analyze_timeline(months=6)
    """
    pass
```

---

### Git 规范

#### Commit Message 格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Type 类型

| Type | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat(skills): 添加技能趋势分析` |
| `fix` | Bug 修复 | `fix(timeline): 修复时间线排序问题` |
| `docs` | 文档更新 | `docs(readme): 添加安装说明` |
| `style` | 代码格式 | `style(cli): 格式化代码` |
| `refactor` | 重构 | `refactor(analyzer): 提取公共方法` |
| `test` | 测试相关 | `test(skills): 添加单元测试` |
| `chore` | 构建/工具 | `chore(deps): 更新依赖版本` |

#### Commit 示例

```bash
# ✅ 好的示例
git commit -m "feat(skills): 添加技能趋势分析

- 实现技能频率统计
- 添加技能增长趋势计算
- 支持按类别分组显示

Closes #42"

git commit -m "fix(timeline): 修复时间线排序问题

当月份数据缺失时，时间线排序错误。
现在使用 sorted() 确保正确排序。

Fixes #38"

# ❌ 坏的示例
git commit -m "update code"
git commit -m "fix bug"
git commit -m "asdfasdf"
```

#### Branch 命名

```
feature/<name>     # 新功能
fix/<name>         # Bug 修复
hotfix/<name>      # 紧急修复
release/<version>  # 发布分支
docs/<name>        # 文档更新
test/<name>        # 测试相关
```

示例:
```
feature/github-import
fix/timeline-sorting
release/v0.3.0
```

---

### 测试规范

#### 测试结构

```python
# tests/unit/test_skill_analyzer.py
import pytest
from src.analyzers.skill_analyzer import SkillAnalyzer

class TestSkillAnalyzer:
    """技能分析器测试"""
    
    def setup_method(self):
        """每个测试前的准备"""
        self.analyzer = SkillAnalyzer()
    
    def test_extract_skills_from_title(self):
        """测试从标题提取技能"""
        title = "Python 机器学习实战"
        skills = self.analyzer.extract_from_text(title)
        
        assert "Python" in skills
        assert "机器学习" in skills
    
    def test_extract_skills_with_no_matches(self):
        """测试无匹配技能的情况"""
        title = "随便的文章"
        skills = self.analyzer.extract_from_text(title)
        
        assert len(skills) == 0
    
    def test_skill_counting(self):
        """测试技能计数"""
        bookmarks = [
            {"name": "Python 教程", "url": "..."},
            {"name": "Python 进阶", "url": "..."},
            {"name": "Java 入门", "url": "..."},
        ]
        
        result = self.analyzer.analyze(bookmarks)
        
        assert result["Python"] == 2
        assert result["Java"] == 1
```

#### 测试覆盖率要求

| 模块 | 覆盖率要求 | 优先级 |
|------|-----------|--------|
| 核心分析器 | > 90% | P0 |
| 数据源适配器 | > 80% | P0 |
| CLI 命令 | > 70% | P1 |
| 工具函数 | > 80% | P1 |
| API 层 | > 70% | P2 |

---

### 文档规范

#### README 结构

```markdown
# 项目名称

简短描述 (1-2 句话)

## ✨ 特性

- 特性 1
- 特性 2
- 特性 3

## 🚀 快速开始

### 安装

```bash
pip install personal-insights
```

### 使用

```bash
# 导入数据
personal-insights import --platform browser

# 查看分析
personal-insights stats
personal-insights skills
```

## 📖 文档

- [安装指南](docs/installation.md)
- [使用教程](docs/usage.md)
- [API 文档](docs/api.md)
- [架构设计](docs/architecture.md)

## 🤝 贡献

欢迎贡献！查看 [贡献指南](CONTRIBUTING.md)

## 📄 License

MIT License
```

#### API 文档

```markdown
# API 文档

## 分析 API

### POST /api/v1/analyze

分析书签数据

**请求**:
```json
{
  "bookmarks": [...],
  "options": {
    "include_skills": true,
    "include_timeline": true
  }
}
```

**响应**:
```json
{
  "status": "success",
  "data": {
    "skills": {...},
    "timeline": {...}
  }
}
```
```

---

## 🔧 工具链

### 开发工具

```toml
# pyproject.toml
[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.28.0"
cryptography = "^38.0.0"
python-dateutil = "^2.8.2"
rich = "^13.0.0"  # 终端美化
click = "^8.0.0"  # CLI 框架
pydantic = "^2.0.0"  # 数据验证

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
pytest-cov = "^4.0.0"  # 覆盖率
mypy = "^1.0.0"  # 类型检查
black = "^23.0.0"  # 代码格式化
flake8 = "^6.0.0"  # 代码检查
pre-commit = "^3.0.0"  # Git 钩子
```

### Pre-commit 配置

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
  
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
        language_version: python3.10
  
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=100]
  
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.0.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests, types-python-dateutil]
```

### CI/CD 配置

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11"]
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          pip install poetry
          poetry install
      
      - name: Lint
        run: |
          poetry run black --check src/
          poetry run flake8 src/
          poetry run mypy src/
      
      - name: Test
        run: |
          poetry run pytest --cov=src --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

---

## 📊 质量指标

### 代码质量

| 指标 | 目标 | 当前 | 状态 |
|------|------|------|------|
| 单元测试覆盖率 | > 80% | ~0% | ❌ |
| 类型注解覆盖率 | > 90% | ~10% | ❌ |
| Code Smell | < 50 | ? | ⚠️ |
| 技术债务比率 | < 5% | ? | ⚠️ |
| 文档覆盖率 | > 80% | ~60% | ⚠️ |

### 性能指标

| 操作 | 目标时间 | 当前 | 状态 |
|------|---------|------|------|
| 加载 1000 书签 | < 1s | ~0.5s | ✅ |
| 分析 1000 书签 | < 2s | ~1s | ✅ |
| 生成报告 | < 5s | ~3s | ✅ |
| GitHub 导入 (100) | < 10s | ~8s | ✅ |

---

## 🎯 下一步行动

### 立即行动 (本周)

1. **项目结构重组** (4h)
   - [ ] 创建新的目录结构
   - [ ] 移动文件到新位置
   - [ ] 更新导入路径

2. **添加类型注解** (6h)
   - [ ] 为核心类添加类型注解
   - [ ] 配置 mypy
   - [ ] 修复类型错误

3. **配置开发工具** (2h)
   - [ ] 创建 pyproject.toml
   - [ ] 配置 pre-commit
   - [ ] 配置 CI/CD

### 短期目标 (本月)

1. **单元测试** (8h)
   - [ ] 配置 pytest
   - [ ] 编写核心分析器测试
   - [ ] 编写数据源测试

2. **错误处理** (3h)
   - [ ] 添加自定义异常类
   - [ ] 完善异常处理
   - [ ] 添加用户友好的错误消息

3. **日志系统** (3h)
   - [ ] 配置 logging
   - [ ] 添加关键日志点
   - [ ] 配置日志级别

### 中期目标 (本季度)

1. **Web UI** (10h)
   - [ ] 设计 UI 原型
   - [ ] 实现基础页面
   - [ ] 集成 API

2. **新数据源** (8h)
   - [ ] 知乎收藏
   - [ ] B 站收藏

3. **文档完善** (4h)
   - [ ] API 文档
   - [ ] 使用教程
   - [ ] 贡献指南

---

## 📝 决策记录

### 2026-03-13: 项目结构重组

**决策**: 从单体结构重构为模块化结构

**理由**:
1. 当前 `bookmark_analyzer.py` 707 行，过于臃肿
2. 缺少清晰的模块边界
3. 不利于团队协作
4. 难以测试和维护

**权衡**:
- ❌ 需要重构代码，短期工作量增加
- ✅ 长期可维护性提升
- ✅ 便于新功能开发
- ✅ 便于测试

### 2026-03-13: 采用类型注解

**决策**: 全面采用 Python 类型注解

**理由**:
1. 提升代码可读性
2. 早期发现类型错误
3. 更好的 IDE 支持
4. 自动生成文档

**权衡**:
- ❌ 开发时间略增
- ✅ 减少运行时错误
- ✅ 提升代码质量

### 2026-03-13: 测试驱动开发

**决策**: 新功能采用 TDD，旧代码逐步补充测试

**理由**:
1. 保证代码质量
2. 防止回归
3. 文档即测试
4. 重构更安全

**权衡**:
- ❌ 开发时间增加 30-50%
- ✅ Bug 率显著降低
- ✅ 维护成本降低

---

## 🔗 参考资料

- [Python 代码规范](https://peps.python.org/pep-0008/)
- [类型注解最佳实践](https://docs.python.org/3/library/typing.html)
- [Git Commit 规范](https://www.conventionalcommits.org/)
- [测试最佳实践](https://docs.pytest.org/)
- [pre-commit](https://pre-commit.com/)

---

**维护者**: @JerryZ01  
**最后更新**: 2026-03-13  
**版本**: v0.3.0-planning
