import matplotlib.pyplot as plt
import pandas as pd

# Figure - container, axis - data and its points
figure, axis = plt.subplots()
plt.show()

english_grades_section_A = [90, 85, 94, 88, 89, 93, 91, 85, 87, 94, 91, 98]
english_grades_section_B = [75, 83, 86, 77, 71, 84, 75, 84, 83, 77, 76, 83]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
gdp_country1 = [1.2, 1.3, 1.5, 1.7, 1.6, 1.5, 1.4, 1.6, 1.8, 1.9, 2.1, 2.3]  # GDP for country 1
gdp_country2 = [0.9, 1.0, 1.1, 1.3, 1.2, 1.1, 1.0, 1.2, 1.4, 1.5, 1.7, 1.9]  # GDP for country 2

# Version 1 using .hist() to create histograms, messy
figure1, axis1 = plt.subplots()
pd.Series(english_grades_section_A).hist(bins=3, edgecolor="white", alpha=0.7, color="orange", ax=axis1)
pd.Series(english_grades_section_B).hist(bins=3, edgecolor="white", alpha=0.7, color="blue", ax=axis1)
plt.xlabel("English Grades")
plt.ylabel("Number of Students (Occurrences)")
plt.title("English Grades of Section A and B")
plt.legend(["A", "B"])
plt.show()

plt.plot(pd.Series(months), pd.Series(gdp_country1), color="red", marker="o", linestyle="--")
plt.plot(pd.Series(months), pd.Series(gdp_country2), color="green", marker="v", linestyle="--")
plt.xlabel("Months")
plt.ylabel("GDP")
plt.title("GDP per Month of Country 1 and Country 2")
plt.legend(["1", "2"])
plt.show()

# Version 2 - can add more data using .hist() to create histograms, cleaner approach and allow more control over the plot
figure2, axis2 = plt.subplots()
axis2.hist(english_grades_section_A, bins=3, alpha=0.7, label='Section A', color="orange")
axis2.hist(english_grades_section_B, bins=3, alpha=0.7, label='Section B', color="blue")
axis2.set_xlabel("English Grades")
axis2.set_ylabel("Number of Students (Occurrences)")
axis2.set_title("English Grades of Section A and B")
axis2.legend(["A", "B"])
plt.show()

figure3, axis3 = plt.subplots()
axis3.plot(pd.Series(months), pd.Series(gdp_country1), label="Country 1", color="red", marker="o", linestyle="--")
axis3.plot(pd.Series(months), pd.Series(gdp_country2), label="Country 2", color="green", marker="v", linestyle="--")
axis3.set_xlabel("Months")
axis3.set_ylabel("GDP")
axis3.set_title("GDP per Month of Country 1 and Country 2")
axis3.legend(["1", "2"])
plt.show()


# .plot = linear
# .hist = histogram
# .scatter = scatter plot
