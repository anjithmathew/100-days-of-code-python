import pandas as pd

read = pd.read_csv(
    "/home/anjithmathew/Documents/1.Python/100-days-of-code-python/Day-25/2.Pandas/weather.csv")
print(read)
read_dict = read.to_dict()

print(read_dict)

temp_list = read["temp"].to_list()
print(temp_list)

print(read["temp"].mean())

average = sum(temp_list)/len(temp_list)

print(average)


average_2 = pd.DataFrame(temp_list)
print(average_2.mean())

# Printing Maximum Value

print(read["temp"].max())

# coloumn

print(read["condition"])

# or

print(read.condition)

# row

print(read.iloc[0])


print(read[read.temp == read.temp.max()])

monday = read[read.temp == "monday"]

# monday_temp = int(monday.temp)
# print(monday_temp)


#create data frame scrach

data_dict = {
    "a":[1,3,562],
    2:[45,"sdfdfgf","ghjhbhj"]
}

datat = pd.DataFrame(data_dict)
print(datat)

datat.to_csv("new_data_csv")