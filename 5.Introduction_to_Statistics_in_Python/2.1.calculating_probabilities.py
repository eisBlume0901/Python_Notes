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