import unittest
import bankAccount


class TestBankAccount(unittest.TestCase):
    def test_init(self):
        user = bankAccount("J", 1234)

        self.assertEqual(user.name, "J")
        self.assertEqual(user.accountNumber, 1234)
        self.assertEqual(user.balance, 0)
        self.assertNotEqual(user.name, "")

    def test_withdrawMoney(self):
        user = bankAccount("J", 1234, 100)
        user.withdraw(100)

        self.assertEqual(user.balance, 0)
        self.assertRaises(ValueError, user.withdraw(1000))

    # def test_depositMoney(self):
    # self.assertEqual()

    # def test_printBalance(self):
    # self.assertEqual()


if __name__ == "__main__":
    unittest.main()
