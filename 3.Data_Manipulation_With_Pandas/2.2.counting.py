import pandas as pd

dogFile = pd.read_csv('dogs.csv')
dog_df = pd.DataFrame(dogFile)

print(dog_df.shape)  # 29, 4

dog_names = dog_df.drop_duplicates(subset="name") # SELECT DISTINCT name FROM dogs;
print(dog_names.shape)  # 10, 4

unique_dogs = dog_df.drop_duplicates(subset=["name", "breed"]) # SELECT DISTINCT name, breed FROM dogs;
print(unique_dogs.shape) # 19, 4
print(unique_dogs["breed"].value_counts(sort=True)) # Counts the number of selected parameter to be countered
# and sorts (optional) the value in descending order

print(unique_dogs["breed"].value_counts(normalize=True)) # Returns relative frequencies of the unique values with respect to breed
# (proportion not frequency, if frequency expect it to be a whole number)

dog_df["is_light"] = dog_df["weight_kg"] < 60
light_dogs = dog_df[dog_df["is_light"]].drop_duplicates("visited_date") # It returns the date when does light dogs visit
print(light_dogs.shape) # 19, 5

