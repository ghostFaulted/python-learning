baseline_xp = [100, 200, 300]
bonus_xp = baseline_xp.copy()
bonus_xp[1] = 250
print(f"Baseline: {baseline_xp}")
print(f"Bonus: {bonus_xp}")
print(f"Same object: {baseline_xp is bonus_xp}")