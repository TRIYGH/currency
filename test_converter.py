#
from currency import Currency
from converter import Converter


def test_myself():
    c1 = Converter('USD', 400)
    assert Converter.convert(c1, 'USD') == 400


def test_simple_convert():
    c1 = Converter('USD', 400)
    assert Converter.convert(c1,'EUR') == 361.18960000000004


def test():
    c1 = Converter('EUR', 400)
    assert Converter.super_convert(c1, 'CRC') == 242023.80134976198

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
test()
