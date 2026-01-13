from decimal import Decimal
from money import Money


class Account:
    def __init__ (self, currency):
        self.currency = currency
        self.money = []
    
    def add_money (self, m):
        if m.currency == self.currency:
            self.money.append(m)
        else:
            raise ValueError("Another currency")



    def balance (self):
        total = Money(Decimal("0.00"), self.currency)
        for m in self.money:
            total = total + m 
        return total
    