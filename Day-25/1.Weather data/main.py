# import csv

# with open("Day-25/weather.csv", "r+") as fh:
#     data = csv.reader(fh)
#     print(data)
#     temperature = []
#     for row in data:
#         temperature.append(row[1])
#     temperature.remove(temperature[0])
#     print(temperature)

import pandas as pd

data = pd.read_csv("/home/anjithmathew/Documents/1.Python/100-days-of-code-python/Day-25/1.Weather data/weather.csv") 
print(data)
print(data["temp"])

conv_dict = data.to_dict()

print(conv_dict)

for key in conv_dict:
    print(conv_dict[key])

clear()
