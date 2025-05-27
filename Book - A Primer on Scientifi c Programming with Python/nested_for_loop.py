'''
Suppose we use a nested list scores to record the scores of players in a game:
scores[i] holds a list of the historical scores obtained by player number i. Different
players have played the game a different number of times, so the length of
scores[i] depends on i. Traversing a nested list is done with a nested for loop, as shown in the following code snippet:
'''

# Nested for loop to traverse a nested list
player_1 = [12, 16, 11, 12]
player_2 = [9]
player_3 = [6, 9, 11, 14, 17, 15, 14, 20]
scores = []

for player_scores in (player_1, player_2, player_3):
    scores.append(player_scores)  # Append each player's scores to the scores list

# transverse the nested list "scores"

for player in scores:
    i = 1
    for game_score in player:
        print(f'Game {i}: Score {game_score}')
        i += 1
    print(f'Player {scores.index(player) + 1} finished playing.')  # Print a newline after all scores are printed


