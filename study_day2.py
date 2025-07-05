# 条件分岐
# if 条件 :
#   条件を満たしたときの処理(頭にインデント1個)
age = 22

if age >= 20:
    print("adalt")

# if 条件A:
#     条件を満たしたときの処理
# else:
#     条件を満たさないときの処理
age = 18

if age >= 20:
    print("adalt")
else:
    print("child")

age = 22

if age >= 20:
    print("adalt")
else:
    print("child")

# if 条件A:
#     条件を満たしたときの処理
# elif 条件B:
#     条件Bを満たしたときの処理
# else:
#     条件を満たさないときの処理
age = 0

if age >= 20:
    print("adalt")
elif age == 0:
    print("baby")
else:
    print("child")

# 繰り返し
# for 変数 in range(繰り返す回数):
#     繰り返し中に実行する処理（頭にインデント1個）
for i in range(5):
    print(i)
# 実行結果:01234

# break文
# if文で指定した条件を満たした時点で繰り返しを抜ける
for i in range(5):
    if i == 3:
        break
    print(i)
# 実行結果:012

# continue文
# if分で指定した条件を満たした処理をスキップする
for i in range(5):
    if i == 3:
        continue
    print(i)
# 実行結果:0124

# for文のネスト
for i in range(3):
    for j in range(3):
        print(i, j, sep="-")

# for文でリスト内を参照(リストの中身を順番に追っていく)
arr = [2, 4, 6, 8, 10]
for i in arr:
    print(i)

sum = 0
for i in arr:
    sum += i
print(sum)

# ユーザーに1〜5の数字を入力してもらい、
# それに応じて「運勢」を表示するプログラムを書いてみる
num = int(input("1~5までの数字を入力:"))
if num == 1:
    print("大吉")
elif num ==2:
    print("中吉")
elif num ==3:
    print("小吉")
elif num == 4:
    print("吉")
elif num == 5:
    print("凶")
else:
    print("1~5までの数字を入力")

# 九九表の作成
for i in range(1,10):
    for j in range(1,10):
        print(i,"×",j,"=",i * j)
# もう少しきれいに修正
for i in range(1,10):
    for j in range(1,10):
        print(f"{i} × {j} = {i * j}")

# 関数の定義
# 文字列「hello world」を表示させる関数を定義してみる

def say_hello():
    print("hello world")

say_hello()
say_hello()
say_hello()

# add関数を使用
def add(num1,num2):
    return(num1 + num2)

print(add(6,2))

# 9，4，2の平均を出す関数を定義する
def average(num1,num2,num3):
    return((num1 + num2 + num3)/3)

print(average(9,4,2))

