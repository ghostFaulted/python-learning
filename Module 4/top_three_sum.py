raw_matches = [140, -10, 450, 0, 220, 510, -5, 380]
valid_matches = []
top_sum = 0

for match in raw_matches:
    if match > 0:
        valid_matches.append(match)

ranked_matches = sorted(valid_matches, reverse=True)
top_three = ranked_matches[:3]

for match in top_three:
    top_sum += match

print(f"Valid matches: {valid_matches}")
print(f"Top 3: {top_three}")
print(f"Top 3 sum: {top_sum}")