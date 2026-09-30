from datetime import datetime

CATEGORIES = ["Food", "Travel", "Education", "Shopping", "Bills", "Entertainment", "Other"]

def validate_amount(value):
    try:
        amount = float(value)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount
    except (TypeError, ValueError):
        raise ValueError("Enter a valid positive amount.")

def validate_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")

def validate_category(value):
    if value not in CATEGORIES:
        raise ValueError(f"Category must be one of: {', '.join(CATEGORIES)}")
    return value
