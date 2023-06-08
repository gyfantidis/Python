import random

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

new_list = [item * 2 for item in number]

print(new_list)

name = "Giannis"

new_name_list = [letter for letter in name]

print(new_name_list)

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
short_names = [name for name in names if len(name) < 4]
print(short_names)
up_names = [name.upper() for name in names]
print(up_names)

# *********** Dictionary *********************************

new_names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# ={new_key: new_value for item in list}
students_scores = {student: random.randint(1, 100) for student in new_names}

# ={new_key: new_value for (key, value) in dictionary.items()}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}

print(students_scores)
print(passed_students)
