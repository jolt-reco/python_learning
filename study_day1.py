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

# リストの作成
a = ["sato","suzuki","takahashi"]
print(a)
print(a[0])
print(a[1])
print(a[2])

a[1] = "tanaka"
print(a[1])

# リストの内部にリストを作成
a = [["sato","suzuki"],["takahashi","tanaka"]]
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])

# 演算子での計算
x = 10
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)# %は剰余

# 関係演算子
print(x > y)
print(x < y)

z = 10
print(x >= z)

# 等価は == 、非等価は != で表現する
print(x == z)
print(x != z)

# 論理演算
x = 8
y = 3

print(x >= 5 and x <= 10)
print(y >= 5 and y <= 10)
print(x == 3 or y == 3)
print(x == 1 or y == 1)

# 代入演算子
x = 8
y = 12
z = 20

# xに10を加算し、その数値をxに代入する
x +=10
# zにyを加算し、その数値をzに代入する
z += y

print(x)
print(z)
