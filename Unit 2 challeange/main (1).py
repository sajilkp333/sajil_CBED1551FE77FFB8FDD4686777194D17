class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount > self.__account_balance:
            print("Insufficient funds")
        else:
            self.__account_balance -= amount

    def display_balance(self):
        return self.__account_balance



account1 = BankAccount("12345", "John Doe", 1000)


account1.deposit(500)
account1.withdraw(200)

balance = account1.display_balance()
print(f"Account Balance: ${balance}")
