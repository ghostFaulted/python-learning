total_score = 0
while True:
    score = int(input("Enter score (-1 to finish): "))
    if score == -1:
        break
    if score < 0:
        print("Invalid score skipped")
        continue
    total_score += score

print(f"Valid total: {total_score}")