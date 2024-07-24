import pandas as pd
import matplotlib.pyplot as plt

# Load the data
climate_change_data = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col="date")
climate_change = pd.DataFrame(climate_change_data)

# Calculate days since the start of the dataset
days_since_start = (climate_change.index - climate_change.index.min()).days

# Plotting
figure, axis = plt.subplots()
scatter = axis.scatter(climate_change["co2"], climate_change["relative_temp"], c=days_since_start)
axis.set_xlabel("CO2 (ppm)")
axis.set_ylabel("Relative Temperature (C)")

# Adding a colorbar to show the mapping of colors to days since start
plt.colorbar(scatter, label='Days since start')

plt.show()