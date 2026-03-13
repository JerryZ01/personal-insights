#!/usr/bin/env python3
"""
Personal Insights - CLI 工具
"""

import sys
import json
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# 导入分析器和数据源
sys.path.insert(0, str(Path(__file__).parent / 'src'))
from analyzer.bookmark_analyzer import BookmarkAnalyzer
from sources.github import GitHubStarsSource


def cmd_stats(args):
    """显示统计信息"""
    analyzer = BookmarkAnalyzer(args.input)
    analyzer.load()
    
    domains = analyzer.analyze_domains()
    content = analyzer.analyze_content()
    
    print(f"\n📊 书签统计\n")
    print(f"总书签数：{len(analyzer.bookmarks)}")
    print(f"独立域名：{domains['total_domains']}")
    print(f"\n🌐 热门域名 TOP 5:")
    for i, (domain, count) in enumerate(list(domains['top_domains'].items())[:5], 1):
        print(f"  {i}. {domain}: {count}")
    
    print(f"\n📚 技术领域 TOP 5:")
    sorted_content = sorted(content.items(), key=lambda x: -sum(x[1].values()))
    for category, techs in sorted_content[:5]:
        total = sum(techs.values())
        print(f"  • {category}: {total}篇")


def cmd_report(args):
    """生成完整报告"""
    analyzer = BookmarkAnalyzer(args.input)
    analyzer.load()
    
    report = analyzer.generate_report()
    
    if args.output:
        Path(args.output).write_text(report, encoding='utf-8')
        print(f"✅ 报告已保存：{args.output}")
    else:
        print(report)


def cmd_health(args):
    """健康检查 - 增强版"""
    analyzer = BookmarkAnalyzer(args.input)
    analyzer.load()
    
    health = analyzer.health_check()
    
    print(f"\n🏥 书签健康检查\n")
    
    # 基础统计
    print(f"📊 基础数据:")
    print(f"  总书签：{health['total']}")
    print(f"  唯一 URL: {health['unique_urls']}")
    
    # 重复检查
    print(f"\n🔄 重复检查:")
    if health['duplicates'] > 0:
        print(f"  ⚠️  重复收藏：{health['duplicates']} 个")
        if health.get('duplicate_urls'):
            print(f"  示例:")
            for url in health['duplicate_urls'][:3]:
                print(f"    - {url[:50]}...")
    else:
        print(f"  ✅ 无重复收藏")
    
    # 死链检查
    print(f"\n🔗 链接健康:")
    if health['suspicious'] > 0:
        print(f"  ⚠️  疑似失效：{health['suspicious']} 个")
        if health.get('suspicious_urls'):
            print(f"  示例:")
            for url in health['suspicious_urls'][:3]:
                print(f"    - {url[:50]}...")
    else:
        print(f"  ✅ 未发现明显失效链接")
    
    # 内容质量
    quality = health.get('quality', {})
    if quality:
        print(f"\n⭐ 内容质量:")
        print(f"  高质量：{quality.get('high_quality', 0)} ({quality.get('high_quality_ratio', 0)}%)")
        print(f"  中质量：{quality.get('medium_quality', 0)}")
        print(f"  低质量：{quality.get('low_quality', 0)}")
        
        ratio = quality.get('high_quality_ratio', 0)
        if ratio >= 30:
            print(f"  ✅ 质量优秀！")
        elif ratio >= 15:
            print(f"  👍 质量良好")
        else:
            print(f"  💡 建议：多收藏官方文档和高质量资源")
    
    # 平台分布
    platform = health.get('platform_health', {})
    if platform:
        print(f"\n🌐 平台分布:")
        for plat, count in sorted(platform.get('platforms', {}).items(), key=lambda x: -x[1])[:5]:
            print(f"  {plat}: {count}")
        diversity = platform.get('diversity', '未知')
        print(f"  多样性：{diversity}")
    
    # 时间健康
    time_health = health.get('time_health', {})
    if time_health and isinstance(time_health, dict):
        print(f"\n📅 学习持续性:")
        if 'status' in time_health:
            status = time_health['status']
            status_icon = '✅' if '持续' in status else '⚠️' if '减缓' in status else '💪'
            print(f"  状态：{status_icon} {status}")
        if 'recent_6months_avg' in time_health:
            print(f"  近 6 个月均：{time_health['recent_6months_avg']} 篇/月")
        if 'average_per_month' in time_health:
            print(f"  总月均：{time_health['average_per_month']} 篇/月")
    
    # 综合建议
    print(f"\n💡 综合建议:")
    suggestions = []
    if health['duplicates'] > 5:
        suggestions.append("清理重复收藏，提高管理效率")
    if quality.get('high_quality_ratio', 0) < 20:
        suggestions.append("增加官方文档和高质量资源收藏")
    if platform.get('platform_count', 0) < 3:
        suggestions.append("拓展学习平台，增加多样性")
    if time_health.get('recent_6months_avg', 0) < 3:
        suggestions.append("保持学习节奏，持续积累")
    
    if suggestions:
        for i, sug in enumerate(suggestions, 1):
            print(f"  {i}. {sug}")
    else:
        print(f"  ✅ 收藏习惯很健康，继续保持！")


