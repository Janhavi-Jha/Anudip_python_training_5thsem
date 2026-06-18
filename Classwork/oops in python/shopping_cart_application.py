'''Create a Product class containing product name, quantity, and price per unit.
Implement methods to:
• Calculate total price.
• Update quantity.
• Display product details.'''
#creating a product class
class Product:
    #defining a constructor
    def __init__(self,name,qty,price):
        self.__name=name
        self.__qty=qty
        self.__price=price
    #Method to calculate total price 
    def total_price(self):
        total = self.__qty * self.__price
        print("The total price is", total)
    #Method to update quantity 
    def updated_qty(self):
        self.__qty = int(input("Enter new quantity: "))
        print("Quantity updated successfully.")
    #Method to display product details
    def display_Details(self):
        print("Product Name = ",self.__name)
        print("Product Quantity=",self.__qty)
        print("Product Price=",self.__price)
#Taking user input
name=input("Enter the Product Name=")
qty=int(input("Enter the product quantity="))
#validating the input
if qty<0:
    print("Product can't be negative in quantity")
price=float(input("Enter the product price="))
#validating the input
if price<0:
    print("Invalid Input!")
#creating an object
prdct=Product(name,qty,price)
#displaying Product details
prdct.display_Details()
#Updated quantity
prdct.updated_qty()
#total price
prdct.total_price()

  

         