"""自定义异常"""


class PersonalInsightsError(Exception):
    """基础异常类"""
    pass


class DataLoadError(PersonalInsightsError):
    """数据加载失败"""
    pass


class DataFormatError(PersonalInsightsError):
    """数据格式错误"""
    pass


class AnalysisError(PersonalInsightsError):
    """分析失败"""
    pass


class DataSourceError(PersonalInsightsError):
    """数据源错误"""
    pass
