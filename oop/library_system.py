class Book:
    def __init__(self, title, author):
        self.title = title.__str__()
        self.author = author.__str__()


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            class_name = book.__class__.__name__
            match class_name:
                case "Book":
                    print(f"{class_name}: {book.title} by {book.author}")
                
                case "EBook":
                    print(f"{class_name}: {book.title} by {book.author}, File Size: {book.file_size}KB")
                
                case "PrintBook":
                    print(f"{class_name}: {book.title} by {book.author}, Page Count: {book.page_count}")

                case _:
                    print(f"Unsupported book type")