# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)



# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#
#     # temperatures.remove("temp")
#
#     print(temperatures)


import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print("- - - - - - - - - - - - - - - -- -- - - - --  ")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())
#
# maxim = max(temp_list)
# print(maxim)
# print(data["temp"].max())
#
# # Get data to columns
# print(data["condition"])
# print(data.condition)
#
# # Get data to row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # Create a dataframe from scratch
# data_dict2 = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [78,56,65]
# }
#
# data2 = pandas.DataFrame(data_dict2)
# print(data2)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrel_count,cinnamon_squirrel_count,black_squirrel_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

print(df)











































