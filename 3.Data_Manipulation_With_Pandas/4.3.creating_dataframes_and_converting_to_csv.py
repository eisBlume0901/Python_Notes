import pandas as pd

# There are two types of creating dataframes
# From a list of dictionaries (row based)
# If the number of data in each dictionary is not matched, it will simply return NaN
list_of_dogs = [
    {
        "name": "Ginger",
        "breed": "Dachshund",
        "height_cm": 22,
        "weight_kg": 10,
        "date_of_birth": "2019-03-14"
    },
    {
        "name": "Scout",
        "breed": "Dalmatian",
        "height_cm": 59,
        "weight_kg": 25,
        "date_of_birth": "2019-05-09"
    }
]

dogs_v1 = pd.DataFrame(list_of_dogs)
print(dogs_v1)

# From a dictionary of lists (column based)
# If each array does not match, it will return a ValueError: All arrays must be of the same length
dictionary_of_dogs = {
    "name": ["Ginger", "Scout"],
    "breed": ["Dachshund", "Dalmatian"],
    "height_cm": [22, 59],
    "weight_kg": [10, 25],
    "date_of_birth": ["2019-03-14", "2019-05-09"]
}

dogs_v2 = pd.DataFrame(dictionary_of_dogs)
print(dogs_v2)


# CONVERTING DATAFRAME to CSV file
# Create a new blank .csv file for the DataFrame's data to fill in
dogs_v1.to_csv('dogs_v2.csv')
