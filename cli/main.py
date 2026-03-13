"""CLI 入口"""
import click
import json
from pathlib import Path
from typing import Optional


@click.group()
@click.version_option(version='0.3.0')
def cli():
    """Personal Insights - 个人洞察工具"""
    pass


@cli.command()
@click.option('--input', '-i', 'input_file', help='输入文件路径')
def stats(input_file: Optional[str]) -> None:
    """显示统计信息"""
    from src.services.analysis_service import AnalysisService
    
    input_path = Path(input_file) if input_file else Path(__file__).parent.parent / 'data' / 'output' / 'merged.json'
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    bookmarks = []
    roots = data.get('roots', {})
    for root_data in roots.values():
        if isinstance(root_data, dict) and 'children' in root_data:
            bookmarks.extend([c for c in root_data.get('children', []) if c.get('url')])
    
    service = AnalysisService()
    result = service.analyze_all(bookmarks)
    
    click.echo(f"\n📊 书签统计\n")
    click.echo(f"总书签数：{len(bookmarks)}")
    click.echo(f"独立域名：{result['domains']['total_domains']}")
    
    click.echo(f"\n🌐 热门域名 TOP 5:")
    for i, (domain, count) in enumerate(list(result['domains']['top_domains'].items())[:5], 1):
        click.echo(f"  {i}. {domain}: {count}")


@cli.command()
@click.option('--input', '-i', 'input_file', help='输入文件路径')
def skills(input_file: Optional[str]) -> None:
    """显示技能清单"""
    from src.services.analysis_service import AnalysisService
    
    input_path = Path(input_file) if input_file else Path(__file__).parent.parent / 'data' / 'output' / 'merged.json'
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    bookmarks = []
    roots = data.get('roots', {})
    for root_data in roots.values():
        if isinstance(root_data, dict) and 'children' in root_data:
            bookmarks.extend([c for c in root_data.get('children', []) if c.get('url')])
    
    service = AnalysisService()
    skills = service.analyze_skills(bookmarks)
    
    click.echo(f"\n🎯 技能清单\n")
    for category, skill_list in sorted(skills.items()):
        if skill_list:
            click.echo(f"### {category}")
            for skill in skill_list[:5]:
                stars = '⭐' * min(5, (skill['count'] // 5) + 1)
                click.echo(f"  {stars} {skill['skill']}: {skill['count']}次")
            click.echo()


if __name__ == '__main__':
    cli()
