from datetime import date, timedelta


def weekend_checker(day: date) -> bool:
    """Check whether a date falls on a weekend."""
    return day.weekday() >= 5


def add_business_days(start_date: date, number_of_days: int) -> list[date]:
    """Add business days to a date, skipping weekends."""
    if weekend_checker(start_date):
        raise ValueError("Start date cannot be a weekend day.")
    weekdays_added = []
    current = start_date
    while len(weekdays_added) <= number_of_days:
        current += timedelta(days=1)
        if not weekend_checker(current):
            weekdays_added.append(current)
    return weekdays_added


if __name__ == "__main__":
    print(add_business_days(date.today(), 3))
