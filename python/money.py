class Money:
    amount: float
    currency: str

    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.currency} {self.amount:0.2f}"

    def __eq__(self, value) -> bool:
        if not isinstance(value, Money):
            return False
        return self.amount == value.amount and self.currency == value.currency

    def times(self, multiplier: float) -> "Money":
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor: int) -> "Money":
        return Money(self.amount / divisor, self.currency)
