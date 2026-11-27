raw_scores = [120, -5, 0, 340, -20, 80, 15]
valid_scores = []
bonus_eligible = []
for score in raw_scores:
    if score > 0:
        valid_scores.append(score)
        if score >= 100:
            bonus_eligible.append(score)

print(f"Raw: {raw_scores}")
print(f"Valid: {valid_scores}")
print(f"Bonus eligible: {bonus_eligible}")