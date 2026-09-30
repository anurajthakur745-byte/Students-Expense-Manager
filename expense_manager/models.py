from dataclasses import dataclass
from datetime import datetime

@dataclass
class Expense:
    expense_id: int
    date: str
    category: str
    amount: float
    description: str

    def to_dict(self):
        return {
            "id": self.expense_id,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
        }
