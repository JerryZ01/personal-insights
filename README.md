# 🔐 Personal Insights

**做成一个比自己更懂自己的开源项目**

让所有收藏不再落灰，但数据永远留在本地！

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Privacy First](https://img.shields.io/badge/privacy-first-green.svg)](https://en.wikipedia.org/wiki/Privacy_by_design)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Privacy First](https://img.shields.io/badge/privacy-first-green.svg)](https://en.wikipedia.org/wiki/Privacy_by_design)

基于你的全平台收藏数据（浏览器、GitHub、知乎、B 站...），在**本地**生成个人知识图谱、学习轨迹、能力画像和趋势预测。

**核心承诺：数据不出设备，隐私绝不泄露！**

---

## 🎯 能做什么

### 📊 个人知识图谱
```
从你的 616 个浏览器书签 + 45 个 GitHub Stars 分析：

AI/大模型 (精通度：⭐⭐⭐⭐⭐)
├─ Transformer: 45 篇 → 深度理解
├─ PyTorch: 34 篇 → 熟练使用
└─ LLM: 56 篇 → 持续关注

云计算 (精通度：⭐⭐⭐⭐)
├─ Kubernetes: 18 篇 → 实践级
└─ OpenStack: 32 篇 → 专家级
```

### 📈 学习轨迹分析
```
2025-Q1: 云计算深入期 (35 篇)
2025-Q2: AI 转型期 (67 篇)
2025-Q3: 昇腾开发期 (45 篇)
2025-Q4: 面试准备期 (78 篇)

洞察：你每 3-4 个月深入学习一个新领域
预测：2026-Q1 会关注大模型推理优化
```

### 🎯 能力雷达图
```
技术深度：⭐⭐⭐⭐⭐
学习能力：⭐⭐⭐⭐⭐
行业洞察：⭐⭐⭐⭐
表达能力：⭐⭐⭐

综合评估：T 型人才，技术深度突出
```

### 💡 智能推荐
```
知识缺口:
- [ ] vLLM 源码 (你收藏了 FlashAttention 但没 vLLM)
- [ ] RAG 实战 (理论够了，缺项目)

推荐学习路径:
Transformer → FlashAttention → vLLM → SGLang
```

### 🧹 健康检查
```
总书签：616 个
重复收藏：0 个
疑似失效：3 个
建议清理：3 个
```

---

## 🚀 快速开始

### 安装

```bash
# 克隆项目
git clone https://github.com/JerryZ01/personal-insights.git
cd personal-insights

# 安装依赖
pip install -r requirements.txt
```

### 使用

#### 1️⃣ 导入浏览器书签

```bash
# 从 Chrome 导出书签 (手动)
# Chrome → Ctrl+Shift+O → 导出书签 → bookmarks.html

# 放到输入目录
cp bookmarks.html data/input/

# 或者直接复制 Bookmarks 文件
cp /path/to/Chrome/Bookmarks data/input/bookmarks.json
```

#### 2️⃣ 运行分析

```bash
# 查看统计
python cli.py stats

# 技能清单
python cli.py skills

# 学习轨迹
python cli.py timeline

# 健康检查
python cli.py health

# 完整报告
python cli.py report
```

#### 3️⃣ 生成可视化

```bash
# 生成知识图谱
python cli.py graph

# 在浏览器打开
open output/graph.html
```

---

## 📱 支持的平台

| 平台 | 状态 | 隐私风险 | 说明 |
|------|------|----------|------|
| **浏览器书签** | ✅ 已完成 | 🟢 低 | Chrome/Edge/Firefox |
| **GitHub Stars** | 🟡 开发中 | 🟢 低 | 公开数据，API 友好 |
| **知乎收藏** | ⏳ 计划中 | 🟡 中 | 需要登录 |
| **B 站收藏** | ⏳ 计划中 | 🟡 中 | 需要登录 |
| **豆瓣** | ⏳ 计划中 | 🟡 中 | 需要登录 |

---

## 🔐 隐私保护

### 技术保障

```
✅ 所有数据本地存储
✅ AES-256 加密
✅ 密钥由用户密码派生 (我们不知道)
✅ 不开启云端分析
✅ 不收集使用统计
✅ 不上传任何个人数据
✅ 100% 开源代码 (可审计)
```

### 架构设计

```
┌─────────────────────────────────┐
│     你的设备 (本地运行)          │
│  ┌───────────────────────────┐  │
│  │  数据收集                  │  │
│  │  - 浏览器 ✅               │  │
│  │  - GitHub (待接入)         │  │
│  │  - 知乎/B 站 (待接入)      │  │
│  └───────────────────────────┘  │
│            ↓                     │
│  ┌───────────────────────────┐  │
│  │  AI 分析 (本地)            │  │
│  │  - 技能提取               │  │
│  │  - 画像构建               │  │
│  │  - 趋势预测               │  │
│  └───────────────────────────┘  │
│            ↓                     │
│  ┌───────────────────────────┐  │
│  │  AES-256 加密存储          │  │
│  │  密钥只有你知道            │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

### 数据最小化

```
✅ 采集的数据:
- 收藏的 URL/ID
- 收藏时间
- 标题/描述
- 分类/标签

❌ 不采集的数据:
- 账号密码
- 浏览历史
- 聊天记录
- 个人信息 (姓名、电话、地址)
- 设备信息
```

---

## 📊 示例输出

### 统计信息

```bash
$ python cli.py stats

📊 书签统计

总书签数：616
独立域名：178

🌐 热门域名 TOP 5:
  1. blog.csdn.net: 135
  2. zhuanlan.zhihu.com: 94
  3. cnblogs.com: 51
  4. cloud.tencent.com: 28
  5. github.com: 16

📚 技术领域 TOP 5:
  • AI/大模型：121 篇
  • 大数据：100 篇
  • 云计算：91 篇
  • 编程语言：62 篇
  • AI 芯片：48 篇
```

### 技能清单

```bash
$ python cli.py skills

🎯 技能清单

### AI 芯片
  ⭐⭐⭐⭐ Ascend: 17 次
  ⭐⭐⭐⭐ 昇腾：15 次
  ⭐⭐⭐ CANN: 14 次

### 云计算
  ⭐⭐⭐⭐⭐ OpenStack: 32 次
  ⭐⭐⭐⭐ CVM: 18 次
  ⭐⭐⭐⭐ K8s: 18 次

### 大模型
  ⭐⭐⭐⭐⭐ 大模型：32 次
  ⭐⭐⭐⭐⭐ LLM: 23 次
  ⭐⭐⭐ RAG: 11 次
```

### 学习轨迹

```bash
$ python cli.py timeline

📅 学习轨迹

2025-02 | ███████████ 22 篇 - AI/大模型
2025-03 | ██████ 12 篇 - 深度学习
2025-08 | █████████ 19 篇 - AI/大模型
2025-09 | ████████ 17 篇 - AI/大模型
```

---

## 🛠️ 项目结构

```
personal-insights/
├── cli.py                    # 命令行工具
├── requirements.txt          # Python 依赖
├── README.md                 # 项目说明
├── LICENSE                   # MIT License
│
├── src/                      # 源代码
│   ├── analyzer/             # 分析引擎
│   │   ├── bookmark_analyzer.py
│   │   ├── skill_extractor.py
│   │   ├── timeline_analyzer.py
│   │   └── health_checker.py
│   ├── sources/              # 数据源适配器
│   │   ├── browser.py        # ✅ 浏览器
│   │   ├── github.py         # 🟡 GitHub (开发中)
│   │   └── zhihu.py          # ⏳ 知乎 (计划)
│   └── visualizer/           # 可视化
│       ├── knowledge_graph.py
│       └── radar_chart.py
│
├── data/                     # 数据目录
│   ├── input/                # 输入 (你的收藏数据)
│   ├── output/               # 输出 (分析报告)
│   └── encrypted/            # 加密存储 (可选)
│
└── tests/                    # 测试
    ├── test_analyzer.py
    └── test_sources.py
```

---

## 🗺️ 开发路线图

### Phase 1: 核心功能 (2026-Q1)
- [x] 浏览器书签分析 ✅
- [ ] GitHub Stars 接入
- [ ] 统一数据模型
- [ ] 基础画像生成
- [ ] CLI 工具

### Phase 2: 平台扩展 (2026-Q2)
- [ ] 知乎收藏接入
- [ ] B 站收藏接入
- [ ] 豆瓣接入
- [ ] 跨平台分析

### Phase 3: 用户体验 (2026-Q3)
- [ ] Web UI (可视化)
- [ ] 报告导出 (PDF)
- [ ] 桌面应用 (Electron)

### Phase 4: 隐私增强 (2026-Q4)
- [ ] 端到端加密同步
- [ ] 零知识证明
- [ ] 第三方安全审计

---

## 🤝 贡献指南

欢迎贡献！这是一个隐私优先的开源项目。

### 开发环境

```bash
# 克隆项目
git clone https://github.com/JerryZ01/personal-insights.git
cd personal-insights

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发依赖
pip install -r requirements-dev.txt

# 运行测试
pytest tests/
```

### 贡献方式

1. 🐛 报告 Bug (提交 Issue)
2. 💡 提出新功能建议
3. 🔧 提交代码 (Pull Request)
4. 📖 改进文档
5. 🌍 翻译

### 代码规范

- 遵循 PEP 8
- 添加类型注解
- 写单元测试
- 代码需要审查

---

## 📄 License

MIT License - 见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

感谢所有为隐私保护做出贡献的开发者！

---

## 📬 联系方式

- 📧 Email: jerryz01@proton.me
- 🐦 Twitter: @JerryZ01
- 💬 Discord: [个人成长洞察社区](https://discord.gg/xxx)

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=JerryZ01/personal-insights&type=Date)](https://star-history.com/#JerryZ01/personal-insights&Date)

---

**🔐 你的数据永远属于你！**
