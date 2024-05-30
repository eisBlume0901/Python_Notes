import pandas as pd

# When merging two dataframes, it is often useful to have common index on both. This way, the merge
# operation can correctly align the rows without even using the left_on and right_on

# Note, can also set multiple index_col=[] and use them for the merging using the on-keyword
animesFile = pd.read_csv('animes.csv', index_col='id')
quotesFile = pd.read_csv('quotes.csv', index_col='id')

animes = pd.DataFrame(animesFile)
quotes = pd.DataFrame(quotesFile)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited
pd.set_option('display.max_colwidth', None)  # None means unlimited

animes_quotes = animes.merge(quotes, on="id")
print(animes_quotes)

# Alternative Version 1
anime_quotes_v1 = animes.merge(quotes, left_index=True, right_index=True)
print(anime_quotes_v1)

animesFile1 = pd.read_csv('animes.csv', index_col="id")
animeGenres = pd.read_csv('anime_genres.csv', index_col="id")
genres = pd.read_csv('genres.csv')

animes_v1 = pd.DataFrame(animesFile1)
anime_genres = pd.DataFrame(animeGenres)
genres = pd.DataFrame(genres)

# Note left_index is an alternative for left_on which uses the index we set while we read our csv files
anime_genres = animes_v1.merge(anime_genres, left_index=True, right_on="anime_id")
