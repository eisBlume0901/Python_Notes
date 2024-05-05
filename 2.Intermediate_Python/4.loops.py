import numpy as np
import pandas as pd

# While loop
# repeating action until condition is met

error = 100.0

while error > 1:
    error = error / 4
    print(error)

# offset = -5 # Output would be -4, -3, -2, -1, 0
offset = 5 # Output would be 4, 3, 2, 1, 0
while offset != 0:
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)


# For loop (for each loop)
fruits = ["apple", "grapes", "strawberry", "banana", "orange", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
print(fruits[5], "\n")

# Rather than accessing the elements each which is tedious, use for each loop

# Looping a list
# Version 1 using for in
for fruit in fruits:
    print(fruit)

print()
# Version 2 using for in enumerate
for index, fruit in enumerate(fruits):
    print(str(index + 1) + ". " + str(fruit))
    if fruit.__eq__("mango"):
        print("My favorite fruit is " + fruit)

# Looping a 2d list using enumerate()
# enumerate() is generating a sequence of tuples, where each tuples contains an index and value
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

for x in house:
    print("the " + str(x[0]) + " is " + str(x[1]) + " sqm")

# Version 2 Using for in enumerate
for i, part in enumerate(house):
    # part[0] references to first column, part[1] references to second column
    print("the " + str(part[0]) + " is " + str(part[1]) + " sqm")

# Counter part in Java
# Map<String, Float> house = new HashMap<>();

# Use the put method to add entries to the map
# house.put("hallway", 11.25f);
# house.put("kitchen", 18.0f);
# house.put("living room", 20.0f);
# house.put("bedroom", 10.75f);
# house.put("bathroom", 9.50f);

# Use a for-each loop to iterate over the entries in the map
# For each entry, print out a message that includes the key (the room name)
# and the value (the room size)
# for (Map.Entry<String, Float> entry : house.entrySet()) {
#   System.out.println("The " + entry.getKey() + " is " + entry.getValue() + " sqm");
# }
 
# Looping a string
for character in "pythonista":
    print(character.capitalize())



# Looping Data Structures (Dictionary, Numpy, Pandas)
# Dictionary .items()
# Numpy .nditer()
# Panda .iterrow()

# Dictionary
south_east_asia_countries_info = {
    'Indonesia':
        {
            'Capital': 'Jakarta',
            'Area': 1904569,
            'Population': 273.5,
        },
    'Thailand':
        {
            'Capital': 'Bangkok',
            'Area': 513120,
            'Population': 69.8,
        },
    'Malaysia':
        {
            'Capital': 'Kuala Lumpur',
            'Area': 330803,
            'Population': 32.4,
        },
    'Singapore':
        {
            'Capital': 'Singapore',
            'Area': 722.5,
            'Population': 5.7
        },
    'Philippines':
        {
            'Capital': 'Manila',
            'Area': 300000,
            'Population': 110.8,
        },
    'Vietnam':
        {
            'Capital': 'Hanoi',
            'Area': 331212,
            'Population': 97.3
        },
    'Myanmar':
        {
            'Capital': 'Naypyidaw',
            'Area': 676578,
            'Population': 54.4
        },
    'Cambodia':
        {
            'Capital': 'Phnom Penh',
            'Area': 181035,
            'Population': 16.7
        },
    'Laos':
        {
            'Capital': 'Vietiane',
            'Area': 236800,
            'Population': 7.3
        },
    'Brunei':
        {
            'Capital': 'Bandar Seri Begawan',
            'Area': 236800,
            'Population': 0.4
        },
    'Norway':
        {
            'Capital': 'Oslo',
            'Area': 385207,
            'Population': 5.5
        }
}

# Version 3 using for in .items()
for key, value in south_east_asia_countries_info.items():
    print(str(key) + ": " + str(value))


# NumPy array
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2

# Version 1 for in loop for 1d array
for val in bmi:
    print(val)


meas = np.array([np_height, np_weight])

# Version 1 for in enumerate and using two nested for loops
for i, x in enumerate(meas):
    for j, y in enumerate(x):
        print(meas[i][j])

# Version 2 for in nditer(np_array) loop for 2d array
# nditer = nth dimensional iterator for arrays
for val in np.nditer(meas):
    print(val)

# Panda DataFrame
south_east_asia_dataframe = pd.read_csv('south_east_asia_countries_info.csv', index_col=0)
# Version 1 for in loop only iterates column headers
for key in south_east_asia_dataframe:
    print(key)

# Version 2 .iterrows() - iterate rows, returns dtype: object
for label, value in south_east_asia_dataframe.iterrows():
    print(label)
    print(value)

# Version 2 accessing column specific rows of data in this case, Capital
for label, row in south_east_asia_dataframe.iterrows():
    print(label + ": " + row['capital'])

# Version 3.A adding new column with rows of data
# Not recommended since we are creating new series in each iteration that only holds one data entry.
# This can affect the efficiency of dataframes.
for label, row in south_east_asia_dataframe.iterrows():
    # This creates a series on every iteration and adds a new column with rows of data (not in csv file)
    south_east_asia_dataframe.loc[label, 'name_length'] = len(row['country'])

print(south_east_asia_dataframe)

# Version 3.B adding new column with rows of data using .apply()
# Recommended since .apply() operates an entire row or column at once. Creating one series only
# It is like SQL or Excel wherein you apply the changes at once which is why it is faster than using iterrows()
south_east_asia_dataframe['name_length'] = south_east_asia_dataframe['country'].apply(len)
print(south_east_asia_dataframe)

south_east_asia_dataframe['COUNTRY'] = south_east_asia_dataframe['country'].apply(str.upper)
print(south_east_asia_dataframe)

