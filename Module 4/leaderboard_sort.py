match_scores = [310, 890, 150, 940, 620, 480]
sorted_desc = sorted(match_scores, reverse=True)
top_three = sorted_desc[:3]

print(f"Original: {match_scores}")
print(f"Sorted DESC: {sorted_desc}")
print(f"Top 3: {top_three}")