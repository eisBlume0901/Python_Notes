import numpy as np
import pandas as pd

sales_team = [
    {
        "name": "Brian",
        "sales": 128
    },
    {
        "name": "Clarrisa",
        "sales": 75
    },
    {
        "name": "Matthew",
        "sales": 104
    },
    {
        "name": "Josephina",
        "sales": 64
    }
]

sales_df = pd.DataFrame(sales_team)
np.random.seed(456) # seed allows you to make your first random generated value the same throughout the code
# Sample without replacement (is an example of an Dependent event)
print(sales_df.sample())
print(sales_df.sample(2)) # retrieves 2 data from the dataframe

# Sample with replacement (is an example of an Independent event)
print(sales_df.sample(5, replace=True))

# Calculating the probability of choosing each product type from all product types
amirDealsFile = pd.read_csv("amir_deals.csv")
amir_deals = pd.DataFrame(amirDealsFile)
print(amir_deals.head(3))

counts = amir_deals.value_counts("product")
print((counts / counts.sum()) * 100) # in percentage
# For instance, there are 34.8% product B will be chosen among all products

