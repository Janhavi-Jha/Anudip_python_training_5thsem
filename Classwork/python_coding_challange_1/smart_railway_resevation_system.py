'''A railway reservation system stores the booking status of seats in a train coach.
Sample Data
seats = {
 1: "Booked",
 2: "Available",
 3: "Booked",
 4: "Available",
 5: "Booked",
 6: "Booked",
 7: "Available",
 8: "Booked",
 9: "Available",
 10: "Booked"
}
Tasks
1. Display all available seat numbers.
2. Count booked and available seats.
3. Reserve the first available seat.
4. Cancel booking for a given seat number.
5. Store the updated reservation status in reservations.txt.
6. Display occupancy percentage. '''
seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}

# 1. Display all available seat numbers
print("Available Seats:")
for seat, status in seats.items():
    if status == "Available":
        print(seat)
print()

# 2. Count booked and available seats
booked = 0
available = 0

for status in seats.values():
    if status == "Booked":
        booked += 1
    else:
        available += 1

print("Booked Seats =", booked)
print("Available Seats =", available)

# 3. Reserve the first available seat
for seat, status in seats.items():
    if status == "Available":
        seats[seat] = "Booked"#updating the status to booked
        print("First available seat reserved:", seat)
        break

# 4. Cancel booking for a given seat number
seat_no = int(input("Enter seat number to cancel booking: "))#user input for seat no.

if seat_no in seats:
    seats[seat_no] = "Available"#available means no longer booked4
    print("Booking cancelled for seat", seat_no)
else:
    print("Invalid seat number")

# 5. Store updated reservation status in reservations.txt
file = open("reservations.txt", "w")#opeing reservations.txt for write operation

for seat, status in seats.items():
    file.write(f"Seat {seat}: {status}")

file.close()

print("Updated reservation status saved to reservations.txt")

# 6. Display occupancy percentage
booked = 0

for status in seats.values():
    if status == "Booked":
        booked += 1

occupancy = (booked / len(seats)) * 100

print("Occupancy Percentage =", occupancy, "%")
