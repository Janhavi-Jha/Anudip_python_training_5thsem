'''Correct answers:
correct = ['A', 'C', 'B', 'D', 'A']
Student answers:
student = ['A', 'B', 'B', 'D', 'C']
Write a program to:
• Calculate score.
• Display incorrectly answered question numbers.
• Count correct and wrong answers.
• Determine pass/fail (minimum 60%'''
correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']
#calculating score
score = 0

for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1

print("Score:", score)
#incorrectly answered question number
print("Incorrectly answered questions:")

for i in range(len(correct)):
    if correct[i] != student[i]:
        print(i + 1)
#count wrong and correct answers
correct_count = 0
wrong_count = 0

for i in range(len(correct)):
    if correct[i] == student[i]:
        correct_count += 1
    else:
        wrong_count += 1

print("Correct answers:", correct_count)
print("Wrong answers:", wrong_count)
#determine pass and fail
for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1

percentage = (score / len(correct)) * 100

if percentage >= 60:
    print("Pass")
else:
    print("Fail")