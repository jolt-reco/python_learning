# クラスの作成
# Personクラスの定義
class Person():
    def __init__(self,name,age,height): # コンストラクタの定義
        self.name = name # 名前
        self.age = age # 年齢
        self.height = height # 身長

    def say_hello(self): # メソッドの定義
        print(f"こんにちは、私は{self.name}、{self.age}歳です")
    
    def is_adult(self): # 年齢で成人かどうかを判別するメソッド追加
        if self.age >= 20:
            print("私は大人です")
        else:
            print("私は未成年です")

    def is_height(self):
        if self.height >= 170:
            print("高いです")

# インスタンス作成
person1 = Person("石井",24,169)
person2 = Person("田中",18,180)

# メソッドを呼び出す
person1.say_hello()
person1.is_adult()
person1.is_height()

person2.say_hello()
person2.is_adult()
person2.is_height()