import csv

def save_to_csv(data, filename="data/stock_prices.csv"):
    """
    將股票價格資料儲存到 CSV 檔案
    """
    with open(filename, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        
        # ✅ 修正這行，應該傳入一個 list，而不是兩個參數
        writer.writerow(["股票代碼", "即時股價"])  

        for stock_number, price in data.items():
            writer.writerow([stock_number, price])  # ✅ 這裡沒問題

    print(f"✅ 即時股價已存入 {filename}")
