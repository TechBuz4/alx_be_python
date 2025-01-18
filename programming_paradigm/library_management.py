class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
    def check_out_book(self, title):
        self._is_checked_out = True
        print(f"You have checked out {title}")

    def return_book(self):
        self._is_checked_out = False
        print(f"You have returned {title}")

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out:
                book.check_out_book(title)
                return
            else:
                print(f"Sorry, {title} is not available.")
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book(title)
                return
            else:
                print(f"Sorry, {title} was not checked out or does not exist.")
    def list_available_books(self):
        available_books = [book.title for book in self._books if not book.is_available()]
        print("Available Books:")
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
            print(f"{book.title} by {book.author}")

