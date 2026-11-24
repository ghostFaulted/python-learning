groups = int(input("Enter groups: "))
players = int(input("Enter players per group: "))
has_mvp = False
grand_total = 0

for g in range(1, groups + 1):
    score_group = 0
    for p in range(1, players + 1):
        while True:
            score = int(input(f"Group {g}, Player {p} score: "))
            if score < 0:
                print("Invalid score, try again")
            else:
                if score >= 100:
                    MVP = True
                score_group += score 
                break
    grand_total += score_group

    print(f"Group {g} total: {score_group}")

print(f"Tournament grand total: {grand_total}")
print(f"MVP detected: {MVP}")