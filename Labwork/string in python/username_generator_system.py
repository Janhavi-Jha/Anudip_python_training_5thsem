'''A student enters:
Rahul Sharma
Tasks
Generate a username using the rules:
1. Remove spaces.
2. Convert to lowercase.
3. Append current year (2026).
4. If username length exceeds 12, keep only first 12 characters.
5. Count vowels in the generated username.
6. Count consonants.
7. Display username statistics'''
student="Rahul Sharma"
#removing spaces
Username=student.strip()
print("Username=",Username)
#converting to lowercase
print("Lower Case=",student.lower())
#append current year
students=student+"2026"
print("generted username",students)
#keeping only 12 characters
if len(student) > 12:
    student = student[:12]
print("Username=",student)
#counting vowels and consonants
vowels = 0
consonants = 0

for ch in student:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels=",vowels)
print("Consonants=",consonants)