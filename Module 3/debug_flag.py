has_penalty = False

for round_num in range(1, 4):
    score = int(input(f"Enter score for round {round_num}: "))
    if score < 0:
        has_penalty = True

print(f"Penalty applied: {has_penalty}")