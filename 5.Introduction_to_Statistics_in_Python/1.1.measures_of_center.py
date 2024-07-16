import pandas as pd
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt

# Data use: https://ourworldindata.org/food-supply

file = pd.read_csv("daily-per-capita-caloric-supply.csv")
food_consumption = pd.DataFrame(file)
food_consumption.rename(columns={"Entity": "Country"}, inplace=True)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

print(food_consumption.head(3))

ph_consumption = food_consumption[food_consumption["Country"] == "Philippines"]
print(ph_consumption.head(3))
print(ph_consumption.tail(3))
nor_consumption = food_consumption[food_consumption["Country"] == "Norway"]
print(nor_consumption.head(3))
print(nor_consumption.tail(3))

print(np.mean(ph_consumption["Daily calorie supply per person"]))
print(np.median(ph_consumption["Daily calorie supply per person"]))
print(stat.mode(ph_consumption["Daily calorie supply per person"]))

print(np.mean(nor_consumption["Daily calorie supply per person"]))
print(np.median(nor_consumption["Daily calorie supply per person"]))
print(stat.mode(nor_consumption["Daily calorie supply per person"]))

print(food_consumption.groupby("Country")["Daily calorie supply per person"].agg(["mean", "median"]))


file1 = pd.read_csv('food_consumption.csv', index_col=0)
food_consumption_v1 = pd.DataFrame(file1)
print(food_consumption_v1.head())

print(food_consumption_v1.groupby("country")["consumption"].agg(["mean","median"]))

ph_nor_consumption = food_consumption_v1[ (food_consumption_v1["country"] == "Philippines") | (food_consumption_v1["country"] == "Norway") ]
print(ph_nor_consumption.groupby("country")["consumption"].agg(["mean", "median"]))

rice_consumption = food_consumption_v1[food_consumption_v1["food_category"] == "rice"]
print(rice_consumption["co2_emission"].agg(["mean", "median"])) # Mean 37.5, Median 15.2
print("Mode: ", stat.mode(rice_consumption["co2_emission"]))
# Since the mode is around 6.35, the median measurement of 15.2 is considered since it is more closed to the mode's value
rice_consumption.plot(kind="hist", x="co2_emission")
plt.title("Distribution of CO2 emissions from Rice Consumption")
plt.xlabel("CO2 emissions")
plt.show() # Expect it to be positively / right skewed
