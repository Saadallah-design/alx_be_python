# Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.


# the Book class represents a book in the library | OBJECT
class Book: 
    """ A class representing a book in the library. """
    """ Class: A blueprint or template (e.g., the idea of a "Book")."""

    # IMPLEMENTING THE CONSTRUCTOR __init__ METHOD to accept title and author parameters
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # private atribute _is_checked_out to track if the book is checked out
        # private attributes are not meant to be accessed directly from outside the class
        # by convention, we prefix private attributes with an underscore (_)
        self._is_checked_out = False
    
    # adding two methods to the Book class to check out and return a book
    def check_out(self):
        """ Method to check out the book. """
        if self._is_checked_out == False:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Book was already checked out
    
    def return_book(self):
        """ Method to return the book. """
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Book was not checked out

    
# Library class structure: Container for Book objects and methods to manage them
class Library:
    """ A class representing a library that manages a collection of books. """
    # initialize a library with an empty list of books
    def __init__(self):
        self._books = []  # List to store Book objects

    # Method to add a book to the library
    def add_book(self, book):
        # here we simply append the book object to the list of books
        # we assume that the book parameter is an instance of the Book class
        # we don't perform type checking here for simplicity
        self._books.append(book)

    # list available books
    def list_available_books(self):
        # here we need to iterate through the list of books
        # and print the details of each book that is not checked out
        for book in self._books:
            if book._is_checked_out == False:
                print(f"Title: {book.title}, Author: {book.author}")

    # check_out_book and return book methods
    def check_out_book(self, title):
        # here we need to find the book by title
        # therefore, we need to iterate through the list of books 
        for book in self._books:
            if book.title == title and book._is_checked_out == False:
                book._is_checked_out = True
                return True  # Successfully checked out
        return False  # Book not found or already checked out

    # Method to return a book to the library
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out == True:
                book._is_checked_out = False
                return True  # Successfully returned
        return False  # Book not found or wasn't checked out
    


# Example usage:
# if __name__ == "__main__":
#     # Create a library instance
#     library = Library()

#     # Create some book instances
#     book1 = Book("1984", "George Orwell")
#     book2 = Book("To Kill a Mockingbird", "Harper Lee")
#     book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

#     # Add books to the library
#     library.add_book(book1)
#     library.add_book(book2)
#     library.add_book(book3)

#     # List available books
#     print("Available books:")
#     library.list_available_books()

#     # Check out a book
#     if library.check_out_book("1984"):
#         print("\nChecked out '1984'.")

#     # List available books after checking out one
#     print("\nAvailable books after checking out '1984':")
#     library.list_available_books()

#     # Return the book
#     if library.return_book("1984"):
#         print("\nReturned '1984'.")

#     # List available books after returning one
#     print("\nAvailable books after returning '1984':")
#     library.list_available_books()