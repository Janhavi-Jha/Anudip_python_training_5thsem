#check if three angles form a triangle...if yes then find the type of triangle
angle1=int(input("Enter the first angle :"))
#validate angle 1
if angle1<=0:
    exit("Angle cannot be negative or zero")
#-------------------------------------------------------
angle2=int(input("Enter the second angle :"))
#validate angle 2   
if angle2<=0:
    exit("Angle cannot be negative or zero")
#-------------------------------------------------------
angle3=int(input("Enter the third angle :"))
#validate angle 3
if angle3<=0:
    exit("Angle cannot be negative or zero")
#-------------------------------------------------------
#verifying angle formation
if angle1+angle2+angle3==180:
    #print("The angles form a triangle")
    #acute triangle
    if angle1<90 and angle2<90 and angle3<90:
        print("The triangle is an acute triangle")
    #right triangle
    elif angle1==90 or angle2==90 or angle3==90:
        print("The triangle is a right triangle")
    #obtuse triangle
    else:
        print("The triangle is an obtuse triangle")
else:
    print("The angles do not form a triangle")
    