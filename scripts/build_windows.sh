#!/bin/bash
echo "🔧 正在打包 Windows 執行檔..."

# 確保 Python 環境啟動
source ../.venv/bin/activate

# 使用 PyInstaller 打包
pyinstaller --onefile --name stock_fetcher --hidden-import=twstock src/main.py

# 移動可執行檔到 `dist/`
mkdir -p dist
mv dist/stock_fetcher.exe dist/

echo "✅ 打包完成！執行檔位於 dist/stock_fetcher.exe"
