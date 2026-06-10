'''5. Daily Expense Tracker and Report Generator 
Problem Statement 
Daily expenses are recorded in expenses.txt. 
File Format 
Food,450 
Travel,300 
Shopping,1200 
Electricity,850 
Internet,700 
Entertainment,600 
Medicine,400 
Education,1500 
Fuel,900 
Miscellaneous,250 
Requirements 
Develop a program to: 
1. Display all expenses.  
2. Calculate total expenditure.  
3. Find the category with highest and lowest spending.  
4. Display expenses greater than ₹800.  
5. Add a new expense category.  
6. Update an existing expense amount.  
7. Generate a summary report in report.txt containing:  
o Total Expenses  
o Highest Expense Category  
o Lowest Expense Category  
o Categories spending more than ₹800  '''
# Function to display all expenses
def display_expenses():

    file = open("expenses.txt", "r")

    print("Expenses List:")

    for line in file:
        print(line.strip())

    file.close()


# Function to calculate total expenditure
def total_expenses():

    file = open("expenses.txt", "r")

    total = 0

    for line in file:
        category, amount = line.strip().split(",")
        total += int(amount)

    file.close()

    return total


# Function to find highest and lowest expense category
def highest_lowest_expense():

    file = open("expenses.txt", "r")

    highest_category = ""
    lowest_category = ""

    highest_amount = 0
    lowest_amount = 999999

    for line in file:

        category, amount = line.strip().split(",")
        amount = int(amount)

        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

        if amount < lowest_amount:
            lowest_amount = amount
            lowest_category = category

    file.close()

    print("Highest Expense Category =", highest_category, highest_amount)
    print("Lowest Expense Category =", lowest_category, lowest_amount)


# Function to display expenses greater than 800
def expenses_above_800():

    file = open("expenses.txt", "r")

    print("Expenses Greater Than 800:")

    for line in file:

        category, amount = line.strip().split(",")
        amount = int(amount)

        if amount > 800:
            print(category, amount)

    file.close()


# Function to add a new expense
def add_expense():

    category = input("Enter new category: ")
    amount = input("Enter amount: ")

    file = open("expenses.txt", "a")

    file.write("\n" + category + "," + amount)

    file.close()

    print("Expense Added Successfully")


# Function to update an expense amount
def update_expense():

    category_name = input("Enter category to update: ")

    file = open("expenses.txt", "r")

    data = file.readlines()

    file.close()

    file = open("expenses.txt", "w")

    for line in data:

        category, amount = line.strip().split(",")

        if category == category_name:
            new_amount = input("Enter new amount: ")
            file.write(category + "," + new_amount + "\n")

        else:
            file.write(line)

    file.close()

    print("Expense Updated Successfully")


# Function to generate report
def generate_report():

    file = open("expenses.txt", "r")

    total = 0

    highest_category = ""
    lowest_category = ""

    highest_amount = 0
    lowest_amount = 999999

    above_800 = []

    for line in file:

        category, amount = line.strip().split(",")
        amount = int(amount)

        total += amount

        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

        if amount < lowest_amount:
            lowest_amount = amount
            lowest_category = category

        if amount > 800:
            above_800.append(category)

    file.close()

    report = open("report.txt", "w")

    report.write("Total Expenses = " + str(total) + "\n")
    report.write("Highest Expense Category = " + highest_category + "\n")
    report.write("Lowest Expense Category = " + lowest_category + "\n")

    report.write("Categories Spending More Than 800:\n")

    for category in above_800:
        report.write(category + "\n")

    report.close()

    print("Report Generated Successfully")


# Function Calls
display_expenses()

print("Total Expenses =", total_expenses())

highest_lowest_expense()

expenses_above_800()

# Uncomment when needed
# add_expense()

# update_expense()

generate_report()