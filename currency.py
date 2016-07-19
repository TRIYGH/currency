class Currency:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code


    def __eq__(self, other_stuff):
        return self.amount == other_stuff.amount and self.currency_code == other_stuff.currency_code


    def __add__(self, other_amt):
        if self.currency_code != other_amt.currency_code:
            raise DifferentCurrencyCodeError

        return (self.amount + other_amt.amount, self.currency_code)


    def __sub__(self, other_amt):
        if self.currency_code != other_amt.currency_code:
            raise DifferentCurrencyCodeError

        return (self.amount - other_amt.amount, self.currency_code)


    def __mul__(self, other_amt):
        return (self.amount * other_amt, self.currency_code)


    def money_identifier(self):
        symbols = {'€': 'EUR', '$': 'USD', '¥': 'JPY'}
        x = list(self)
        for each in x:
            if each in symbols:
                symbol = symbols[each]
                x.pop(0)
                money = float("".join(x))
                return (money, symbol)




class DifferentCurrencyCodeError(Exception):
    pass


    # def raise_cc_error(self, other):
    #     if self.currency_code != other.currency_code:
    #         raise Exception ("Your currencies aren't the same.")
    #     else:
