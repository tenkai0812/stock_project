#!/bin/bash
echo "🚀 開始部署專案..."

# 確保 Python 環境啟動
source ../.venv/bin/activate

# 拉取最新程式碼
git pull origin main

# 安裝需求套件
pip install -r ../requirements.txt

# 重新啟動服務（如果有用 supervisor 或 systemd）
echo "🔄 重新啟動 stock_fetcher 服務..."
pkill -f stock_fetcher
nohup python ../src/main.py > ../logs/output.log 2>&1 &

echo "✅ 部署完成！"
