class Account:
    # クラス変数
    # account_number = 0
    count = 0

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.account_number = Account.count
        Account.count += 1
        # Account.account_number += 1

    def withdraw(self, inputMoney):
        print(f"{inputMoney}円入金します。")
        self.balance += inputMoney
        # print(f"self.balance:{self.balance}")
        self.show_balance()

    def deposit(self, outputMoney):
        if outputMoney <= self.balance:
            print(f"{outputMoney}円出金します。")
            self.balance -= outputMoney
            self.show_balance()
        else:
            print(f"残高{self.balance}円足りません")

        # print(f"self.balance:{self.balance}")

    def show_balance(self):
        print(f"{self.name}の残高は{self.balance}円です。")


TakashiAccount = Account(balance=10000, name="Takashi")
print(TakashiAccount.balance)
print(TakashiAccount.name)
print(TakashiAccount.account_number)
TakashiAccount.withdraw(2000)
print(TakashiAccount.balance)
TakashiAccount.deposit(10000)
print(TakashiAccount.balance)

YoshioAccount = Account(10000, "Yoshio")
print(YoshioAccount.balance)
print(YoshioAccount.name)
print(YoshioAccount.account_number)
