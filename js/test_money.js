import assert from "assert";

class Money {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  times(multiplier) {
    return new Money(this.amount * multiplier, this.currency);
  }
}

const fiver = new Money(5, "USD");

const tenner = fiver.times(2);

assert.strictEqual(tenner.amount, 10);
assert.strictEqual(tenner.currency, "USD");

const tenEuro = new Money(10, "EUR");
const twentyEuro = tenEuro.times(2);

assert.strictEqual(twentyEuro.amount, 20);
assert.strictEqual(twentyEuro.currency, "EUR");
