import pandas as pd

dogFile = pd.read_csv('dogs.csv')
dogs = pd.DataFrame(dogFile)

# Pivot_Tables and GroupBy as opposed with setting multiple indices, are already sorted
dogs_height_by_breed_vs_color = dogs.pivot_table("weight_kg", index="breed", columns="color", margins=True, fill_value=0)
# Calculates the mean across row AND column of existing ROW and COLUMN in pivot go back to
# topic 2.4 pivot_tables.py (compare it with groupby)
print(dogs_height_by_breed_vs_color)

# Retrieves the mean of the pivot_table through index (calculating mean across row)
dog_colors = dogs_height_by_breed_vs_color.mean(axis="index") # Calculates the mean of different breeds with the same color
print(dog_colors)

# Retrieves the mean of the pivot_table through column (calculating mean across column)
print(dogs_height_by_breed_vs_color.mean(axis="columns")) # Calculates the mean of different colors with the same breed

# Retrieves the maximum height in each dog breed type
print(dogs_height_by_breed_vs_color.max(axis="columns"))

# Retrieves the minimum height in each dog breed type
print(dogs_height_by_breed_vs_color.min(axis="columns"))

# Ensure the 'visited_date' column is of datetime type
dogs['visited_date'] = pd.to_datetime(dogs['visited_date'])

# Extract the year from the 'visited_date' column
dogs['visited_date_year'] = dogs['visited_date'].dt.year
print(dogs)

# Extract the month from the 'visited_date' column
dogs['visited_date_month'] = dogs['visited_date'].dt.month
print(dogs)


# Sub-setting with pivot tables, could also subset with tuples
# review topic of 3.2 slicing_and_subsetting_with_iloc_and_loc.py
print(dogs_height_by_breed_vs_color.loc["Beagle":"Chow Chow"])
print(dogs_height_by_breed_vs_color.loc["Beagle":"Chow Chow", "Black":"Blue"])