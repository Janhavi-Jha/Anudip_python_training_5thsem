'''An organization wants to create backups of important text files to prevent accidental data loss. You have been asked to develop a utility that creates an exact copy of an existing file. Requirements Write a Python program that reads the entire contents of a source file and copies them into another destination file. The program should: 1. Accept the names of the source file and destination file from the user.  2. Read the complete contents of the source file.  3. Write the contents into the destination file.  4. Display a success message after the copying process is completed.  Sample Source File (notes.txt) Functions help in code reusability. File handling enables persistent storage. Python provides various modes to work with files. '''
# Take source and destination file names from user
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

# Open source file in read mode
file1 = open(source, "r")

# Read complete content
data = file1.read()

# Close source file
file1.close()

# Open destination file in write mode
file2 = open(destination, "w")

# Copy content into destination file
file2.write(data)

# Close destination file
file2.close()

# Display success message
print("File copied successfully.")