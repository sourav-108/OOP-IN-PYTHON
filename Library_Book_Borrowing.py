class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def borrow(self):
        if not self.available:
            return "Already borrowed"
        self.available = False
        return "Borrowed"

    def return_book(self):
        self.available = True


book = Book("Python Basics")
print(book.borrow())  # Borrowed
print(book.borrow())  # Already borrowed