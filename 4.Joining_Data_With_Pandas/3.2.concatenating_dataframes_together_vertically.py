import pandas as pd
import matplotlib.pyplot as plt

classicalMusicFile = pd.read_csv('classical_music.csv')
popMusicFile = pd.read_csv('pop_music.csv')

classical_music = pd.DataFrame(classicalMusicFile)
pop_music = pd.DataFrame(popMusicFile)


pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

all_musics = pd.concat([classical_music, pop_music])
print(all_musics)

# It sorts the columnar variable alphabetically (sort=True)
all_musics_sorted = pd.concat([classical_music, pop_music], sort=True)
print(all_musics_sorted)

# It ignores the original index and increments them (ignore_index=True)
all_musics_with_proper_index = pd.concat([classical_music, pop_music], ignore_index=True, sort=True)
print(all_musics_with_proper_index)

# It merges all tables that has matching columnar headers (join="inner")
all_musics_and_duration = pd.concat([classical_music, pop_music], join="inner", ignore_index=True, sort=True)
print(all_musics_and_duration)

juneExpensesFile = pd.read_csv('june_expenses.csv')
julyExpensesFile = pd.read_csv('july_expenses.csv')
augustExpensesFile = pd.read_csv('august_expenses.csv')

june_exp = pd.DataFrame(juneExpensesFile)
july_exp = pd.DataFrame(julyExpensesFile)
august_exp = pd.DataFrame(augustExpensesFile)

# It allows you to put a hierarchical index or multilevel index
# keys allows set a multilevel index
three_month_expenses = pd.concat([june_exp, july_exp, august_exp], keys=["6Jun", "7Jul", "8Aug"])
print(three_month_expenses)

# level=0 groups the DataFrame by the first level of the multi-index which is the keys we declared
# note we can change the level value but the outer level which is 0 (keys) makes sense to get the average of expenses per month
avg_expense_per_month = three_month_expenses.groupby(level=0).agg({"cost": "mean"})
print(avg_expense_per_month)

# To see the expense per month, it must have keys and groupby level=0
avg_expense_per_month.plot(kind="bar")
plt.show()