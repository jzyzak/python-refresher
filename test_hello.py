import unittest
import hello
import bankAccount


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "hi")
        self.assertNotEqual(hello.hello(), "hello")

    def test_add(self):
        self.assertEqual(hello.add(1, 1), 2)
        self.assertEqual(hello.add(2, 2), 4)
        self.assertEqual(hello.add(3, 3), 6)

    def test_sub(self):
        self.assertEqual(hello.sub(2, 1), 1)
        self.assertEqual(hello.sub(4, 2), 2)
        self.assertEqual(hello.sub(6, 3), 3)

    def test_mul(self):
        self.assertEqual(hello.mul(1, 1), 1)
        self.assertEqual(hello.mul(2, 2), 4)
        self.assertEqual(hello.mul(3, 3), 9)

    def test_div(self):
        self.assertEqual(hello.div(1, 1), 1)
        self.assertEqual(hello.div(4, 2), 2)
        self.assertEqual(hello.div(9, 3), 3)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(1), 1)
        self.assertEqual(hello.sqrt(4), 2)
        self.assertEqual(hello.sqrt(9), 3)

    def test_power(self):
        self.assertEqual(hello.power(1, 2), 1)
        self.assertEqual(hello.power(2, 3), 8)
        self.assertEqual(hello.power(3, 4), 81)

    def test_log(self):
        self.assertEqual(hello.log(1), 0)
        self.assertEqual(hello.log(2), 0.6931471805599453)
        self.assertEqual(hello.log(3), 1.0986122886681098)

    def test_exp(self):
        self.assertEqual(hello.exp(0), 1)
        self.assertEqual(hello.exp(1), 2.718281828459045)
        self.assertEqual(hello.exp(2), 7.38905609893065)

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertEqual(hello.sin(90), 0.8939966636005579)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertEqual(hello.cos(90), -0.4480736161291701)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)
        self.assertEqual(hello.tan(2), -2.185039863261519)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)
        self.assertEqual(hello.cot(90), -0.5012027833801532)


if __name__ == "__main__":
    unittest.main()
