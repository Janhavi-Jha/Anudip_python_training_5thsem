#calculating simple interest of a program and validating the input
principal=int(input("Enter the principal amount:"))
rate=float(input("Enter the rate of interest:"))
time=int(input("Enter the time in years:"))
#validating the input
if principal<0 or rate<0 or time<0:
    exit("Principal, rate and time cannot be negative")

#calculating simple interest
simple_interest=(principal*rate*time)/100
print("The simple interest is:",simple_interest)