# UML Design

## Use Case
```text
             +---------------------------+
             | Student Expense Manager   |
             |                           |
Student ---->| Add Expense               |
Student ---->| View Expenses             |
Student ---->| Delete Expense            |
Student ---->| Generate Report           |
Student ---->| Check Budget              |
             +---------------------------+
```

## Class Diagram
```text
+------------------+
| Expense          |
+------------------+
| expense_id       |
| date             |
| category         |
| amount           |
| description      |
+------------------+

+------------------+       +------------------+
| ExpenseManager   |------>| ExpenseStorage   |
+------------------+       +------------------+
| add_expense()    |       | load()           |
| delete_expense() |       | save()           |
| get_expenses()   |       +------------------+
| total()          |
+------------------+
```

## Sequence
```text
Student -> CLI: Add expense
CLI -> Manager: add_expense(data)
Manager -> Validator: validate(data)
Validator --> Manager: valid
Manager -> Storage: save(expenses)
Storage --> Manager: saved
Manager --> CLI: success
CLI --> Student: confirmation
```

## ER/Storage Design
CSV entity: Expense(id, date, category, amount, description)
