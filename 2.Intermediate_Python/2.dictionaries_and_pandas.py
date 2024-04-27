import pandas as pd

# Dictionary vs List
# Population in millions, area in square kilometers
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

# Accessing a value element using keys
print(south_east_asia_countries_info['Philippines'])
print(south_east_asia_countries_info['Philippines']['Population'])

# Printing keys of a dictionary
print(south_east_asia_countries_info.keys())

# Deleting a key-value pair
del(south_east_asia_countries_info['Norway'])

# Changing the value of an existing key
south_east_asia_countries_info['Philippines'] = 109.0

south_east_asia_countries = ['Indonesia', 'Thailand', 'Malaysia', 'Singapore', 'Philippines', 'Vietnam', 'Myanmar',
                             'Cambodia', 'Laos', 'Brunei'] # Can be converted to dictionary
south_east_asia_pop = [273.5, 69.8, 32.4, 5.7, 110.8, 97.3, 54.4, 16.7, 7.3, 0.4]  # in millions

ind_phil = south_east_asia_countries.index('Philippines')
# Accessing a value element using index
print(south_east_asia_pop[ind_phil])

# Pandas
# Dictionary can be converted as Pandas' DataFrame
# When working with dataframes, remember that the keys correspond to column names and their associated values represent
# the data in each row.
south_east_asia_countries_dataFrame_v1 = pd.DataFrame(south_east_asia_countries_info)
print(south_east_asia_countries_dataFrame_v1)
print()


# This is how the dictionary must be initialized and assigned to
south_east_asia_countries_info_v2 = {
    'Countries': ['Indonesia', 'Thailand', 'Malaysia', 'Singapore', 'Philippines', 'Vietnam', 'Myanmar', 'Cambodia', 'Laos', 'Brunei'],
    'Capital': ['Jakarta', 'Bangkok', 'Kuala Lumpur', 'Singapore', 'Manila', 'Hanoi', 'Naypyidaw', 'Phnom Penh', 'Vietiane', 'Bandar Seri Begawan'],
    'Area': [1904569, 513120, 330803, 722.5, 300000, 331212, 676578, 181035, 236800, 5765],
    'Population': [273.5, 69.8, 32.4, 5.7, 110.8, 97.3, 54.4, 16.7, 7.3, 0.4]
}

south_east_asia_countries_dataFrame_v2 = pd.DataFrame(south_east_asia_countries_info_v2)
print(south_east_asia_countries_dataFrame_v2)
print()

# Instead of using row index based, it can be changed to row label based
south_east_asia_countries_dataFrame_v2.index = ['ID', 'TH', 'MY', 'SG', 'PH', 'VN', 'MM', 'KH', 'LA', 'BN']
print(south_east_asia_countries_dataFrame_v2)
print()

# Importing csv file to DataFrame using .read_csv() method
south_east_asia_countries_imported_from_csv_dataFrame_v3 = pd.read_csv('south_east_asia_countries_info.csv')
print(south_east_asia_countries_imported_from_csv_dataFrame_v3)
print()

# index_col means defining the first (0th) column of the data as the index of the resulting DataFrame,
# If index_col is not used, the default index is integer based
south_east_asia_countries_imported_from_csv_dataFrame_v4 = pd.read_csv('south_east_asia_countries_info.csv', index_col=0)
print(south_east_asia_countries_imported_from_csv_dataFrame_v4)
print()

# Indexing and selecting data from dataframes
# Using Column Access []
# Series - one dimensional array, cannot have multiple columns
print(south_east_asia_countries_dataFrame_v2['Countries'])
print(type(south_east_asia_countries_dataFrame_v2['Countries']))
print(south_east_asia_countries_dataFrame_v2['Countries'].shape) # (10, ) = 10 elements in an array
# DataFrame - two dimensional array, can have multiple columns, each of different type
print(south_east_asia_countries_dataFrame_v2[['Countries']])
print(type(south_east_asia_countries_dataFrame_v2[['Countries']]))
print(south_east_asia_countries_dataFrame_v2[['Countries']].shape) # (10, 1) = 10 rows of data and 1 column

# Using Row Access []
print(south_east_asia_countries_dataFrame_v2[1:4]) # Returns row indices inclusive of 1 to exclusive 4

# Using loc() - label-position based
# Reminder: : means all elements of data either in column or row
# Series
print(south_east_asia_countries_dataFrame_v2.loc['PH']) # Limited to one row of data
# Sample Output:
# Countries     Philippines
# Capital            Manila
# Area             300000.0
# Population          110.8
# Name: PH, dtype: object

# Pandas
print(south_east_asia_countries_dataFrame_v2.loc[['PH']])
# Sample Output:
#       Countries Capital      Area  Population
# PH  Philippines  Manila  300000.0       110.8
print(south_east_asia_countries_dataFrame_v2.loc[['PH', 'SG', 'TH']]) # Can select multiple row datas
print(south_east_asia_countries_dataFrame_v2.loc[['PH', 'SG', 'TH'], ['Capital', 'Population']]) # Can select multiple rows of datas and intersect with its columnar variable
print(south_east_asia_countries_dataFrame_v2.loc[:, ['Capital', 'Population']])
print(south_east_asia_countries_dataFrame_v2.loc[['PH', 'SG', 'TH'], :])

# Using iloc() - integer-position based
# Series
print(south_east_asia_countries_dataFrame_v2.iloc[4])
# Pandas
print(south_east_asia_countries_dataFrame_v2.iloc[[4]])
print(south_east_asia_countries_dataFrame_v2.iloc[[4, 3, 1], [1, 3]]) # Can select multiple rows of datas and intersect with its columnar variable
print(south_east_asia_countries_dataFrame_v2.iloc[:, [1, 3]])
print(south_east_asia_countries_dataFrame_v2.iloc[[4, 3, 1], :])