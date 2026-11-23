streak_days = int(input("Enter streak days: "))
milestones = 0
for day in range(1, streak_days + 1):
    if day % 3 == 0:
        milestones += 1

print(f"Milestones reached: {milestones}")