from .models import Expense
from .validators import validate_amount, validate_date, validate_category

class ExpenseManager:
    def __init__(self, storage):
        self.storage = storage
        self.expenses = storage.load()

    def _next_id(self):
        return max((e.expense_id for e in self.expenses), default=0) + 1

    def add_expense(self, date, category, amount, description):
        expense = Expense(self._next_id(), validate_date(date),
                          validate_category(category), validate_amount(amount), description.strip())
        self.expenses.append(expense)
        self.storage.save(self.expenses)
        return expense

    def delete_expense(self, expense_id):
        before = len(self.expenses)
        self.expenses = [e for e in self.expenses if e.expense_id != expense_id]
        if len(self.expenses) == before:
            raise ValueError("Expense ID not found.")
        self.storage.save(self.expenses)

    def get_expenses(self, category=None):
        if category:
            return [e for e in self.expenses if e.category == category]
        return list(self.expenses)

    def total(self):
        return sum(e.amount for e in self.expenses)
