class Person:    # クラス名はCamelCase、先頭の文字は大文字
    # クラス変数
    num_legs = 2
    count = 0

    # constructor (__new__)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f"{self.name} is walking")

    def run(self):
        print(f"{self.name} is running")


print(Person.count)
john = Person("John", 28, "male")
print(Person.count)
taro = Person("Taro", 18, "male")
print(Person.count)
emma = Person("Emma", 40, "female")
print(Person.count)

# インスタンス変数 (インスタンスに紐づく変数)
# .に続けてアクセス可能
print(john.name)
print(john.age)
print(john.gender)

print(taro.name)
print(taro.age)
print(taro.gender)

john.walk()
emma.walk()
john.run()

print(john.num_legs)
print(taro.num_legs)
print(Person.num_legs)
Person.num_legs = 3
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)
# ↓この書き方はバグの元なので基本的にはやらない
john.num_legs = 4
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)

