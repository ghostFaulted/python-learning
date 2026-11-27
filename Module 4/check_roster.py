registered_students = ["olena", "taras", "dmytro", "iryna", "maksym"]
submitted_students = ["taras", "iryna"]
missing_students = []

for student in registered_students:
    if student not in submitted_students:
        missing_students.append(student)

dmytro_submitted = "dmytro" in submitted_students

print(f"Missing submissions: {missing_students}")
print(f"Dmytro submitted: {dmytro_submitted}")