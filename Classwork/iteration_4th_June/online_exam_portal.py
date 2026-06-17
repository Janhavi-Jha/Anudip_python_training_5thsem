'''A student must score at least 40 marks to pass an online assessment. The system allows the student to reattempt the test until 
the passing score is achieved. 
Problem Statement: 
Write a program that accepts marks from the user and continues asking for marks until the entered score is 40 or more. 
Display a congratulatory message once the student passes the assessment. 
'''
marks = int(input("Enter your marks: "))

while marks < 40:
    print("You have not passed. Please reattempt the test.")
    marks = int(input("Enter your marks: "))

print("Congratulations! You have passed the assessment.")