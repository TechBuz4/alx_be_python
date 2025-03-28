# library_system.py

# Base Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"  

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition: Library
class Library:
    def __init__(self):
        self.books = []  # A list to store instances of Book, EBook, and PrintBook

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Only instances of Book or its subclasses can be added to the library.")

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)
