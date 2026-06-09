'''A vehicle number plate is entered:
MH12AB4589
Tasks
Write a program to:
1. Extract state code.
2. Extract district code.
3. Extract vehicle series.
4. Extract vehicle number.
5. Count letters and digits separately.
6. Verify:
o First 2 characters must be alphabets.
o Next 2 must be digits.
o Next 2 must be alphabets.
o Last 4 must be digits.
7. Display whether the number plate is valid'''
# Storing the vehicle number plate
plate = "MH12AB4589"

# 1. Extract state code
state_code = plate[:2]
print("State Code:", state_code)

# 2. Extract district code
district_code = plate[2:4]
print("District Code:", district_code)

# 3. Extract vehicle series
vehicle_series = plate[4:6]
print("Vehicle Series:", vehicle_series)

# 4. Extract vehicle number
vehicle_number = plate[6:]
print("Vehicle Number:", vehicle_number)

# 5. Count letters and digits separately
letters = 0
digits = 0

for ch in plate:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Total Letters:", letters)
print("Total Digits:", digits)

# 6. Verify the format
state_check = plate[:2].isalpha()
district_check = plate[2:4].isdigit()
series_check = plate[4:6].isalpha()
number_check = plate[6:].isdigit() and len(plate[6:]) == 4

print("State Code Valid:", state_check)
print("District Code Valid:", district_check)
print("Vehicle Series Valid:", series_check)
print("Vehicle Number Valid:", number_check)

# 7. Display whether the number plate is valid
if state_check and district_check and series_check and number_check:
    print("Number Plate is Valid")
else:
    print("Number Plate is Invalid")
    