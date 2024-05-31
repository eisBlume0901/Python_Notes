import pandas as pd

# Semi-joins - does not include any columns from the second table but includes the matching data between two tables
# (it is not a left-join, NOTE IT IS MORE OF A FILTERING OPERATION rather THAN JOINING OPERATION)

# Steps of Semi Joins
# Load two dataframes you want to join
# Identify the common columns between two dataframes
# Use isin() function to filter rows from the first dataframe that have a MATCH in the second dataframe (this will return boolean Series)
# Use this boolean Series to index into first dataframe. This will return a filtered dataframe


animesFile = pd.read_csv('animes.csv')
animesGenresFile = pd.read_csv('anime_genres.csv')
genresFile = pd.read_csv('genres.csv')

animes = pd.DataFrame(animesFile)
animes_genres = pd.DataFrame(animesGenresFile)
genres = pd.DataFrame(genresFile)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited
pd.set_option('display.max_colwidth', None)  # None means unlimited

anime_and_its_genres = genres.merge(animes_genres, left_on="id", right_on="genre_id").merge(animes, left_on="anime_id", right_on="id")
print(anime_and_its_genres[["type", "anime_id", "title"]])

# The anime_and_its_genres contains anime and their respective genres. We then compare it to the genres dataframe to check which are the
most_common_genres_in_anime = genres[genres["type"].isin(anime_and_its_genres["type"])]
print(most_common_genres_in_anime)

# This is not related to the topic of semi-joins but it does show how many animes are there in a specific genre
top_genres_in_anime = anime_and_its_genres.groupby("type").agg({"type": "count"})
print(top_genres_in_anime)


# Anti-joins - does not include any columns from the second table but excludes the matching data or returns no matches between two tables

# Steps of Anti-Joins
# Load two dataframes
# Identify the common columns between two dataframes
# Use isin() function to filter rows from the first dataframe that does NOT HAVE A MATCH in the second dataframe
# Use this boolean series to index into first dataframe. This will return a filtered dataframe

# Note, indicator shows the source of each record. both means both are existing in two tables, left_only means existing only in left table
genres_in_anime = genres.merge(animes_genres, left_on="id", right_on="genre_id", how="left", indicator=True)
print(genres_in_anime)

genres_without_animes = genres_in_anime.loc[genres_in_anime["_merge"] == "left_only", "type"]
uncommon_genres_in_anime = genres[genres["type"].isin(genres_without_animes)]
print(uncommon_genres_in_anime)