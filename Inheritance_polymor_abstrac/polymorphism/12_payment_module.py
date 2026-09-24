# 12. Online shopping payment module using polymorphism

class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} using UPI")


class CardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} using Card")


class WalletPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} using Wallet")


def process_payment(payment_method, amount):
    payment_method.make_payment(amount)


process_payment(UPIPayment(), 500)
process_payment(CardPayment(), 1500)
process_payment(WalletPayment(), 300)
