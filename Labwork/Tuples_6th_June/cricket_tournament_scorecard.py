''' A batsman's scores in different matches are stored in a list.
scores = [45, 78, 12, 100, 67, 8, 90, 55]
Write a program to:
• Count half-centuries and centuries.
• Find the highest score.
• Display all scores below 20.
• Calculate the average score. 
'''
scores=[45,78,12,100,67,8,90,55]
#counting half centuries and centuries 
half_centuries=0
centuries=0
for score in scores:
    if score>=100:
        centuries+=1
    elif score>=50:
        half_centuries+=1
    else:
        print("No centuries or half centuries scored")
print("Centuries=",centuries)
print ("Half centuries=",half_centuries)
#finding the highest score 
for score in scores:
    Highestscore=max(scores)
print("Highest score",Highestscore)
#calculating the average score 
total=0
for score in scores:
    total+=score
average=total/len(scores)
print("Average scores=",average)   
