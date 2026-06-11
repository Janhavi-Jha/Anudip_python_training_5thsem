try:
    #taking input of all the 3 sides
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))
#ensuring no negative sides are given as input
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Triangle sides must be greater than zero.")
#validating the triangle is possible to be formed 
    elif a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle.")
except ValueError:
    print("Please enter numeric values only.")
#using Heron's formula to find the area
else:
        s = (a + b + c) / 2
        area =(s * (s - a) * (s - b) * (s - c))**0.5
        print("Area of triangle =", area)

finally:
    print("Triangle area calculation process completed.")