'''Passenger count at each stop:
passengers = [12, 18, 25, 30, 28, 15, 8]
Write a program to:
• Find the busiest stop.
• Display stops with fewer than 10 passengers.
• Calculate average passengers.
• Determine whether any stop exceeded 25 passengers. '''
passengers = [12, 18, 25, 30, 28, 15, 8]

maximum = max(passengers)
stop_number = passengers.index(maximum) + 1

print("Busiest Stop:", stop_number)
print("Passengers:", maximum)

print("Stops with fewer than 10 passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print(i + 1)


total = 0

for p in passengers:
    total += p

average = total / len(passengers)

print("Average passengers:", average)
found = False

for p in passengers:
    if p > 25:
        found = True
        break

if found:
    print("Yes, a stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")