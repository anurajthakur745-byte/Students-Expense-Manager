from collections import defaultdict
from .models import Expense

def category_summary(expenses):
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense.category] += expense.amount
    return dict(sorted(summary.items(), key=lambda x: x[1], reverse=True))

def monthly_summary(expenses):
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense.date[:7]] += expense.amount
    return dict(sorted(summary.items()))

def budget_status(expenses, monthly_budget):
    total = sum(e.amount for e in expenses)
    remaining = monthly_budget - total
    return {"spent": total, "budget": monthly_budget, "remaining": remaining,
            "status": "Within Budget" if remaining >= 0 else "Budget Exceeded"}
