import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ddof=1 population variance, ddof=0 sample variance

foodConsumptionFile = pd.read_csv('food_consumption.csv', index_col=0)
food_consumption = pd.DataFrame(foodConsumptionFile)
pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

# Quartiles
print(np.quantile(food_consumption["co2_emission"], [0, 0.25, 0.50, 0.75, 1]))
print(food_consumption["co2_emission"].quantile(np.linspace(0, 1, 5)))

# Quintiles
print(np.quantile(food_consumption["co2_emission"], [0, 0.20, 0.40, 0.60, 0.80, 1]))
print(food_consumption["co2_emission"].quantile(np.linspace(0, 1, 6)))

# Deciles
print(np.quantile(food_consumption["co2_emission"], [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))
print(food_consumption["co2_emission"].quantile(np.linspace(0, 1, 11)))

print(food_consumption.groupby("food_category")["co2_emission"].agg(["var", "std"]))
food_consumption[food_consumption["food_category"] == "beef"].plot(kind="hist", x="co2_emission")
plt.show()

food_consumption[food_consumption["food_category"] == "pork"].plot(kind="hist", x="co2_emission")
plt.show()