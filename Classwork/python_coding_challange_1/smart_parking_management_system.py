'''parking_slots = [     "Occupied", "Vacant", "Occupied", "Vacant",     "Occupied", "Occupied", "Vacant", "Occupied",     "Vacant", "Occupied" ] Tasks 1. Display vacant parking slot numbers.  2. Count occupied and vacant slots.  3. Allocate the first vacant slot to a new vehicle.  4. Calculate parking occupancy percentage.  5. Store updated parking information in parking.txt.  '''
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# 1. Display vacant parking slot numbers
print("Vacant Parking Slots:")
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        print(i + 1)
print()

# 2. Count occupied and vacant slots
occupied = 0
vacant = 0

for slot in parking_slots:
    if slot == "Occupied":
        occupied += 1
    else:
        vacant += 1

print("Occupied Slots =", occupied)
print("Vacant Slots =", vacant)

# 3. Allocate the first vacant slot to a new vehicle
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print("Allocated Slot Number =", i + 1)
        break

# 4. Calculate parking occupancy percentage
occupied = 0
for slot in parking_slots:
    if slot == "Occupied":
        occupied += 1

occupancy_percentage = (occupied / len(parking_slots)) * 100

print("Occupancy Percentage =", occupancy_percentage)

