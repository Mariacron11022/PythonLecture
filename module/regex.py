import re

# Regular Expression（正規表現　通称RegEX）

# challenge1
# patter_birthday = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[01])$"
# while True:
#     birthday = input("生年月日を入力してください(yyyy/mm/dd)")
#     matched = re.search(patter_birthday, birthday)
#     if matched:
#         print(matched)
#         print("Matched")
#         break
#     else:
#         print("format miss")

# challenge2
patter_email = "^(\w|.|-)+@(\w|.|-)+\.([a-zA-z]){2,3}$"
while True:
    email_address = input("メールアドレスを入力してください")
    matched = re.search(patter_email, email_address)
    if matched:
        print(matched)
        print("Matched")
        break
    else:
        print("format miss")
# email = "myemail@gmail.com"
#
# print("@" in email)

# ↓この書き方はよくある
# matched = re.search("@\w+\.", email)
# print(matched)
# if matched:
#     print(matched)
#     print("Matched")
# else:
#     print("Not found!")

# metacharacter
# []
# print(re.search("[abc]", "a"))
# print(re.search("[a-c]", "a"))
# print(re.search("[0-9]", "5"))
#
# # ^ 最初の文字
# print(re.search("^[0-9]", "0test0"))
#
# # {n} n回リピート
# print(re.search("[0-9]{4}", "2021/3/31"))
#
# # {n, m} 最低n回、最高m回リピート
# print(re.search("[0-9]{2,4}", "21/3/31"))
#
# # $ 最後の文字
# print(re.search("[0-9]{2}$", "2021/3/31"))
#
# # * 左のパターンを0回以上繰り返す
# print(re.search("a*b", "ab"))
#
# # + 左のパターンを1回以上繰り返す
# print(re.search("a+b", "aaab"))
#
# # ? 左のパターンを0回か1回繰り返す
# print(re.search("ab?c", "abbc"))
#
# # | or
# print(re.search("abc|012", "012"))
#
# # () グループ
# print(re.search("te(s|x)t", "test"))
#
# # . 任意の一文字
# print(re.search("h.t", "h0t"))
#
# # \ エスケープ
# print(re.search("h\.t", "h.t"))
#
# # \w [a-zA-Z0-9_] 全てのアルファベット、数字及びアンダースコア
# print(re.search("h\wt", "hiit"))
