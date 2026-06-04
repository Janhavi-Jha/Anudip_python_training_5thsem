#Check whether the left half of a number is identical to the right half. Example: Input: 123123 Output: Mirror Number Input: 123456 Output: Not a Mirror Numbe
#taking input from the user
number = input("Enter a number: ")
#validating the input
if len(number) % 2 != 0 or not number.isdigit():    
    print("Please enter a valid even-digit number.")
else:    
    mid = len(number) // 2
    left_half = number[:mid]
    right_half = number[mid:]
    #checking if the left half is identical to the right half
    if left_half == right_half:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")
        