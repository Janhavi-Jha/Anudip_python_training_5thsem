'''sales = {     "Laptop": 15,     "Mouse": 45,     "Keyboard": 32,     "Monitor": 12,     "Headphones": 28,     "Printer": 8,     "Webcam": 20,     "Speaker": 18,     "Tablet": 10,     "Router": 25 } Tasks 1. Display products sold more than 20 times.  2. Find the best-selling product.  3. Find the least-selling product.  4. Calculate total products sold.  5. Create a list of products requiring promotion (sales < 15).  6. Count products having sales between 10 and 30.  '''
sales = {     "Laptop": 15,     "Mouse": 45,     "Keyboard": 32,     "Monitor": 12,     "Headphones": 28,     "Printer": 8,     "Webcam": 20,     "Speaker": 18,     "Tablet": 10,     "Router": 25 } 
#display products sold more than 20 times 
products=list(sales.items())
name=products[0][0]
sale=products[0][1]
for item in sales.items():
    if item[1]>20:
        print(item)
#finding the best selling product
for item in sales.items():
    if item[1]>sale:
        name=item[0]
        sale=item[1]
print("Highest purchase is:",name)
#finding the least selling product
for item in sales.items():
    if item[1]<sale:
        name=item[0]
        sale=item[1]
print("Least selling product is :",name)
#calculate total product sold
total=0
for item in sales.items():
    total+=item[1]
print("Total product sold= ",total)
#create a list of products requiring promotion
for item in sales.items():
    if item[1]<15:
       print("Improvement required for ",item)
#count products having sales between 10 and 30
count=0
for item in sales.items():
    if item[1]>10 and item[1]<30:
        count+=1
print("the products having sale between 10 and 30 are :",count)

