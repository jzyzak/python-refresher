class BankAccount:
    def __init__(self, name, accountNumber, balance):
        self.balance = balance
        self.name = name
        self.accountNumber = accountNumber

    def withdrawMoney(self, amount):
        if self.balance - amount < 0:
            raise ValueError(
                "You can't withdraw more money than you have in your balance."
            )
        else:
            self.balance -= amount

    def depositMoney(self, amount):
        if amount < 0:
            raise ValueError(
                "This is an invalid amount, please enter a positive amount."
            )
        else:
            self.balance += amount

    def printBalance(self):
        print(f"You have {self.balance} in your balance.")
