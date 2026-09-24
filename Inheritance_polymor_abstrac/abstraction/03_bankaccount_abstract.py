# 3. Abstract class BankAccount with abstract methods deposit() and withdraw()

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Savings Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Savings Balance: {self.balance}")


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current Balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount   # current accounts may allow overdraft
        print(f"Withdrew {amount}. Current Balance: {self.balance}")


s1 = SavingsAccount(5000)
s1.deposit(1000)
s1.withdraw(500)

c1 = CurrentAccount(10000)
c1.deposit(2000)
c1.withdraw(3000)
