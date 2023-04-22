fruits_color = {"apple": "red", "lemon": "yellow", "grapes": "purple"}

# print(fruits_color["apple"])
if "peach" in fruits_color:
    print(fruits_color["peach"])
else:
    print("the key is not found")

# .get()
fruit = input("フルーツの名前を指定して下さい")
print(fruits_color.get(fruit, "Nothing"))

# .update()
fruits_color2 = {"peach": "pink", "kiwi": "green"}
fruits_color.update(fruits_color2)
print(fruits_color)