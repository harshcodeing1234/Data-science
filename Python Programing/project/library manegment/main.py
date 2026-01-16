# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.book = []
                   
    def add_book(self,book):
        self.book.append(book)
        
        with open("Aiit_lib.txt", "w")as f:
            f.write("Welcome to Aiit Library:\n\nTotal books: ")
            f.write(str(self.book))
        print(f"book : '{book}' are succesfull added in library")

    def remove_book(self,book):
        if book in self.book:
            self.book.remove(book)
            with open("Aiit_lib.txt", "w")as f:
                f.write("Welcome to Aiit Library:\n\nTotal books: ")
                f.write(str(self.book))
            print(f"Book : '{book}' removed successfully")
        else:
            print(f"Book: '{book}' are not found")

    def display_book(self):
        if self.book:
            print(f"books in library:")
            for idx,book in enumerate(self.book, 1):
                print(f"{idx}. {book}")
            count = len(self.book)
            print(f"Total {count} books in library")
        else:
            print("No books avilable in library")

        
Aiit_Lib = Library()
Aiit_Lib.add_book("C programing")
Aiit_Lib.add_book("Fundamental of computer")
Aiit_Lib.add_book("French language")
Aiit_Lib.add_book("Communication skills")
Aiit_Lib.add_book("Envoirment Science")
Aiit_Lib.add_book("Digital circut design")
Aiit_Lib.add_book("Descreat mathmatics")
Aiit_Lib.remove_book("Biology")
Aiit_Lib.remove_book("French language")
Aiit_Lib.display_book()


