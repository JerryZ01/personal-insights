# 🚀 快速开始指南

## 5 分钟上手

### 1. 安装

```bash
# 克隆项目
git clone https://github.com/JerryZ01/personal-insights.git
cd personal-insights

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 导入书签数据

**方法 A: 从 Chrome 导出**
```bash
# 1. Chrome 浏览器 → Ctrl+Shift+O → 导出书签 → bookmarks.html
# 2. 复制到输入目录
cp /path/to/bookmarks.html data/input/
```

**方法 B: 直接复制 Bookmarks 文件**
```bash
# Windows (WSL2):
cp "/mnt/c/Users/<用户名>/AppData/Local/Google/Chrome/User Data/<Profile>/Bookmarks" \
   data/input/bookmarks.json

# macOS:
cp ~/Library/Application\ Support/Google/Chrome/Default/Bookmarks \
   data/input/bookmarks.json

# Linux:
cp ~/.config/google-chrome/Default/Bookmarks \
   data/input/bookmarks.json
```

### 3. 运行分析

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
python cli.py report > output/report.md
```

### 4. 查看结果

```bash
# 查看报告
cat output/report.md

# 或者用文本编辑器打开
code output/report.md
```

---

## 常用命令

### 基础命令

```bash
# 显示帮助
python cli.py --help

# 查看统计
python cli.py stats

# 技能清单 (按领域分组)
python cli.py skills

# 学习轨迹 (按时间)
python cli.py timeline

# 健康检查 (死链/重复)
python cli.py health
```

### 高级命令

```bash
# 生成完整报告
python cli.py report

# 导出为 Markdown
python cli.py report > my-profile.md

# 指定输入文件
python cli.py stats -i /path/to/bookmarks.json

# 生成知识图谱 (开发中)
python cli.py graph
```

---

## 示例输出

### stats 命令
```
📊 书签统计

总书签数：616
独立域名：178

🌐 热门域名 TOP 5:
  1. blog.csdn.net: 135
  2. zhuanlan.zhihu.com: 94
  3. cnblogs.com: 51

📚 技术领域 TOP 5:
  • AI/大模型：121 篇
  • 大数据：100 篇
  • 云计算：91 篇
```

### skills 命令
```
🎯 技能清单

### AI 芯片
  ⭐⭐⭐⭐ Ascend: 17 次
  ⭐⭐⭐⭐ 昇腾：15 次
  ⭐⭐⭐ CANN: 14 次

### 云计算
  ⭐⭐⭐⭐⭐ OpenStack: 32 次
  ⭐⭐⭐⭐ K8s: 18 次
```

### timeline 命令
```
📅 学习轨迹

2025-08 | █████████ 19 篇 - AI/大模型
2025-09 | ████████ 17 篇 - AI/大模型
2026-03 | ██ 4 篇 - 其他
```

---

## 常见问题

### Q: 支持哪些浏览器？
A: 目前支持 Chrome/Edge (Chromium 内核)，Firefox 和 Safari 计划中。

### Q: 数据安全吗？
A: 非常安全！所有数据本地处理，不上传云端，代码开源可审计。

### Q: 如何删除我的数据？
A: 直接删除 `data/input/` 和 `data/output/` 目录下的文件即可。

### Q: 可以分析其他平台吗？
A: 计划支持 GitHub、知乎、B 站等，欢迎贡献代码！

---

## 下一步

- 📖 阅读 [README.md](README.md) 了解项目详情
- 🔐 查看 [PRIVACY.md](PRIVACY.md) 了解隐私保护措施
- 🤝 查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何贡献
- 💬 加入 Discord 社区讨论
