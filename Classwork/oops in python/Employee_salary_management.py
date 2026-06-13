'''Create an Employee class containing employee ID, name, and monthly salary.
Implement methods to:
• Display employee details.
• Calculate annual salary.
• Increase salary by a given percentage.
Sample Output:
Employee Name : Rohan
Monthly Salary: ₹50000
Annual Salary : ₹600000
Updated Salary: ₹55000'''
class Employee:
    #defining a constructor
    def __init__(self,name,ID,monthly):
        self.__name=name
        self.__ID=ID
        self.__monthly=monthly
    #Method to display employee details
    def emp_details(self):
        print("Employee Name=",self.__name)
        print("Employee ID=",self.__ID)
        print("Monthly Salary=",self.__monthly)
    #Method to calculate Annual Salary
    def annual_salary(self):
        annual=self.__monthly*12
        print("Annual Salary of the employee is=",annual)
    #Method to increase salary by a given percentage
    def updated_salary(self):
        #Assuming 10%
        updated=(10*self.__monthly)/100
        print("Updated Salary of the employee=",updated)
#Taking user input
name=input("Enter the employee name")
#to validate name input
if name.isspace():
    exit("Name cannot be empty.")
ID=int(input("Enter the employee ID="))
if ID<=0:
    print("Invalid INput!")
monthly=int(input("Enter your monthly salary"))
if monthly<=0:
    print("Invalid Input")
#creating object
emp=Employee(name,ID,monthly)
#displaying employee details
emp.emp_details()
#calculate annual salary
emp.annual_salary()
#Updated salary
emp.updated_salary()

        