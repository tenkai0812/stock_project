import requests

URL = "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL"
FILE_PATH = "../data/stock_list.txt"

def fetch_stock_list():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        stock_ids = [item["Code"] for item in data if "Code" in item]
        
        with open(FILE_PATH, "w") as f:
            f.write("\n".join(stock_ids))
        
        print(f"✅ 股票代號已更新，儲存至 {FILE_PATH}")
    else:
        print("❌ 無法取得最新的股票代號")

if __name__ == "__main__":
    fetch_stock_list()
