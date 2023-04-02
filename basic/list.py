# リスト：複数のオブジェクトを順序づけて保存するデータ型
# オブジェクトとは文字列型、数値型、リストそのものもオブジェクト、つまり変数＝オブジェクト

fruits = ["apple", "peach", "melon", "grapes"]

hetro_list = ["string", 1, 3.4, True, fruits]

# print(hetro_list)
# print(fruits[0])
# print(fruits[-3])
# print(hetro_list[-1][-1])

# append:新しいオブジェクトを追加する
print(fruits)
fruits.append("banana")
print(fruits)

# insert:指定したindexに指定したオブジェクトを追加する
print(fruits)
fruits.insert(3, "lemon")
print(fruits)

# remove:マッチした最初のオブジェクトを除く
print(fruits)
fruits.remove("peach")
print(fruits)

# sort:昇順に並び替える
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# len():リストの要素数を取得する
print(len(fruits))
print(len("hello world"))
