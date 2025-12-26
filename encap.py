class BankAccount:
    def __init__(self, name, balance):
        self.__name = name        # private variable
        self.__balance = balance  # private variable

    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount")
account = BankAccount("Alice", 1000)
print("Current balance:", account.get_balance())

account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
