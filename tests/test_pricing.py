import pytest
from shopcalc.pricing import net_to_gross, apply_discount, cart_total

def test_net_to_gros_default_vat():
    assert net_to_gross(100) == 119.0

@pytest.mark.parametrize("net, rate, expected", [
    (100, 0.07, 107.0),
    (0, 0.19, 0.0),
    (19.99, 0.19, 23.79),
])


def test_net_to_gross_with_various_rates(net, rate, expected):
    assert net_to_gross(net, rate) == expected

def test_net_to_gross_negative_raises():
    with pytest.raises(ValueError):
        net_to_gross(-5)

@pytest.mark.parametrize("price, percent, expected", [(100, 10, 90.0), (50, 0, 50.0)])
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected

@pytest.mark.parametrize("price, percent", [(100, -10), (50, 150)])
def test_apply_discount_price_raised(price, percent):
    with pytest.raises(ValueError):
        apply_discount(price, percent)

def test_cart_total_with_multiple_items():
    items = [
        {"price": 10.0, "quantity": 2},
        {"price": 5.0, "quantity": 3},
    ]
    assert cart_total(items) == 35.0

def test_cart_total_all_items_zero_quantity():
    items = [
        {"price": 10.0, "quantity": 0},
        {"price": 5.0, "quantity": 0},
    ]
    assert cart_total(items) == 0.0

