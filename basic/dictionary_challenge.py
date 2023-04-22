# dictionaryを使ったリファクタリング
# Challenge
casino_age = 18
casino_game = {"a": "バカラ", "b": "ブラックジャック", "c": "ポーカー", "d": "スロット"}


age = int(input("カジノには年齢制限があります。あなたは何歳ですか？"))
if not 0 <= age < 120:
    print("入力された値は正しくない")
else:
    if age >= casino_age:
        while True:
            print("{}歳であれば、カジノに入れます。ご入場ください。".format(age))
            print("プレイするゲームを選択して下さい。")
            for num, game_name in casino_game.items():
                print(f"{num}: {game_name}")
            game = input(":")
            if game in casino_game:
                print(casino_game[str(game)] + "で遊んでください")
                break
            else:
                print("入力された値は正しくない")
                continue
    else:
        print("{}歳未満の方はご入場できません。".format(casino_age))
