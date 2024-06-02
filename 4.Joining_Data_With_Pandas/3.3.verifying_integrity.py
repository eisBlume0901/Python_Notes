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

anime_and_its_genres = animes.merge(anime_genres, left_on="id", right_on="anime_id", validate='one_to_many', suffixes=("_a", "_ag")).merge(genres, left_on="id_ag", right_on="id", suffixes=("_ag1", "g"), validate="one_to_many")
print(anime_and_its_genres[["title", "studio", "type"]]) # It is expected to not return any errors

# anime_and_its_genres_v1 = animes.merge(anime_genres, left_on="id", right_on="anime_id", validate='many_to_one', suffixes=("_a", "_ag")).merge(genres, left_on="id_ag", right_on="id", suffixes=("_ag1", "g"), validate="one_to_many")
# It is expected to return an error of pandas.errors.MergeError: Merge keys are not unique in right dataset; not a many-to-one merge (since I change the first merge from one_to_many to many_to_one
# The relationship is one_to_many because one anime has many genres

juneExpensesFile = pd.read_csv('june_expenses.csv')
julyExpensesFile = pd.read_csv('july_expenses.csv')
augustExpensesFile = pd.read_csv('august_expenses.csv')

june_exp = pd.DataFrame(juneExpensesFile)
july_exp = pd.DataFrame(julyExpensesFile)
august_exp = pd.DataFrame(augustExpensesFile)

# With verify_integrity, we can also implement the anti and semi joins for further analysis
three_month_expenses = pd.concat([june_exp, july_exp, august_exp], ignore_index=True, verify_integrity=True)
print(three_month_expenses) # If index is not ignored, it will throw an error ValueError: Indexes have overlapping values: Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='int64')

three_month_expenses_v1 = pd.concat([june_exp, july_exp, august_exp], keys=["June", "July", "August"], verify_integrity=True)
print(three_month_expenses_v1)