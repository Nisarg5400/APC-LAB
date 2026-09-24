# 7. BankAccount base class, calculate_interest() overridden

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.04


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return 0   # current accounts usually don't earn interest


class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.07


accounts = [SavingsAccount(10000), CurrentAccount(10000), FixedDepositAccount(10000)]
for a in accounts:
    print(f"{a.__class__.__name__} Interest: {a.calculate_interest()}")
