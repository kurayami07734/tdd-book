import unittest


class Money:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def times(self, multiplier: int) -> "Money":
        return Money(self.amount * multiplier, self.currency)


class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        fiver = Money(5, "USD")
        tenner = fiver.times(2)

        self.assertEqual(tenner.amount, 10)
        self.assertEqual(tenner.currency, "USD")

    def testMultiplicationEUR(self):
        fiver = Money(10, "EUR")
        tenner = fiver.times(2)

        self.assertEqual(tenner.amount, 20)
        self.assertEqual(tenner.currency, "EUR")


if __name__ == "__main__":
    unittest.main()
