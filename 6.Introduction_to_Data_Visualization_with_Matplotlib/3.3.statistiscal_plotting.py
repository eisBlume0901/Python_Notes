import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(5465)
# How to read error bar charts?
# https://www.biologyforlife.com/interpreting-error-bars.html
# https://youtu.be/otqk4eIDMcg (Error bars could also show how skewed a data is)

# Bar charts with error bars
pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited
pd.set_option('display.max_colwidth', None)  # None means unlimited

iq_women_norway = np.random.normal(102, 15, 100)
iq_women_philippines = np.random.normal(97, 12, 100)
print("Norway")
iq_women_norway_df = pd.Series(iq_women_norway)
print(iq_women_norway_df.sort_values())
print("Philippines")
iq_women_philippines_df = pd.Series(iq_women_philippines)
print(iq_women_philippines_df.sort_values())

figure, axis = plt.subplots()
axis.bar("Norway", iq_women_norway.mean(), yerr=iq_women_norway.std())
axis.bar("Philippines", iq_women_philippines.mean(), yerr=iq_women_philippines.std())
axis.set_ylabel("IQ score")
plt.show()

# Line charts with error bars
seattle_weather_data = pd.read_csv('seattle_weather.csv')
seattle_weather_only = seattle_weather_data[seattle_weather_data["NAME"] == "SEATTLE BOEING FIELD, WA US"]
seattle_weather_data_df = pd.DataFrame(seattle_weather_only)
austin_weather_data = pd.read_csv('austin_weather.csv')
austin_weather_data_df = pd.DataFrame(austin_weather_data)

figure1, axis1 = plt.subplots()
axis1.errorbar(seattle_weather_data_df["DATE"], seattle_weather_data_df["MLY-TAVG-NORMAL"], yerr=seattle_weather_data_df["MLY-TAVG-STDDEV"])
axis1.errorbar(austin_weather_data_df["DATE"], austin_weather_data_df["MLY-TAVG-NORMAL"], yerr=austin_weather_data_df["MLY-TAVG-STDDEV"])
axis1.set_ylabel("Temperature (Fahrenheit)")
plt.show()

# How to read boxplots? https://www.simplypsychology.org/boxplots.html
# How to manually graph boxplot? https://youtu.be/mhaGAaL6Abw
figure2, axis2 = plt.subplots()
axis2.boxplot([iq_women_norway, iq_women_philippines])
axis2.set_xticklabels(["Norway", "Philippines"])
axis2.set_ylabel("Height (cm)")
plt.show() # There is an outlier for Philippines