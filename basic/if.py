# if文

age = -20
age_alchol = 21
age_drive = 18

if age >= age_alchol:
    print("お酒が飲める")
else:
    print("お酒が飲めない")

if age >= age_alchol:
    print("You can drink beer")
elif age < age_drive:
    print("You cannot even drive")
else:
    print("You are not allowed to drink beer but you can drive only if you have a driver's license")

if not 0 < age < 120:
    print("age is invlid")

balance = 101  # 単位：万
withdraw = 101  # 単位：万
withdraw_limit = 100

if withdraw > withdraw_limit:
    print(f"{withdraw_limit}万円以上は引き出せません")
elif balance >= withdraw:
    balance -= withdraw
    print(f"残額は{balance}")
else:
    print("引き出せません")

