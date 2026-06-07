'''Attendance for 15 days is recorded as:
attendance  = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
Write a program to:
• Count present and absent days.
• Calculate attendance percentage.
• Determine eligibility (minimum 75% attendance).
• Display positions where the student was absent.'''

attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

present = 0
absent = 0
#count present and absent days
for day in attendance:
    if day == 'P':
        present += 1
    else:
        absent += 1

print("Present days:", present)
print("Absent days:", absent)
#calculate attendance percentage
present = 0

for day in attendance:
    if day == 'P':
        present += 1

percentage = (present / len(attendance)) * 100

print("Attendance Percentage:", percentage)
#determine eligibility
for day in attendance:
    if day == 'P':
        present += 1

percentage = (present / len(attendance)) * 100

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")
    for day in attendance:
     if day == 'P':
        present += 1

percentage = (present / len(attendance)) * 100

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")
for day in attendance:
    if day == 'P':
        present += 1

percentage = (present / len(attendance)) * 100

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")
#Display positions where the student was absent
print("Absent positions:")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)
