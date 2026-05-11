import sqlite3

# Connect to Database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create Books Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    publisher TEXT,
    publication_date TEXT,
    quantity INTEGER
)
""")

# Create Members Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    membership_date TEXT
)
""")

# Create Borrowings Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS borrowings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    member_id INTEGER,
    borrow_date TEXT,
    return_date TEXT,
    FOREIGN KEY(book_id) REFERENCES books(id),
    FOREIGN KEY(member_id) REFERENCES members(id)
)
""")

conn.commit()