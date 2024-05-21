import pandas as pd
import matplotlib.pyplot as plt

dogFile = pd.read_csv('dogs_v1.csv')
dogs = pd.DataFrame(dogFile)

# MONITORING MISSING VALUES
# Returns a dataframe of boolean values (True means there is a data, False means there is not / null)
# Not suitable for large datasets
print(dogs.isna())

# Also returns boolean values for columns
# Suitable for large datasets as it can easily detect null values
print(dogs.isna().any())

# Returns number of missing values
print(dogs.isna().sum())

# Using counts to visualize missing values
dogs.isna().sum().plot(kind="bar")
plt.tight_layout()
plt.show() # It is expected that there is no missing values, thus a blank graph


# REMOVING MISSING VALUES
# Drops all NaN values but not suitable for large datasets as it may affect the results
dogs.dropna()


# REPLACING MISSING VALUES
# Fills NaN values with 0
dogs.fillna(0)