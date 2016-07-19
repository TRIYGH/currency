#
from currency import Currency
from converter import Converter, UnknownCurrencyCodeError
from nose.tools import assert_raises


def test_myself():
    c1 = Converter('USD', 400)
    assert Converter.convert(c1, 'USD') == 400


def test_simple_convert():
    c1 = Converter('USD', 400)
    assert Converter.convert(c1,'EUR') == 361.18960000000004


def test_super_converter():
    c1 = Converter('EUR', 400)
    assert Converter.super_convert(c1, 'CRC') == 242023.80134976198


def test_unknown_error():
    c1 = Converter('USD', 400)

    assert_raises(UnknownCurrencyCodeError, Converter.convert, c1, "XYZ")

    assert_raises(UnknownCurrencyCodeError, Converter.super_convert, c1, "XYZ")



    #assert Converter.super_convert(c1, 'CRC')


    # c2 = Converter.super_convert(c1,'CRC')
    #
    # print(c2)
    #

##############

# def test_simple_convert():
#     c1 = Converter('USD', 400)
#     c2 = Converter.convert(c1,'EUR')
#
#     print(c2)
#
# test_simple_convert()
#test()
