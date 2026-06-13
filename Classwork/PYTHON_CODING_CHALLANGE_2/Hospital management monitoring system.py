'''heart_rate = {
 "P101": 72,
 "P102": 105,
 "P103": 88,
 "P104": 120,
 "P105": 65,
 "P106": 98,
 "P107": 110,
 "P108": 70,
 "P109": 85,
 "P110": 130
}
Tasks
1. Display critical patients (heart rate >100).
2. Find highest and lowest heart rate.
3. Calculate average heart rate.
4. Count stable patients (60–100 bpm). '''
heart_rate = {
 "P101": 72,
 "P102": 105,
 "P103": 88,
 "P104": 120,
 "P105": 65,
 "P106": 98,
 "P107": 110,
 "P108": 70,
 "P109": 85,
 "P110": 130
}
#display critical patients
print("Critical patients=")
for i in heart_rate.items():
    if i[1]>100:
        print(i[0])
#find highest and lowest heart rate
high=0
low=72
name=" "
for i in heart_rate.items():
    if i[1]>high:
        high=i[1]
        name=i[0]
print("Highest=",name)
for i in heart_rate.items():
    if i[1]<low:
        low=i[1]
        name=i[0]
print("Lowest =",name)
#Calculate average heart rate
total=0
for i in heart_rate.items():
    total+=i[1]
average=total/len(heart_rate)
print("Average=",average)
#stable patients
count=0
for i in heart_rate.items():
    if i[1]>=60 and i[1]<=100:
        count+=1
print("Stable Patients=",count)
