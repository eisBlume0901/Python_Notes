import pandas as pd
import matplotlib.pyplot as plt

stockPriceAFile = pd.read_csv('stock_price_A.csv')
stockPriceBFile = pd.read_csv('stock_price_B.csv')

stock_A = pd.DataFrame(stockPriceAFile)
stock_B = pd.DataFrame(stockPriceBFile)

stock_A_and_B = pd.merge_ordered(stock_A, stock_B, on="date", suffixes=("_a", "_b"))
print(stock_A_and_B)

# ffill - forward fill, allows interpolation of missing data based on the previous data
stock_A_and_B_v1 = pd.merge_ordered(stock_A, stock_B, on="date", suffixes=("_a", "_b"), fill_method="ffill")
print(stock_A_and_B_v1)


gdpCountryX = pd.read_csv('gdp_countryX.csv')
standardOfLivingCountryX = pd.read_csv('standard_of_living_countryX.csv')

gdp = pd.DataFrame(gdpCountryX)
living_index = pd.DataFrame(standardOfLivingCountryX)

gdp_living_index = pd.merge_ordered(gdp, living_index, on="year")

corr_gdp_living_index = gdp_living_index[["gdp", "standard_of_living_index"]].corr()
print(corr_gdp_living_index) # If the correlation returns almost to 1 such as 0.99 then there is a strong correlation

gdp_living_index.plot(x="gdp", y="standard_of_living_index", kind="scatter")
plt.show()

gdpUSAGermanyDummyDataFile = pd.read_csv('gdp_usa_germany_dummy_data.csv')
popUSAGermanyDummyDataFile = pd.read_csv('pop_usa_germany_dummy_data.csv')

# Order of joining matters how it is sorted
gdp_usa_germany = pd.DataFrame(gdpUSAGermanyDummyDataFile)
pop_usa_germany = pd.DataFrame(popUSAGermanyDummyDataFile)

# Ordered Germany first then USA then afterward the date (hierarchy of sorting)
country_date_merge_type_1 = pd.merge_ordered(gdp_usa_germany, pop_usa_germany, on=["country", "date"], fill_method="ffill")
print(country_date_merge_type_1)

# Ordered by dates then Germany and USA
date_country_merge_type_2 = pd.merge_ordered(gdp_usa_germany, pop_usa_germany, on=["date", "country"], fill_method="ffill")
print(date_country_merge_type_2)