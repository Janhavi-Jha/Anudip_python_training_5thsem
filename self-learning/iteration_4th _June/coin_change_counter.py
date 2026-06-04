#Problem Statement: Given an amount, determine the minimum number of notes required using: ₹500, ₹200, ₹100, ₹50, ₹20, ₹10 Example: Input: 880 200 x 1 100 x 1 50 x 1 20 x 1 10 x 1 
#taking input from the user
amount = int(input("Enter the amount: "))
#defining the denominations
denominations = [500, 200, 100, 50, 20, 10]
#initializing a dictionary to store the count of each denomination
note_count = {}
#calculating the minimum number of notes required
for denomination in denominations:
    count = amount // denomination
    if count > 0:
        note_count[denomination] = count
        amount -= denomination * count
#displaying the result
for denomination, count in note_count.items():
    print(f"{denomination} x {count}")

        