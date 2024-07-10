import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")


figure, axis = plt.subplots(figsize=(15, 5))
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params("y", colors=color)

plot_timeseries(axis, climate_change.index, climate_change["co2"], "orange", "Time", "CO2 (ppm)")
axis2 = axis.twinx()
plot_timeseries(axis2, climate_change.index, climate_change["relative_temp"], "blue", "Time", "Relative Temperature (Celsius)")

# x = "2015-10-06", y = 1
# xytext is places the annotation where it does not overlap with the data
# arrowprops - places an arrow of the xytext to the xy, can be customized
# https://matplotlib.org/stable/users/explain/text/annotations.html
axis2.annotate(">1 degree", xy=(pd.Timestamp("2015-10-06"), 1), xytext=(pd.Timestamp('2008-10-06'), -0.2), arrowprops={"arrowstyle": "->", "color": "green"})
plt.show()
