'''books = {     "Python Basics": 5,     "Data Structures": 0,     "Machine Learning": 3,     "Java Programming": 2,     "DBMS": 0,     "Operating Systems": 6,     "Networking": 4,     "Cloud Computing": 1,     "Cyber Security": 0,     "Web Development": 7 } Tasks • Display books that are currently unavailable.  • Count the number of available books.  • Find the book with the maximum copies.  • Create a list of books having less than 3 copies.  • Calculate the total number of books available.  '''
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}
#unavailable books
print("Unavailable books:")

for book, copies in books.items():
    if copies == 0:
        print(book)
