'''Parking slots are represented as:
slots = [1, 0, 1, 1, 0, 0, 1, 0]
Where:
• 1 = Occupied
• 0 = Available
Write a program to:
• Count occupied and available slots.
• Find the first available slot.
• Display all available slot numbers.
• Check whether parking occupancy exceeds 75%. 
'''
slots = [1, 0, 1, 1, 0, 0, 1, 0]
#counting occupied and available slots .
available=0
counting=0
for i in slots:
    if i==0:
        available+=1
    else:
        counting+=1
print("Available Slots=",available)
print("Occupied Slots=",counting)
#finding the first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("First available slot:", i + 1)
        break
#displaying all available slots

for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1)
#checking whether parking exceeds by 75%
occupied=0
for i in slots:
    if i == 1:
        occupied += 1

occupancy = (occupied / len(slots)) * 100

if occupancy > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")