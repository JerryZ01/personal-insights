#!/bin/bash
# 快速启动脚本

echo "🚀 启动 Personal Insights..."

# 检查 Python 环境
if ! command -v python &> /dev/null; then
    echo "❌ 需要 Python 环境"
    exit 1
fi

# 安装 Python 依赖
echo "📦 安装 Python 依赖..."
pip install -q fastapi uvicorn click

# 启动后端 API
echo "🔧 启动后端 API (端口 8000)..."
uvicorn api.main:app --reload --port 8000 &
BACKEND_PID=$!

# 等待后端启动
sleep 3

# 检查 Node.js
if command -v npm &> /dev/null; then
    echo "📦 安装前端依赖..."
    cd web
    npm install --silent
    
    echo "🎨 启动前端开发服务器 (端口 3000)..."
    npm run dev &
    FRONTEND_PID=$!
    
    echo ""
    echo "✅ 启动完成！"
    echo ""
    echo "📊 前端：http://localhost:3000"
    echo "🔌 API:   http://localhost:8000"
    echo "📖 API 文档：http://localhost:8000/docs"
    echo ""
    echo "按 Ctrl+C 停止服务"
    
    wait
else
    echo ""
    echo "✅ 后端 API 已启动！"
    echo ""
    echo "🔌 API:   http://localhost:8000"
    echo "📖 API 文档：http://localhost:8000/docs"
    echo ""
    echo "⚠️  未检测到 Node.js，前端未启动"
    echo "如需前端，请安装 Node.js 后运行：cd web && npm install && npm run dev"
    echo ""
    echo "按 Ctrl+C 停止服务"
    
    wait
fi

# 清理
kill $BACKEND_PID 2>/dev/null
kill $FRONTEND_PID 2>/dev/null
