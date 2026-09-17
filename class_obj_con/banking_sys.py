class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def display(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

acc = BankAccount(name, balance)
acc.display()

deposit_amount = float(input("Enter amount to deposit: "))
acc.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
acc.withdraw(withdraw_amount)

acc.display()