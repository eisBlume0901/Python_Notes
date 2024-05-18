import pandas as pd
import matplotlib.pyplot as plt

# This lesson shows how to make plots with pandas
# Note, pivot_table automatically calculates the mean
dogsFile = pd.read_csv('dogs_v1.csv')
dogs = pd.DataFrame(dogsFile)

# Frequency of Dogs in Certain Height Range from 2019 to 2022 using pivot_table
dogs["visited_date"] = pd.to_datetime(dogs["visited_date"])
dogs["year"] = dogs["visited_date"].dt.year
# dogs_height = dogs.pivot_table(values="height_cm", index="breed", columns="year", fill_value=0)
# print(dogs_height)
# dogs_height.hist(bins=5, edgecolor="white")
# plt.xlabel("Height (cm)")
# plt.ylabel("Height occurrence")
# plt.title("Frequency of Dogs in Certain Height Range from 2019 to 2022")
# plt.tight_layout()
# plt.show()

# Frequency of Dogs in Certain Height Range in 2020 using pivot_table
dogs_height_in_2020 = dogs[dogs["year"] == 2020]
dogs_height_v1 = dogs_height_in_2020.pivot_table(values="height_cm", index="breed", fill_value=0)
print(dogs_height_in_2020)
dogs_height_v1.hist(bins=5, edgecolor="white")
plt.xlabel("Height (cm)")
plt.ylabel("Height occurrence")
plt.title("Frequency of Dogs in Certain Height Range in 2020 Version 1")
plt.tight_layout()
plt.show()


# Frequency of Dogs in Certain Height Range in 2020 using set_index
dogs_height_in_2020_v1 = dogs[dogs["year"] == 2020]
dogs_height_v2 = dogs_height_in_2020_v1.set_index("breed").sort_index()
dogs_height_v2.drop_duplicates("name")["height_cm"].hist(bins=5, edgecolor="white")
plt.xlabel("Height (cm)")
plt.ylabel("Height occurrence")
plt.title("Frequency of Dogs in Certain Height Range in 2020 Version 2")
plt.tight_layout()
plt.show()

# Average Weight of Different Dog Breeds from 2019 to 2022 using pivot_table
dogs_weight_by_breed = dogs.pivot_table(values="weight_kg", index="breed", columns="year", fill_value=0)
print(dogs_weight_by_breed)
dogs_weight_by_breed.plot(kind="bar", rot=45)
plt.xlabel("Breed")
plt.ylabel("Weight (kg)")
plt.title("Average Weight of Different Dog Breeds from 2019 to 2022")
plt.tight_layout()
plt.show()

# Average Weight of Different Dog Breeds in 2021 using sex_index
dogs_weight_in_2021 = dogs[dogs["year"] == 2021]
dogs_weight = dogs_weight_in_2021.set_index("breed").sort_index()
dogs_weight.drop_duplicates("name")["weight_kg"].plot(kind="bar", rot=45)
plt.xlabel("Dog Breeds")
plt.ylabel("Weight (kg)")
plt.title("Average Weight of Different Dog Breeds in 2021")
plt.tight_layout()
plt.show()