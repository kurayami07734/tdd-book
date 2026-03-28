import unittest

from money import Money
from portfolio import Portfolio


class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        fiver = Money(5, "USD")
        tenner = Money(10, "USD")

        self.assertEqual(fiver.times(2), tenner)

    def testMultiplicationEUR(self):
        fiver = Money(10, "EUR")
        tenner = Money(20, "EUR")

        self.assertEqual(fiver.times(2), tenner)

    def testDivision(self):
        og = Money(4002, "KRW")
        quarter = Money(1000.5, "KRW")

        self.assertEqual(og.divide(4), quarter)

    def testAddition(self):
        five = Money(5, "USD")
        ten = Money(10, "USD")
        fifteen = Money(15, "USD")

        portfolio = Portfolio()
        portfolio.add(five, ten)

        self.assertEqual(portfolio.evaluate("USD"), fifteen)


if __name__ == "__main__":
    unittest.main()
