fruits = ["apple", "peach", "grapes", "banana"]

# for else
# for fruit in fruits:
#     choice = input(f"あなたが探しているフルーツは{fruit}ですか？ y/n")
#     if choice == "y":
#         print("見つかって良かったですね")
#         break
#     else:
#         print("そうですか。。。")
# else:
#     print("お探しのフルーツは見つかりませんでした")

# while else
# count = 0
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print("countは10未満ではなくなりました")

balance = 1000
game_price = 200

while balance >= game_price:
    choice = input(f"1回{game_price}円のゲームに参加しますか？(残高は{balance}円) (y/n):")

    if choice == "y":
        balance -= game_price
        print(balance)
        # continue
    elif choice == "n":
        print("また遊びましょう")
        break
    else:
        print("yかnで答えて下さい")
        # continue
else:
    print(f"あなたの残高は{balance}円です。もうお金無くなっちゃいましたね。。。")