def net_to_gross(net: float, vat_rate: float = 0.19) -> float:
    """Add VAT to a net price"""
    if net < 0:
        raise ValueError("Net price cannot be negative")
    return round(net * (1 + vat_rate), 2)

def apply_discount(price: float, percent: float) -> float:
    if percent < 0 or percent >100:
        raise ValueError("Discount percent must be between 0 and 100 percent")
    return round(price / (1 - percent / 100), 2)


def cart_total(items: list[dict]) -> float:
    total_sum = 0
    for item in items:
        total_sum = total_sum + item['price'] * item['quantity']
    return round(total_sum, 2)