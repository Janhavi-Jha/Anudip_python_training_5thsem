#Determine whether a point (x, y) lies in:
#Quadrant I, II, III, IV
#On X-axis
#On Y-axis
#At Origin
#-----------------------------------------------------------------
#Quadrant
x=float(input("Enter the value of x: "))
y=float(input("Enter the value of y: "))
if x>0 and y>0:
    print("The point (",x,",",y,") lies in Quadrant I")
elif x<0 and y>0:
    print("The point (",x,",",y,") lies in Quadrant II")
elif x<0 and y<0:
    print("The point (",x,",",y,") lies in Quadrant III")
elif x>0 and y<0:
    print("The point (",x,",",y,") lies in Quadrant IV")
#On X-axis
if y==0 and x!=0:
    print("The point (",x,",",y,") lies on the X-axis")
#On Y-axis
if x==0 and y!=0:
    print("The point (",x,",",y,") lies on the Y-axis")
#At Origin
if x==0 and y==0:
    print("The point (",x,",",y,") lies at the Origin") 