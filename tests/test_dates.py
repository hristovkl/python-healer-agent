from datetime import date

import pytest

from shopcalc.dates import add_business_days, weekend_checker


@pytest.mark.parametrize("day", [date(2026, 10, 31), date(2026, 11, 1)])
def test_weekend_checker_true_on_weekend(day):
    assert weekend_checker(day) is True


@pytest.mark.parametrize("day", [date(2026, 10, 26), date(2026, 10, 30)])
def test_weekend_checker_false_on_weekday(day):
    assert weekend_checker(day) is False


def test_add_business_days_skips_weekend():
    # Friday + 3 business days -> Monday, Tuesday, Wednesday
    assert add_business_days(date(2026, 10, 30), 3) == [
        date(2026, 11, 2),
        date(2026, 11, 3),
        date(2026, 11, 4),
    ]


def test_add_business_days_weekend_start_raises():
    with pytest.raises(ValueError):
        add_business_days(date(2026, 10, 31), 2)
