current_score = 1000
saved_score = current_score
print(f"Initial same ID: {id(current_score) == id(saved_score)}")
current_score = current_score + 250
print(f"Current score: {current_score}, saved score: {saved_score}")
print(f"After update same ID: {id(current_score) == id(saved_score)}")
