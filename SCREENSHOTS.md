# 📸 Personal Insights - 项目截图

## CLI 命令演示

### 1️⃣ 查看统计

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

---

### 2️⃣ 技能清单

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

---

### 3️⃣ 学习轨迹

```bash
$ python cli.py timeline

📅 学习轨迹

2025-02 | ███████████ 22 篇 - AI/大模型
2025-03 | ██████ 12 篇 - 深度学习
2025-08 | █████████ 19 篇 - AI/大模型
2025-09 | ████████ 17 篇 - AI/大模型
2026-03 | ██ 4 篇 - 其他
```

---

### 4️⃣ 健康检查

```bash
$ python cli.py health

🏥 书签健康检查

总书签：616
唯一 URL: 616

✅ 重复收藏：0 个
⚠️ 疑似失效：3 个

建议清理：3 个书签
```

---

## 🎨 可视化效果 (开发中)

### 知识图谱
![Knowledge Graph](screenshots/graph_preview.png)
*交互式 D3.js 知识图谱 - 开发中*

### 能力雷达图
![Skill Radar](screenshots/radar_preview.png)
*技能雷达图 - 开发中*

---

## 📱 使用场景

### 场景 1: 年度复盘
```bash
$ python cli.py report > output/annual_review.md
# 生成年度学习报告
```

### 场景 2: 求职准备
```bash
$ python cli.py skills
# 生成技能清单，直接用于简历
```

### 场景 3: 学习规划
```bash
$ python cli.py timeline
# 分析学习轨迹，规划下一步方向
```

### 场景 4: 数字断舍离
```bash
$ python cli.py health
# 检查重复和失效链接，清理收藏
```

---

## 🔐 隐私保护

```
✅ 所有数据本地存储
✅ 不开启云端分析
✅ 不收集使用统计
✅ 100% 开源代码 (可审计)
✅ MIT License
```

---

## 🚀 快速开始

```bash
# 克隆项目
git clone https://github.com/JerryZ01/personal-insights.git
cd personal-insights

# 安装依赖
pip install -r requirements.txt

# 导入书签
cp /path/to/Bookmarks data/input/

# 运行分析
python cli.py stats
```

---

**🪞 做成一个比自己更懂自己的开源项目**

**🔐 你的数据永远属于你！**
