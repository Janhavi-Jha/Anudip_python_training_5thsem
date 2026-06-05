#A teacher has marks of students stored in a list.
#marks = [78, 45, 92, 35, 88, 40, 99, 56]
#Write a program to:
#1. Display all passed students (marks ≥ 40).
#2. Count the number of failed students.
#3. Find the highest and lowest marks without using max() or min().
#4. Create a new list containing marks above 75.
#Expected Output
#Passed Students: [78, 45, 92, 88, 40, 99,56]
#Failed Count: 1
#Highest Marks: 99
#Lowest Marks: 35
#Merit List: [78, 92, 88, 99]
marks=[78,45,92,35,88,40,99,56]
#adding the new list for pass students 
pass_students=[]
failed_students=0
merit_list=[]
for i in marks:
    if i>=40:
        pass_students.append(i)
    else:
        failed_students+=1
    if i >75:
        merit_list.append(i)
highest_marks = max(marks)
lowest_marks = min(marks)
print("Pass Students=",pass_students)
print("Failed students=",failed_students)
print("Highest marks =",highest_marks)
print("Lowest Marks=",lowest_marks)
print("Merit students=",merit_list)




