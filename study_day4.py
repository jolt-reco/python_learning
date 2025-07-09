# ファイル操作の実践
# ファイル:sample.txtに文字を書き込む。
with open("sample.txt","w",encoding="utf-8") as f:
    f.write("こんにちは\n")
    f.write("pythonでファイル操作中")

# 作成したファイルの中身を読み取る
with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)

# CSVファイルの読み込み
# モジュールのインポート
import csv

# csvファイルに書き込み
with open("import.csv", "w", newline="", encoding="utf-8") as f:
    writedata = csv.writer(f)
    writedata.writerow(["商品名","価格"])
    writedata.writerow(["チョコ",120])
    writedata.writerow(["コーラ",150])

# csvファイルの読み込み
with open("import.csv", "r", encoding="utf-8") as f:
    readerdata = csv.reader(f)
    for row in readerdata:
        print(row)

# 例外処理
# 0で割るときのエラー処理
try:
    a = int(input("割られる数字を入力:"))
    b = int(input("割る数字を入力:"))
    print("結果:",a/b)
except ZeroDivisionError:
    print("0で割っています")
except ValueError:
    print("数字以外が入力されています")
finally:
    print("処理終了")

# 存在しないファイルを読もうとしたときの処理
try:
    with open("存在しないファイル.txt", "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
except FileNotFoundError:
    print("ファイルが見つかりません")