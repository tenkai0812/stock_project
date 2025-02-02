from concurrent.futures import ThreadPoolExecutor
from services.fetch_stock import get_prices
import time

def fetch_all_prices(stock_numbers, batch_size=10, max_workers=3):
    """
    批次查詢股票價格，減少 API 請求次數
    """
    stock_prices = {}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        batches = [stock_numbers[i:i + batch_size] for i in range(0, len(stock_numbers), batch_size)]
        results = executor.map(get_prices, batches)

    for batch_result in results:
        stock_prices.update(batch_result)
        time.sleep(1)  # 避免短時間內過多請求

    return stock_prices
