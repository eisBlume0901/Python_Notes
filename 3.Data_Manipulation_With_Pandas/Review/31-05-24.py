import pandas as pd

# Question 2 - subsetting dataframes
# mistake, typographical error only

# Answer: sales_2019 = sales[sales["year"] == 2019]
# Correct answer: sales_2019 = sales[sales["Year"] == 2019]

# Question 3, Seaborn related (not yet tackled)

# Question 4, go to 1.transforming_dataframes.py under .index and .column

# .index returns row data such as RangeIndex(start=0, stop=15, step=1)
# .column returns column header data such as Index(['name', 'position', 'salary', 'hired_date'], dtype='object')

employees = [
    {
        "name": "Claire Ethereal",
        "position": "Data Analyst",
        "salary": "90000",
        "hired_date": "2022-09-01"
    }
]

employees_df = pd.DataFrame(employees)
print(employees_df.columns)
print(employees_df.index)

# Question 12, Seaborn related (not yet tackled)

# Question 13, Seaborn related (not yet tackled)

