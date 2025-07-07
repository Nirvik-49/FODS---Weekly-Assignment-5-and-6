import json
import os
from datetime import datetime, timedelta

class Book:
    def __init__(self, isbn, title, author, quantity):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity
    
    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'quantity': self.quantity
        }

class Transaction:
    def __init__(self, book_isbn, user_id, action):
        self.book_isbn = book_isbn
        self.user_id = user_id
        self.action = action  # 'issue' or 'return'
        self.date = datetime.now()
        self.due_date = None
        if action == 'issue':
            self.due_date = self.date + timedelta(days=14)  # 2 weeks due date

    def to_dict(self):
        return {
            'book_isbn': self.book_isbn,
            'user_id': self.user_id,
            'action': self.action,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S'),
            'due_date': self.due_date.strftime('%Y-%m-%d %H:%M:%S') if self.due_date else None
        }

class Library:
    BOOKS_FILE = 'books.json'
    TRANSACTIONS_FILE = 'transactions.json'
    
    def __init__(self):
        self.books = []
        self.transactions = []
        self._load_data()
    
    def _load_data(self):
        try:
            # Load books
            
            if os.path.exists(self.BOOKS_FILE):
                with open(self.BOOKS_FILE, 'r') as f:
                    books_data = json.load(f)
                    self.books = [Book(**data) for data in books_data]
            
            # Load transactions
            
            if os.path.exists(self.TRANSACTIONS_FILE):
                with open(self.TRANSACTIONS_FILE, 'r') as f:
                    transactions_data = json.load(f)
                    self.transactions = [Transaction(
                        data['book_isbn'], 
                        data['user_id'], 
                        data['action']
                    ) for data in transactions_data]
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self):
        try:
            # Save books
            
            with open(self.BOOKS_FILE, 'w') as f:
                json.dump([book.to_dict() for book in self.books], f, indent=2)
            
            # Save transactions
            
            with open(self.TRANSACTIONS_FILE, 'w') as f:
                json.dump([t.to_dict() for t in self.transactions], f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_book(self, isbn, title, author, quantity):
        for book in self.books:
            if book.isbn == isbn:
                book.quantity += quantity
                break
        else:
            self.books.append(Book(isbn, title, author, quantity))
        self._save_data()
    
    def issue_book(self, isbn, user_id):
        for book in self.books:
            if book.isbn == isbn and book.quantity > 0:
                book.quantity -= 1
                transaction = Transaction(isbn, user_id, 'issue')
                self.transactions.append(transaction)
                self._save_data()
                return transaction.due_date
        return None
    
    def return_book(self, isbn, user_id):
        for book in self.books:
            if book.isbn == isbn:
                book.quantity += 1
                transaction = Transaction(isbn, user_id, 'return')
                self.transactions.append(transaction)
                self._save_data()
                return True
        return False
    
    def search_book(self, search_term):
        results = []
        search_term = search_term.lower()
        for book in self.books:
            if (search_term in book.isbn.lower() or 
                search_term in book.title.lower() or 
                search_term in book.author.lower()):
                results.append(book)
        return results
    
    def get_book_status(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                issued_count = sum(
                    1 for t in self.transactions 
                    if t.book_isbn == isbn and t.action == 'issue' and (
                        not any(
                            rt.book_isbn == isbn and rt.action == 'return' 
                            for rt in self.transactions 
                            if rt.date > t.date
                        )
                    )
                )
                return {
                    'total': book.quantity + issued_count,
                    'available': book.quantity,
                    'issued': issued_count
                }
        return None

def display_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Check Book Status")
    print("6. Exit")

def main():
    library = Library()
    
    # Add some sample books if the database is empty
    
    if not library.books:
        library.add_book("978-3-16-148410-0", "Python Programming", "John Smith", 5)
        library.add_book("978-1-23-456789-0", "Advanced Python", "Jane Doe", 3)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            try:
                isbn = input("Enter ISBN: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                quantity = int(input("Enter Quantity: "))
                library.add_book(isbn, title, author, quantity)
                print("Book added successfully!")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        
        elif choice == '2':
            isbn = input("Enter ISBN of book to issue: ")
            user_id = input("Enter your User ID: ")
            due_date = library.issue_book(isbn, user_id)
            if due_date:
                print(f"Book issued successfully! Due date: {due_date.strftime('%Y-%m-%d')}")
            else:
                print("Book not available or invalid ISBN.")
        
        elif choice == '3':
            isbn = input("Enter ISBN of book to return: ")
            user_id = input("Enter your User ID: ")
            if library.return_book(isbn, user_id):
                print("Book returned successfully!")
            else:
                print("Invalid ISBN or user ID.")
        
        elif choice == '4':
            search_term = input("Enter search term (ISBN, Title, or Author): ")
            results = library.search_book(search_term)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"ISBN: {book.isbn}, Title: {book.title}, "
                          f"Author: {book.author}, Available: {book.quantity}")
            else:
                print("No books found matching your search.")
        
        elif choice == '5':
            isbn = input("Enter ISBN to check status: ")
            status = library.get_book_status(isbn)
            if status:
                print(f"\nBook Status:")
                print(f"Total Copies: {status['total']}")
                print(f"Available: {status['available']}")
                print(f"Issued: {status['issued']}")
            else:
                print("Book not found.")
        
        elif choice == '6':
            print("Exiting Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
