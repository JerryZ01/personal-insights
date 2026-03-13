"""FastAPI 后端 API"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
from pathlib import Path
import json

app = FastAPI(title="Personal Insights API", version="0.3.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalysisResponse(BaseModel):
    total_bookmarks: int
    unique_domains: int
    skills: Dict[str, List[Dict]]
    timeline: Dict
    health: Dict
    domains: Dict


@app.get("/api/health")
async def health_check():
    """健康检查"""
    return {"status": "ok", "version": "0.3.0"}


@app.get("/api/stats", response_model=AnalysisResponse)
async def get_stats(input_file: Optional[str] = None):
    """获取统计数据"""
    input_path = Path(input_file) if input_file else Path(__file__).parent.parent / "data" / "output" / "merged.json"
    
    if not input_path.exists():
        raise HTTPException(status_code=404, detail="数据文件不存在")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 提取书签
    bookmarks = []
    roots = data.get('roots', {})
    for root_data in roots.values():
        if isinstance(root_data, dict) and 'children' in root_data:
            bookmarks.extend([c for c in root_data.get('children', []) if c.get('url')])
    
    # 分析
    from src.services.analysis_service import AnalysisService
    service = AnalysisService()
    result = service.analyze_all(bookmarks)
    
    return AnalysisResponse(
        total_bookmarks=len(bookmarks),
        unique_domains=result['domains']['total_domains'],
        skills=result['skills'],
        timeline=result['timeline'],
        health=result['health'],
        domains=result['domains'],
    )


@app.get("/api/skills")
async def get_skills(input_file: Optional[str] = None):
    """获取技能数据"""
    input_path = Path(input_file) if input_file else Path(__file__).parent.parent / "data" / "output" / "merged.json"
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    bookmarks = []
    roots = data.get('roots', {})
    for root_data in roots.values():
        if isinstance(root_data, dict) and 'children' in root_data:
            bookmarks.extend([c for c in root_data.get('children', []) if c.get('url')])
    
    from src.services.analysis_service import AnalysisService
    service = AnalysisService()
    skills = service.analyze_skills(bookmarks)
    
    return {"skills": skills}


@app.get("/api/timeline")
async def get_timeline(input_file: Optional[str] = None):
    """获取时间线数据"""
    input_path = Path(input_file) if input_file else Path(__file__).parent.parent / "data" / "output" / "merged.json"
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    bookmarks = []
    roots = data.get('roots', {})
    for root_data in roots.values():
        if isinstance(root_data, dict) and 'children' in root_data:
            bookmarks.extend([c for c in root_data.get('children', []) if c.get('url')])
    
    from src.services.analysis_service import AnalysisService
    service = AnalysisService()
    timeline = service.analyze_timeline(bookmarks)
    
    return {"timeline": timeline}


@app.get("/api/health-check")
async def get_health(input_file: Optional[str] = None):
    """获取健康检查数据"""
    input_path = Path(input_file) if input_file else Path(__file__).parent.parent / "data" / "output" / "merged.json"
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    bookmarks = []
    roots = data.get('roots', {})
    for root_data in roots.values():
        if isinstance(root_data, dict) and 'children' in root_data:
            bookmarks.extend([c for c in root_data.get('children', []) if c.get('url')])
    
    from src.services.analysis_service import AnalysisService
    service = AnalysisService()
    health = service.analyze_health(bookmarks)
    
    return {"health": health}
