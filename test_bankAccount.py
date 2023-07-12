import unittest
from bankAccount import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_init(self):
        user = BankAccount("J", 1234, 0)

        self.assertEqual(user.name, "J")
        self.assertEqual(user.accountNumber, 1234)
        self.assertEqual(user.balance, 0)
        self.assertNotEqual(user.name, "")

    def test_withdrawMoney(self):
        user = BankAccount("J", 1234, 100)
        user.withdrawMoney(100)

        self.assertEqual(user.balance, 0)
        self.assertRaises(ValueError, user.withdrawMoney, 1000)

    def test_depositMoney(self):
        user = BankAccount("J", 1234, 0)
        user.depositMoney(100)

        self.assertEqual(user.balance, 100)
        self.assertNotEqual(user.balance, 0)

    def test_printBalance(self):
        user = BankAccount("J", 1234, 100)
        self.assertIsNone(user.printBalance())


if __name__ == "__main__":
    user = BankAccount("J", 1234, 100)
    user.deposit(100)
    user.withdraw(150)
    user.printBalance()
