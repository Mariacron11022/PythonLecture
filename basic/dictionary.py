# dictionary:キーと値の組み合わせを複数保持するデータ型
fruits_color = {"apple": "red", "lemon": "yellow", "grape": "purple"}

print(fruits_color["apple"])
fruits_color["peach"] = "pink"
print(fruits_color)

fruits_color["peach"] = "shockingpink"
print(fruits_color)

dict_sample = {1: "one", "two": 2, "three": [1, 2, 3], "four": {"inner": "dict"}}
print(dict_sample)
print(dict_sample["four"]["inner"])

colors = {}
colors[1] = "blue"
colors[0] = "red"
colors[2] = "green"
print(colors)

# .keys() values()
for color in fruits_color:
    print(color)

# .items
for fruit, color in fruits_color.items():
    print(f"{fruit} is {color}")