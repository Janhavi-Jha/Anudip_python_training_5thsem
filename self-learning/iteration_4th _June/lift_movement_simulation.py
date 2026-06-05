#A lift starts at floor 0. The user repeatedly enters destination floors. Display: • Floors travelled in each trip  • Total floors travelled  • Stop when user enters -1  Example: Current Floor: 0 Enter Destination: 5  Travelled: 5 floors  Enter Destination: 2  Travelled: 3 floors  Total Travelled: 8 floors   
#taking input from the user
current_floor = 0
total_floors_travelled = 0
while True:
    destination_floor = int(input("Enter Destination (or -1 to stop): "))
    if destination_floor == -1:
        break
    floors_travelled = abs(destination_floor - current_floor)
    total_floors_travelled += floors_travelled
    print(f"Travelled: {floors_travelled} floors")
    current_floor = destination_floor
print(f"Total Travelled: {total_floors_travelled} floors")

 