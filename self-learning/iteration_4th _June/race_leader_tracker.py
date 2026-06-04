#Input lap times of N racers. Display: • Fastest racer position  • Slowest racer position  • Difference between fastest and slowest lap time  Output: 500 x 1 7. Number Mirror Check 
#taking input for the number of racers
n = int(input("Enter the number of racers: "))
#validating the input
if n <= 0:
    print("Please enter a positive integer.")
else:
    #taking input for lap times
    lap_times = []
    for i in range(n):
        time = float(input(f"Enter the lap time for racer {i+1}: "))
        lap_times.append(time)

    #finding the fastest and slowest lap times
    fastest = min(lap_times)
    slowest = max(lap_times)

    #finding the positions of the fastest and slowest racers
    fastest_position = lap_times.index(fastest) + 1
    slowest_position = lap_times.index(slowest) + 1

    #calculating the difference
    difference = slowest - fastest

    #displaying the results
    print(f"Fastest racer position: {fastest_position}")
    print(f"Slowest racer position: {slowest_position}")
    print(f"Difference between fastest and slowest lap time: {difference}") 
    
