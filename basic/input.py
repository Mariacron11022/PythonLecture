# input():　ユーザーの入力した値（文字列）を取得する

# age = input("何歳ですか？")
# print("あなたは{}歳です".format(age))

# challeng1 + 2
age = int(input("カジノには年齢制限があります。あなたは何歳ですか？"))
casino_age = 18
game_text = """カジノで遊ぶゲームを選んでください。
1:ルーレット
2:ブラックジャック
3:ポーカー
"""

if age >= casino_age:
    print("{}歳であれば、カジノに入れます。ご入場ください。".format(age))
    game = (int)(input(game_text))
    if game == 1:
        print("ルーレットで遊んでください")
    elif game == 2:
        print("ブラックジャックで遊んでください")
    elif game == 3:
        print("ポーカーで遊んでください")
    else:
        print("そのゲームは選べません")

else:
    print("{}歳未満の方はご入場できません。".format(casino_age))