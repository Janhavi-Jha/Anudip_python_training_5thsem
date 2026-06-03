# verify whether the given three sides can form a triangle or not
side1=int(input("Enter the first side :"))
#validate side 1
if side1<=0:
    exit("Side cannot be negative or zero")
#-------------------------------------------------------
side2=int(input("Enter the second side :")) 
#validate side 2
if side2<=0:
    exit("Side cannot be negative or zero")
#-------------------------------------------------------
side3=int(input("Enter the third side :"))
#validate side 3
if side3<=0:
    exit("Side cannot be negative or zero")
#-------------------------------------------------------
#verifying triangle formation
if (side1+side2>side3) and (side2+side3>side1) and (side1+side3>side2):
    print("The sides form a triangle")
else:
    print("The sides do not form a triangle")
    