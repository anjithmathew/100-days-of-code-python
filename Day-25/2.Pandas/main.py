import pandas as pd

read = pd.read_csv(
    "/home/anjithmathew/Documents/1.Python/100-days-of-code-python/Day-25/2.Pandas/weather.csv")
print(read)
read_dict = read.to_dict()

print(\n,read_dict)

temp_list = read["temp"].to_list()

