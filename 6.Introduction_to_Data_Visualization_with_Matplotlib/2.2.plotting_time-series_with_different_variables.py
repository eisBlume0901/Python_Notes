import pandas as pd
import matplotlib.pyplot as plt

# Version 1
climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")
# Version 2
# climate_change = pd.read_csv('climate_change.csv', parse_dates=True, index_col="date")

figure, axis = plt.subplots(figsize=(15, 5))

# Using twin axes
# axis.plot(climate_change.index, climate_change["co2"], color="orange")
# axis.set_xlabel("Time")
# axis.set_ylabel("CO2 (ppm)", color="orange")
# axis.tick_params("y", colors="orange")
# axis2 = axis.twinx()
# axis2.plot(climate_change.index, climate_change["relative_temp"], color="blue")
# axis2.set_ylabel("Relative Temperature (Celcius)", color="blue")
# axis2.tick_params("y", colors="blue")
#
# plt.tight_layout()
# plt.show()

# Instead of repeatedly calling the same set of methods use a function
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params("y", colors=color)

plot_timeseries(axis, climate_change.index, climate_change["co2"], "orange", "Time", "CO2 (ppm)")
axis2 = axis.twinx()
plot_timeseries(axis2, climate_change.index, climate_change["relative_temp"], "blue", "Time", "Relative Temperature (Celsius)")
plt.show()

