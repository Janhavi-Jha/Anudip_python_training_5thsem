#A number whose digit first increases and then decreases is called a mountain number.
#taking input from the user
n = int(input("Enter a number: "))
#converting the number to a string to access each digit
num_str = str(n)
#initializing variables to track the increasing and decreasing phases
increasing = True
mountain = True
#iterating through the digits of the number
for i in range(1, len(num_str)):
    if increasing:
        if num_str[i] > num_str[i - 1]:
            continue
        elif num_str[i] < num_str[i - 1]:
            increasing = False
        else:
            mountain = False
            break
    else:
        if num_str[i] < num_str[i - 1]:
            continue
        else:
            mountain = False
            break