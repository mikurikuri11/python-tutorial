# age = input("何歳ですか？")
# print("あなたは{}歳です".format(age))

age = input("何歳ですか？")

format_age = int(age)
available_age = 18

if format_age >= available_age:
    print("カジノに入りました")
    game = (input("""何ゲームをしますか。以下から選択してください。
    1：ルーレット
    2：ブラックジャック
    3：ポーカー
    """))

    format_game = int(game)

    if format_game == 1:
        print("ルーレット")
    elif format_game == 2:
        print("ブラックジャック")
    elif format_game == 3:
        print("ポーカー")
    else:
        print("1or2or3を選択してください")



