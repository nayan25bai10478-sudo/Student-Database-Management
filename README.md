Student Database Program
A comprehensive database management system for tracking and managing student information, academic records, and related data.
Features

Student Management: Add, update, delete, and search student records
Academic Records: Track grades, courses, and GPA calculations
Attendance Tracking: Monitor student attendance and generate reports
Data Export: Export student data to CSV, Excel, or PDF formats
Search & Filter: Advanced filtering by name, ID, grade level, or course
User Authentication: Secure login system with role-based access control

Installation
Prerequisites:

Python 3.8 or higher
pip (Python package installer)
SQLite3 (included with Python)

Setup Instructions

Clone the repository: https://github.com/nayan25bai10478-sudo/Student-Database-Management.git

bashgit clone 
cd student-database

Create a virtual environment:

bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required dependencies:

bashpip install -r requirements.txt

Initialize the database:

bashpython setup_db.py

Run the application:

python main.py
