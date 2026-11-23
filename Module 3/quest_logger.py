quest_count = 0
quest = input("Enter quest name (or DONE to finish): ")

while quest != "DONE":
    quest_count += 1
    quest = input("Enter quest name (or DONE to finish): ")

print(f"Total quests completed: {quest_count}")
