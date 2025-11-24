# Student Management System (SMS) — Project Report

## 1. Introduction
This project is a command-line Student Management System developed in Python. It helps manage students, courses, and enrollments in an organized way using SQLite database.

## 2. Problem Statement
Manual management of students and courses is inefficient and prone to errors. This system automates record keeping, ensures data integrity, and allows easy reporting.

## 3. Functional Requirements
- CRUD operations for students
- CRUD operations for courses
- Enrollment management (enroll/unenroll)
- Search students by name
- View all enrollments for a student

## 4. Non-Functional Requirements
- **Performance:** Fast access and retrieval using SQLite
- **Security:** Database constraints prevent duplicates
- **Usability:** CLI menus for easy navigation
- **Reliability:** Handles invalid input gracefully
- **Maintainability:** Modular Python code with separate files for services, UI, DB

## 5. System Architecture
- Modular Python code with `src/` folder
- SQLite3 database stored in `data/sms.db`
- CLI interface via `main.py` → `ui.py` → `services.py`

## 6. Design Diagrams
*(You can include Use Case, Class, Sequence, ER diagrams as images here if required)*

## 7. Implementation Details
- Python modules:
  - `main.py` – entry point
  - `ui.py` – CLI menus
  - `services.py` – business logic
  - `db.py` – database connection & schema
  - `models.py` – data classes
  - `validators.py` – input validation
  - `utils.py` – helper functions
  - `logger.py` – logging
  - `config.py` – paths & settings
- SQLite database with 3 tables: `students`, `courses`, `enrollments`

## 8. Screenshots / Results
*(Add CLI screenshots here)*

## 9. Testing Approach
- Unit tests using `pytest`
- Manual testing via CLI menus
- Verified adding, updating, deleting, listing, and enrollment

## 10. Challenges Faced
- Designing modular code structure for CLI menus
- Managing foreign key constraints in SQLite
- Validating user inputs

## 11. Learnings & Key Takeaways
- Practical understanding of CRUD operations
- Database integration in Python
- Modular programming and logging

## 12. Future Enhancements
- GUI using Tkinter or web app using Flask
- Reporting & analytics
- Exporting data to CSV / PDF
- Role-based access for admin/teacher/student

## 13. References
- Python 3.x documentation: https://docs.python.org/3/
- SQLite official site: https://www.sqlite.org/
- Git & GitHub tutorials
