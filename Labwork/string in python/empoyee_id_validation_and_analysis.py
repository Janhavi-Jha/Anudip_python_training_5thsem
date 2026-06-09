'''A company generates employee IDs in the following format: EMP2026ANUJ458 Tasks Write a program to: 1. Count the number of uppercase letters.  2. Count the number of digits.  3. Extract the joining year.  4. Extract the employee name.  5. Check whether the ID follows these rules:  o Starts with "EMP"  o Contains exactly 4 digits for the year  o Ends with exactly 3 digits  6. Create a list containing all digits present in the ID.  7. Find the sum of all digits present in the ID.  8. Display whether the ID is valid or invalid.  '''
Id="EMP2026ANUJ458".strip()
#counting number of uppercase digits
upper=0
for i in Id:
    if i.isupper():
        upper+=1
print("Uppercase digits=",upper)
#counting number of digits
digit=0
for i in Id:
    if i.isdigit():
        digit+=1
print("The number of digits are=",digit)
#extracting the joining year
joining_extract=Id.split("EMP")
joining_year=joining_extract[1].split("ANUJ")[0]
print("Joining Year",joining_year)
#Extracting the employee name
employee_extract=Id.split("2026")
employee_name=employee_extract[1].split("4")[0]
print("Employee name=",employee_name)
'''checking  whether the ID follows these rules: 
o Starts with "EMP" 
o Contains exactly 4 digits for the year 
o Ends with exactly 3 digits  ''' 
#starts with "EMP"
print("Starts with EMP",Id.startswith("EMP"))
#Contains exactly 4 digits for the year
year = Id[3:7]#position of year

if len(year) == 4 and year.isdigit():
    print("Exactly 4 digits for the year")
#end with exactly 3 digits
if Id[-3:].isdigit():#negative indexing for checking digits
    print("Ends with 3 digits")
#creating list containing all digits
Digtis=[]
for i in Id:
    if i.isdigit():
        Digtis.append(i)
print("Digits=",Digtis)
#Sum of all digits
total = 0

for ch in Id:
    if ch.isdigit():
        total += int(ch)

print("Sum of digits:", total)
#checking whether id is valid or not
year = Id[3:7]
if Id.startswith("EMP") and len(year) == 4 and year.isdigit() and Id[-3:].isdigit():
    print("Valid ID")
else:
    print("Invalid ID")