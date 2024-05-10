import pandas as pd
import numpy as np
import matplotlib.pyplot as mplt

employeeFile = pd.read_csv('employee.csv')
employee_df = pd.DataFrame(employeeFile)
print(employee_df.describe()) # Summary of descriptive statistics
employee_df["annual_salary"] = employee_df["salary"] * 12


software_engineers = employee_df[employee_df["position"] == "Software Engineer"]
print("Mean Salary of Software Engineers")
print(software_engineers[["salary"]].mean())
print("Maximum Salary of Software Engineer")
print(software_engineers[["salary"]].max())
print("Minimum Salary of Software Engineer")
print(software_engineers["salary"].min())
print("Variance Salary of Software Engineer")
print(software_engineers["salary"].var()) # There
print("Standard Deviation Salary of Software Engineer")
print(software_engineers["salary"].std())
print("Third Quartile Salary of Software Engineer")
print(software_engineers["salary"].quantile(0.75))


def getFirstQuartile(column):
    return column.quantile(0.25)
def getSecondQuartile(column):
    return column.quantile(0.50)

# Using .agg to do aggregate calculations (computing summary statistics about each group)
# .agg also allows to apply custom functions for calculations
print("First Quartile Salary of Software Engineer")
print(getFirstQuartile(software_engineers["salary"])) # Can be done this way
print(software_engineers["salary"].agg(getFirstQuartile)) # Can be done this way too

# Multiple columns in single aggregation
print(software_engineers[["salary", "annual_salary"]].agg(getFirstQuartile))

# Multiple columns in multiple aggregation
print(software_engineers[["salary", "annual_salary"]].agg([getFirstQuartile, getSecondQuartile, "median", ]))

# Aggregations = mean(), sum(), size(), count(), std(), var(), describe(), first(), last(), nth(), min(), max()
# Non-aggregations = cumsum(), cumprod(), cummax(), cummin()

print("Latest Hired Date for Software Engineer")
print(software_engineers["hired_date"].min())

mplt.plot(software_engineers["salary"])
mplt.show()

common_positions = employee_df["position"].mode()
print("Most common job positions")
print(common_positions)

total_salary_being_distributed = employee_df["salary"].sum()
print("Total Monthly Salary being distributed")
print(total_salary_being_distributed)

total_salary_being_distributed_to_software_engineers = software_engineers["salary"].sum()
print(total_salary_being_distributed_to_software_engineers)

cumulative_sum_of_salary_for_software_engineers = software_engineers["salary"].cumsum()
print(cumulative_sum_of_salary_for_software_engineers)

software_engineers = software_engineers.copy()
software_engineers.loc[:, "cumulative_sum_max"] = software_engineers["salary"].cummax()