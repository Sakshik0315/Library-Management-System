from functions import *
from database import conn


def main():

    while True:

        print("""
========== LIBRARY MANAGEMENT SYSTEM ==========
1. Add Book
2. View Books
3. Add Member
4. View Members
5. Borrow Book
6. View Borrowings
7. Exit
===============================================
""")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            add_member()

        elif choice == "4":
            view_members()

        elif choice == "5":
            borrow_book()

        elif choice == "6":
            view_borrowings()

        elif choice == "7":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice! Please Try Again.\n")

    conn.close()


# Run Program
if __name__ == "__main__":
    main()