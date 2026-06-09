#module to create functions to calculate area and perimeter of circle,square,rectangle
#function to create perimeter of square
def square_perimeter(side):
    #calculating perimeter
    perimeter=4*side
    #returning the calculated perimeter
    return perimeter
#----------------------------------------------------
#Function for calculating area of square
def square_area(side):
    #calculating area
    area=side**2
    #returning the calculated area
    return area
#Function to calculate perimeter of rectangle
def rectangle_perimeter(length,breadth):
    #calculating perimeter
    perimeter=2*(length+breadth)
    #returning the calculated perimeter
    return perimeter
#------------------------------------------------
#Function to calculate area of rectangle
def rectangle_area(length,breadth):
    #calculating area
    area=length*breadth
    #returning the calculated area
    return area
#Function to calculate perimeter of circle
def circle_perimeter(radius):
    #calculating perimeter
    perimeter=2*(3.14*radius)
    #returning calculated perimter
    return perimeter
#function to calculate area of circle 
def circle_area(radius):
    #calculating area
    area=3.14*(radius**2)
    #calculating value returning
    return area
