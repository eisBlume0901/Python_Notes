import pandas as pd
import matplotlib.pyplot as plt

# Time-series data (x = time), either parse the date or set pd.to_datetime()
# breaks in line graph = NaN values

# Read the CSV file
co2_data = pd.read_csv("co2-long-term-concentration.csv")
co2_df = co2_data.set_index("Year")
print(co2_df.head())

co2_df_from_1970_to_2023 = co2_df.loc[1970:2023]

# Good method is to parse it to string and add 01-01 for each year to properly label it as year level data
co2_df_from_1970_to_2023.index = co2_df_from_1970_to_2023.index.astype(str) + '-01-01'
co2_df_from_1970_to_2023.index = pd.to_datetime(co2_df_from_1970_to_2023.index)
print(co2_df_from_1970_to_2023.head())
print(co2_df_from_1970_to_2023.tail())

temperature_data = pd.read_csv("temperature-anomaly.csv")
global_temperature = temperature_data[temperature_data["Entity"] == "Global"]
global_temperature_df = pd.DataFrame(global_temperature)
global_temperature_df_v2 = global_temperature_df.set_index("Year")
print(global_temperature_df_v2.tail())
# global_temperature_df_v2.index = global_temperature_df_v2.index.astype(str) + "-01-01"
# print(global_temperature_df_v2.head())
# print(global_temperature_df_v2.tail())


figure, axis = plt.subplots(2, 1)
axis[0].plot(co2_df_from_1970_to_2023.index, co2_df_from_1970_to_2023["Long-run CO₂ concentration"])
axis[0].set_xlabel("Year")
axis[0].set_ylabel("CO₂ concentration (PPMV)")

axis[1].plot(global_temperature_df_v2.index, global_temperature_df_v2["Global average temperature anomaly relative to 1961-1990"])
axis[1].set_xlabel("Year")
axis[1].set_ylabel("Global average temperature")

plt.subplots_adjust(wspace=0.3, hspace=0.3)

plt.show()

# Using the data from DataCamp, parse_dates is fine to use as long as the index is already date
climate_change_csv_file = pd.read_csv('climate_change.csv', parse_dates=True, index_col="date")
figure1, axis1 = plt.subplots(2, 1)

seventies = climate_change_csv_file["1970-01-01": "1979-12-31"]
axis1[0].plot(seventies.index, seventies["co2"])
axis1[1].plot(seventies.index, seventies["relative_temp"])

plt.show()