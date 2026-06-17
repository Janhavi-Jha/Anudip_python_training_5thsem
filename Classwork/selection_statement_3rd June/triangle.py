print("-----------------triangle-----------------")
#taking input from the user of the three sides
side1=int(input("Enter the first side (in cm ):"))
side2=int(input("Enter the second side (in cm ):"))
side3=int(input("Enter the third side (in cm ):"))
#calculating perimeter
perimeter=side1+side2+side3
#using Heron's formula
s=perimeter/2
area=(s*(s-side1)*(s-side2)*(s-side3)**0.5,"sq.cm")
#print statement
print("Permiter :",perimeter,"cm")

