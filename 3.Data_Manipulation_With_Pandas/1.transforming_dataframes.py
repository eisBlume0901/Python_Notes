import pandas as pd

# INCLUDES TOPIC about sorting values of a dataframe
employeeFile = pd.read_csv('employee.csv')
employee_df = pd.DataFrame(employeeFile)
print(employee_df.head()) # Returns the first 5 data
print(employee_df.head(10)) # Returns the first 10 data
print(employee_df.info()) # Displays the name and type of columns (This is quite the same with SQL using terminal based)
print(employee_df.shape) # Returns the number of rows and column of a dataframe datastructure, shape is an attribute not a method
print(employee_df.describe()) # Returns a descriptive statistics of integer such as count, mean, std, min, max, quartile
print(employee_df.values) # Returns the value (rows of data in 2d array), values is an attribute not a method
print(employee_df.columns) # Returns the name of index and their dtype, columns is an attribute not a method
print(employee_df.index) # Returns row number, start means the starting index, stop means the ending index, and step is the interval
print(employee_df.sort_values("salary", ascending=False)) # Sort the dataframe as defined by the column (This is the same with SQL in terms of ORDER BY keyword)
print(employee_df.sort_values(["salary", "hired_date"], ascending=[False, True])) # Sort the dataframe defined by the first column being applied and then the nth column
print(employee_df["name"]) # Returns subset of name from the employee_df (sub-setting single column)
print(employee_df[["name", "position"]]) # Returns subset of name and position from the employee_df (sub-setting multiple columns)

employee_name_position = ["name", "position"]
print(employee_df[employee_name_position]) # Subsetting using a list variable

salary_greater_than_70000 = employee_df["salary"] > 70000
print(employee_df[salary_greater_than_70000]) # Subsetting using logical condition for numerical values

hired_date_before_2021 = employee_df["hired_date"] < "2021-01-01"
print(employee_df[hired_date_before_2021]) # Subsetting using logical condition for String values (date specific)

employee_named_ava = employee_df["name"] == "Ava Taylor"
print(employee_df[employee_named_ava]) # Subsetting using logical condition for String values

software_engineers = employee_df["position"] == "Software Engineer"
employee_amelia_garcia = employee_df["name"] == "Amelia Garcia"
print(employee_df[software_engineers | employee_amelia_garcia]) # Subsetting using logical condition with logical operators (| = or), can use np.logical_or()
print(employee_df[software_engineers & employee_amelia_garcia]) # Subsetting using logical condition with logical operators (& = and), can use np.logical_and()
print(employee_df[ (employee_df["position"] == "Data Scientist") & (employee_df["salary"] == 82000) ])

# Subsetting using .isin()
# SQL counterpart is IN keyword
data_analysts_and_data_scientists = employee_df["position"].isin(["Data Analyst", "Data Scientist"])
print(employee_df[data_analysts_and_data_scientists])

# Adding columns in dataframes
employee_df["annual_salary"] = employee_df["salary"] * 12
# Name the new column and assign a value (in this case, we assigned values based form the salary and use mathematical
# operator to produce new value)
print(employee_df)

# Multiple manipulations with pandas (sorting rows, sub-setting columns, sub-setting rows, adding new columns)
high_salary_employees = employee_df[employee_df["salary"] > 75000]
newly_high_salary_employees = high_salary_employees.sort_values("hired_date", ascending=False)
print(newly_high_salary_employees[["name", "salary", "hired_date"]].head())
