import sqlite3
from pathlib import Path

# Path to your database
db_path = Path("data/sms.db")  # make sure this matches your folder structure

conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("\n--- Tables in database ---")
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
for t in tables:
    print(t[0])

# View all students
print("\n--- Students ---")
cur.execute("SELECT * FROM students")
for row in cur.fetchall():
    print(row)

# View all courses
print("\n--- Courses ---")
cur.execute("SELECT * FROM courses")
for row in cur.fetchall():
    print(row)

# View all enrollments
print("\n--- Enrollments ---")
cur.execute("SELECT * FROM enrollments")
for row in cur.fetchall():
    print(row)

conn.close()
