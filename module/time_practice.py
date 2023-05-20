import time

# .time(): 1970/1/1 秒数が表示(Unix時間)
print(time.time())
print(time.time()/(60*60*24*365))

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


before = time.time()
print(fib(30))
# 処理
after = time.time()
print(f"recursive fibonacci took {after - before:.2f} sec.")
