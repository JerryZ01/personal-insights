"""技能分析器"""
from typing import List, Dict, Any
from collections import Counter
from .base import BaseAnalyzer


class SkillAnalyzer(BaseAnalyzer):
    """技能分析器"""
    
    SKILL_KEYWORDS = {
        # AI/大模型
        'Transformer': '深度学习',
        'LLM': '大模型',
        '大模型': '大模型',
        'LangChain': '大模型',
        'RAG': '大模型',
        '微调': '大模型',
        'LoRA': '大模型',
        'vLLM': '大模型推理',
        'PyTorch': '深度学习框架',
        'TensorFlow': '深度学习框架',
        
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
        'Go': '编程语言',
        'JavaScript': '编程语言',
        
        # 硬件/芯片
        '昇腾': 'AI 芯片',
        'Ascend': 'AI 芯片',
        'CANN': 'AI 芯片',
        'CUDA': 'GPU 编程',
        
        # 大数据
        'Hadoop': '大数据',
        'Spark': '大数据',
        'Flink': '大数据',
        'Hive': '大数据',
        'Hudi': '大数据',
        '大数据': '大数据',
    }
    
    def analyze(self, bookmarks: List[Dict]) -> Dict[str, List[Dict]]:
        """提取技能"""
        skill_counts: Dict[str, int] = {}
        
        for bookmark in bookmarks:
            text = f"{bookmark.get('name', '')} {bookmark.get('url', '')}"
            text += f" {bookmark.get('description', '')}"
            
            for skill, category in self.SKILL_KEYWORDS.items():
                if skill.lower() in text.lower():
                    skill_counts[skill] = skill_counts.get(skill, 0) + 1
        
        # 按类别组织
        category_skills: Dict[str, List[Dict]] = {}
        for skill, count in skill_counts.items():
            category = self.SKILL_KEYWORDS.get(skill, '其他')
            if category not in category_skills:
                category_skills[category] = []
            category_skills[category].append({
                'skill': skill,
                'count': count,
            })
        
        # 排序
        for category in category_skills:
            category_skills[category].sort(key=lambda x: -x['count'])
        
        return category_skills
    
    def get_summary(self) -> str:
        """获取摘要"""
        return "技能提取完成"
