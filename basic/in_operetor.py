# in演算子
fruits = ["apple", "peach", "grapes", "banana"]
# print("lemon" in fruits)

# challenge
fruits_name = input("フルーツを入力してください")
if fruits_name in fruits:
    # フルーツを削除
    print("{}ですね、差し上げますよ".format(fruits_name))
    fruits.remove(fruits_name)
    print(fruits)
else:
    # フルーツを追加
    print("{}ですね、仕入れました！".format(fruits_name))
    fruits.append(fruits_name)
    print(fruits)
