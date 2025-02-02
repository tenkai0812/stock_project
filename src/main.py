from thread_pool_service import fetch_all_prices
from services.csv_service import save_to_csv
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    # 讀取股票代碼列表
    with open("data/stock_list.txt", "r") as f:
        stock_numbers = [line.strip() for line in f.readlines()]

    # 抓取股票即時股價
    stock_prices = fetch_all_prices(stock_numbers)

    # 儲存到 CSV
    save_to_csv(stock_prices)

except KeyboardInterrupt:
    print("\n⛔️ 使用者中斷了程式執行，安全退出。")
    sys.exit(1)  # **確保 Python 立即完全關閉**
