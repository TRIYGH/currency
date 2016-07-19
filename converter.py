#
class Converter:
    def __init__(self, from_code, from_amount):
        self.from_code = from_code
        self.from_amount = from_amount


    def convert(self,to_code):
        conversion_table = {'USD': 1.0, 'EUR': 0.902974, 'JPY': 106.157}
        if to_code not in conversion_table:
            raise UnknownCurrencyCodeError
        rate = conversion_table.get(to_code)
        to_amount = self.from_amount * rate
        return to_amount


    def super_convert(self, to_code):
        conversion_table = {'USD': 1.0, 'EUR': 0.902974, 'JPY': 106.157, 'MXN': 18.3903, 'CRC': 546.353, 'COP': 2920.45}
        if to_code not in conversion_table:
            raise UnknownCurrencyCodeError
        if self.from_code != 'USD':
            rate = 1 / conversion_table.get(self.from_code)
            if to_code != 'USD':
                rate = rate * conversion_table.get(to_code)
                to_amount = rate * self.from_amount
                return to_amount
            else:
                to_amount = rate * self.from_amount
                return to_amount


class UnknownCurrencyCodeError(Exception):
    pass

########
                #new_obj = (to_code, to amount)
                #return (new_obj)
