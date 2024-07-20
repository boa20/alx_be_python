class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []
        self.book = Book(title="any", author="any")

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        self.title = title
        for book in self._books:
            if book.title == title:
                #book._is_checked_out()
                self.book = book
                self._books.remove(book)
        

    def return_book(self, title):
        self.title = title
        if self.book.title == title:
            self._books.append(self.book)

    def list_available_books(self):
        for book in self._books:
            print(f"{book.title} by {book.author}")
        
    
