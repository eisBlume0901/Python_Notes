import pandas as pd


# Question 4, using seaborn (not tackled under DataFrames with Pandas)

# Question 5, go to 2.1.summary_statistics.py to know how to rename columns

list_of_dicts = [
    {
        "nAmE": "Emerald Dendron",
        "MaJoR": "Biochemistry"
    },
    {
        "nAmE": "Claire Ethereal",
        "MaJoR": "Neuroscience"
    }
]

students = pd.DataFrame(list_of_dicts)
print(students.columns)

students_v1 = students.rename(columns={"nAmE" : "Name" , "MaJoR": "Major"})
print(students_v1.columns)

# Question 6, using seaborn (not tackled under DataFrames with Pandas)

# Question 10, go to 3.2.slicing_and_subsetting_with_iloc_and_loc.py (it is highly related but it is not yet tackled this kind
# of subsetting for columns without iloc and loc)

print(students_v1[["Name"]])

# Question 15, using seaborn (not tackled under DataFrames with Pandas)
