# 再帰関数(recursive function)：関数内で自身の関数をcallする
# 階乗(factorial)：3! = 3 * 2 * 1
# n! = n * (n - 1) * (n -2) * ・・・ * 1
# n! = n * (n - 1)!

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(3))


def fibonacci_recursive(num):
    if num < 2:
        return num
    else:
        return fibonacci_recursive(num - 2) + fibonacci_recursive(num - 1)


# print(fibonacci(4))

def fibonacci(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


# print(fibonacci(6))

for i in range(50):
    print(i, fibonacci(i))

