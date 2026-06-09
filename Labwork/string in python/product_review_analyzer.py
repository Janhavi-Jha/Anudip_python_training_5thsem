'''A customer submits a review:
This product is excellent excellent excellent and very useful
Tasks
Write a program to:
1. Count total words.
2. Create a dictionary containing word frequencies.
3. Find the most frequently used word.
4. Find all words appearing only once.
5. Count words having more than 5 characters.
6. Display words in reverse order.
7. Create a list of unique words. '''
# Storing the review
review = "This product is excellent excellent excellent and very useful"

# Converting review into a list of words
words = review.split()

# 1. Count total words
print("Total Words:", len(words))

# 2. Create a dictionary containing word frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequencies:", frequency)

# 3. Find the most frequently used word
most_word = ""
highest_count = 0

for word, count in frequency.items():
    if count > highest_count:
        highest_count = count
        most_word = word

print("Most Frequently Used Word:", most_word)

# 4. Find all words appearing only once
single_words = []

for word, count in frequency.items():
    if count == 1:
        single_words.append(word)

print("Words Appearing Only Once:", single_words)

# 5. Count words having more than 5 characters
count = 0

for word in words:
    if len(word) > 5:
        count += 1

print("Words Having More Than 5 Characters:", count)

# 6. Display words in reverse order
print("Words in Reverse Order:")

for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")

print()

# 7. Create a list of unique words
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("Unique Words:", unique_words)