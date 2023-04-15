# whileループ
# count = 0
# while count < 10:
#     print(count)
#     count += 1

# breakとcontinue
# while True:
#     age = int(input("あなたは何歳ですか？"))
#     if not 0 <= age < 120:
#         print("入力された値は正しくない")
#         continue
#     else:
#         print(f"あなたは{age}歳です")
#         break


# Challenge
casino_age = 18
game_text = """カジノで遊ぶゲームを選んでください。
1:ルーレット
2:ブラックジャック
3:ポーカー
"""

while True:
    age = int(input("カジノには年齢制限があります。あなたは何歳ですか？"))
    if not 0 <= age < 120:
        print("入力された値は正しくない")
        continue
    else:
        if age >= casino_age:
            while True:
                print("{}歳であれば、カジノに入れます。ご入場ください。".format(age))
                game = (int)(input(game_text))
                if game == 1:
                    print("ルーレットで遊んでください")
                    break
                elif game == 2:
                    print("ブラックジャックで遊んでください")
                    break
                elif game == 3:
                    print("ポーカーで遊んでください")
                    break
                else:
                    print("入力された値は正しくない")
                    continue
                break
            break

        else:
            print("{}歳未満の方はご入場できません。".format(casino_age))
            break
