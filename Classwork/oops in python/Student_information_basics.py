'''Create a Student class to store the student's name, roll number, and marks obtained in three subjects.
Implement methods to:
• Accept student details.
• Calculate the total marks.
• Calculate the percentage.
• Display the complete student report. '''
class Student:
    #defining a constructor
    def __init__(self,name,roll,mark1,mark2,mark3):
        self.__mark1=mark1
        self.__mark2=mark2
        self.__mark3=mark3
        self.__roll=roll
        self.__name=name
    #Method to accept account details
    def student_details(self):
        print("Student Name:",self.__name)
        print("Roll Number:",self.__roll)
        print("Marks:",self.__mark1,self.__mark2,self.__mark3)
    #method to calculate total marks
    def total_marks(self):
        total=self.__mark1+self.__mark2+self.__mark3
        print("Total marks scored =",total)
    #Method to calculate percentage
    def percentage(self):
        total=self.__mark1+self.__mark2+self.__mark3
        percentage=(total/300)*100
        print("Total percentage marks=",percentage,"%")
    #displaying complete student report 
    def display_report(self):
        print("-----Student Report--------------\n",self.__name,self.__roll,self.__mark1,self.__mark3,self.__mark2)
#-----------------------------------------------------
#Main program -------------------------
#Ask the user to input data
name=input("Enter student's name: ")
#to validate name input
if name.isspace():
    exit("Name cannot be empty.")
#---------------------------------------------------------------
roll=int(input("Enter roll number"))
#validating input
if roll<=0:
    exit("Invalid input")
mark1=int(input("Enter the mark of English="))
mark2=int(input("Enter the marks of Hindi= "))
mark3=int(input("Enter marks of Maths="))
#creating an object of Student Class
students=Student(name,roll,mark1,mark2,mark3)
#menu driven program
while True:
    print("--------------Student Information---------------")
    print("1.Student Details")
    print("2.Total Marks scored")
    print("3.Percentage")
    print("4.Complete Student Report")
    print("5.Exit")
    choice=int(input("Select operation"))
    if choice==1:
        students.student_details()
    elif choice==2:
        students.total_marks()
    elif choice==3:
        students.percentage()
    elif choice==4:
        students.display_report()
    elif choice==5:
        print("Thankyou!")
        break
    else:
        print("Invalid Input!")
    #Ask the user if they want to perform another operation
    another_operation=input("Do you want to perform another operation? (yes/no): ")
    if another_operation.lower()!="yes":
        print("Thank you for using our services!")
        break
    print("\n----------------------------------")
