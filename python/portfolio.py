from money import Money


class Portfolio:
    moneys: list[Money]

    def __init__(self) -> None:
        self.moneys = []

    def add(self, *moneys: Money) -> None:
        self.moneys.extend(moneys)

    def evaluate(self, currency: str) -> Money:
        total = sum(m.amount for m in self.moneys if m.currency == currency)
        return Money(total, currency)
