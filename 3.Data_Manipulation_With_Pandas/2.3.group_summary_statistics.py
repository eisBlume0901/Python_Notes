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

print("Minimum, Maximum, Total, Average, and Median Salary of Each Position in Tech Industry")
print(employees.groupby("position")["salary"].agg(["min", "max", "sum", "mean", "median"]))

dogFile = pd.read_csv('dogs.csv')
dogs = pd.DataFrame(dogFile)

print("Average Weight of Each Dog Breeds")
print(dogs.groupby("breed")["weight_kg"].mean())

print("Minimum, Maximum, Total, Average, and Median Weight of Each Breed per Color")
print(dogs.groupby(["breed", "color"])["weight_kg"].agg(["min", "max", "sum", "mean", "median"]))

# DataCamp examples
data_analysts_salary = employees[employees["position"] == "Data Analyst"]["salary"].sum()
data_scientists_salary = employees[employees["position"] == "Data Scientist"]["salary"].sum()
product_managers_salary = employees[employees["position"] == "Project Manager"]["salary"].sum()
software_engineers_salary = employees[employees["position"] == "Software Engineer"]["salary"].sum()
total_salary = employees["salary"].sum()
proportion_of_salary = [data_analysts_salary, data_scientists_salary, product_managers_salary, software_engineers_salary] / total_salary
print(proportion_of_salary)