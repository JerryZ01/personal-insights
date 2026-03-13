# 🏗️ Personal Insights - 系统架构设计

**版本**: v0.2.0  
**最后更新**: 2026-03-13  
**状态**: 设计中

---

## 📋 目录

1. [系统概览](#系统概览)
2. [架构原则](#架构原则)
3. [分层架构](#分层架构)
4. [核心模块](#核心模块)
5. [数据流设计](#数据流设计)
6. [隐私保护架构](#隐私保护架构)
7. [扩展性设计](#扩展性设计)
8. [技术栈选型](#技术栈选型)
9. [部署架构](#部署架构)
10. [性能优化](#性能优化)

---

## 🎯 系统概览

### 核心价值主张

```
┌─────────────────────────────────────────────────────────┐
│              Personal Insights                           │
│                                                          │
│   输入：全平台收藏数据 (书签/Stars/收藏...)               │
│           ↓                                              │
│   处理：本地分析引擎 (技能提取/画像构建/趋势预测)         │
│           ↓                                              │
│   输出：个人洞察报告 (知识图谱/成长轨迹/发展建议)         │
│                                                          │
│   核心承诺：数据不出设备，隐私绝不泄露！                  │
└─────────────────────────────────────────────────────────┘
```

### 高层架构图

```
┌──────────────────────────────────────────────────────────────┐
│                      用户界面层                                │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐             │
│  │   CLI 工具   │ │  OpenClaw   │ │   Web UI    │             │
│  │             │ │   Skill     │ │  (可选)     │             │
│  └─────────────┘ └─────────────┘ └─────────────┘             │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                      应用服务层                                │
│  ┌──────────────────────────────────────────────────────┐    │
│  │              Personal Insights CLI                    │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐ │    │
│  │  │  stats   │ │  skills  │ │ timeline │ │ github  │ │    │
│  │  └──────────┘ └──────────┘ └──────────┘ └─────────┘ │    │
│  └──────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                      分析引擎层                                │
│  ┌──────────────────────────────────────────────────────┐    │
│  │              BookmarkAnalyzer                         │    │
│  │  - 域名分析                                           │    │
│  │  - 内容分类                                           │    │
│  │  - 技能提取                                           │    │
│  │  - 时间线分析                                         │    │
│  │  - 健康检查                                           │    │
│  └──────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                      数据源适配层                              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐             │
│  │  Browser    │ │   GitHub    │ │  (更多...)  │             │
│  │  Bookmarks  │ │   Stars     │ │             │             │
│  └─────────────┘ └─────────────┘ └─────────────┘             │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                      数据存储层                                │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐             │
│  │  输入数据   │ │  分析结果   │ │  加密存储   │             │
│  │  (JSON)     │ │  (JSON)     │ │  (可选)     │             │
│  └─────────────┘ └─────────────┘ └─────────────┘             │
└──────────────────────────────────────────────────────────────┘
```

---

## 🏛️ 架构原则

### 1. 本地优先 (Local-First)

```
✅ 所有数据处理在本地完成
✅ 不依赖云端服务 (除数据源 API 外)
✅ 离线可用
✅ 低延迟响应
```

### 2. 隐私优先 (Privacy-First)

```
✅ 数据不出设备
✅ 最小化数据采集
✅ 可选加密存储
✅ 用户完全控制
```

### 3. 模块化设计 (Modular)

```
✅ 数据源可插拔
✅ 分析器可扩展
✅ 界面可替换
✅ 功能可组合
```

### 4. 开放扩展 (Extensible)

```
✅ 开源代码可审计
✅ API 接口标准化
✅ 支持自定义分析器
✅ 支持第三方数据源
```

---

## 🏗️ 分层架构

### Layer 1: 用户界面层 (Presentation Layer)

**职责**: 与用户交互，展示分析结果

#### 1.1 CLI 工具
```python
# 命令行入口
cli.py
├── stats         # 统计信息
├── skills        # 技能清单
├── timeline      # 学习轨迹
├── health        # 健康检查
├── report        # 完整报告
├── github        # GitHub Stars 导入
└── import        # 通用导入命令 (TODO)
```

**特点**:
- 开发者友好
- 脚本化自动化
- 低资源占用

#### 1.2 OpenClaw Skill (TODO)
```python
# OpenClaw 集成
/openclaw-skill/
├── skill.py      # Skill 入口
├── commands.py   # 命令处理
└── templates.py  # 回复模板
```

**特点**:
- 聊天式交互
- 自然语言查询
- 日常使用场景

#### 1.3 Web UI (TODO)
```
/web-ui/
├── index.html    # 主页面
├── app.js        # 前端逻辑
├── styles.css    # 样式
└── components/   # UI 组件
    ├── KnowledgeGraph.vue
    ├── Timeline.vue
    ├── RadarChart.vue
    └── SkillTree.vue
```

**特点**:
- 可视化展示
- 交互式探索
- 报告导出

### Layer 2: 应用服务层 (Application Layer)

**职责**: 业务逻辑编排，命令处理

#### 2.1 命令处理器
```python
class CommandHandler:
    """命令处理器"""
    
    def __init__(self):
        self.analyzer = None
        self.sources = {}
    
    def execute(self, command: str, args: Dict) -> Result:
        """执行命令"""
        if command == 'stats':
            return self.cmd_stats(args)
        elif command == 'skills':
            return self.cmd_skills(args)
        # ... 其他命令
```

#### 2.2 服务编排
```python
class PersonalInsightsService:
    """个人洞察服务"""
    
    def __init__(self, config: Config):
        self.config = config
        self.data_loader = DataLoader()
        self.analyzer = Analyzer()
        self.reporter = Reporter()
    
    def generate_profile(self) -> PersonalProfile:
        """生成个人画像"""
        # 1. 加载数据
        items = self.data_loader.load_all()
        
        # 2. 分析
        profile = self.analyzer.analyze(items)
        
        # 3. 生成报告
        report = self.reporter.generate(profile)
        
        return report
```

### Layer 3: 分析引擎层 (Analysis Layer)

**职责**: 核心分析逻辑，算法实现

#### 3.1 BookmarkAnalyzer (核心)
```python
class BookmarkAnalyzer:
    """书签分析引擎"""
    
    # 配置映射
    DOMAIN_CATEGORIES = {...}      # 域名→分类
    SKILL_KEYWORDS = {...}         # 关键词→技能
    TECH_TAXONOMY = {...}          # 技术分类体系
    
    def load(self) -> List[Dict]:
        """加载数据"""
    
    def analyze_domains(self) -> Dict:
        """域名分析"""
    
    def analyze_content(self) -> Dict:
        """内容分类"""
    
    def extract_skills(self) -> Dict:
        """技能提取"""
    
    def analyze_timeline(self) -> Dict:
        """时间线分析"""
    
    def health_check(self) -> Dict:
        """健康检查"""
    
    def generate_report(self) -> str:
        """生成报告"""
```

#### 3.2 未来扩展的分析器 (TODO)
```python
class LearningStyleAnalyzer:
    """学习风格分析"""
    def analyze(self, items) -> LearningStyle:
        # 分析内容类型偏好
        # 分析学习时间模式
        # 分析学习强度

class CareerAnalyzer:
    """职业能力分析"""
    def analyze(self, items) -> CareerProfile:
        # 硬技能评估
        # 软技能评估
        # 市场价值估算

class TrendPredictor:
    """趋势预测"""
    def predict(self, items) -> TrendPrediction:
        # 基于历史模式预测
        # 识别知识缺口
        # 推荐学习路径
```

### Layer 4: 数据源适配层 (DataSource Layer)

**职责**: 从各平台获取数据，转换为统一格式

#### 4.1 统一接口
```python
class DataSource(ABC):
    """数据源基类"""
    
    def __init__(self, name: str, privacy_level: str):
        self.name = name
        self.privacy_level = privacy_level  # low/medium/high
    
    @abstractmethod
    def fetch(self, credentials: Optional[Dict] = None) -> List[Dict]:
        """获取原始数据"""
        pass
    
    @abstractmethod
    def to_unified_format(self, raw_data: Any) -> List[Dict]:
        """转换为统一格式"""
        pass
```

#### 4.2 已实现的数据源
```python
class BrowserBookmarksSource(DataSource):
    """浏览器书签"""
    # ✅ 已完成
    # 支持：Chrome/Edge/Firefox
    # 格式：JSON/HTML
    # 隐私：🟢 低风险

class GitHubStarsSource(DataSource):
    """GitHub Stars"""
    # ✅ 已完成
    # API: GitHub REST API v3
    # 认证：Personal Access Token
    # 隐私：🟢 低风险 (公开数据)
```

#### 4.3 计划中的数据源 (TODO)
```python
class ZhihuFavoritesSource(DataSource):
    """知乎收藏"""
    # ⏳ 计划中
    # API: 知乎爬虫 (需要登录)
    # 隐私：🟡 中风险

class BilibiliFavoritesSource(DataSource):
    """B 站收藏"""
    # ⏳ 计划中
    # API: B 站开放 API
    # 隐私：🟡 中风险

class DoubanSource(DataSource):
    """豆瓣"""
    # ⏳ 计划中
    # API: 豆瓣开放 API / 爬虫
    # 隐私：🟡 中风险
```

### Layer 5: 数据存储层 (Storage Layer)

**职责**: 数据持久化，加密存储

#### 5.1 目录结构
```
personal-insights/
├── data/
│   ├── input/              # 输入数据
│   │   ├── bookmarks.json         # 浏览器书签
│   │   ├── github_stars.json      # GitHub Stars
│   │   └── ...                    # 其他平台
│   │
│   ├── output/             # 分析结果
│   │   ├── report.md              # 完整报告
│   │   ├── analysis.json          # 详细数据
│   │   └── ...                    # 导出文件
│   │
│   └── encrypted/          # 加密存储 (可选)
│       ├── profile.enc              # 加密画像
│       └── ...                      # 其他加密数据
```

#### 5.2 加密存储 (TODO)
```python
class EncryptedStorage:
    """加密存储管理器"""
    
    def __init__(self, master_password: str):
        self.key = self.derive_key(master_password)
    
    def encrypt_and_save(self, data: Dict, path: str):
        """加密并保存"""
        encrypted = self.aes_encrypt(data, self.key)
        Path(path).write_bytes(encrypted)
    
    def load_and_decrypt(self, path: str) -> Dict:
        """加载并解密"""
        encrypted = Path(path).read_bytes()
        return self.aes_decrypt(encrypted, self.key)
    
    def derive_key(self, password: str) -> bytes:
        """从密码派生密钥 (PBKDF2)"""
        # 使用用户密码 + salt 派生 AES-256 密钥
        pass
```

---

## 🔄 数据流设计

### 典型数据流：导入 → 分析 → 展示

```
┌─────────────┐
│   用户操作   │  python cli.py github --token <token>
└──────┬──────┘
       ↓
┌─────────────────────────────────────────┐
│  1. 数据源适配层                         │
│                                         │
│  GitHubStarsSource.fetch()              │
│    ↓                                    │
│  GitHub API → 原始 JSON                 │
│    ↓                                    │
│  to_unified_format()                    │
│    ↓                                    │
│  统一格式 Bookmark[]                    │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│  2. 数据存储层                           │
│                                         │
│  保存至 data/input/github_stars.json    │
│  保存至 data/input/github_stars_bookmarks.json │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│  3. 分析引擎层                           │
│                                         │
│  BookmarkAnalyzer.load()                │
│    ↓                                    │
│  BookmarkAnalyzer.analyze_domains()     │
│  BookmarkAnalyzer.analyze_content()     │
│  BookmarkAnalyzer.extract_skills()      │
│  BookmarkAnalyzer.analyze_timeline()    │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│  4. 应用服务层                           │
│                                         │
│  CommandHandler.execute('stats')        │
│    ↓                                    │
│  格式化输出                             │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────┐
│  5. 展示层   │  终端输出统计信息
└─────────────┘
```

### 跨平台合并分析流程 (TODO)

```
┌─────────────────────────────────────────┐
│  多平台数据合并                          │
│                                         │
│  data/input/                            │
│  ├── bookmarks.json (浏览器)            │
│  ├── github_stars.json (GitHub)         │
│  ├── zhihu.json (知乎) ← 未来          │
│  └── bilibili.json (B 站) ← 未来       │
│            ↓                            │
│  Merger.merge_all()                     │
│            ↓                            │
│  UnifiedItem[] (去重 + 标准化)          │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│  跨平台分析                              │
│                                         │
│  - 跨平台兴趣分析                       │
│  - 内容消费习惯                         │
│  - 学习强度统计                         │
│  - 平台偏好分析                         │
└──────────────┬──────────────────────────┘
```

---

## 🔐 隐私保护架构

### 隐私分层设计

```
┌─────────────────────────────────────────────────────┐
│  L1: 公开数据 (🟢 低风险)                            │
│  - GitHub Stars (公开可见)                          │
│  - 公开博客书签                                     │
│  处理：直接分析，无需加密                           │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│  L2: 半私密数据 (🟡 中风险)                          │
│  - 知乎收藏 (需登录)                                │
│  - B 站收藏 (需登录)                                │
│  处理：本地分析，可选加密                           │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│  L3: 私密数据 (🔴 高风险)                            │
│  - 微信读书                                         │
│  - 私人笔记                                         │
│  处理：必须加密，用户确认                           │
└─────────────────────────────────────────────────────┘
```

### 加密架构

```
用户密码 (Passphrase)
       ↓
  PBKDF2 (100000 次迭代 + 随机 Salt)
       ↓
  AES-256 密钥 (256-bit)
       ↓
  加密数据 (AES-GCM 模式)
       ↓
  存储：encrypted/profile.enc
```

### 零知识证明设计 (TODO)

```python
class ZeroKnowledgeSync:
    """零知识同步 (未来云端同步场景)"""
    
    def __init__(self, password: str):
        # 密钥从用户密码派生，服务器不知道
        self.key = self.derive_key(password)
    
    def encrypt_for_sync(self, data: Dict) -> bytes:
        """本地加密后上传"""
        # 只有用户能解密
        # 服务器只看到加密数据
        pass
    
    def decrypt_from_sync(self, encrypted: bytes) -> Dict:
        """下载后本地解密"""
        # 用本地密钥解密
        pass
```

---

## 🔌 扩展性设计

### 插件化架构 (TODO)

```
personal-insights/
├── core/               # 核心框架
│   ├── analyzer.py
│   ├── datasource.py
│   └── storage.py
│
├── plugins/            # 插件目录
│   ├── builtin/        # 内置插件
│   │   ├── browser.py
│   │   └── github.py
│   └── community/      # 社区插件
│       └── zhihu.py    # (用户安装)
│
└── plugin_api.py       # 插件 API
```

### 插件接口

```python
class Plugin(ABC):
    """插件基类"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """插件名称"""
        pass
    
    @property
    @abstractmethod
    def version(self) -> str:
        """插件版本"""
        pass
    
    @abstractmethod
    def install(self, config: Dict):
        """安装插件"""
        pass
    
    @abstractmethod
    def run(self, context: Dict) -> Result:
        """运行插件"""
        pass
```

### 分析器扩展 (TODO)

```python
class CustomAnalyzer(Analyzer):
    """自定义分析器"""
    
    def __init__(self, config: Dict):
        # 用户可自定义分析逻辑
        self.config = config
    
    def analyze(self, items: List[Dict]) -> Dict:
        # 自定义分析算法
        pass
```

---

## 🛠️ 技术栈选型

### 核心技术栈

| 层级 | 技术 | 理由 |
|------|------|------|
| **核心语言** | Python 3.10+ | 生态丰富，AI/分析库完善 |
| **CLI 框架** | argparse (内置) | 零依赖，简单够用 |
| **Web 框架** | FastAPI (可选) | 异步，自动文档 |
| **前端** | Vue 3 + D3.js (可选) | 响应式，可视化强 |
| **桌面应用** | Electron (可选) | 跨平台，成熟稳定 |
| **加密** | cryptography | Python 标准，AES-256 |
| **数据库** | SQLite (可选) | 轻量，嵌入式 |

### 依赖管理

```txt
# requirements.txt
requests>=2.28.0      # HTTP 请求
cryptography>=38.0.0  # 加密
python-dateutil>=2.8.2 # 日期处理
rich>=13.0.0          # 终端美化 (可选)
fastapi>=0.95.0       # Web API (可选)
uvicorn>=0.21.0       # Web 服务器 (可选)
```

### 开发工具

```txt
# requirements-dev.txt
pytest>=7.0.0         # 测试
black>=23.0.0         # 代码格式化
mypy>=1.0.0           # 类型检查
flake8>=6.0.0         # 代码检查
```

---

## 🚀 部署架构

### 部署模式 1: CLI 工具 (当前)

```
用户设备 (本地运行)
    ↓
安装：pip install personal-insights
    ↓
运行：personal-insights <command>
    ↓
数据：本地存储 ~/.personal-insights/
```

### 部署模式 2: OpenClaw Skill (当前)

```
OpenClaw 环境
    ↓
Skill 目录：~/.openclaw/workspace/personal-insights/
    ↓
运行：通过 OpenClaw CLI 调用
    ↓
数据：工作空间内存储
```

### 部署模式 3: Web 服务 (TODO)

```
本地运行:
    personal-insights web --port 8080
    ↓
浏览器访问：http://localhost:8080
    ↓
数据：本地存储，不上传
```

### 部署模式 4: 桌面应用 (TODO)

```
下载安装包 (.exe/.dmg/.deb)
    ↓
安装到本地
    ↓
自动后台运行，定期分析
    ↓
系统托盘通知
```

---

## ⚡ 性能优化

### 性能目标

| 操作 | 目标时间 | 当前实现 |
|------|---------|---------|
| 加载 1000 个书签 | < 1s | ✅ 已实现 |
| 分析 1000 个书签 | < 2s | ✅ 已实现 |
| 生成完整报告 | < 5s | ✅ 已实现 |
| GitHub Stars 导入 (100 个) | < 10s | ✅ 已实现 |
| 跨平台合并 (5000+ 项目) | < 30s | ⏳ 待优化 |

### 优化策略

#### 1. 懒加载
```python
class LazyAnalyzer:
    """懒加载分析器"""
    
    def __init__(self, data_path: str):
        self.data_path = data_path
        self._cache = None
    
    @property
    def data(self):
        # 只在首次访问时加载
        if self._cache is None:
            self._cache = self._load_data()
        return self._cache
```

#### 2. 增量分析
```python
class IncrementalAnalyzer:
    """增量分析"""
    
    def analyze_new_items(self, new_items: List) -> Dict:
        # 只分析新增项目
        # 合并到现有结果
        pass
```

#### 3. 缓存机制
```python
@lru_cache(maxsize=100)
def extract_skills(title: str, url: str) -> List[str]:
    """技能提取缓存"""
    # 相同标题/URL 不重复分析
    pass
```

#### 4. 并行处理 (TODO)
```python
from concurrent.futures import ThreadPoolExecutor

def analyze_in_parallel(items: List) -> Dict:
    """并行分析"""
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(analyze_item, items)
    return merge_results(results)
```

---

## 📊 监控与可观测性 (TODO)

### 本地日志

```python
import logging

logging.basicConfig(
    filename='~/.personal-insights/logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### 性能指标

```python
class Metrics:
    """性能指标收集"""
    
    def record(self, operation: str, duration_ms: int):
        # 记录操作耗时
        pass
    
    def report(self) -> Dict:
        # 生成性能报告
        return {
            'avg_load_time': ...,
            'avg_analyze_time': ...,
            'cache_hit_rate': ...,
        }
```

---

## 🧪 测试策略 (TODO)

### 测试分层

```
┌─────────────────────────────────────┐
│  E2E 测试 (10%)                      │
│  - 完整流程测试                     │
│  - 用户场景测试                     │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  集成测试 (20%)                      │
│  - 模块间交互                       │
│  - 数据流测试                       │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  单元测试 (70%)                      │
│  - 函数级测试                       │
│  - 边界条件测试                     │
└─────────────────────────────────────┘
```

### 测试覆盖率目标

```
- 核心分析器：> 90%
- 数据源适配器：> 80%
- CLI 工具：> 70%
- UI 组件：> 60%
```

---

## 🔮 未来架构演进

### v0.3.0 (2026-Q2)
- [ ] 多平台数据合并
- [ ] 跨平台分析
- [ ] Web UI 基础版

### v0.5.0 (2026-Q3)
- [ ] 加密存储
- [ ] 学习风格分析
- [ ] 趋势预测

### v1.0.0 (2026-Q4)
- [ ] 桌面应用
- [ ] 插件系统
- [ ] 零知识同步

### v2.0.0 (2027-Q1)
- [ ] AI 驱动推荐
- [ ] 人格特质分析
- [ ] 职业发展建议

---

## 📝 决策记录

### 2026-03-13: 选择 Python 而非 Node.js

**决策**: 使用 Python 作为核心语言

**理由**:
1. 数据分析生态更成熟 (pandas, numpy)
2. AI/ML 库丰富 (未来扩展)
3. 团队更熟悉 Python
4. CLI 工具开发简单

**权衡**:
- ❌ 前端开发需要额外技术栈
- ✅ 但核心是分析，不是 UI

### 2026-03-13: 本地优先而非云端

**决策**: 100% 本地运行

**理由**:
1. 隐私保护是核心价值
2. 降低用户信任门槛
3. 离线可用
4. 降低运营成本

**权衡**:
- ❌ 无法做跨用户洞察
- ✅ 但符合产品定位

### 2026-03-13: CLI 优先而非 UI 优先

**决策**: 先做 CLI，后做 UI

**理由**:
1. 开发成本低
2. 易于自动化
3. 开发者友好 (早期用户)
4. 快速验证核心功能

**权衡**:
- ❌ 普通用户门槛高
- ✅ 但可以逐步增加 UI

---

## 📚 参考资料

- [本地优先架构](https://localfirstweb.dev/)
- [零知识证明](https://en.wikipedia.org/wiki/Zero-knowledge_proof)
- [隐私设计原则](https://www.privacybydesign.foundation/)
- [Python 加密最佳实践](https://cryptography.io/)

---

**最后更新**: 2026-03-13  
**维护者**: @JerryZ01  
**状态**: 设计中 (v0.2.0)
