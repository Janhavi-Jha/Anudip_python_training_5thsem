#A company stores employee details in a tuple. Each employee record contains:
'''----------------------------------------------------------------------
employees = (
 ("E101", "Anuj", 92),
 ("E102", "Rahul", 76),
 ("E103", "Priya", 58),
 ("E104", "Neha", 88),
 ("E105", "Amit", 45)
)
Where:
• First value = Employee ID
• Second value = Employee Name
• Third value = Performance Score
Tasks
Write a Python program to:
1. Display details of employees scoring 80 or above.
2. Count the number of employees who need improvement (score below 60).
3. Find the employee with the highest score.
4. Create a list containing the names of all employees scoring above 75.
5. Display the performance category for each employee:
o 90 and above → Excellent
o 75 to 89 → Good
o 60 to 74 → Average
o Below 60 → Needs Improvement
------------------------------------------------------------------------'''
#creating employee data 
employees=(
 ("E101", "Anuj", 92),
 ("E102", "Rahul", 76),
 ("E103", "Priya", 58),
 ("E104", "Neha", 88),
 ("E105", "Amit", 45)
)
#----------------------------------------------------------------------------------
#Task 1:Displaying details of employee scoring 80 and above
for record in employees:
    if record[2]>=80:
       print("Employees scoring 80 and above:",record[0],[1],[2])
#Task 2: Displaying details of employee needing improvement
count=0
for record in employees:
    if record[2]<60:
        count=count+1
print("Employees needing improvement =",count)
#Task 3:Find the employee with highest score 
highest = employees[0]

for emp in employees:
    if emp[2] > highest[2]:
        highest = emp

print("Employee with highest score:")
print(highest)
#Task 4:a list containing the names of all employees scoring above 75.
for emp in employees:
    if emp[2]>75:
        print("Employee scoring greater than 75=",emp[1])
#Task 5:Displaying performance category 
for emp in employees:
    if emp[2]>=90:
        print(emp[1],"Excellent")
    elif emp[2]>75 and emp[2]<=89:
        print(emp[1],"Good")
    elif emp [2]>60 and emp[2]<=79:
        print(emp[1],"Average")
    else:
        print(emp[1],"Needs Improvement")
