#creating a class to perform operations on a rectangle
class Rectangle:
    #defining a constructor
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    #Method to calculate area
    def area_rectangle(self):

        area=self.__length*self.__breadth
        print("The area of rectangle is=",area)
    def perimeter_rectangle(self):
        perimeter=2*(self.__length+self.__breadth)
        print("The perimeter of rectangle is=",perimeter)
#----------------------------------------------------------------
#Asking the user to input length and breadth
length=float(input("Enter the length of rectangle"))
#validating the length
if length <=0:
    print("Length can't be negative or zero")
breadth=float(input("Enter the breadth of rectangle"))
#validating the breadth
if breadth<=0:
    print("Breadth can't be negative or zero")
#creating object of rectangle 
rectangle=Rectangle(length,breadth)
#menu driven program for rectangle
while True:
    print("---------------Rectangle opertaions----------------------")
    print("1.Calculate perimeter")
    print("2.Calculate Area")
    print("3.Exit")
    choice=int(input("Select operation:"))
    if choice==1:
        rectangle.perimeter_rectangle()
    elif choice==2:
        rectangle.area_rectangle()
    elif choice==3:
        print("Thankyou!")
    else:
        print("Invalid Input")

    #Ask the user if they want to perform another operation
    another_operation=input("Do you want to perform another operation? (yes/no): ")
    if another_operation.lower()!="yes":
        print("Thank you for using our services!")
        break
    print("\n----------------------------------")




