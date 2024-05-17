import pandas as pd

dogFile = pd.read_csv('dogs.csv')
dogs = pd.DataFrame(dogFile)

print(dogs.groupby("breed")["weight_kg"].agg(["mean", "max", "min"]))

# values - data values
# index - row indices
# aggfunc - to get a summary of aggregate statistics same with agg for groupby
print(dogs.pivot_table(values="weight_kg",  index="breed", aggfunc=["mean", "max", "min"]))


print(dogs.groupby(["breed", "color"])["weight_kg"].agg(["mean", "max", "min"]))

# columns - column headers
# fill_value - default is NaN, you can set a new fill_value for null values
# margins - margin set to True returns the mean/average specified by the index and column, it is not the average of all
# visible values in that row or column.

# 'All' row and column contain the respective statistics (mean, max, min, etc., depending on the aggfunc parameter)
# over all the data in the respective rows or columns, not just the visible data
# Note: index allows multiple indices and columns (e.g. index=["skin_color", "eye_color"], columns=["breed","origin"])
print(dogs.pivot_table(values="weight_kg", index="color", columns="breed", aggfunc=["mean", "max", "min"], fill_value=0, margins=True))