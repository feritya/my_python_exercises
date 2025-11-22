class Book:
    def __init__(self,tittle,author,pages):
        self.title = tittle
        self.author = author
        self.pages = pages


class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        name=input("Enter the name of the book to add: ")
        author=input("Enter the author of the book: ")
        pages=int(input("Enter the number of pages: "))
        new_book = Book(name, author, pages)
        self.books.append(new_book)
        print(f'Book "{name}" by {author} added to the library.')
    
    def display_book(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author}, Pages: {book.pages}')
    def remove_book(self):
        name=input("Enter the name of the book to remove: ")
        for book in self.books:
            if book.title == name:
                self.books.remove(book)
                print(f'Book "{name}" removed from the library.')
                return
        print(f'Book "{name}" not found in the library.')
    def search_book(self):
        serch_title=input("Enter the title of the book to search: ")
        for book in self.books:
            if book.title == serch_title:
                print(f'Found Book - Title: {book.title}, Author: {book.author}, Pages: {book.pages}')
                return
        print(f'Book "{serch_title}" not found in the library.')


library = Library()
print("Welcome to the Library System please choose an option :")
choice = int(input("Your choice: "))
while (True):
    print("1- Add Book\n2- Display Books\n3- Remove Book\n4- Search Book\n5- Exit")
    choice = int(input("Your choice: "))
    if  choice == 1:
        library.add_book(Book)
    elif choice == 2:
        library.display_book()
    elif choice == 3:
        library.remove_book()
    elif choice == 4:
        library.search_book()
    elif choice == 5:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")