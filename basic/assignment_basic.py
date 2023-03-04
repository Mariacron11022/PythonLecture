#変数へ代入
hello = "konnichiwa"
world = "sekai"
print(hello + world) # ハードコーディング

# format
print("{} {}".format(hello, world))

#name = "Emily"
#print("Hey, {}!! How are you doing".format(name))

name = "Emily"
print(f"Hey, {name}!! How are you doing")

#balance = "100"
#print("balance:{}".format(balance))

balance = "100"
print(f"balance:{balance}")

# fstring
print(f"{hello} {world}")