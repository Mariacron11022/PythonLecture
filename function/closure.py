# Closure（クロージャー）

# # 関数（function）もオブジェクト
# def compute_square(num):
#     return num * num
#
#
# f = compute_square
# print(type(f))
# print(f(10))
#
#
# def execute_func(func, param):
#     return func(param)
#
#
# print(execute_func(f, 10))


# # 関数をreturnする
# def return_func():
#     def inner_func():
#         print("This is an inner function")
#
#     return inner_func
#
#
# e = return_func()
# print(e)
# print(type(e))
# e()


# Closure:状態をキープした関数を作ることができる
# 状態が静的
def power(exponent):

    def inner_power(base):
        return base ** exponent
    return inner_power


power_four = power(4)
print(power_four(3))


# 状態が動的
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average


average_nums = average()
print(average_nums(5))
print(average_nums(15))
