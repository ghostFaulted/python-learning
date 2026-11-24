long_matches = 0
total_minutes = 0

while True:
    duration = int(input("Enter duration (0 to stop): "))
    if duration == 0:
        break
    if duration < 0:
        print("Invalid duration")
        continue
    if duration >= 30:
        long_matches += 1
    total_minutes += duration

print(f"Long matches: {long_matches}, Total time: {total_minutes} min")