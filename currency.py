class Currency:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code


    def __eq__(self, other_stuff):
        return self.amount == other_stuff.amount and self.currency_code == other_stuff.currency_code


    def __add__(self, other_amt):
        if self.currency_code == other_amt.currency_code:
            return (self.amount + other_amt.amount, self.currency_code)


    # def atsnt(num1, num1)
    #     reutrn n1=n2
