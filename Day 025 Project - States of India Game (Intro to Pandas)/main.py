# Using file methods
print("Using file methods...")
with open(file="weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

print("--"*10)

# Using CSV Library
import csv

print("Using CSV Library...")
with open(file="weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)

print("--"*10)

# Using pandas library
import pandas as pd

print("Using Pandas Library...")
data = pd.read_csv("weather_data.csv")
print(type(data))
print(data)
print(data["temp"])

print("Converting to dictionary...")
data_dict = data.to_dict()
print(data_dict)

print("Fetching temperatures adn creating a list...")
temp_list = data["temp"].to_list()
print(len(temp_list))

print(f"Mean temp: {data['temp'].mean()}")
print(f"Max Temp: {data['temp'].max()}")

#Get Data in Columns
print("Get data in columns")
print(data["condition"])
print(data.condition)

# Get Data in Row
print("get data in row")
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Get Row data value
monday = data[data.day == "Monday"]
#monday_temp = int(monday.temp) #deprecated
monday_temp = int(monday.temp.iloc[0])
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")


#Central Park Squirrel Data Analysis

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")