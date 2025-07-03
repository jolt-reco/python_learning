# 文字列や数値を表示させる
print("good morning")
print(1234)

# 数値と文字列を同時表示させカンマで区切ると表示には半角スペースが生成される
print(1234,"good morning") 
# 実行結果
# 1234 goodmorning

# 文字列の連結、strで文字列に変換
print(str(1234) + "good morning")

# 変数の代入
num = 1
print(num)

# 変数名にはアンダースコア、数字、アルファベットが使用可能
num01 = 2
num_01 = 3
print(num01)
print(num_01)

# 数字から始まる、アンダースコア以外の記号が含まれるとエラー
# 01num = 4
# num$1 = 5

# データ型の判別
num02 = 1.2
print(type(num01))
print(type(num02))

string_a = "hello"
print(string_a)
print(type(string_a))

a = 10
b = 1

bool01 = (a < b)
print(bool01)
print(type(bool01))
