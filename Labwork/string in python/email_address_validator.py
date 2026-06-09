'''A user enters an email address:
rahul.sharma2026@gmail.com
Tasks
Write a program to:
1. Extract username.
2. Extract domain name.
3. Extract extension.
4. Count digits present in username.
5. Count special characters.
6. Check whether:
o Exactly one '@' exists.
o At least one '.' exists after '@'.
7. Display Valid Email or Invalid Email'''
# Storing the email address
email = "rahul.sharma2026@gmail.com"

# 1. Extract username
username = email.split("@")[0]
print("Username:", username)

# 2. Extract domain name
domain = email.split("@")[1].split(".")[0]
print("Domain:", domain)

# 3. Extract extension
extension = email.split("@")[1].split(".")[1]
print("Extension:", extension)

# 4. Count digits present in username
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

print("Digits in Username:", digit_count)

# 5. Count special characters
special_count = 0

for ch in email:
    if not ch.isalnum() and ch != "@":
        special_count += 1

print("Special Characters:", special_count)

# 6. Check email rules

# Check exactly one @
at_check = email.count("@") == 1

# Check at least one . after @
after_at = email.split("@")[1]
dot_check = "." in after_at

print("Exactly One @:", at_check)
print("Dot After @:", dot_check)

# 7. Display Valid Email or Invalid Email
if at_check and dot_check:
    print("Valid Email")
else:
    print("Invalid Email")