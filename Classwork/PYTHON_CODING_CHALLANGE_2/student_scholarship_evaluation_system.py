'''The marks obtained by students in the final examination are stored as follows: 
Sample Data marks = {    
"Anuj": 92,   
"Rahul": 76,    
"Priya": 88,     
"Neha": 64,     
"Amit": 58,     
"Sneha": 95,     
"Karan": 81,     
"Pooja": 73,     
"Rohit": 47,     
"Anjali": 90 } 
Tasks 1. Display students scoring above 85 marks.  
2. Find the topper.  
3. Find the student with the lowest marks.  
4. Calculate class average marks.  
5. Generate grades:  o A (90+)  o B (75–89)  o C (50–74)  o F (<50)  
6. Create a list of scholarship students (marks ≥ 90).'''
marks = {    
"Anuj": 92,   
"Rahul": 76,    
"Priya": 88,     
"Neha": 64,     
"Amit": 58,     
"Sneha": 95,     
"Karan": 81,     
"Pooja": 73,     
"Rohit": 47,     
"Anjali": 90 } 
#display students scoring above 85 marks
print("The students scoring above 85 marks are:")
for i in marks.items():
    if i[1]>85:
        print(i[0])
#find the topper
top=0
name=" "
for i in marks.items():
    if i[1]>top:
        top=i[1]
        name=i[0]
print("The topper of the class is ",name,"with marks",top)
#find the student with lowest marks
low=92
low_s=" "
for i in marks.items():
    if i[1]<low:
        low=i[1]
        low_s=i[0]
print("The student with lowest marks is",low_s,"with marks",low)
#calculate class average marks
total=0
for i in marks.items():
    total+=i[1]
average=total/len(marks)
print("Average marks=",average)
#generating grades o A (90+)  o B (75–89)  o C (50–74)  o F (<50)
for i in marks.items():
    if i[1]>=90:
        grade="A"
    elif i[1]>=75 and i[1]<=89:
        grade="B"
    elif i[1]>=50 and i[1]<=74:
        grade="C"
    else:
        grade="F"
print (grade)
#creating a list of scholarship students 
scholarship=[]
for i in marks.items():
    if i[1]>=90:
        scholarship.append(i[0])
print("Students with scholarship=",scholarship)