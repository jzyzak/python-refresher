class BankAccount:
    def __init__(self, name, accountNumber, balance=0):
        self.balance = balance
        self.name = name
        self.accountNumber = accountNumber

    def withdrawMoney(self, amount):
        if self.balance - amount < 0:
            raise ValueError("You can't withdraw more money than in your balance")
        else:
            self.balance -= amount

    def depositMoney(self, amount):
        if amount < 0:
            raise ValueError("Invalid Amount")
        else:
            self.balance += amount

    def printBalance(self):
        print(
            self.name + "(Account " + self.accountNumber + ")'s Balance:" + self.balance
        )
