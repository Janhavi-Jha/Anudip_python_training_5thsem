'''temperature = {
 "Delhi": 41,
 "Mumbai": 33,
 "Chennai": 37,
 "Kolkata": 39,
 "Bengaluru": 28,
 "Pune": 30,
 "Jaipur": 42,
 "Lucknow": 40,
 "Hyderabad": 35,
 "Ahmedabad": 43
}
Tasks
1. Display cities with temperature above 40°C.
2. Find the hottest city.
3. Find the coolest city.
4. Calculate average temperature.
5. Create a list of pleasant cities (<35°C).'''
temperature = {
 "Delhi": 41,
 "Mumbai": 33,
 "Chennai": 37,
 "Kolkata": 39,
 "Bengaluru": 28,
 "Pune": 30,
 "Jaipur": 42,
 "Lucknow": 40,
 "Hyderabad": 35,
 "Ahmedabad": 43
}
#Display cities with temperature above 40°C.
print("Cities with temperature below 40")
for i in temperature.items():
    if i[1]>40:
        print(i[0])
#hottest cities
hot=0
for i in temperature.items():
    if i[1]>hot:
        hot=i[1]
print("Hottest city=",i[0])
#coolest cities
cool=41
city=" "
for i in temperature.items():
    if i[1]<cool:
        cool=i[1]
        city=i[0]
print("Coolest city=",city)
#avergae temperature
total=0
for i in temperature.items():
    total=total+i[1]
average=total/len(temperature)
print("Average=",average)
#pleasant cities
pleasent=[]
for i in temperature.items():
    if i[1]<35:
     pleasent.append(i[0])
print("Pleasent cities=",pleasent)
