'''units = {     
"House101": 320,    
House102": 180,  
House103": 510,  
"House104": 275,   
"House105": 150,  
"House106": 430, 
"House107": 220, 
"House108": 390,  
"House109": 145,   
"House110": 600 }
Tasks 1. Display houses consuming more than 400 units. 
2. Find the highest-consuming house. 
3. Find the lowest-consuming house. 
4. Calculate the total units consumed. 
5. Create separate lists for: 
o Low Consumption (< 200) 
o Medium Consumption (200–400
o High Consumption (> 400) 
 6. Count houses eligible for an energy-saving campaign (consumption > 300).  '''
units={
    "House101": 320,    
"House102": 180,  
"House103": 510,  
"House104": 275,   
"House105": 150,  
"House106": 430, 
"House107": 220, 
"House108": 390,  
"House109": 145,   
"House110": 600 }
#display houses consuming more than 400 units
print("The houses consuming more than 400 units are:")
for i in units.items():
    if i[1]>400:
        print(i[1])
#finding the highest consuming house
highest=0
for i in units.items():
    if i[1]>highest:
        highest=i[1]
        
print("The highest consuming house is", i[0],"with units",i[1])
#finding the lowest consuming house
lowest=320
lowest_house = ""
for i in units.items():
    if i[1] < lowest:
        lowest = i[1]
        lowest_house = i[0]
print("The lowest consuming house is", lowest_house, "with units", lowest)
#calculating the total units consumed 
total=0
for i in units.items():
    total=total+i[1]
print("The total units=",total)
'''Create separate lists for: 
o Low Consumption (< 200) 
o Medium Consumption (200–400
o High Consumption (> 400)'''
low =[]
med=[]
high=[]
print("Low Consumption")
for i in units.items():
    if i[1]<200:
        low.append(i[0])
print(low)
print("Medium Consumption")
for i in units.items():
    if i[1]>200 and i[1]<400:
        med.append(i[0])
print(med)
print("High Consumption")
for i in units.items():
    if i[1]>400:
        high.append(i[0])
print(high)
#count houses eligible for energy saving campaign
count=0
for i in units.items():
    if i[1]>300:
        count+=1
print("Houses eligible for energy saving campaign=",count)
