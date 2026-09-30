import tempfile
from pathlib import Path
import unittest
from expense_manager.storage import ExpenseStorage
from expense_manager.manager import ExpenseManager

class TestExpenseManager(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.manager = ExpenseManager(ExpenseStorage(str(Path(self.temp.name) / "expenses.csv")))

    def tearDown(self):
        self.temp.cleanup()

    def test_add_expense(self):
        e = self.manager.add_expense("2026-09-28", "Food", "120", "Lunch")
        self.assertEqual(e.expense_id, 1)
        self.assertEqual(self.manager.total(), 120)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.manager.add_expense("2026-09-28", "Food", "-10", "Invalid")

    def test_delete_expense(self):
        e = self.manager.add_expense("2026-09-28", "Travel", "50", "Bus")
        self.manager.delete_expense(e.expense_id)
        self.assertEqual(len(self.manager.expenses), 0)

if __name__ == "__main__":
    unittest.main()
