# Student Expense Manager

A modular Python command-line project for recording and analysing student expenses.

## Features
- Add expenses with date, category, amount and description.
- Validate dates, categories and positive amounts.
- View all expenses and total spending.
- Delete expenses by ID.
- Generate category-wise spending reports.
- Compare spending with a monthly budget.
- Store data locally in CSV format.

## Technologies
- Python 3.10+
- Python standard library
- CSV file storage
- unittest
- Git/GitHub

## Project Structure
```text
Student_Expense_Manager/
├── main.py
├── requirements.txt
├── README.md
├── statement.md
├── data/
│   └── expenses.csv
├── docs/
├── expense_manager/
│   ├── __init__.py
│   ├── models.py
│   ├── validators.py
│   ├── storage.py
│   ├── manager.py
│   ├── reports.py
│   └── cli.py
└── tests/
    └── test_manager.py
```

## Installation & Run
1. Install Python 3.10 or newer.
2. Clone/download the repository.
3. Open a terminal in the project folder.
4. Run:
```bash
python main.py
```

## Testing
Run:
```bash
python -m unittest discover -s tests -v
```

## Input Format
Date: `YYYY-MM-DD`  
Amount: positive numeric value  
Category: Food, Travel, Education, Shopping, Bills, Entertainment or Other

## GitHub
Recommended commits:
- Initial project structure
- Add expense management modules
- Add reports and validation
- Add tests and documentation
- Final project report
