# クラスの作成
# Personクラスの定義
class Person():
    def __init__(self,name,age): # コンストラクタの定義
        self.name = name # 名前
        self.age = age # 年齢
    
    def say_hello(self): # メソッドの定義
        print(f"こんにちは、私は{self.name}、{self.age}歳です")

# クラスからインスタンス（オブジェクト）を作る
person1 = Person("石井",24)

# メソッドを呼び出す
person1.say_hello()