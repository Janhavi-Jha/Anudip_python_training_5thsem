'''Delivery times (in minutes) for different orders are recorded below: 
Sample Data 
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Tasks 1. Find the fastest delivery time.  
2. Find the slowest delivery time.  
3. Calculate the average delivery time.  
4. Display delayed orders (>45 minutes).  
5. Categorize deliveries:  
o Fast (≤30 minutes)  
o Normal (31–45 minutes)  
o Delayed (>45 minutes)  '''
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
#finding the fastest delivery time
for i in delivery_times:
     i=min(delivery_times)
print("The fastest delivery time is",i,"minutes")
#finding the slowest delivery time
for i in delivery_times:
     i=max(delivery_times)
print("The slowest delivery time is",i,"minutes")
#calculate the average delivery time
total=0
for i in delivery_times:
     total+=i
average=total/len(delivery_times)
print("Average=",average)
#displaying delayed orders
delay=[]
print("Delayed orders are=")
for i in delivery_times:
     if i>45:
          delay.append(i)
print(delay)
#Categorizing deliveries
fast=0
Normal=0
Delayed=0
for i in delivery_times:
     if i<=30:
          fast+=1
     elif i>=31 and i<=45:
          Normal+=1
     else:
          Delayed+=1   
print("Fast=",fast)
print("Normal=",Normal)
print("Delayed=",Delayed)

