'''Create Attendance tracker of 30 students. Ask the user to input roll number of student and also input whether student is Present or Absent. Store the data in dictionary where roll number will be used as a key and Attendance as Value. Display the roll number of students who are Present '''
attendance = {}

# Input attendance for 30 students
for i in range(1, 31):
    status = input(f"Enter attendance for Roll No {i} (P/A): ")
    attendance[i] = status

# Display students who are Present
print("\nStudents who are Present:")

for roll_no, status in attendance.items():
    if status == "P":
        print(roll_no)