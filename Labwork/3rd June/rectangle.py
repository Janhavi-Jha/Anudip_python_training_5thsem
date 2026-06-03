#calculate area and perimeter of rectangle and validate the input
length=int(input("Enter the length of the rectangle (in cm):"))
if length<0:
    exit("Length cannot be negative")
breadth=int(input("Enter the breadth of the rectangle (in cm):"))
if  breadth<0:
    exit("breadth cannot be negative")
#calculating area and perimeter
area=length*breadth
perimeter=2*(length+breadth)
print("Area of the rectangle is:",area,"sq.cm")
print("Perimeter of the rectangle is:",perimeter,"cm")  
