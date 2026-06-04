#Input transaction amounts continuously. Stop when -1 is entered. Count: • Transactions above ₹50,000  • Transactions below ₹1,000  • Total transaction amount  
#taking input from the user
transaction_amounts = []
while True:
    amount = float(input("Enter a transaction amount (or -1 to stop): "))
    if amount == -1:
        break
    transaction_amounts.append(amount)
#initializing counters
above_50000 = 0
below_1000 = 0
total_amount = 0
#counting the transactions
for amount in transaction_amounts:
    total_amount += amount
    if amount > 50000:
        above_50000 += 1
    elif amount < 1000:
        below_1000 += 1
#displaying the results
print(f"Number of transactions above ₹50,000: {above_50000}")
print(f"Number of transactions below ₹1,000: {below_1000}")
print(f"Total transaction amount: ₹{total_amount:.2f}")
