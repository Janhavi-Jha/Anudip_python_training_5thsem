#Accept a number and check whether every digit is exactly 1 greater than its previous digit. 
#taking input from the user
number = input("Enter a number: ")
#validating the input
if not number.isdigit():
    print("Please enter a valid number.")
#checking the condition for consecutive digits
for i in range(len(number) - 1):
    if int(number[i + 1]) != int(number[i]) + 1:
        print("The digits are not consecutive.")
        break
else:
    print("The digits are consecutive.")
