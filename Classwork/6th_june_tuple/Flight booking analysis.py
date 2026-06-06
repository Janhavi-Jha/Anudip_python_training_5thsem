'''A flight reservation system stores passenger records as tuples:
bookings = (
 ("P101", "Delhi", "Confirmed"),
 ("P102", "Mumbai", "Waiting"),
 ("P103", "Delhi", "Confirmed"),
 ("P104", "Chennai", "Cancelled"),
 ("P105", "Mumbai", "Confirmed"),
 ("P106", "Delhi", "Waiting")
)
Where:
• Passenger ID
• Destination
• Booking Status
Tasks
Write a Python program to:
1. Display all passengers whose booking status is Confirmed.
2. Count the number of passengers travelling to Delhi.
3. Count Confirmed, Waiting, and Cancelled bookings separately.
4. Create a list containing passenger IDs with Waiting status.
5. Determine which destination has the highest number of bookings'''
bookings = (
 ("P101", "Delhi", "Confirmed"),
 ("P102", "Mumbai", "Waiting"),
 ("P103", "Delhi", "Confirmed"),
 ("P104", "Chennai", "Cancelled"),
 ("P105", "Mumbai", "Confirmed"),
 ("P106", "Delhi", "Waiting")
)
for psg in bookings:
    if psg[2]=="Confirmed":
        print("Passangers with confirmed bookings:",psg[0],[1],[2])
#Task 2:Counting no. of passangers travelling to Delhi 
count=0
for psg in bookings:
    if psg[1]=="Delhi":
        count+=1
print("Passangers going to delhi are:",count)
#Task 3:Separately counting waiting ,confirmed and cancelled
waiting=0
confirmed=0
cancelled=0
for psg in bookings:
    if psg[2]=="Confirmed":
        confirmed+=1
    elif psg[2]=="Waiting":
        waiting+=1
    else:
        cancelled+=1
print("Confirmed =",confirmed)
print("Waiting",waiting)
print("Cancelled",cancelled)
#Task 4:Making a list of passangers with waiting issues 
wait=[]
for psg in bookings:
    if psg[2]=="Waiting":
        wait.append(psg)
print(wait)
#determining the destination with highest number of bookings 
bookings_count = {}

for booking in bookings:
    destination = booking[1]

    if destination in bookings_count:
        bookings_count[destination] += 1

highest_destination = max(bookings_count, key=bookings_count.get)

print("Destination with highest bookings:", highest_destination)


