total = 0
for round_num in range(1, 5):
    if round_num == 3:
        continue
    total += round_num * 10
print(f"Final total: {total}")