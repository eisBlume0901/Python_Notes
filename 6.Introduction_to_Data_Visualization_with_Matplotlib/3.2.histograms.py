import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1500)
height_in_germany_women = np.random.normal(165, 6, 100)
height_in_philippines_women = np.random.normal(150, 5, 100)

# Creating overlapping histograms
figure, axis = plt.subplots()
axis.hist(height_in_germany_women, label="Germany", histtype="step", bins=5, color="red")
axis.hist(height_in_philippines_women, label="Philippines", histtype="step", bins=5, color="blue")
axis.legend()
axis.set_xlabel("Height (cm)")
axis.set_ylabel("Number of observations")
axis.set_title("Height of Women in Germany and Philippines")
plt.show()