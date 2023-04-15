# forループ
fruits = ["apple", "peach", "grapes", "banana"]

# for fruits in fruits:
#     print(f"I love {fruits}!!")
#
# for char in "hello world!!":
#     print(f"char: {char}")

# iterationとiterable

# Challenge1
# favorite = input("好きなフルーツを入力してください")
# for fruit in fruits:
#     if fruit == favorite:
#         print(f"あなたの好きな{fruit}です。")
#     else:
#         print(f"あなたが好きではない{fruit}です。")

# Challenge2
# 空のリストを定義
like_fruitsList = []
unlike_fruitsList = []
for fruit in fruits:
    answer = input(f"あなたは{fruit}は好きですか？ Yes/No、で答えて下さい。")
    if answer == "Yes":
        like_fruitsList.append(fruit)
    elif answer == "No":
        unlike_fruitsList.append(fruit)
    else:
        print("入力し直して下さい")

print(f"favorite fruits: {like_fruitsList}")
print(f"normal fruits: {unlike_fruitsList}")

# for fruits in like_fruitsList:
#     print(f"あなたの好きな{fruits}です。")
#
# for fruits in unlike_fruitsList:
#     print(f"あなたの好きなではない{fruits}です。")
