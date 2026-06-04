#Accept a number from the user. Display: • Reverse Number  • Whether it is a Palindrome  Example: Input: 1221 Output: Reverse: 1221 Palindrome Number 
num = int(input("Enter a number: "))
#validating the number
if num < 0:
    print("Negative numbers cannot be palindromes.")
else:
    temp = num
    reverse_num = 0
    #calculating the reverse of the number
    while temp > 0:
        digit = temp % 10
        reverse_num = reverse_num * 10 + digit
        temp //= 10
    print("Reverse:", reverse_num)
    #checking if the original number is equal to its reverse
    if num == reverse_num:
        print(num, "is a Palindrome Number.")
    else:
        print(num, "is not a Palindrome Number.")
        