import pandas as pd
import matplotlib.pyplot as plt

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

genre_animes = anime_genres.merge(animes, how="right", left_on="anime_id", right_on="id", suffixes=("_ag", "_a"))
print(genre_animes)
genre_count = genre_animes.groupby("genre_id").agg({'anime_id' : 'count'})
genre_count.plot(kind="bar")
plt.tight_layout()
plt.show()

genre_animes_with_name = genre_animes.merge(genres, how="left", left_on="genre_id", right_on="id", suffixes=("_ag2", "_g"))
print(genre_animes_with_name)
