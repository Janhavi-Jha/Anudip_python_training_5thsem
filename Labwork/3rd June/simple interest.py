#calculating simple interest of a program and validating the input
principal=int(input("Enter the principal amount:"))
if principal<0:
    exit("Principal amount cannot be negative")
rate=float(input("Enter the rate of interest:"))
if rate<0:
    exit("Rate of interest cannot be negative")
time=int(input("Enter the time in years:"))
if time<0:
    exit("Time cannot be negative")

#calculating simple interest
simple_interest=(principal*rate*time)/100
print("The simple interest is:",simple_interest)