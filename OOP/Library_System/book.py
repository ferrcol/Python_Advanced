class Book:
    def __init__(self, title, author, gender):
        self._title = title
        self._author = author
        self._gender = gender

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def gender(self):
        return self._gender
    
if __name__ == "__main__":
    book = Book("title", "author", "gender")
    print(f"Access title property: {book.title}")