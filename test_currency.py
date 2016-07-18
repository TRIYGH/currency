#W2D1 normal

from currency import Currency

def c_amount_and_c_code():
    dollar = Currency(1, 'USD')
    assert dollar == (1, 'USD')


def test_currency_is_equal():
    currency1 = Currency(10, 'USD')
    currency2 = Currency(10, 'USD')

    assert currency1 == currency2


def test_currency_is_not_equal():
    currency1 = Currency(20, 'USD')
    currency2 = Currency(10, 'USD')

    assert currency1 != currency2
