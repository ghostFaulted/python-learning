event_points = [15, 120, 40, 200, 10, 85]
total_xp = 0
high_value_count = 0

for event in event_points:
    total_xp += event
    if event >= 50:
        high_value_count += 1

print(f"Total XP: {total_xp}")
print(f"High-value events: {high_value_count}")