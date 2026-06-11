'''Sample Input/Data (marks.txt) S101,Anuj,92 S102,Rahul,76 S103,Priya,88 S104,Neha,45 S105,Amit,58 S106,Sneha,95 S107,Karan,81 S108,Pooja,73 S109,Rohit,39 S110,Anjali,90 Tasks 1. Calculate grades for all students.  Passed Students: 9 Failed Students: 1 2. Generate a report card file report_card.txt.  3. Display topper details.  4. Count pass and fail students.  5. Display students eligible for merit certificates (marks ≥ 90).  
'''
data = [
    ("S101", "Anuj", 92),
    ("S102", "Rahul", 76),
    ("S103", "Priya", 88),
    ("S104", "Neha", 45),
    ("S105", "Amit", 58),
    ("S106", "Sneha", 95),
    ("S107", "Karan", 81),
    ("S108", "Pooja", 73),
    ("S109", "Rohit", 39),
    ("S110", "Anjali", 90)
]
#display all grades
for grade in data:
    if grade[2]>=90:
        print("Grade A",grade[2])
    elif grade[2]>=80 and grade[2]<=89:
        print("Grade B",grade[2])
    elif grade[2]>=70 and grade[2]<79:
        print("Grade C",grade[2])
    elif grade[2]>=60 and grade[2]<69:
        print("Grade D",grade[2])
    else:
        print("Fail",grade[2])
#display topper details
topper=0
for grade in data:
    if grade[2]>topper:
      topper=grade[2]
print("the topper is ",grade[1],"with marks",grade[2])
#count pass and fail students
passed=0
fail=0
for grade in data:
    if grade[2]>60:
        passed+=1
    else:
        fail+=1
print("pass=",passed)
print("Fail=",fail)
#students eligible for merit list
print("Merit students=")
for grade in data:
    if grade[2]>=90:
        print(grade[1])

