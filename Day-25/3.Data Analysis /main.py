import pandas as pd
data = pd.read_csv(
    "/home/anjithmathew/Documents/1.Python/100-days-of-code-python/Day-25/3.Data Analysis /228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

fur = pd.Series(data["Primary Fur Color"])
count = fur.value_counts()
dount_dict = count.to_dict()
