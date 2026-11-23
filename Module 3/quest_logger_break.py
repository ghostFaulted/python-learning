quest_count = 0

while True:
    quest = input("Enter quest name (or DONE to finish): ")
    if quest == "DONE":
        break
    quest_count += 1

print(f"Total quests completed: {quest_count}")