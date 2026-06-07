'''Books available in a library:
books = [
 ("Python Basics", 5),
 ("Data Science", 0),
 ("Java Programming", 3),
 ("Machine Learning", 0)
]
Write a program to:
• Display unavailable books.
• Find all books with more than 2 copies.
• Count available books.
• Stop searching once a requested book is found. '''
#displaying unavailable books 
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

for name, copies in books:
    if copies == 0:
        print(name)
#find all books with more than 2 copies 
for name, copies in books:
    if copies > 2:
        print(name, copies)
#count available books
count = 0

for name, copies in books:
    if copies > 0:
        count += 1

print("Available books:", count)
#stop searching once book requested 
requested_book = "Java Programming"

for name, copies in books:
    if name == requested_book:
        print("Book found:", name)
        break