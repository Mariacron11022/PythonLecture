CALL_COUNT = 0  # 関数の外で定義する変数は書き換えないようにする、大文字にしておくのがマナー


def print_count1():
    global CALL_COUNT
    CALL_COUNT += 1
    print(f"関数1:{CALL_COUNT}回目")


def print_count2():
    global CALL_COUNT
    CALL_COUNT += 1
    print(f"関数2:{CALL_COUNT}回目")


print_count1()
print_count2()
print_count1()
