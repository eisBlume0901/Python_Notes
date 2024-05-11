import pandas as pd

employeeFile = pd.read_csv('employee.csv')
employees = pd.DataFrame(employeeFile)

# Version 1
print("Average Salary of Software Engineer")
print("Data Analyst ", employees[employees["position"] == "Data Analyst"]["salary"].mean())
print("Data Scientist ", employees[employees["position"] == "Data Scientist"]["salary"].mean())
print("Product Manager ", employees[employees["position"] == "Project Manager"]["salary"].mean())
print("Software Engineer ", employees[employees["position"] == "Software Engineer"]["salary"].mean())


# Version 2 - Improved version
print("Average Salary of Each Position in a Tech Industry")
print(employees.groupby("position")["salary"].mean())