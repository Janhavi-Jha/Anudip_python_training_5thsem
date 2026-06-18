'''Create a Book class with attributes:
• Book ID
• Title
• Author
• Availability Status
Implement methods to:
• Issue a book.
• Return a book.
• Display book details.
Prevent issuing a book that is already issued.'''
# Creating a class
class Book:

    # Constructor
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    # Method to issue a book
    def issue_book(self):
        if self.__availability:
            self.__availability = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    # Method to return a book
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print("Book returned successfully.")
        else:
            print("Book is already available in the library.")

    # Method to display details
    def display_details(self):
        status = "Available" if self.__availability else "Issued"

        print("\nBook Details")
        print("Book ID:", self.__book_id)
        print("Title:", self.__title)
        print("Author:", self.__author)
        print("Status:", status)


# Creating an object
book1 = Book(101, "Python Programming", "Guido van Rossum")

# Display details
book1.display_details()

# Issue book
book1.issue_book()

# Try issuing again
book1.issue_book()

# Return book
book1.return_book()

# Display updated details
book1.display_details()
#Taking user input

