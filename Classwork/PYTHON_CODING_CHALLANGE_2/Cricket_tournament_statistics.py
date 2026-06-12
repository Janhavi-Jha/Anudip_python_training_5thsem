'''runs = {
 "Virat": 645,
 "Rohit": 512,
 "Gill": 698,
 "Rahul": 435,
 "Hardik": 278,
 "Pant": 534,
 "Surya": 389,
 "Jadeja": 301,
 "Iyer": 455,
 "KL": 410
}
Tasks
1. Find the Orange Cap winner.
2. Find the lowest scorer.
3. Calculate total runs scored.
4. Display players scoring more than 500 runs.
5. Create a list of players scoring below 400. '''
runs = {
 "Virat": 645,
 "Rohit": 512,
 "Gill": 698,
 "Rahul": 435,
 "Hardik": 278,
 "Pant": 534,
 "Surya": 389,
 "Jadeja": 301,
 "Iyer": 455,
 "KL": 410
}
#find the orange cap winner
high=0
cricketer=" "
for i in runs.items():
    if i[1]>high:
        high=i[1]
        cricketer=i[0]
print("The orange cap winner is ",cricketer)
#find the lowest scorer
low=645
cric=" "
for i in runs.items():
    if i[1]<low:
        low=i[1]
        cric=i[0]
print("The lowest scorer is",cric)
#total runs scored
total=0
for i in runs.items():
    total+=i[1]
print("Total runs scored =",total)
#players scoring above 500 runs
print("Players scoring more than 500=")
for i in runs.items():
    if i[1]>500:
        print(i[0])
#players scoring below 400
players=[]
for i in runs.items():
    if i[1]<400:
        players.append(i[0])
print("Players with runs below =",players)