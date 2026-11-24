quests = int(input("Enter number of quests: "))
total_xp = 0

for quest in range(1, quests + 1):
    if quest % 5 == 0:
        total_xp += 50
    elif quest % 2 == 0:
        total_xp += 20
    else:
        total_xp += 10

print(f"Total XP earned: {total_xp}")