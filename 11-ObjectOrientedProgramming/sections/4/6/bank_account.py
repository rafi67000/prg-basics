from decimal import Decimal

class BankAccount:
    def __init__(self, number):
        self.number = number # numer konta
        self.balance = Decimal("0") # saldo konta

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount # wplata pieniedzy

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds on the account")
        elif amount > 0:
            self.balance -= amount # wyplata pieniedzy

    def show_status(self):
        print("Bank Account No:", self.number)
        balance = f"{self.balance:.2f}".replace(".", ",") # przecinek zamiast kropki
        print("Balance: PLN", balance)


account = BankAccount("12 3456 5555 9090 1111 0000 7722")
account.show_status()
account.deposit(Decimal("25.30"))
account.show_status()
account.withdraw(Decimal("31.70"))
account.show_status()
account.withdraw(Decimal("14"))
account.show_status()
