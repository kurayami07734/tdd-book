from money import Money


class Portfolio:
    moneys: list[Money]

    def __init__(self) -> None:
        self.moneys = []

    def add(self, *moneys: Money) -> None:
        self.moneys.extend(moneys)

    def __convert(self, money: Money, currency: str) -> float:
        factor = 1 if money.currency == currency else 1.2
        return money.amount * factor

    def evaluate(self, currency: str) -> Money:
        total = sum(self.__convert(m, currency) for m in self.moneys)
        return Money(total, currency)
