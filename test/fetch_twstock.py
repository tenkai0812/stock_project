import twstock

stock = twstock.realtime.get(["2330","2337"])
if stock['success']:
    print(f"{stock['success']}")
else:
    print("獲取股價失敗")
