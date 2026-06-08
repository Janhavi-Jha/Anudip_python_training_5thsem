'''scores = {     "Virat": 78,     "Rohit": 112,     "Gill": 45,     "Rahul": 89,     "Hardik": 32,     "Jadeja": 61,     "Surya": 105,     "Pant": 95,     "Bumrah": 18,     "Shami": 25 } Tasks • Display players who scored 50 or more runs.  • Count the number of centuries.  • Find the player with the highest score.  • Create a list of players scoring below 30 runs.  • Determine how many players scored between 50 and 99.   '''
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}
#Players who scored 50 or more runs
print("Players scoring 50 or more:")

for player, runs in scores.items():
    if runs >= 50:
        print(player, runs)
#Count centuries (100+ runs)
centuries = 0

for runs in scores.values():
    if runs >= 100:
        centuries += 1

print("Number of centuries:", centuries)
#Player with highest score
top_player = max(scores, key=scores.get)

print("Highest scorer:", top_player, scores[top_player])
#Players scoring below 30 runs
low_scores = []

for player, runs in scores.items():
    if runs < 30:
        low_scores.append(player)

print("Players scoring below 30:", low_scores)
#Players scoring between 50 and 99
mid_scores = 0

for runs in scores.values():
    if 50 <= runs <= 99:
        mid_scores += 1

print("Players scoring between 50 and 99:", mid_scores)