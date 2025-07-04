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