# Dictionary vs List
south_east_asia_countries_population = {
    'Indonesia': 273.5,
    'Thailand': 69.8,
    'Malaysia': 32.4,
    'Singapore': 5.7,
    'Philippines': 110.8,
    'Vietnam': 97.3,
    'Myanmar': 54.4,
    'Cambodia': 16.7,
    'Laos': 7.3,
    'Brunei': 0.4
}

print(south_east_asia_countries_population['Philippines']) # Uses key

south_east_asia_countries = ['Indonesia', 'Thailand', 'Malaysia', 'Singapore', 'Philippines', 'Vietnam', 'Myanmar', 'Cambodia', 'Laos', 'Brunei'] # Can be converted to dictionary
south_east_asia_pop = [273.5, 69.8, 32.4, 5.7, 110.8, 97.3, 54.4, 16.7, 7.3, 0.4]  # in millions

ind_phil = south_east_asia_countries.index('Philippines')
print(south_east_asia_pop[ind_phil]) # Uses index