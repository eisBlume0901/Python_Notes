import pandas as pd
import matplotlib.pyplot as plt

# .query() in pandas is similar to SQL query statements, but not exactly the same. It allows for filtering data
# using string expressions.

# .merge(), .merge_asof(), .merge_ordered(), and .concat() in pandas provide functionality similar to SQL's joins,
# but they are not exactly the same. They are used to combine different DataFrames along a particular column (or index).
# Summary statistics can indeed be calculated with these methods, similar to SQL. However, the way these statistics are
# calculated and used can differ between pandas and SQL.
# One advantage of pandas over SQL is the ability to integrate data manipulation and analysis with visual graph creation,
# which is not directly possible in SQL.

animeFile = pd.read_csv('animes.csv', index_col=0)
animeGenresFile = pd.read_csv('anime_genres.csv', index_col=0)
genresFile = pd.read_csv('genres.csv', index_col=0)

animes = pd.DataFrame(animeFile)
anime_genres = pd.DataFrame(animeGenresFile)
genres = pd.DataFrame(genresFile)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

animes_and_its_genres = animes.merge(anime_genres, left_index=True, right_on="anime_id", how="inner", suffixes=("", "_ag")).merge(genres, left_on="genre_id", right_index=True, how="inner", suffixes=("_a", "_g"))
print(animes_and_its_genres)

print("Adventure Animes")
print(animes_and_its_genres.query('type == "Adventure"'))

print("Fantasy Animes from Madhouse")
print(animes_and_its_genres.query('type == "Fantasy" and studio == "Madhouse"'))

gdpUSAGermanyFile = pd.read_csv('gdp_usa_germany_dummy_data.csv')
popUSAGermanyFile = pd.read_csv('pop_usa_germany_dummy_data.csv')

gdp_us_ger = pd.DataFrame(gdpUSAGermanyFile)
pop_us_ger = pd.DataFrame(popUSAGermanyFile)

gdp_pop = pd.merge_ordered(gdp_us_ger, pop_us_ger, on=["country", "date"], fill_method="ffill", suffixes=("_g", "_p"))
print(gdp_pop)
gdp_pop["gdp_per_capita"] = gdp_pop["gdp"] / gdp_pop["pop"]
print(gdp_pop)

# Go back to Data Manipulation with Pandas > 2.4.pivot_tables.py (we do not need to declare the variables values, index, and columns as long as they are in order)
gdp_pop_pivot = gdp_pop.pivot_table("gdp_per_capita", "date", "country")
print(gdp_pop_pivot)

gdp_pop_pivot.plot(rot=90)
plt.show() # Expect it to be linear since the population is only increasing from 2000s to today's unlike in 90's

recent_gdp_pop_in_5_years = gdp_pop_pivot.query('date >= "2014"')
recent_gdp_pop_in_5_years.plot(rot=90)
plt.show() # Expect it to be linear since the population is only increasing from 2000s to today's unlike in 90's