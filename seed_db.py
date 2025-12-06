import sqlite3

# 1. Connect to the database (It creates the file if it doesn't exist)
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 2. SQL: Create a Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        tuition INTEGER,
        status TEXT,
        date_joined DATE
    )
''')

# 3. SQL: Insert Data (The "Seed")
students = [
    ('Somchai', 'IELTS', 5000, 'Enrolled', '2025-11-01'),
    ('Nong May', 'Grammar', 3500, 'Trial', '2025-12-02'),
    ('John', 'Business Eng', 8000, 'Enrolled', '2025-10-15'),
    ('Sarah', 'Conversation', 4000, 'Paused', '2025-09-20'),
    ('Boss', 'Kids Class', 3000, 'Graduated', '2025-08-10'),
    ('Jenny', 'IELTS', 5000, 'Enrolled', '2025-12-05')
]

# Bulk Insert
cursor.executemany('''
    INSERT INTO students (name, course, tuition, status, date_joined)
    VALUES (?, ?, ?, ?, ?)
''', students)

# 4. Commit (Save) and Close
conn.commit()
conn.close()

print("✅ SQL Database 'school.db' created successfully!")
