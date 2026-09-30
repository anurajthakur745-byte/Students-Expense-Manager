from .validators import CATEGORIES

def show_menu():
    print("\n=== Student Expense Manager ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Category report")
    print("5. Budget status")
    print("6. Exit")

def run(manager):
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                date = input("Date (YYYY-MM-DD): ")
                print("Categories:", ", ".join(CATEGORIES))
                category = input("Category: ")
                amount = input("Amount (₹): ")
                description = input("Description: ")
                e = manager.add_expense(date, category, amount, description)
                print(f"Added expense #{e.expense_id}.")
            elif choice == "2":
                expenses = manager.get_expenses()
                if not expenses:
                    print("No expenses recorded.")
                for e in expenses:
                    print(f"#{e.expense_id} | {e.date} | {e.category} | ₹{e.amount:.2f} | {e.description}")
                print(f"Total: ₹{manager.total():.2f}")
            elif choice == "3":
                manager.delete_expense(int(input("Expense ID: ")))
                print("Expense deleted.")
            elif choice == "4":
                for cat, total in __import__("expense_manager.reports", fromlist=["category_summary"]).category_summary(manager.expenses).items():
                    print(f"{cat}: ₹{total:.2f}")
            elif choice == "5":
                budget = float(input("Monthly budget (₹): "))
                status = __import__("expense_manager.reports", fromlist=["budget_status"]).budget_status(manager.expenses, budget)
                print(status)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except (ValueError, TypeError) as exc:
            print("Error:", exc)
