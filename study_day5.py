# 商品メモアプリ(CSV)の作成
item = input("商品名を入力:")

try:
    price = int(input("価格を入力:"))
except ValueError:
    print("数字を入力してください")
    exit()

import csv
with open("item.csv", "a", newline = "", encoding = "utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([item , price])
try:
    with open("item.csv", "r", newline = "", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"{row[0]} : {row[1]}円")
except FileNotFoundError:
    print("まだデータがありません")