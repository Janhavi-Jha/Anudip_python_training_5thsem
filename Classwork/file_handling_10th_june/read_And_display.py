# Open the file in read mode
file = open("sample.txt", "r")

# Read complete file content
data = file.read()

# Close the file
file.close()

# Count vowels
vowels = 0

for ch in data.lower():
    if ch in "aeiou":
        vowels += 1

# Count characters
characters = len(data)

# Count lines
file = open("sample.txt", "r")

lines = 0

for line in file:
    lines += 1

file.close()

# Display results
print("Number of vowels =", vowels)
print("Number of characters =", characters)
print("Number of lines =", lines)