myvariable = "This is global variable"

def myfunc():
    print("This is my function!!")

def anotherfunc():
    print("This is another function!!")

print("This is mymodule!!")

if __name__ == "__main__":
    print(f"mymodule.__name__:{__name__}")