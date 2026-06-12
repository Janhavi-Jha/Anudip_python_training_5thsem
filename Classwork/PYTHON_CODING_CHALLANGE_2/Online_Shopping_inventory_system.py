'''An online store maintains stock quantities of products.
Sample Data
inventory = {
 "Laptop": 15,
 "Mouse": 45,
 "Keyboard": 32,
 "Monitor": 12,
 "Headphones": 28,
 "Printer": 8,
 "Webcam": 20,
 "Speaker": 18,
 "Tablet": 10,
 "Router": 25
}
Tasks
1. Display products with stock below 15 units.
2. Find the product with maximum stock.
3. Find the product with minimum stock.
4. Calculate total stock available.
5. Create a list of products requiring restocking (<10 units). '''
inventory = {
 "Laptop": 15,
 "Mouse": 45,
 "Keyboard": 32,
 "Monitor": 12,
 "Headphones": 28,
 "Printer": 8,
 "Webcam": 20,
 "Speaker": 18,
 "Tablet": 10,
 "Router": 25
}
#display product with stock below 15 units
print("Product with stock below 15 units are=")
for i in inventory.items():
    if i[1] <15:
        print(i[0]) 
#finding the product with maximum stock
max=0
product=" "
for i in inventory.items():
    if i[1]>max:
        max=i[1]
        product=i[0]
print("The product with maximum stock is",product,"with",max,"units")
#finding the product with minimum stock
min=15
prdct=" "
for i in inventory.items():
    if i[1]<min:
        min=i[1]
        prdct=i[0]
print("The product with minimum stock is",prdct,"with",min,"units")
#calculate total stock available
total=0
for i in inventory.items():
    total+=i[1]
print("Total stock=",total)
#product requiring restocking
restock=[]
for i in inventory.items():
    if i[1]<10:
      restock.append(i[0])
print("Products requiring restocking are",restock)