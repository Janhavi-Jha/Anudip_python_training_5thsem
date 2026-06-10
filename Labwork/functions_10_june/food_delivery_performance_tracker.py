'''Delivery times (in minutes) for different orders are given below: delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] Requirements Create the following functions: 1. fastest_delivery(times) Returns the shortest delivery time. 2. delayed_orders(times) Returns a list of orders taking more than 45 minutes. 3. average_delivery_time(times) Returns the average delivery time. 4. delivery_category(times) Displays order categories: • Fast → ≤ 30 minutes  • Normal → 31–45 minutes  • Delayed → > 45 minutes  '''
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Function to find fastest delivery
def fastest_delivery(times):
    return min(times)


# Function to find delayed orders
def delayed_orders(times):
    delayed = []

    for time in times:
        if time > 45:
            delayed.append(time)

    return delayed


# Function to calculate average delivery time
def average_delivery_time(times):
    total = 0

    for time in times:
        total += time

    return total / len(times)


# Function to display categories
def delivery_category(times):
    print("Categories:")

    for time in times:
        if time <= 30:
            print(time, "-> Fast")

        elif time <= 45:
            print(time, "-> Normal")

        else:
            print(time, "-> Delayed")


# Function calls
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")

print("Delayed Orders:")
print(delayed_orders(delivery_time))

print("Average Delivery Time:")
print(round(average_delivery_time(delivery_time), 1), "minutes")

delivery_category(delivery_time)