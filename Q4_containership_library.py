
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, book):
        self.book = book

    def show(self):
        print("Title:", self.book.title)
        print("Author:", self.book.author)

b = Book("Python", "Guido")
l = Library(b)
l.show()
