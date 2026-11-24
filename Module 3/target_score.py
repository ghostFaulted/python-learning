target = int(input("Enter target score: "))
total_score = 0

while True:
    score = int(input("Enter round score: "))
    total_score += score
    if total_score >= target:
        break

print(f"Target reached! Final score: {total_score}")