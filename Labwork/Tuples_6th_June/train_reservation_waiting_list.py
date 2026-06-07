'''Passenger records:
passengers = [
 ("Anuj", "Confirmed"),
 ("Rahul", "Waiting"),
 ("Priya", "Confirmed"),
 ("Amit", "Waiting"),
 ("Neha", "Confirmed")
]
Write a program to:
• Display all waiting-list passengers.
• Count confirmed and waiting passengers.
• Find whether a specific passenger has a confirmed ticket.
• Create separate lists for confirmed and waiting passenger'''
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

print("Waiting-list passengers:")

for name, status in passengers:
    if status == "Waiting":
        print(name)
confirmed = 0
waiting = 0

for name, status in passengers:
    if status == "Confirmed":
        confirmed += 1
    else:
        waiting += 1

print("Confirmed passengers:", confirmed)
print("Waiting passengers:", waiting)
name_to_search = "Rahul"

found = False

for name, status in passengers:
    if name == name_to_search:
        if status == "Confirmed":
            print(name, "has a confirmed ticket")
        else:
            print(name, "does NOT have a confirmed ticket")
        found = True
        break

if not found:
    print("Passenger not found")
    confirmed_list = []
waiting_list = []

for name, status in passengers:
    if status == "Confirmed":
        confirmed_list.append(name)
    else:
        waiting_list.append(name)

print("Confirmed passengers:", confirmed_list)
print("Waiting passengers:", waiting_list)