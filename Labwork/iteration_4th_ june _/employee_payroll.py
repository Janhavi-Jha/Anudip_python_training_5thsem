#Accept: • Employee Name  • Basic Salary  Calculate: Component Percentage HRA 20% DA 10% PF Deduction 12% Display: • Gross Salary  • Net Salary  Additionally: Net Salary > 50000 → Senior Grade Net Salary > 30000 → Mid Grade Else → Junior Grade  
#taking employee details as input
employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
#calculating components
hra = basic_salary * 0.20
da = basic_salary * 0.10
pf = basic_salary * 0.12
#calculating gross salary
gross_salary = basic_salary + hra + da
#calculating net salary
net_salary = gross_salary - pf
#determining grade
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"
#displaying results
print("Employee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)
print("Grade:", grade)
