#e-commerce analysis 
'''An online store records orders as:
orders = [
 ("Laptop", 55000),
 ("Mouse", 800),
 ("Keyboard", 1500),
 ("Monitor", 12000),
 ("Pen Drive", 600)
]
Write a program to:
• Display all products costing more than ₹1000.
• Find the most expensive product.
• Calculate the total order value.
• Count products costing below ₹1000''' 
#---------------------------------------------------------------------------------
orders = [
 ("Laptop", 55000),
 ("Mouse", 800),
 ("Keyboard", 1500),
 ("Monitor", 12000),
 ("Pen Drive", 600)
]
#displaying all products costing more than 1000
for i in orders:
    if i[1]>1000:
        print(i[0])
#finding the most expensive product
highest =orders[1]
for i in orders:
    if i[1]>highest[1]:
        highest=i
        print("highest product=",highest)
#Task 3:Total order value 
total = 0

for i in orders:
    total += i[1]

print("Total Order Value:", total)
#counting products below 1000
count=0
for i in orders:
    if i[1]<1000:
        count+=1
print("order less than 1000=",count)
