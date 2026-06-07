'''marks = {     "Aarav": 78,     "Diya": 92,     "Rohan": 45,     "Ishita": 88,     "Kabir": 56,     "Meera": 39,     "Arjun": 95,     "Saanvi": 67,     "Vivaan": 82,     "Anaya": 51 } Tasks • Display students scoring 80 or above.  • Count the number of students who failed (marks < 40).  • Find the highest scorer.  • Create a list of students scoring between 60 and 75.  • Assign grades:  o A: ≥ 90  o B: 75–89  o C: 50–74  o F: < 50  '''
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}
#student scoring 80 or above
print("Students scoring 80 or above:")

for name, mark in marks.items():
    if mark >= 80:
        print(name, mark)
#count students who failed
fail_count = 0

for mark in marks.values():
    if mark < 40:
        fail_count += 1

print("Failed students:", fail_count)
#highest scorer
top_student = max(marks, key=marks.get)

print("Highest scorer:", top_student, marks[top_student])
#score between 60 and 75
mid_range = []

for name, mark in marks.items():
    if 60 <= mark <= 75:
        mid_range.append(name)

print("Students scoring 60-75:", mid_range)
#grade assigning
print("Grades:")

for name, mark in marks.items():
    if mark >= 90:
        grade = "A"
    elif 75 <= mark <= 89:
        grade = "B"
    elif 50 <= mark <= 74:
        grade = "C"
    else:
        grade = "F"
    
    print(name, ":", grade)
    