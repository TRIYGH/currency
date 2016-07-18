class Currency:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code


    def __eq__(self, other_stuff):
        return self.amount == other_stuff.amount and self.currency_code == other_stuff.currency_code


    def __add__(self, other_amt):
        try:
            if self.currency_code != other_amt.currency_code:
                raise DifferentCurrencyCodeError
            return (self.amount + other_amt.amount, self.currency_code)
        except ZeroDivisionError:
            pass

    def __sub__(self, other_amt):
        try:
            if self.currency_code != other_amt.currency_code:
                raise DifferentCurrencyCodeError
            return (self.amount - other_amt.amount, self.currency_code)
        except ZeroDivisionError:
            pass








class DifferentCurrencyCodeError(Exception):
    pass


    # def raise_cc_error(self, other):
    #     if self.currency_code != other.currency_code:
    #         raise Exception ("Your currencies aren't the same.")
    #     else:
