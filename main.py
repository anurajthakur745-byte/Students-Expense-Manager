from expense_manager.storage import ExpenseStorage
from expense_manager.manager import ExpenseManager
from expense_manager.cli import run

if __name__ == "__main__":
    storage = ExpenseStorage("data/expenses.csv")
    manager = ExpenseManager(storage)
    run(manager)
