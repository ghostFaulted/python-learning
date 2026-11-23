streak_days = int(input("Enter streak days: "))
curr = 1
milestones = 0

while curr <= streak_days:
    if curr % 3 == 0:
        milestones += 1
    curr += 1

print(f"Milestones reached: {milestones}")