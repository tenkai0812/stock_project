import twstock
import time

def get_prices(stock_numbers, max_retries=3):
    """
    一次查詢多個台股即時股價，並增加重試機制
    """
    for attempt in range(max_retries):
        try:
            stocks = twstock.realtime.get(stock_numbers)

            if stocks and stocks.get("success"):
                stock_prices = {
                    stock: stocks[stock]["realtime"].get("latest_trade_price", "N/A")
                    for stock in stock_numbers
                    if stocks.get(stock) and stocks[stock].get("success")
                }
                return stock_prices  # 回傳所有股票的即時價格

        except Exception as e:
            print(f"⚠️ 股票群 {stock_numbers} 取得價格失敗，重試中 ({attempt + 1}/{max_retries}): {e}")

        time.sleep(2)  # 每次重試前等待 2 秒，避免伺服器封鎖

    return {stock: "N/A" for stock in stock_numbers}  # 若失敗，回傳 N/A
