'''Create a python program which provides the menu to the user to select the 2D figures(circle,square,rectangle)
After selecting figure user is again asked to provide the input of corresponding data for the figure.After 
input of corresponding data for again provide a menu to select the operation (area/perimeter)and as per the
data provided by the user,display the result of the operation.This task will be repeated again and again
until the user selects the option to exit from that figure.'''
#importing the file
from figuresmodule import *
#taking input for figures
while True:
 figures = int(input("Enter your desired shape=\n1.Rectangle\n2.Square\n3.Circle\n4.Exit"))
 if figures>4:
    print("Invalid Input")
    break
 if figures==4:
    exit("Program ended")
 #taking input for operation
 operation = int(input("Enter operation:\n1.Area\n2.Perimeter\n"))
 #performing operation for rectangle
 if figures == 1:
    #taking data input
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    #area calculation
    if operation == 1:
        area = rectangle_area(length, breadth)
        print("Area =", area)
        #perimeter calculation
    elif operation == 2:
        perimeter = rectangle_perimeter(length, breadth)
        print("Perimeter =", perimeter)
 #performing operation for square
 elif figures == 2:
    #taking data input
    side = float(input("Enter side: "))
 #area calculation
    if operation == 1:
        area = square_area(side)
        print("Area =", area)
 #perimeter calculation
    elif operation == 2:
        perimeter = square_perimeter(side)
        print("Perimeter =", perimeter)
#performing operation on circle
 elif figures == 3:
    #data inpput
    radius = float(input("Enter radius: "))
#area calculation
    if operation == 1:
        area = circle_area(radius)
        print("Area =", area)
#perimeter calculation
    elif operation == 2:
        perimeter = circle_perimeter(radius)
        print("Perimeter =", perimeter)
