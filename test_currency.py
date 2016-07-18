#W2D1 normal

from currency import Currency
from currency import DifferentCurrencyCodeError
from nose.tools import assert_raises


def c_amount_and_c_code():
    dollar = Currency(1, 'USD')
    
    assert dollar.amount == 1
    assert dollar.currency_code == 'USD'


def test_currency_is_equal():
    currency1 = Currency(10, 'USD')
    currency2 = Currency(10, 'USD')

    assert currency1 == currency2


def test_currency_is_not_equal():
    currency1 = Currency(20, 'USD')
    currency2 = Currency(10, 'USD')

    assert currency1 != currency2

def test_add_currency():
    currency1 = Currency(11, 'USD')
    currency2 = Currency(22, 'USD')

    assert currency1 + currency2 == (33, 'USD')


def test_subtract_currency():
    currency1 = Currency(22, 'USD')
    currency2 = Currency(10, 'USD')

    assert currency1 - currency2 == (12, 'USD')


def test_add_currency_error():
    currency1 = Currency(11, 'PES')
    currency2 = Currency(22, 'USD')

    assert_raises(DifferentCurrencyCodeError, Currency.__add__, currency1, currency2)


def test_sub_currency_error():
    currency1 = Currency(55, 'PES')
    currency2 = Currency(22, 'USD')

    assert_raises(DifferentCurrencyCodeError, Currency.__sub__, currency1, currency2)
