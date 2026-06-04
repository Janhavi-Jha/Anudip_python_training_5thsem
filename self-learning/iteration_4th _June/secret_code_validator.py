 #A secret code is valid if: • It contains exactly 6 digits.  • Sum of first 3 digits equals sum of last 3 digits.  Example: Input: 123321 Output: Valid Code Input: 123456 Output: Invalid Code 
#taking input from the user
code = input("Enter the secret code: ")
#validating the input
if len(code) != 6 or not code.isdigit():
    print("Invalid code. Please enter a 6-digit number.")
else:
    #calculating the sum of the first 3 digits and the last 3 digits
    sum_first_half = sum(int(code[i]) for i in range(3))
    sum_second_half = sum(int(code[i]) for i in range(3, 6))
    #checking if the sums are equal
    if sum_first_half == sum_second_half:
        print("Valid Code")
    else:
        print("Invalid Code")

