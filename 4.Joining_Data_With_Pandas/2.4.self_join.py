import pandas as pd

# self join commonly used in hierarchical data (employee - manager relationship),
# sequential data (time series data to compare a row with subsequent rows),
# data analysis and data cleaning (find and analyze duplicate, similar, or missing data within the same table),
# network data (where nodes are connected, self join can be used to find connections between different nodes (social networking)

employeesFile = pd.read_csv('employees.csv')

employees = pd.DataFrame(employeesFile)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

employees_managers = employees.merge(employees, how="left", left_on="manager_id", right_on="id", suffixes=("_employee", "_manager"))
print(employees_managers[["full_name_employee", "salary_employee", "full_name_manager", "salary_manager"]])