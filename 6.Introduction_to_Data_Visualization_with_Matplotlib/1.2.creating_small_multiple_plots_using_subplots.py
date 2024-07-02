import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(349)
months = pd.date_range(start="2023-01-01", periods=12, freq="ME").strftime("%b")
temperature_A = np.random.randint(low=20, high=40, size=12)
precipitation_A = np.random.randint(low=0, high=200, size=12)
temperature_B = np.random.randint(low=20, high=40, size=12)
precipitation_B = np.random.randint(low=0, high=200, size=12)

# nrows = number of rows, ncols = number of columns, sharey=True (shares y-axis values), figsize=lengthxwidth
figure, axis = plt.subplots(2, 2, figsize=(15, 8))
axis[0, 0].plot(months, temperature_A, color="orange", label="Temperature A", marker="o")
axis[0, 1].plot(months, precipitation_A, color="blue", label="Precipitation A", marker="o")
axis[1, 0].plot(months, temperature_B, color="orange", label="Temperature A", marker="o")
axis[1, 1].plot(months, precipitation_B, color="blue", label="Precipitation A", marker="o")
for ax in axis.flat:
    plt.setp(ax.get_xticklabels(), rotation=45)
plt.subplots_adjust(wspace=0.3, hspace=0.3)
plt.show()


