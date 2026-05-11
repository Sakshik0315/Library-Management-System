from database import conn, cursor

# Add Book
def add_book():

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    publisher = input("Enter Publisher Name: ")
    publication_date = input("Enter Publication Date (YYYY-MM-DD): ")
    quantity = int(input("Enter Quantity: "))

    cursor.execute("""
    INSERT INTO books (title, author, publisher, publication_date, quantity)
    VALUES (?, ?, ?, ?, ?)
    """, (title, author, publisher, publication_date, quantity))

    conn.commit()

    print("Book Added Successfully!\n")


# View Books
def view_books():

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n------ BOOK LIST ------")

    if len(books) == 0:
        print("No books available.")

    else:
        for book in books:

            print(f"""
Book ID           : {book[0]}
Title             : {book[1]}
Author            : {book[2]}
Publisher         : {book[3]}
Publication Date  : {book[4]}
Quantity          : {book[5]}
-----------------------------------
""")


# Add Member
def add_member():

    name = input("Enter Member Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    membership_date = input("Enter Membership Date (YYYY-MM-DD): ")

    cursor.execute("""
    INSERT INTO members (name, email, phone, membership_date)
    VALUES (?, ?, ?, ?)
    """, (name, email, phone, membership_date))

    conn.commit()

    print("Member Added Successfully!\n")


# View Members
def view_members():

    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    print("\n------ MEMBER LIST ------")

    if len(members) == 0:
        print("No members found.")

    else:
        for member in members:

            print(f"""
Member ID         : {member[0]}
Name              : {member[1]}
Email             : {member[2]}
Phone             : {member[3]}
Membership Date   : {member[4]}
-----------------------------------
""")


# Borrow Book
def borrow_book():

    book_id = int(input("Enter Book ID: "))
    member_id = int(input("Enter Member ID: "))
    borrow_date = input("Enter Borrow Date (YYYY-MM-DD): ")
    return_date = input("Enter Return Date (YYYY-MM-DD): ")

    # Check Quantity
    cursor.execute(
        "SELECT quantity FROM books WHERE id = ?",
        (book_id,)
    )

    result = cursor.fetchone()

    if result is None:
        print("Book Not Found.\n")
        return

    quantity = result[0]

    if quantity <= 0:
        print("Book Not Available.\n")
        return

    # Insert Borrowing Record
    cursor.execute("""
    INSERT INTO borrowings
    (book_id, member_id, borrow_date, return_date)
    VALUES (?, ?, ?, ?)
    """, (book_id, member_id, borrow_date, return_date))

    # Update Quantity
    cursor.execute("""
    UPDATE books
    SET quantity = quantity - 1
    WHERE id = ?
    """, (book_id,))

    conn.commit()

    print("Book Borrowed Successfully!\n")


# View Borrowings
def view_borrowings():

    cursor.execute("""
    SELECT borrowings.id,
           books.title,
           members.name,
           borrowings.borrow_date,
           borrowings.return_date
    FROM borrowings
    JOIN books
    ON borrowings.book_id = books.id
    JOIN members
    ON borrowings.member_id = members.id
    """)

    records = cursor.fetchall()

    print("\n------ BORROWING RECORDS ------")

    if len(records) == 0:
        print("No borrowing records found.")

    else:
        for record in records:

            print(f"""
Borrow ID         : {record[0]}
Book Title        : {record[1]}
Member Name       : {record[2]}
Borrow Date       : {record[3]}
Return Date       : {record[4]}
-----------------------------------
""")