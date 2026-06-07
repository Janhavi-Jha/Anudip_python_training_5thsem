'''Employee data is stored as tuples:
employees = [
 ("Rahul", 35000),
 ("Priya", 55000),
 ("Amit", 42000),
 ("Neha", 65000)
]
Write a program to:
• Display employees earning above ₹50,000.
• Find the highest-paid employee.
• Calculate total salary expenditure.
• Count employees earning below ₹40,000. 
'''
employees = [
 ("Rahul", 35000),
 ("Priya", 55000),
 ("Amit", 42000),
 ("Neha", 65000)
] 
#employees earning above 50,000
for name, salary in employees:
    if salary > 50000:
        print(name, salary)
#highest paid employee
highest = employees[0]

for emp in employees:
    if emp[1] > highest[1]:
        highest = emp

print("Highest-paid employee:", highest[0])
print("Salary:", highest[1])
#Total salary expenditure
total_salary = 0

for name, salary in employees:
    total_salary += salary

print("Total salary expenditure:", total_salary)
#employee earning below 40,000
count = 0

for name, salary in employees:
    if salary < 40000:
        count += 1

print("Employees earning below ₹40,000:", count)

