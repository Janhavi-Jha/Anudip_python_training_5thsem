'''books = {
 "Python": 5,
 "Java": 2,
 "DBMS": 4,
 "Networking": 1,
 "OS": 3,
 "AI": 6,
 "ML": 2,
 "Cloud": 5,
 "Cyber Security": 1,
 "Web Development": 4
}
Tasks
1. Display books with fewer than 3 copies.
2. Find the book with maximum copies.
3. Find the book with minimum copies.
4. Count total books available.
5. Generate a restocking list. '''
books = {
 "Python": 5,
 "Java": 2,
 "DBMS": 4,
 "Networking": 1,
 "OS": 3,
 "AI": 6,
 "ML": 2,
 "Cloud": 5,
 "Cyber Security": 1,
 "Web Development": 4
}
#displaying book with fewer than 3 copies
print("Books with less than 3 copies are:")
for i in books.items():
    if i[1]<3:
        print(i[0])
#find the book with maximum copies
max=0
name=" "
for i in books.items():
    if i[1]>max:
        max=i[1]
        name=i[0]
print("The  book with maximum copies is ",name)
#find the minimum copies
min=5
book=" "
for i in books.items():
    if i[1]<min:
        min=i[1]
        book=i[0]
print("The book with minimum copies is ",book)
#total book count
total=0
for i in books.items():
    total+=i[1]
print("Total book count available=",total)
#generating a restocking list 
restock=[]
for i in books.items():
    if i[1]<3:
        restock.append(i[0])
print("Restock =",restock)
