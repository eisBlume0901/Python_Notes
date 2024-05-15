import pandas as pd
import numpy as np

dogFile = pd.read_csv('dogs.csv')
dogs = pd.DataFrame(dogFile)

# Selecting data by its integer indices
# (review Intermediate Python, 2.dictionaries_and_pandas.py)
print(dogs.iloc[[0, 10, 13]])

# Selecting data by its integer indices and specifying what column data to return
# (review Intermediate Python, 2.dictionaries_and_pandas.py)
print(dogs.iloc[[0, 10, 13], [2]])


# Setting an existing column as an index instead of using default integer indices or
# specifying row labels index
dogs_v2 = dogs.set_index('name')
print(dogs_v2)

# Reset the existing column as an index and use the default integer based indices
print(dogs_v2.reset_index())

# Resetting the existing column as an index and use the default integer based indices then dropping its index values
# (meaning it is not existing in the dataframe anymore)
print(dogs_v2.reset_index(drop=True))

# Sub-setting with isin() method vs specified column as index using loc
# isin() method
print(dogs[dogs["name"].isin(["Bella", "Lucy"])])

# specified column as index using loc
print(dogs_v2.loc[["Bella", "Lucy"]])

# using the usual iloc and loc is only applicable to return a data specified in row and column which is
# hard when you know that specific data and have to think and look at the csv file to know where it is
# unlike using is in and specified columns, you can easily retrieve the desired data

# Note: index values does not need to be unique (same with the usual / default iloc and loc)
# Notice that names and breed contains duplicates
dogs_v3 = dogs.set_index("breed")
print(dogs_v3)

# Setting multiple index values
# Benefit of multi-level indexes is to make reason to nested categorical variables
# Example: Clinical trial with control and treatment group then each test subject is nested inside treatment group
# Example: Temperature data set and city is located in the country, so we can say a city is nested inside the country
dogs_v4 = dogs.set_index(["breed", "color"])
print(dogs_v4)
print(dogs_v4.loc[["Beagle", "Golden Retriever"]]) # Returns duplicate values

# Sub-setting inner levels with a list of tuples (this is where tuples - immutable objects, come into play)
print(dogs_v4.loc[[("Beagle", "Golden"), ("Golden Retriever", "Brown")]])

# Sorting created index values

print(dogs_v2.sort_index())
print(dogs_v3.sort_index())
print(dogs_v4.sort_index(level=["color", "breed"], ascending=[True, True]))
