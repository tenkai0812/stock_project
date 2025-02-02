# 讀取檔案
with open("data/stock_list.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 清理資料
cleaned_lines = [line.strip().replace('"', '') for line in lines]

# 寫入新的檔案
with open("data/stock_list_cleaned.txt", "w", encoding="utf-8") as f:
    for line in cleaned_lines:
        f.write(line + "\n")

print("✅ 資料已清理完畢，儲存為 stock_list_cleaned.txt")
