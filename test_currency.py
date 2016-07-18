#

def test_currency_is_equal():
    currency1 = (10, USD)
    currency2 = (10, USD)
    assert currency1 == currency2

    def test_currency_is_not_equal():
        currency1 = (20, USD)
        currency2 = (10, USD)
        assert currency1 != currency2
