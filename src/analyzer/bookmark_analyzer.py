#!/usr/bin/env python3
"""
Bookmark Insights - 书签价值挖掘工具
分析书签数据，生成个人知识图谱、学习轨迹、技能清单
"""

import json
import re
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
from urllib.parse import urlparse
from typing import Dict, List, Tuple, Optional
import time


class BookmarkAnalyzer:
    """书签分析引擎"""
    
    # 域名分类映射
    DOMAIN_CATEGORIES = {
        # 技术博客
        'blog.csdn.net': '技术博客',
        'zhuanlan.zhihu.com': '深度文章',
        'cnblogs.com': '技术博客',
        'jianshu.com': '技术博客',
        'segmentfault.com': '技术博客',
        'juejin.cn': '技术博客',
        'juejin.im': '技术博客',
        
        # 官方文档
        'github.com': '开源项目',
        'gitee.com': '开源项目',
        'docs.python.org': '官方文档',
        'developer.mozilla.org': '官方文档',
        'cloud.tencent.com': '云厂商',
        'developer.aliyun.com': '云厂商',
        'huaweicloud.com': '云厂商',
        'aws.amazon.com': '云厂商',
        
        # 学习平台
        'coursera.org': '学习平台',
        'udemy.com': '学习平台',
        'bilibili.com': '视频平台',
        'youtube.com': '视频平台',
        
        # 社区论坛
        'stackoverflow.com': '社区论坛',
        'reddit.com': '社区论坛',
        'v2ex.com': '社区论坛',
        
        # 内部文档
        'iwiki.woa.com': '内部文档',
        'km.ooa.woa.com': '内部文档',
    }
    
    # 技能关键词映射
    SKILL_KEYWORDS = {
        # AI/大模型
        'Transformer': '深度学习',
        'Attention': '深度学习',
        'FlashAttention': '深度学习',
        'LLM': '大模型',
        '大模型': '大模型',
        'LangChain': '大模型',
        'RAG': '大模型',
        'Fine-tuning': '大模型',
        '微调': '大模型',
        'LoRA': '大模型',
        'vLLM': '大模型推理',
        'SGLang': '大模型推理',
        
        # 深度学习框架
        'PyTorch': '深度学习框架',
        'TensorFlow': '深度学习框架',
        'MindSpore': '深度学习框架',
        
        # 云计算
        'Kubernetes': '云计算',
        'K8s': '云计算',
        'Docker': '云计算',
        'OpenStack': '云计算',
        'CVM': '云计算',
        
        # 编程语言
        'Python': '编程语言',
        'Java': '编程语言',
        'C++': '编程语言',
        'AscendC': '编程语言',
        
        # 硬件/芯片
        '昇腾': 'AI 芯片',
        'Ascend': 'AI 芯片',
        'CANN': 'AI 芯片',
        'CUDA': 'GPU 编程',
        'NPU': 'AI 芯片',
    }
    
    # 技术栈分类
    TECH_TAXONOMY = {
        'AI/大模型': ['Transformer', 'LLM', '大模型', 'PyTorch', 'FlashAttention', 
                      'RAG', 'LangChain', '微调', 'LoRA', 'vLLM', 'SGLang'],
        '深度学习': ['神经网络', 'CNN', 'RNN', 'LSTM', 'Attention', '深度学习'],
        '云计算': ['Kubernetes', 'K8s', 'Docker', 'OpenStack', 'CVM', '云计算'],
        '编程语言': ['Python', 'Java', 'C++', 'JavaScript', 'Go', 'AscendC'],
        'AI 芯片': ['昇腾', 'Ascend', 'CANN', 'NPU', '华为 AI'],
        'GPU 编程': ['CUDA', 'GPU', 'Tensor Core'],
        '大数据': ['Hadoop', 'Spark', 'Flink', 'Hive', 'Hudi', '大数据'],
        '前端开发': ['Vue', 'React', 'JavaScript', 'TypeScript', '前端'],
        '后端开发': ['Spring', 'Django', 'Flask', '后端', '微服务'],
    }
    
    def __init__(self, bookmarks_path: str):
        self.bookmarks_path = Path(bookmarks_path)
        self.bookmarks = []
        self.stats = {}
        self.skills = defaultdict(list)
        self.timeline = defaultdict(list)
        
    def load(self) -> List[Dict]:
        """加载 Chrome 书签 JSON"""
        with open(self.bookmarks_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self._parse_roots(data.get('roots', {}), [])
        return self.bookmarks
    
    def _parse_roots(self, roots: Dict, path: List[str]):
        """递归解析所有根文件夹"""
        for name, folder in roots.items():
            if isinstance(folder, dict):
                self._parse_folder(folder, path + ['Root'])
    
    def _parse_folder(self, folder: Dict, path: List[str]):
        """递归解析文件夹"""
        if not folder:
            return
            
        folder_name = folder.get('name', 'Unknown')
        current_path = path + [folder_name]
        
        for child in folder.get('children', []):
            if child.get('type') == 'url':
                bookmark = {
                    'name': child.get('name', ''),
                    'url': child.get('url', ''),
                    'path': current_path,
                    'domain': self._extract_domain(child.get('url', '')),
                    'date_added': child.get('date_added', ''),
                }
                self.bookmarks.append(bookmark)
                
                # 提取时间线
                if bookmark['date_added']:
                    date_str = self._chrome_date_to_str(bookmark['date_added'])
                    if date_str:
                        self.timeline[date_str].append(bookmark)
                
            elif child.get('type') == 'folder':
                self._parse_folder(child, current_path)
    
    def _extract_domain(self, url: str) -> str:
        """从 URL 提取域名"""
        try:
            parsed = urlparse(url)
            return parsed.netloc.replace('www.', '')
        except:
            return ''
    
    def _chrome_date_to_str(self, chrome_date: str) -> Optional[str]:
        """转换 Chrome 时间戳到日期字符串"""
        try:
            # Chrome 时间戳是从 1601-01-01 开始的微秒数
            timestamp = int(chrome_date) / 1000000 - 11644473600
            dt = datetime.fromtimestamp(timestamp)
            return dt.strftime('%Y-%m')
        except:
            return None
    
    def analyze_domains(self) -> Dict:
        """域名分析"""
        domains = Counter([b['domain'] for b in self.bookmarks if b['domain']])
        
        # 按分类统计
        category_stats = defaultdict(int)
        for domain, count in domains.items():
            category = self.DOMAIN_CATEGORIES.get(domain, '其他')
            category_stats[category] += count
        
        return {
            'total_domains': len(domains),
            'top_domains': dict(domains.most_common(20)),
            'by_category': dict(category_stats),
        }
    
    def analyze_content(self) -> Dict:
        """内容分类分析"""
        tech_stats = defaultdict(lambda: defaultdict(int))
        
        for bookmark in self.bookmarks:
            title = bookmark['name'].lower()
            url = bookmark['url'].lower()
            text = f"{title} {url}"
            
            # 匹配技术关键词
            for category, keywords in self.TECH_TAXONOMY.items():
                for keyword in keywords:
                    if keyword.lower() in text:
                        tech_stats[category][keyword] += 1
        
        # 转换为普通字典并排序
        result = {}
        for category, keywords in tech_stats.items():
            result[category] = dict(sorted(keywords.items(), key=lambda x: -x[1]))
        
        return result
    
    def extract_skills(self) -> Dict:
        """提取技能清单"""
        skill_counts = defaultdict(int)
        
        for bookmark in self.bookmarks:
            title = bookmark['name']
            url = bookmark['url']
            text = f"{title} {url}"
            
            for skill, category in self.SKILL_KEYWORDS.items():
                if skill in text or skill.lower() in text.lower():
                    skill_counts[skill] += 1
                    self.skills[category].append({
                        'skill': skill,
                        'count': skill_counts[skill],
                        'bookmarks': []
                    })
        
        # 按技能数量排序
        result = {}
        for category, skills in self.skills.items():
            skill_counter = Counter([s['skill'] for s in skills])
            result[category] = [
                {'skill': skill, 'count': count}
                for skill, count in skill_counter.most_common(10)
            ]
        
        return result
    
    def analyze_timeline(self) -> Dict:
        """时间线分析"""
        timeline_stats = {}
        
        for date, bookmarks in sorted(self.timeline.items()):
            # 分析这个月的主要领域
            tech_counter = defaultdict(int)
            for b in bookmarks:
                text = f"{b['name']} {b['url']}".lower()
                for category, keywords in self.TECH_TAXONOMY.items():
                    for keyword in keywords:
                        if keyword.lower() in text:
                            tech_counter[category] += 1
            
            top_tech = max(tech_counter.items(), key=lambda x: x[1])[0] if tech_counter else '其他'
            
            timeline_stats[date] = {
                'count': len(bookmarks),
                'top_category': top_tech,
                'categories': dict(tech_counter),
            }
        
        return timeline_stats
    
    def health_check(self) -> Dict:
        """健康检查"""
        # 检测重复（基于 URL）
        url_counter = Counter([b['url'] for b in self.bookmarks])
        duplicates = {url: count for url, count in url_counter.items() if count > 1}
        
        # 检测可能的死链（需要网络请求，这里只做简单检查）
        suspicious = []
        for b in self.bookmarks:
            if '404' in b['name'] or 'not found' in b['name'].lower():
                suspicious.append(b['url'])
        
        return {
            'total': len(self.bookmarks),
            'unique_urls': len(set([b['url'] for b in self.bookmarks])),
            'duplicates': len(duplicates),
            'duplicate_urls': list(duplicates.keys())[:10],
            'suspicious': len(suspicious),
        }
    
    def generate_report(self) -> str:
        """生成综合报告"""
        domain_stats = self.analyze_domains()
        content_stats = self.analyze_content()
        skill_stats = self.extract_skills()
        timeline_stats = self.analyze_timeline()
        health = self.health_check()
        
        report = f"""# 📊 书签洞察报告

生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📈 总览

- **总书签数**: {len(self.bookmarks)}
- **独立域名**: {domain_stats['total_domains']}
- **唯一 URL**: {health['unique_urls']}
- **重复收藏**: {health['duplicates']}

---

## 🌐 热门域名 TOP 10

"""
        for i, (domain, count) in enumerate(list(domain_stats['top_domains'].items())[:10], 1):
            category = self.DOMAIN_CATEGORIES.get(domain, '其他')
            report += f"{i}. **{domain}** - {count} 个 ({category})\n"
        
        report += f"""
---

## 📚 技术领域分布

"""
        for category, techs in sorted(content_stats.items(), key=lambda x: -sum(x[1].values())):
            total = sum(techs.values())
            report += f"### {category} ({total}篇)\n"
            for tech, count in list(techs.items())[:5]:
                report += f"- {tech}: {count}\n"
            report += "\n"
        
        report += f"""---

## 🎯 技能清单

"""
        for category, skills in skill_stats.items():
            if skills:
                report += f"### {category}\n"
                for skill in skills[:5]:
                    report += f"- {skill['skill']}: {skill['count']}次\n"
                report += "\n"
        
        report += f"""---

## 📅 学习轨迹

"""
        recent_months = list(timeline_stats.items())[-6:]
        for date, stats in recent_months:
            report += f"**{date}**: {stats['count']}篇 - 主要关注：{stats['top_category']}\n"
        
        report += f"""
---

## ⚠️ 健康检查

- 重复收藏：{health['duplicates']} 个
- 疑似失效：{health['suspicious']} 个

---

## 💡 建议

1. **清理重复**: 删除 {health['duplicates']} 个重复收藏
2. **聚焦重点**: 你的核心领域是 {max(content_stats.items(), key=lambda x: sum(x[1].values()))[0]}
3. **补充短板**: 可以考虑学习 {self._suggest_gaps(content_stats)}

"""
        return report
    
    def _suggest_gaps(self, content_stats: Dict) -> str:
        """建议学习方向"""
        # 简单逻辑：收藏少的领域可能是短板
        if not content_stats:
            return "继续广泛学习"
        
        min_category = min(content_stats.items(), key=lambda x: sum(x[1].values()))[0]
        return f"{min_category} (收藏较少)"


def main():
    """主函数"""
    base_path = Path(__file__).parent.parent.parent
    input_path = base_path / 'data' / 'input' / 'bookmarks.json'
    output_path = base_path / 'data' / 'output'
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    print('🔖 Bookmark Insights - 书签价值挖掘工具')
    print('=' * 50)
    
    # 加载书签
    print(f'📁 加载书签：{input_path}')
    analyzer = BookmarkAnalyzer(str(input_path))
    bookmarks = analyzer.load()
    print(f'✅ 找到 {len(bookmarks)} 个书签')
    
    # 生成报告
    print('📊 生成分析报告...')
    report = analyzer.generate_report()
    
    # 保存报告
    report_path = output_path / 'report.md'
    report_path.write_text(report, encoding='utf-8')
    print(f'✅ 报告已保存：{report_path}')
    
    # 保存详细数据
    data = {
        'domains': analyzer.analyze_domains(),
        'content': analyzer.analyze_content(),
        'skills': analyzer.extract_skills(),
        'timeline': analyzer.analyze_timeline(),
        'health': analyzer.health_check(),
    }
    
    data_path = output_path / 'analysis.json'
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'✅ 详细数据已保存：{data_path}')
    
    print('=' * 50)
    print('✅ 完成！')
    print()
    print('📄 查看报告:')
    print(f'   cat {report_path}')
    
    return str(report_path)


if __name__ == '__main__':
    main()
