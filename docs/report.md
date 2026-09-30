# Student Expense Manager — Project Report

## 1. Cover Page
**Project:** Student Expense Manager  
**Subject:** Python Programming  
**Technology:** Python  
**Student:** ____________________  
**Registration No.:** ____________________  
**Institution:** ____________________  
**Academic Year:** 2026–27

## 2. Introduction
Student Expense Manager is a command-line Python application designed to help students record and understand their personal expenses. The application demonstrates modular programming, classes, functions, validation, file handling, reporting and testing.

## 3. Problem Statement
Students may find it difficult to maintain a consistent record of daily spending. A simple local application can provide structured storage and basic analysis without requiring an online account.

## 4. Functional Requirements
1. Add a new expense.
2. View stored expenses.
3. Delete an expense.
4. Generate category-wise spending summaries.
5. Check total spending against a budget.
6. Store records persistently in CSV format.

## 5. Non-functional Requirements
- **Usability:** Menu-driven interface with clear prompts.
- **Reliability:** Input validation and controlled error handling.
- **Maintainability:** Separate modules for models, validation, storage, management and reporting.
- **Resource efficiency:** Uses lightweight CSV storage and Python standard-library components.
- **Error handling:** Invalid dates, amounts, categories and IDs are reported without terminating the normal application flow.

## 6. System Architecture
The application uses a layered structure: CLI → Manager → Validation/Reports → Storage → CSV. See `docs/architecture.md`.

## 7. Design Diagrams
Use Case, Class, Sequence and storage diagrams are provided in `docs/uml.md`; workflow is provided in `docs/workflow.md`.

## 8. Design Decisions & Rationale
A CLI was selected because the project focuses on Python programming fundamentals rather than web development. CSV was selected because it is human-readable, simple to maintain and available through the standard library. Separate modules reduce coupling and make testing easier.

## 9. Implementation Details
`models.py` defines the Expense data model. `validators.py` validates user input. `storage.py` handles CSV persistence. `manager.py` implements CRUD-style expense operations. `reports.py` performs summaries and budget calculations. `cli.py` manages interaction. `main.py` starts the application.

## 10. Screenshots / Results
Run the application and capture screenshots showing:
- Main menu
- Adding an expense
- Viewing expenses
- Category report
- Budget status

## 11. Testing Approach
Unit tests use Python's `unittest` framework. Tests cover successful expense creation, invalid amount handling and deletion. Run `python -m unittest discover -s tests -v`.

## 12. Challenges Faced
Key implementation challenges include validating different input types, keeping IDs consistent after deletion, separating storage logic from business logic and ensuring invalid user input does not crash the application.

## 13. Learnings & Key Takeaways
The project demonstrates Python classes, dataclasses, functions, modules, exception handling, file handling, collections, testing and modular software design. It also demonstrates how a programming problem can be converted into functional requirements and a maintainable implementation.

## 14. Future Enhancements
- GUI using Tkinter.
- SQLite database support.
- Expense editing.
- Date-range reports.
- Charts and visual analytics.
- Optional login and multi-user support.

## 15. References
- Python documentation: https://docs.python.org/3/
- Course notes and Python programming material provided by the institution.
- VITyarthi Build Your Own Project guidelines.
