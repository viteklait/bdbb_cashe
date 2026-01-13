from decimal import Decimal
from money import Money
from account import Account

acc = Account("USD")

acc.add_money(Money(Decimal("10.00"), "USD"))
acc.add_money(Money(Decimal("5.50"), "USD"))

print(acc.balance())  # ожидаем: 15.50 USD
