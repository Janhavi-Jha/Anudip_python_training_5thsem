'''Write a program to determine whether the password is Strong, Medium, or Weak.
Rules:
• Minimum length 8
• Contains at least:
o 1 uppercase letter
o 1 lowercase letter 
o 1 digit
o 1 special character
Additionally:
1. Count uppercase letters.
2. Count lowercase letters.
3. Count digits.
4. Count special characters.
5. Display all digits separately.
6. Display all special characters separately. 
'''
# Taking password input from the user
password = input("Enter Password: ")
# Initializing counters
uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0
# Creating lists to store digits and special characters
digits = []
special_characters = []
# Traversing through each character of the password
for ch in password:
  # Checking for uppercase letters
    if ch.isupper():
        uppercase_count += 1
 # Checking for lowercase letters
    elif ch.islower():
        lowercase_count += 1
# Checking for digits
    elif ch.isdigit():
        digit_count += 1
        digits.append(ch)
 # Remaining characters are special characters
    else:
        special_count += 1
        special_characters.append(ch)
# Displaying counts
print("Uppercase Letters:", uppercase_count)
print("Lowercase Letters:", lowercase_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)
# Displaying all digits separately
print("Digits Present:", digits)
# Displaying all special characters separately
print("Special Characters Present:", special_characters)
# Checking password strength
if (len(password) >= 8 and
    uppercase_count >= 1 and
    lowercase_count >= 1 and
    digit_count >= 1 and
    special_count >= 1):
    print("Password Strength: Strong")
elif len(password) >= 8 and (
        uppercase_count > 0 or
        lowercase_count > 0 or
        digit_count > 0):
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")