groups = int(input("Enter number of groups: "))
players = int(input("Enter players per group: "))

for group in range(1, groups + 1):
    for player in range(1, players + 1):
        print(f"Group {group} - Player {player}")
    print(f"--- Group {group} complete ---")