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

print(animes.shape)
print(anime_genres.shape)
print(genres.shape)

merged_anime_genres = animes.merge(anime_genres, left_on="id", right_on="anime_id", suffixes=("_a", "_ag"))
print(merged_anime_genres.shape)
print(merged_anime_genres)

action_genre = anime_genres[anime_genres["genre_id"] == 4]
print(action_genre)


drama_animes = action_genre.merge(animes, how="right", left_on="anime_id", right_on="id", suffixes=("_a", "_ag")).merge(genres, left_on="genre_id", right_on="id")
print(drama_animes[["type", "title"]])

drama_animes = action_genre.merge(animes, how="right", left_on="anime_id", right_on="id", suffixes=("_a", "_ag"))
print(drama_animes)

