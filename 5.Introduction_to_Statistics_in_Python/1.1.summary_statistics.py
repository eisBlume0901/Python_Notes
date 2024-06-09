import pandas as pd
import numpy as np

# Data use: https://ourworldindata.org/food-supply

file = pd.read_csv("daily-per-capita-caloric-supply.csv")

food_consumption = pd.DataFrame(file)

food_consumption.rename(columns={"Entity": "Country"}, inplace=True)

print(food_consumption.head(3))

ph_consumption = food_consumption[food_consumption["Country"] == "Philippines"]
print(ph_consumption.head(3))
print(ph_consumption.tail(3))
nor_consumption = food_consumption[food_consumption["Country"] == "Norway"]
print(nor_consumption.head(3))
print(nor_consumption.tail(3))

print(np.mean(ph_consumption["Daily calorie supply per person"]))
print(np.median(ph_consumption["Daily calorie supply per person"]))

print(np.mean(nor_consumption["Daily calorie supply per person"]))
print(np.median(nor_consumption["Daily calorie supply per person"]))

print(food_consumption.groupby("Country")["Daily calorie supply per person"].agg(["mean", "median"]))