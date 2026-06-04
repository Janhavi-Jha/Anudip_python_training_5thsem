#Accept n numbers and find the longest increasing sequence among them.
#taking input from the user
n = int(input("Enter the number of elements: "))
#validating the input
if n <= 0:  
    print("Please enter a positive integer.")
else:   
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    #finding the longest increasing sequence
    longest_seq = []
    current_seq = []
    for i in range(len(numbers)):
        if not current_seq or numbers[i] > current_seq[-1]:
            current_seq.append(numbers[i])
        else:
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq
            current_seq = [numbers[i]]
    #checking the last sequence
    if len(current_seq) > len(longest_seq):
        longest_seq = current_seq
    #printing the longest increasing sequence
    print("The longest increasing sequence is:", longest_seq)
    