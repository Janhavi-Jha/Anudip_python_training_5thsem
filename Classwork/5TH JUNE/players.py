#input of 11 players and displaying the score as well
players_scores = {}
for i in range(1, 12):
    score = int(input("Enter score for player {}: ".format(i)))
    players_scores.append(score)
#displaying the score of each player
print("Player Scores:")
print("Score of 11 players",players_scores)
#finding the highest score 
max_score=players_scores[0]
for index in range(1, len(players_scores)):
    if players_scores[index] > max_score:
        max_score = players_scores[index]
print("Highest Score:", max_score)
