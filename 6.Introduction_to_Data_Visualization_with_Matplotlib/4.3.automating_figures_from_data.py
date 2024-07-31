import matplotlib.pyplot as plt
import pandas as pd

summer_medals_2016 = pd.read_csv('summer2016.csv')
summer_medals_2016_df = pd.DataFrame(summer_medals_2016)
print(summer_medals_2016_df.head(3))

# What are the sports that are held in summer event last 2016?
sports = summer_medals_2016_df["Sport"].unique()
print(sports)

figure, axis = plt.subplots()
figure.set_size_inches([25, 10])

for sport in sports:
    sport_df = summer_medals_2016_df[summer_medals_2016_df["Sport"] == sport]
    axis.bar(sport, sport_df["Height"].mean(), yerr=sport_df["Height"].std())

axis.set_ylabel("Height (cm)")
axis.set_xticklabels(sports, rotation=45)
plt.tight_layout()
plt.show()

figure.savefig("summer_sports_average_height_and_standard_deviation.jpg")