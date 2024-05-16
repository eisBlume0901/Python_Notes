import pandas as pd
import numpy as np

dogFile = pd.read_csv('dogs.csv')
dogs = pd.DataFrame(dogFile)

# Sub-setting and slicing with iloc
# review topic under Intermediate Python, 2.dictionaries_and_pandas.py
# Version 1 - In this case, all are included until row 4 and column 4
print(dogs.iloc[[1, 2, 3, 4], [0, 1, 2, 3, 4]])
# Version 2 - In this case, it is inclusive start and exclusive end (Slicing method)
print(dogs.iloc[1:5, 0:5])
# Version 3 - Using loc / label based index (Slicing method)
print(dogs.loc[:, "name":"breed"])

# Can only sort and slice if its sorted which makes sense because if we just
# set the index without sorting it would not be able to specify the start and end labels
dogs_in_order = dogs.set_index(["breed", "color"]).sort_index(level=["breed", "color"])

# Slicing based on the outer index
# it is inclusive start and inclusive end
print(dogs_in_order.loc["German Shepherd":"Golden Retriever"])

# Slicing based on the inner index (using tuples)
print(dogs_in_order.loc[("German Shepherd", "Black"):("Golden Retriever", "Brown")])

# Slicing based on the inner index (using tuples) for rows with specified column
print(dogs_in_order.loc[("German Shepherd", "Black"):("Golden Retriever", "Brown"), "name":"weight_kg"])


# Slicing with dates, use ISO 8601 Format or yyyy-mm-dd
visited_dates_of_dogs = dogs.set_index("visited_date").sort_index()
print(visited_dates_of_dogs)

# Slicing with full dates
print(visited_dates_of_dogs.loc["2019-01-01": "2020-01-01"])
# Slicing with year dates
print(visited_dates_of_dogs.loc["2019":"2020"])


# Slicing with dates without using index values
# review Intermediate Python, 3.logic_control-flow_and_filtering
# Version 1
print(dogs[ (dogs["visited_date"] >= "2019") & (dogs["visited_date"] <= "2020") ]) # Was able to retrieve but not in sorted order
# Version 2 (using np.logical_and and np.logical_or)
print(dogs[np.logical_and(dogs["visited_date"] >= "2019", dogs["visited_date"] <= "2020")])