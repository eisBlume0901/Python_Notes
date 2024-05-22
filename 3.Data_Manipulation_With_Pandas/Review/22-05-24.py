import pandas as pd
import scipy as sp
import seaborn as sns

# Question 2, renaming columns
inventory_list = [
    {
        "type": "food",
        "name": "bread",
        "price": 2,
        "quantity": 4
    },
    {
        "type": "clothing",
        "name": "blue jeans",
        "price": 10,
        "quantity": 5
    },
    {
        "type": "chemical",
        "name": "boric acid",
        "price": 4,
        "quantity": 2
    }
]

inventory = pd.DataFrame(inventory_list)

print(inventory.columns)

inventory.columns = ["Type", "Name", "Price (PHP)", "Quantity"]

print(inventory.columns)
print(inventory.head())

# Question 3, sub-setting rows

# Version 1, in the problem
print(inventory[inventory["Type"] == "clothing"])
# Version 2, using .iloc
print(inventory.iloc[1])
# Version 3, using set_index and loc
print(inventory.set_index("Type").loc["clothing"])

# Question 6, using scipy (not tackled in the lesson YET)
print("Inter-quartile of Inventory Pricing")
print(sp.stats.iqr(inventory["Price (PHP)"]))

# Question 7, sub-setting multiple rows (with all column headers)
print(inventory.iloc[0:2])

# Question 11, sorting values in ascending order
print(inventory.sort_values("Price (PHP)", ascending=False))

# Question 14, sub-setting rows
print(inventory[inventory["Quantity"] >= 5])

# Question 15, using seaborn (not tackled under DataFrames with Pandas)