import pandas as pd

animesFile = pd.read_csv('animes.csv')
animeGenresFile = pd.read_csv('anime_genres.csv')
genresFile = pd.read_csv('genres.csv')

animes = pd.DataFrame(animesFile)
anime_genres = pd.DataFrame(animeGenresFile)
genres = pd.DataFrame(genresFile)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

# Outer join is opposite of inner join which joins both left and right regardless if each of them contains null, expect both sides to return null
fantasy_genre = anime_genres[anime_genres["genre_id"] == 5]
fantasy_animes = animes.merge(fantasy_genre, how="outer", left_on="id", right_on="anime_id", suffixes=("_a", "_ag"))
print(fantasy_animes)
