#Central-Park-Squirrel-Census-Squirrel-Data.csv
import pandas


data = pandas.read_csv("CSV/learning/Central-Park-Squirrel-Census-Squirrel-Data.csv")

grey_squirrels = len (data [data ["Primary Fur Color"] == "Gray"])
red_squirrels  = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels = len(data[data ["Primary Fur Color"] == "Black"])


print(f"black squirrels: {black_squirrels}")
print(f"grey squirrels: {grey_squirrels}")
print(f"red squirrels: {red_squirrels}")


data_dict = {
    "Fur Color": ["Grey", "Cinnnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("CSV/squirrel_count.csv")