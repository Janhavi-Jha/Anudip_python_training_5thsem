#Calculate electricity bill using slabs: 0-100 units      -> ₹5/unit 101-200 units    -> ₹7/unit Above 200 units  -> ₹10/unit Additionally: • Add 10% surcharge if bill exceeds ₹5000.  Display final payable amount. 
#taking input from the user
units = int(input("Enter the number of units consumed: "))
#calculating the bill based on slabs
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
#adding surcharge if bill exceeds ₹5000
if bill > 5000:
    bill += bill * 0.10
#displaying the final payable amount
print(f"The final payable amount is: ₹{bill:.2f}")
