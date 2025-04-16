from library import Library
from book import Book

#Creating a library object
librarySchool = Library("School Library")

#Create books
book1 = Book("The Hobbit", "J. R. R. Tolkien", "Fantasy")
book2 = Book("PHarry Potter", "J. K. Rowling", "Fantasy")
book3 = Book("The Diary of Anne Frank", "Anne Frank", "Autobiography")
book4 = Book("The Da Vinci Code", "Dan Brown", "Mystery")
book5 = Book("Don Quixote", "Miguel de Cervantes", "Novel")

#Add books to the library
librarySchool.add_book(book1)
librarySchool.add_book(book2)
librarySchool.add_book(book3)
librarySchool.add_book(book4)
librarySchool.add_book(book5)

# Library name
print(f"Welcome to {librarySchool.name}")

#Books at the library:
print(f"\nBooks in {librarySchool.name}: ")
librarySchool.show_all_books()

# Search books for gender Fantasy
print(f"\nFantasy books: ")
librarySchool.search_books_by_gender("fantasy")

# Search Dan Brown books:
print(f"\nDan Brown books: ")
librarySchool.search_books_by_author("dan brown")
