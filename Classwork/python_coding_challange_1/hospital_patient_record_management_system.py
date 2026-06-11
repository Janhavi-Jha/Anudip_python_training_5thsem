'''P101,Anuj,Normal P102,Rahul,Critical P103,Priya,Stable P104,Neha,Critical P105,Amit,Stable P106,Sneha,Normal P107,Karan,Critical P108,Pooja,Stable P109,Rohit,Normal P110,Anjali,Stable Tasks 1. Display all patient records.  2. Display critical patients.  3. Count patients under each status.  4. Search patient details using Patient ID.  5. Save critical patient records to critical_patients.txt.'''
patients={
    "P101": ["Anuj", "Normal"],
    "P102": ["Rahul", "Critical"],
    "P103": ["Priya", "Stable"],
    "P104": ["Neha", "Critical"],
    "P105": ["Amit", "Stable"],
    "P106": ["Sneha", "Normal"],
    "P107": ["Karan", "Critical"],
    "P108": ["Pooja", "Stable"],
    "P109": ["Rohit", "Normal"],
    "P110": ["Anjali", "Stable"]
}

# 1. Display all patient records
print("Patient Records:")
for id, details in patients.items():
    print(id, details[0], details[1])

# 2. Display critical patients
print("Critical Patients:")
for id, details in patients.items():
    if details[1] == "Critical":
        print(details[0])

# 3. Count patients under each status
normal = 0
stable = 0
critical = 0

for details in patients.values():
    if details[1] == "Normal":
        normal += 1
    elif details[1] == "Stable":
        stable += 1
    elif details[1] == "Critical":
        critical += 1

print("Patient Count:")
print("Normal :", normal)
print("Stable :", stable)
print("Critical :", critical)

# 4. Search patient details using Patient ID
search_id = input("Enter Patient ID to search: ")

if search_id in patients:
    print("Patient:",search_id , patients[search_id][0],patients[search_id][1])
else:
    print("Patient Not Found")

# 5. Save critical patient records to critical_patients.txt
file = open("critical_patients.txt", "w")

for id, details in patients.items():
    if details[1] == "Critical":
        file.write(details[0] ,details[1] )

file.close()

print("Critical Patient Report Generated Successfully")