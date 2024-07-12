import pandas as pd
import matplotlib.pyplot as plt

# world_happiness_2023 = pd.read_csv('WHR2023.csv', index_col=0)
# # Using bar chart might not be appropriate for this data (scatter plot is much fitting to get the relationship between two or multiple variables)
# # The data below is just use how to plot stacked bar charts
# logged_gdp_per_capita_greater_than_10_80 = world_happiness_2023[world_happiness_2023["Logged GDP per capita"] > 10.80]
# figure, axis = plt.subplots(figsize=(20, 15))
# axis.bar(logged_gdp_per_capita_greater_than_10_80.index, logged_gdp_per_capita_greater_than_10_80["Logged GDP per capita"])
# axis.bar(logged_gdp_per_capita_greater_than_10_80.index, logged_gdp_per_capita_greater_than_10_80["Healthy life expectancy"], bottom=logged_gdp_per_capita_greater_than_10_80["Logged GDP per capita"])
# axis.set_xticklabels(logged_gdp_per_capita_greater_than_10_80.index, rotation=90)
# axis.set_ylabel("Logged GDP per capita and its Healthy life expectancy")
# axis.set_xlabel("Countries")
# axis.set_title("Countries that has a logged GDP per capita greater than 10.80 along with its healthy life expectancy")
# plt.tight_layout()
# plt.show()

# The data appropriate for stack bar charts are categorical data
