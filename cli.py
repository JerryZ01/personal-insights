#!/usr/bin/env python3
"""
Personal Insights - CLI 工具
"""

import sys
import json
import os
from pathlib import Path
from datetime import datetime

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
    """健康检查"""
    analyzer = BookmarkAnalyzer(args.input)
    analyzer.load()
    
    health = analyzer.health_check()
    
    print(f"\n🏥 书签健康检查\n")
    print(f"总书签：{health['total']}")
    print(f"唯一 URL: {health['unique_urls']}")
    print(f"\n✅ 重复收藏：{health['duplicates']} 个")
    print(f"⚠️ 疑似失效：{health['suspicious']} 个")
    
    if health['duplicate_urls']:
        print(f"\n📋 重复的 URL:")
        for url in health['duplicate_urls'][:5]:
            print(f"  - {url[:60]}...")


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
    """显示学习轨迹"""
    analyzer = BookmarkAnalyzer(args.input)
    analyzer.load()
    
    timeline = analyzer.analyze_timeline()
    
    print(f"\n📅 学习轨迹\n")
    for date, stats in sorted(timeline.items())[-12:]:
        bar = '█' * min(20, stats['count'] // 2)
        print(f"{date} | {bar} {stats['count']}篇 - {stats['top_category']}")


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
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    args.func(args)


if __name__ == '__main__':
    main()
