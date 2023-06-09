# import random
#
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
# new_list = [item * 2 for item in number]
#
# print(new_list)
#
# name = "Giannis"
#
# new_name_list = [letter for letter in name]
#
# print(new_name_list)
#
# names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# short_names = [name for name in names if len(name) < 4]
# print(short_names)
# up_names = [name.upper() for name in names]
# print(up_names)
#
# # *********** Dictionary *********************************
#
# new_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
#
# # ={new_key: new_value for item in list}
# students_scores = {student: random.randint(1, 100) for student in new_names}
#
# # ={new_key: new_value for (key, value) in dictionary.items()}
# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
#
# print(students_scores)
# print(passed_students)
#
#
# #####################################################################
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# # words_list = [word for word in sentence.split()]
#
# result = {word: len(word) for word in sentence.split()}
#
# print(result)
#
#
# #####################################################################
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
#
# weather_f = {day:(temp*9)/5 +32 for (day, temp) in weather_c.items() }
#
#
# print(weather_f)


######################################################################################3


student_dict = {
    "student":["Angela", "James", "Lily"],
    "score":[56,76,98]
}

# for (key,value) in student_dict.items():
#     print(key)
#     print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)


for(index, row) in student_data_frame.iterrows():
    print(row.student)
    if row.student == "Angela":
        print(row.score)