def cmd_skills(args):
    """显示技能清单"""
    analyzer = BookmarkAnalyzer(args.input)
    analyzer.load()
    
    skills = analyzer.extract_skills()
    
    print(f"\n🎯 技能清单\n")
    for category, skill_list in sorted(skills.items()):
        if skill_list:
            print(f"### {category}")
            for skill in skill_list[:5]:
                stars = '⭐' * min(5, (skill['count'] // 5) + 1)
                print(f"  {stars} {skill['skill']}: {skill['count']}次")
            print()


def cmd_timeline(args):
    """显示学习轨迹 - 增强版"""
    analyzer = BookmarkAnalyzer(args.input)
    analyzer.load()
    
    result = analyzer.analyze_timeline()
    timeline = result['monthly'] if isinstance(result, dict) and 'monthly' in result else result
    stats = result.get('stats', {}) if isinstance(result, dict) else {}
    phases = result.get('phases', []) if isinstance(result, dict) else []
    
    print(f"\n📅 学习轨迹\n")
    
    # 显示最近 12 个月
    print("📊 月度趋势:")
    for date, stats in sorted(timeline.items())[-12:]:
        bar = '█' * min(20, stats['count'] // 2)
        intensity = stats.get('intensity', '')
        intensity_icon = '🔥' if intensity == '高' else '📈' if intensity == '中' else '📝'
        print(f"{date} | {bar} {stats['count']:2d}篇 {intensity_icon} - {stats['top_category']}")
    
    # 显示统计信息
    if stats:
        print(f"\n📈 学习强度:")
        print(f"  总月份：{stats.get('total_months', 0)} 个月")
        print(f"  总收藏：{stats.get('total_bookmarks', 0)} 篇")
        print(f"  月均收藏：{stats.get('average_per_month', 0)} 篇")
        print(f"  最高月份：{stats.get('max_in_month', 0)} 篇")
    
    # 显示学习阶段
    if phases:
        print(f"\n🎯 学习阶段:")
        for i, phase in enumerate(phases, 1):
            print(f"  阶段{i}: {phase['period']}")
            print(f"         主题：{phase['category']} ({phase['count']}篇)")


def cmd_github(args):
    """导入 GitHub Stars"""
    token = args.token or os.getenv('GITHUB_TOKEN', '')
    username = args.username or os.getenv('GITHUB_USERNAME', 'JerryZ01')
    
    if not token:
        print("❌ 请设置 GITHUB_TOKEN 环境变量或使用 --token 参数")
        return
    
    print(f"🔗 连接 GitHub: {username}")
    
    source = GitHubStarsSource(token, username)
    
    # 获取 stars
    print("📥 获取 starred repositories...")
    stars = source.fetch_stars()
    print(f"✅ 找到 {len(stars)} 个 starred repos")
    
    # 统计
    lang_stats = source.get_language_stats()
    print(f"\n📊 编程语言分布:")
    for lang, count in list(lang_stats.items())[:10]:
        print(f"  {lang}: {count}")
    
    topic_stats = source.get_topic_stats()
    print(f"\n🏷️  热门主题:")
    for topic, count in list(topic_stats.items())[:10]:
        print(f"  {topic}: {count}")
    
    # 保存原始数据
    if args.save_raw:
        raw_path = args.save_raw
    else:
        raw_path = str(Path(__file__).parent / 'data' / 'input' / 'github_stars.json')
    source.save_to_json(raw_path)
    
    # 转换为书签格式
    bookmarks = source.to_bookmark_format()
    
    if args.save_bookmarks:
        bookmark_path = args.save_bookmarks
    else:
        bookmark_path = str(Path(__file__).parent / 'data' / 'input' / 'github_stars_bookmarks.json')
    
    output_data = {
        'roots': {
            'bookmark_bar': {
                'children': bookmarks,
                'name': 'GitHub Stars'
            }
        },
        'source': 'github_stars',
        'fetched_at': datetime.now().isoformat()
    }
    
    with open(bookmark_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ 原始数据：{raw_path}")
    print(f"✅ 书签格式：{bookmark_path}")
    print(f"\n💡 提示：可以使用 'python cli.py stats -i {bookmark_path}' 分析 GitHub Stars")


def cmd_merge(args):
    """合并多个数据源"""
    input_dir = Path(args.input_dir) if args.input_dir else Path(__file__).parent / 'data' / 'input'
    output_file = args.output or str(input_dir.parent / 'output' / 'merged.json')
    
    print(f"📂 扫描输入目录：{input_dir}")
    
    # 查找所有 JSON 文件
    json_files = list(input_dir.glob('*.json'))
    if not json_files:
        print("❌ 未找到 JSON 文件")
        return
    
    print(f"🔍 找到 {len(json_files)} 个文件:")
    for f in json_files:
        print(f"  - {f.name}")
    
    # 合并所有书签数据
    all_bookmarks = []
    sources = {}
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 提取 bookmarks
            roots = data.get('roots', {})
            for root_name, root_data in roots.items():
                if isinstance(root_data, dict) and 'children' in root_data:
                    children = root_data.get('children', [])
                    # 过滤出 URL 类型的条目
                    urls = [c for c in children if c.get('url') or c.get('type') == 'url']
                    if urls:
                        all_bookmarks.extend(urls)
                        sources[json_file.stem] = len(urls)
                        print(f"  ✅ {json_file.stem}: {len(urls)} 个条目")
            
            # 也检查是否是 github_stars 格式
            if data.get('source') == 'github_stars' and 'stars' in data:
                stars = data.get('stars', [])
                if stars:
                    # 转换为书签格式
                    source = GitHubStarsSource('', '')
                    source.stars = stars
                    bookmarks = source.to_bookmark_format()
                    all_bookmarks.extend(bookmarks)
                    sources['github_stars_raw'] = len(bookmarks)
                    print(f"  ✅ {json_file.stem} (raw stars): {len(bookmarks)} 个条目")
        
        except Exception as e:
            print(f"  ⚠️ {json_file.name}: 读取失败 - {e}")
    
    if not all_bookmarks:
        print("❌ 未找到任何书签数据")
        return
    
    # 去重 (基于 URL)
    seen_urls = set()
    unique_bookmarks = []
    duplicates = 0
    
    for bookmark in all_bookmarks:
        url = bookmark.get('url', '')
        if url and url not in seen_urls:
            seen_urls.add(url)
            unique_bookmarks.append(bookmark)
        elif url:
            duplicates += 1
    
    print(f"\n📊 合并结果:")
    print(f"  总条目数：{len(all_bookmarks)}")
    print(f"  去重后：{len(unique_bookmarks)}")
    print(f"  重复数：{duplicates}")
    
    # 保存合并结果
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    merged_data = {
        'roots': {
            'merged_bookmarks': {
                'name': 'Merged Bookmarks',
                'children': unique_bookmarks
            }
        },
        'source': 'merged',
        'merged_at': datetime.now().isoformat(),
        'sources': sources,
        'stats': {
            'total': len(all_bookmarks),
            'unique': len(unique_bookmarks),
            'duplicates': duplicates
        }
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ 合并文件已保存：{output_path}")
    print(f"\n💡 提示：可以使用 'python cli.py stats -i {output_path}' 分析合并后的数据")
    print(f"💡 提示：可以使用 'python cli.py report -i {output_path} -o report.md' 生成完整报告")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='🔖 Bookmark Insights - 书签价值挖掘工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s stats                    # 显示统计
  %(prog)s report                   # 生成报告
  %(prog)s health                   # 健康检查
  %(prog)s skills                   # 技能清单
  %(prog)s timeline                 # 学习轨迹
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='命令')
    
    # stats 命令
    p_stats = subparsers.add_parser('stats', help='显示统计信息')
    p_stats.add_argument('--input', '-i', default=str(Path(__file__).parent / 'data' / 'input' / 'bookmarks.json'))
    p_stats.set_defaults(func=cmd_stats)
    
    # report 命令
    p_report = subparsers.add_parser('report', help='生成完整报告')
    p_report.add_argument('--input', '-i', default=str(Path(__file__).parent / 'data' / 'input' / 'bookmarks.json'))
    p_report.add_argument('--output', '-o')
    p_report.set_defaults(func=cmd_report)
    
    # health 命令
    p_health = subparsers.add_parser('health', help='健康检查')
    p_health.add_argument('--input', '-i', default=str(Path(__file__).parent / 'data' / 'input' / 'bookmarks.json'))
    p_health.set_defaults(func=cmd_health)
    
    # skills 命令
    p_skills = subparsers.add_parser('skills', help='技能清单')
    p_skills.add_argument('--input', '-i', default=str(Path(__file__).parent / 'data' / 'input' / 'bookmarks.json'))
    p_skills.set_defaults(func=cmd_skills)
    
    # timeline 命令
    p_timeline = subparsers.add_parser('timeline', help='学习轨迹')
    p_timeline.add_argument('--input', '-i', default=str(Path(__file__).parent / 'data' / 'input' / 'bookmarks.json'))
    p_timeline.set_defaults(func=cmd_timeline)
    
    # github 命令
    p_github = subparsers.add_parser('github', help='导入 GitHub Stars')
    p_github.add_argument('--token', '-t', help='GitHub Token (也可用 GITHUB_TOKEN 环境变量)')
    p_github.add_argument('--username', '-u', help='GitHub 用户名 (也可用 GITHUB_USERNAME 环境变量)')
    p_github.add_argument('--save-raw', help='保存原始 JSON 路径')
    p_github.add_argument('--save-bookmarks', help='保存书签格式路径')
    p_github.set_defaults(func=cmd_github)
    
    # merge 命令
    p_merge = subparsers.add_parser('merge', help='合并多个数据源')
    p_merge.add_argument('--input-dir', '-i', help='输入目录 (默认 data/input/)')
    p_merge.add_argument('--output', '-o', help='输出文件路径')
    p_merge.set_defaults(func=cmd_merge)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    args.func(args)


if __name__ == '__main__':
    main()
