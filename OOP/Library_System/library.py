class Library:

    def __init__(self, name):
        self._name = name
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def search_books_by_author(self, author):
        for book in self._books:
            if book.author == author:
                self.show_book(book)

    def search_books_by_gender(self, gender):
        for book in self._books:
            if book.gender == gender:
                self.show_book(book)

    def show_all_books(self):
        print(f"All the books in the library: {self._name}:")
        for book in self.books:
            self.show_book(book)

    
    def show_book(self, book):
        print(f"Book - Title: {book.title}, Author: {book.author}, Gender: {book.gender}")


    @property
    def name(self):
        return self._name
    
    @property
    def books(self):
        return self._books
    
