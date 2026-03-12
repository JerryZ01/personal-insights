# 🤝 Contributing to Personal Insights

欢迎贡献！这是一个隐私优先的个人分析开源项目。

---

## 🌟 贡献方式

### 1️⃣ 报告 Bug
发现 Bug？请提交 Issue：
- 描述问题
- 提供复现步骤
- 附上错误信息
- 说明环境 (OS/Python 版本)

### 2️⃣ 提出建议
有新想法？请开启 Discussion：
- 描述使用场景
- 说明预期效果
- 讨论实现方案

### 3️⃣ 提交代码
想写代码？请提交 PR：
- Fork 项目
- 创建功能分支
- 编写代码和测试
- 提交 Pull Request

### 4️⃣ 改进文档
文档不完整？请帮忙：
- 修正错别字
- 补充使用说明
- 添加示例
- 翻译文档

### 5️⃣ 分享推广
支持项目：
- Star 项目 ⭐
- 分享给朋友
- 写博客介绍
- 社交媒体推广

---

## 🛠️ 开发环境

### 1. 克隆项目

```bash
git clone https://github.com/JerryZ01/personal-insights.git
cd personal-insights
```

### 2. 创建虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 安装开发依赖

```bash
pip install -r requirements-dev.txt
```

### 5. 运行测试

```bash
pytest tests/
```

---

## 📝 代码规范

### Python 风格
- 遵循 [PEP 8](https://pep8.org/)
- 使用类型注解
- 添加文档字符串

### 代码示例

```python
def analyze_bookmarks(path: str) -> Dict:
    """分析浏览器书签
    
    Args:
        path: 书签文件路径
        
    Returns:
        分析结果字典
    """
    # 实现代码
    pass
```

### Git 提交信息

```bash
# 格式：<type>: <description>
git commit -m "feat: add GitHub Stars analyzer"
git commit -m "fix: resolve timeline parsing error"
git commit -m "docs: update README with examples"
git commit -m "test: add unit tests for analyzer"
```

### 类型说明

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式
- `refactor`: 重构
- `test`: 测试
- `chore`: 构建/工具

---

## 🧪 测试指南

### 运行测试

```bash
# 所有测试
pytest tests/

# 特定测试
pytest tests/test_analyzer.py

# 带覆盖率
pytest --cov=src tests/
```

### 编写测试

```python
def test_bookmark_analyzer():
    """测试书签分析器"""
    analyzer = BookmarkAnalyzer("test_data.json")
    bookmarks = analyzer.load()
    
    assert len(bookmarks) > 0
    assert analyzer.analyze_domains() is not None
```

---

## 📦 添加新数据源

### 1. 创建适配器

```python
# src/sources/github.py
from .base import DataSource

class GitHubStars(DataSource):
    def fetch(self, token: str) -> List[Item]:
        # 实现 GitHub API 调用
        pass
    
    def parse(self, raw_data) -> Item:
        # 解析为统一格式
        pass
```

### 2. 注册数据源

```python
# src/sources/__init__.py
from .github import GitHubStars
```

### 3. 添加 CLI 命令

```python
# cli.py
@cli.command()
def import_github(token):
    """导入 GitHub Stars"""
    source = GitHubStars()
    items = source.fetch(token)
    # 保存到 data/input/
```

### 4. 编写测试

```python
def test_github_stars():
    source = GitHubStars()
    # 测试代码
```

### 5. 更新文档

- 更新 README
- 添加使用说明
- 编写示例

---

## 🔐 隐私保护

贡献代码时请遵守：

### 数据最小化
```python
# ✅ 好的做法
item = {
    'url': url,
    'title': title,
    'favorited_at': date
}

# ❌ 不好的做法
item = {
    'username': username,  # 不要收集
    'password': password,  # 绝对不要
    'browsing_history': history  # 不需要
}
```

### 本地处理
```python
# ✅ 好的做法 - 本地分析
def analyze(items):
    return local_processing(items)

# ❌ 不好的做法 - 云端分析
def analyze(items):
    return api_call_to_cloud(items)  # 不要上传
```

### 加密存储
```python
# ✅ 好的做法
from cryptography.fernet import Fernet

def save_sensitive(data, key):
    f = Fernet(key)
    encrypted = f.encrypt(data)
    save(encrypted)
```

---

## 📋 PR 检查清单

提交 PR 前请确认：

- [ ] 代码通过测试
- [ ] 添加了新测试 (如适用)
- [ ] 代码符合 PEP 8
- [ ] 添加了类型注解
- [ ] 更新了文档
- [ ] 提交信息清晰
- [ ] 没有泄露隐私
- [ ] 没有硬编码密钥

---

## 🎯 当前需要帮助

### 高优先级
- [ ] GitHub Stars 接入
- [ ] 死链检测
- [ ] Web UI 设计
- [ ] 单元测试

### 中优先级
- [ ] 知乎收藏接入
- [ ] B 站收藏接入
- [ ] 文档翻译 (English)
- [ ] 示例数据

### 低优先级
- [ ] 桌面应用
- [ ] 移动端
- [ ] 更多可视化
- [ ] 性能优化

---

## 🙏 致谢

感谢所有贡献者！

[![Contributors](https://contrib.rocks/image?repo=JerryZ01/personal-insights)](https://github.com/JerryZ01/personal-insights/graphs/contributors)

---

## 📬 联系方式

- 💬 GitHub Discussions
- 📧 Email: jerryz01@proton.me
- 🐦 Twitter: @JerryZ01

---

**🪞 做成一个比自己更懂自己的开源项目**

**🤝 一起让这个项目更好！**
