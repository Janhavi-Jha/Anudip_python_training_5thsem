#A customer's transactions are stored as:
#transactions = [5000, -2000, 3000, -1000, -500, 7000]
#Positive values represent deposits and negative values represent withdrawals.
#Write a program to:
#1. Calculate the current balance.
#2. Count total deposits and withdrawals.
#3. Find the largest deposit and largest withdrawal.
#4. Create separate lists for deposits and withdrawals.
#Expected Output
#Current Balance: 11500
#Deposits: [5000, 3000, 7000]
#Withdrawals: [-2000, -1000, -500]
#Largest Deposit: 7000
#Largest Withdrawal: -2000
transactions=[5000,-2000,3000,-1000,-500,7000]
current_balance=0
deposits=[]
withdrawals=[]
largestdeposits=0
largestwithdrawals=0
#checking for the current balance
for i in transactions:
    current_balance+=i
    #checking deposit amount 
    if i>0:
        deposits.append(i)
        #checking withdrawal amount 
    else:
        withdrawals.append(i)
#maximum of deposits 
largestdeposits= max(deposits)
#minimum of deposits 
largestwithdrawals= min(withdrawals)
#printing the result to show desired output 
print("Current balance=",current_balance)
print("deposit=",deposits)
print("Withdrawal=",withdrawals)
print("Largest withdrawal=",largestwithdrawals)
print("Largest deposit=",largestdeposits)


