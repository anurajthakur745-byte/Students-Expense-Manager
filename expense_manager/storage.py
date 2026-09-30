import csv
from pathlib import Path
from .models import Expense

FIELDS = ["id", "date", "category", "amount", "description"]

class ExpenseStorage:
    def __init__(self, filename="data/expenses.csv"):
        self.path = Path(filename)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text(",".join(FIELDS) + "\n", encoding="utf-8")

    def load(self):
        expenses = []
        with self.path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                expenses.append(Expense(int(row["id"]), row["date"], row["category"],
                                       float(row["amount"]), row["description"]))
        return expenses

    def save(self, expenses):
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense.to_dict())
