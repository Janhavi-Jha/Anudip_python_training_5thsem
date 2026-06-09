'''Attendance of a student for 15 days is represented as:
PPAPPPAAPPPPAPP
Where:
• P = Present
• A = Absent
Tasks
Write a program to:
1. Count Present and Absent days.
2. Calculate attendance percentage.
3. Find the longest consecutive streak of Presence.
4. Find the longest consecutive streak of Absence.
5. Determine whether attendance is below 75%. '''
attendance = "PPAPPPAAPPPPAPP"
#count present and absent
present=attendance.count("P")
print("Present=",present)
absent=attendance.count("A")
print("Absent=",absent)
#calculate attendance percentage
total=len(attendance)
attendance_percentage=(present/total)*100
print("Attendance percentage=",attendance_percentage)
#finding longest consecutive streak
present_streak=0
absent_streak=0
for i in attendance:
    if i=="P":
        present_streak+=1
    else:
        absent_streak+=1
print("Present streak=",present_streak)
print("Absent streak=",absent_streak)
#checking if attendance below 75%

if attendance_percentage < 75:
    print("Attendance is below 75%")
else:
    print("Attendance is 75% or above")
  

