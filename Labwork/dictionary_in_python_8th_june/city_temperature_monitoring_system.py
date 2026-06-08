'''Daily temperatures of different cities are stored as: temperature = {     "Delhi": 41,     "Mumbai": 33,     "Chennai": 37,     "Kolkata": 39,     "Bengaluru": 28,     "Pune": 30,     "Jaipur": 42,     "Lucknow": 40,     "Hyderabad": 35,     "Ahmedabad": 43 } Tasks 1. Display cities having temperature above 40°C.  2. Find the hottest city.  3. Find the coolest city.  4. Calculate average temperature.  5. Create a list of pleasant cities (temperature < 35°C).  6. Count cities with temperature between 35°C and 40°C.  '''
temperature = {     "Delhi": 41,     "Mumbai": 33,     "Chennai": 37,     "Kolkata": 39,     "Bengaluru": 28,     "Pune": 30,     "Jaipur": 42,     "Lucknow": 40,     "Hyderabad": 35,     "Ahmedabad": 43 } 
c_t=list(temperature.items())
city=c_t[0][0]
temp=c_t[0][1]
#displaying city above 40 temperature
for cities in temperature.items():
    if cities[1]>40:
        print("The cities with tempature above 40=",cities[0])
#finding the hottest  
for cities in temperature.items():
    if cities[1]>temp:
        city=cities[0]
        temp=cities[1]