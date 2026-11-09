total_matches = int(input("Enter total matches: "))
total_wins = int(input("Enter wins: "))
win_percentage = (total_wins / total_matches) * 100
print(f"Win rate: {win_percentage:.1f}%")