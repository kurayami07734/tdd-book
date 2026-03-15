import unittest


class Money:
    amount: float
    currency: str

    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __eq__(self, value) -> bool:
        if not isinstance(value, Money):
            return False
        return self.amount == value.amount and self.currency == value.currency

    def times(self, multiplier: float) -> "Money":
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor: int) -> "Money":
        return Money(self.amount / divisor, self.currency)


class Portfolio:
    moneys: list[Money]

    def __init__(self) -> None:
        self.moneys = []

    def add(self, *moneys: Money) -> None:
        self.moneys.extend(moneys)

    def evaluate(self, currency: str) -> Money:
        total = sum(m.amount for m in self.moneys if m.currency == currency)
        return Money(total, currency)


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
