import yfinance as yf

stock = yf.Ticker("2330.TW")

current_price = stock.history(period="1d")["Close"].iloc[-1]
print(f"台積電最新股價： {current_price}")