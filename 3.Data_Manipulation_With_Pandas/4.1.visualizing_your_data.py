import pandas as pd
import matplotlib.pyplot as plt

# This lesson shows how to make plots with pandas
# Note, pivot_table automatically calculates the mean
# Note, always create a subset if you want to pivot_table of a specific category,
# in this context, dogs_height_in_2020 was created to create a pivot table and create a plot
dogsFile = pd.read_csv('dogs_v1.csv')
dogs = pd.DataFrame(dogsFile)

dogs["visited_date"] = pd.to_datetime(dogs["visited_date"])
dogs["year"] = dogs["visited_date"].dt.year

# Frequency of Dogs in Certain Height Range from 2019 to 2022 using pivot_table
# dogs_height = dogs.pivot_table(values="height_cm", index="breed", columns="year", fill_value=0)
# print(dogs_height)
# dogs_height.hist(bins=5, edgecolor="white")
# plt.xlabel("Height (cm)")
# plt.ylabel("Height occurrence")
# plt.title("Frequency of Dogs in Certain Height Range from 2019 to 2022")
# plt.tight_layout()
# plt.show()

# Frequency of Dogs in Certain Height Range in 2020 using pivot_table
dogs_height_in_2020 = dogs[dogs["year"] == 2020] # We can subset by setting indices and using .loc
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
dogs_height_v2.drop_duplicates("name")["height_cm"].hist(bins=5, edgecolor="white", color="red")
plt.xlabel("Height (cm)")
plt.ylabel("Height occurrence")
plt.title("Frequency of Dogs in Certain Height Range in 2020 Version 2")
plt.tight_layout()
plt.show()

# Frequency of Dogs in Certain Height Range in 2020 using groupby
dogs_height_in_2020_v2 = dogs[dogs["year"] == 2020]
dogs_height_v3 = dogs_height_in_2020_v2.groupby("breed")["height_cm"].mean()
dogs_height_v3.hist(bins=5, edgecolor="white", color="yellow")
plt.xlabel("Height (cm)")
plt.ylabel("Height occurrence")
plt.title("Frequency of Dogs in Certain Height Range in 2020 Version 3")
plt.tight_layout()
plt.show()



# Average Weight of Different Dog Breeds from 2019 to 2022 using pivot_table
# dogs_weight_by_breed = dogs.pivot_table(values="weight_kg", index="breed", columns="year", fill_value=0)
# print(dogs_weight_by_breed)
# dogs_weight_by_breed.plot(kind="bar", rot=45)
# plt.xlabel("Breed")
# plt.ylabel("Weight (kg)")
# plt.title("Average Weight of Different Dog Breeds from 2019 to 2022")
# plt.tight_layout()
# plt.show()

# Average Weight of Different Dog Breeds in 2021 using sex_index
dogs_weight_in_2021 = dogs[dogs["year"] == 2021]
dogs_weight = dogs_weight_in_2021.set_index("breed").sort_index()
dogs_weight.drop_duplicates("name")["weight_kg"].plot(kind="bar", rot=45, color="orange")
plt.xlabel("Dog Breeds")
plt.ylabel("Weight (kg)")
plt.title("Average Weight of Different Dog Breeds in 2021 Version 1")
plt.tight_layout()
plt.show()

# Average Weight of Different Dog Breeds in 2021 using groupby
dogs_weight_in_2021_v1 = dogs[dogs["year"] == 2021]
dogs_weight_v2 = dogs_weight_in_2021_v1.groupby("breed")["weight_kg"].mean()
dogs_weight_v2.plot(kind="bar", rot=45, color="violet")
plt.xlabel("Dog Breeds")
plt.ylabel("Weight (kg)")
plt.title("Average Weight of Different Dog Breeds in 2021 Version 2")
plt.tight_layout()
plt.show()



# Line plot of Dogs for 4 years using pivot_table
dogs_weight = dogs.pivot_table(values="weight_kg", index="name", columns="year",  fill_value=0)
print(dogs_weight)
dogs_weight.plot(rot=45)
plt.xlabel("Dog Names")
plt.ylabel("Weight (kg)")
plt.tight_layout()
plt.show()

# Line plot of Charlie's Weight for 4 years using pivot_table
charlie_the_beagle = dogs[dogs["name"] == "Charlie"]
charlie_the_beagle_weight = charlie_the_beagle.pivot_table(values="weight_kg", index="year", fill_value=0)
charlie_the_beagle_weight.plot(rot=45) # Alternative to use .plot()
plt.xticks([2019, 2020, 2021, 2022], ["2019", "2020", "2021", "2022"])
plt.xlabel("Years")
plt.ylabel("Weight (kg)")
plt.title("Weight of Charlie from 2019 to 2022 Version 1")
plt.tight_layout()
plt.show()

# Line plt of Charlie's Weight for 4 years using set_index
charlie_the_beagle_weight_v1 = charlie_the_beagle.set_index("year").sort_index()
charlie_the_beagle_weight_v1.plot(y="weight_kg", rot=45)
plt.xticks([2019, 2020, 2021, 2022], ["2019", "2020", "2021", "2022"])
plt.xlabel("Years")
plt.ylabel("Weight (kg)")
plt.title("Weight of Charlie from 2019 to 2022 Version 2")
plt.show()

# Line plt of Charlie's Weight for 4 years using groupby
charlie_the_beagle_weight_v2 = charlie_the_beagle.groupby("year")["weight_kg"].mean()
charlie_the_beagle_weight_v2.plot(kind="line", rot=45)
plt.xlabel("Years")
plt.ylabel("Weight (kg)")
plt.title("Weight of Charlie from 2019 to 2022 Version 3")
plt.tight_layout()
plt.show()



# Scatter plot
# dogs.plot(x="height_cm", y="weight_kg", kind="scatter") # Version 1
plt.scatter(x=dogs["height_cm"], y=dogs["weight_kg"]) # Version 2
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Relationship between Dogs' Height and Weight")
plt.show()



# Layering plots
dogs[dogs["sex"] == "Male"]["height_cm"].hist(bins=5, edgecolor="white", alpha=0.7)
dogs[dogs["sex"] == "Female"]["height_cm"].hist(bins=5, edgecolor="white", alpha=0.7)
plt.legend(["M", "F"])
plt.xlabel("Height (cm)")
plt.title("Relationship between Dogs' Height and Weight")
plt.show()