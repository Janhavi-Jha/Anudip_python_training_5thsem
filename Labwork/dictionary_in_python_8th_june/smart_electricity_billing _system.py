'''units = {     "House101": 320,     "House102": 180,     "House103": 510,     "House104": 275,     "House105": 150,     "House106": 430,     "House107": 220,     "House108": 390,     "House109": 145,     "House110": 600 } Tasks 1. Display houses consuming more than 400 units.  2. Find the highest-consuming house.  3. Find the lowest-consuming house.  4. Calculate total units consumed.  5. Create lists:  o Low Consumption (< 200)  o Medium Consumption (200–400)  o High Consumption (> 400)  6. Count houses eligible for an energy-saving campaign (consumption > 300).  Sample Output Houses Consuming More Than 400 Units: '''
units = {     "House101": 320,     "House102": 180,     "House103": 510,     "House104": 275,     "House105": 150,     "House106": 430,     "House107": 220,     "House108": 390,     "House109": 145,     "House110": 600 } 
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, consumption in units.items():
    if consumption > 400:
        print(house, "-", consumption)

# 2. Highest-consuming house
highest_house = ""
highest_units = 0

for house, consumption in units.items():
    if consumption > highest_units:
        highest_units = consumption
        highest_house = house

print("\nHighest Consuming House:", highest_house, "-", highest_units)

# 3. Lowest-consuming house
lowest_house = ""
lowest_units = min(units.values())

for house, consumption in units.items():
    if consumption == lowest_units:
        lowest_house = house

print("Lowest Consuming House:", lowest_house, "-", lowest_units)

# 4. Total units consumed
total_units = sum(units.values())
print("Total Units Consumed:", total_units)

# 5. Create lists
low_consumption = []
medium_consumption = []
high_consumption = []

for house, consumption in units.items():
    if consumption < 200:
        low_consumption.append(house)
    elif consumption <= 400:
        medium_consumption.append(house)
    else:
        high_consumption.append(house)

print("\nLow Consumption:", low_consumption)
print("Medium Consumption:", medium_consumption)
print("High Consumption:", high_consumption)

# 6. Energy-saving campaign (>300)
count = 0

for consumption in units.values():
    if consumption > 300:
        count += 1

print("\nHouses Eligible for Energy-Saving Campaign:", count)