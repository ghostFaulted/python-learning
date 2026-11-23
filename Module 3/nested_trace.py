total_points = 0
for stage in range(1, 3):
    for arena in range(1, 4):
        total_points += stage * arena
    print(f"After stage {stage}: {total_points}")