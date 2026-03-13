# 🚀 Personal Insights - 快速开始

## 方式一：一键启动（推荐）

```bash
# 启动后端 + 前端
./start.sh
```

访问：
- 前端：http://localhost:3000
- API 文档：http://localhost:8000/docs

---

## 方式二：分步启动

### 1. 后端 API

```bash
# 安装依赖
pip install fastapi uvicorn click

# 启动 API
uvicorn api.main:app --reload --port 8000
```

访问 API 文档：http://localhost:8000/docs

### 2. 前端（可选）

```bash
cd web

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

访问：http://localhost:3000

---

## 方式三：仅 CLI

```bash
# 使用新 CLI
python -m cli.main stats

# 或使用旧 CLI（兼容）
python cli.py stats
```

---

## 测试数据

项目已包含测试数据：
- `data/output/merged.json` - 合并后的书签数据（328 条）

如需导入自己的数据：
```bash
# 导入浏览器书签
python cli.py import --platform browser --input /path/to/bookmarks.json

# 导入 GitHub Stars
python cli.py github --token YOUR_TOKEN
```

---

## 项目结构

```
personal-insights/
├── src/                    # 后端源码
│   ├── core/              # 核心模块
│   ├── analyzers/         # 分析器
│   └── services/          # 服务层
├── api/                    # FastAPI 后端
├── web/                    # Vue 3 前端
├── cli/                    # CLI 工具
├── data/                   # 数据目录
└── start.sh               # 启动脚本
```

---

## 技术栈

- **后端**: Python 3.10+, FastAPI
- **前端**: Vue 3, TypeScript, Element Plus, ECharts
- **CLI**: Click
- **分析**: 自定义分析引擎

---

## 功能特性

✅ 书签数据分析
✅ GitHub Stars 导入
✅ 技能提取
✅ 时间线分析
✅ 健康检查
✅ 可视化界面
✅ 隐私保护（本地运行）

---

## 下一步

- [ ] 添加更多数据源（知乎、B 站）
- [ ] 增强分析能力（趋势预测）
- [ ] 导出 PDF 报告
- [ ] 加密存储
