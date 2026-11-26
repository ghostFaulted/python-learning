player_scores = [100, 200, 300, 400]
initial_id = id(player_scores)
player_scores[0] = 150
player_scores[-1] = 500
print(f"Scores: {player_scores}")
print(f"Same object in memory: {initial_id == id(player_scores)}")