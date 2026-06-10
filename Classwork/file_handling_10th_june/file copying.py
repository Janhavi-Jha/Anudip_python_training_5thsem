#copy Entire Content from One File to Another
# Open source file
file1 = open("source.txt", "r")

# Read all data
data = file1.read()

# Close source file
file1.close()

# Open destination file
file2 = open("destination.txt", "w")

# Write data into destination file
file2.write(data)

# Close destination file
file2.close()

print("File copied successfully")