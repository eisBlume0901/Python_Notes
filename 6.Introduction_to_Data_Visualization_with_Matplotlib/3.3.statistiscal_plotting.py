import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Using bar charts to see the difference of mean and standard deviation
# y is always the standard deviation
# x is always the mean
iq_women_norway = np.random.normal(102, 15, 100)
iq_women_philippines = np.random.normal(97, 12, 100)

figure, axis = plt.subplots()
axis.bar("Norway", iq_women_norway.mean(), yerr=iq_women_norway.std())
axis.bar("Philippines", iq_women_philippines.mean(), yerr=iq_women_philippines.std())
axis.set_ylabel("IQ score")
plt.show()