import pandas as pd
import matplotlib.pyplot as plt

seattle_weather_data = pd.read_csv('seattle_weather.csv')
seattle_weather_only = seattle_weather_data[seattle_weather_data["NAME"] == "SEATTLE BOEING FIELD, WA US"]
seattle_weather_data_df = pd.DataFrame(seattle_weather_only)
austin_weather_data = pd.read_csv('austin_weather.csv')
austin_weather_data_df = pd.DataFrame(austin_weather_data)

# plt.style.use("ggplot") # gray background, white grid plot
# plt.style.use("default") # default style of plots
plt.style.use("bmh") # Bayesian Method for Hackers = bmh, clean and minimalist look with a white background and grid lines
# plt.style.use("seaborn-colorblind") # make visualizations more accessible to individuals with color deficiencies
# plt.style.use("tableau-colorblind10") # Also same purpose with seaborn-colorblind
# plt.style.use("grayscale") # best used with printed in black and white
# plt.style.use("Solarize_Light2") # light background with a specific color palette that is designed to be easy on the eyes,
# # this theme (Solarize_Light2) is inspired by the Solarized color theme
figure, axis = plt.subplots()
axis.plot(seattle_weather_data_df["DATE"], seattle_weather_data_df["MLY-TAVG-NORMAL"])
axis.plot(austin_weather_data_df["DATE"], austin_weather_data_df["MLY-TAVG-NORMAL"])
axis.set_xlabel("Time (months)")
axis.set_ylabel("Average temperature (Fahrenheit degrees)")
plt.show()


# Guidelines for choosing plotting style
# Dark backgrounds are usually less visible
# If color is important, consider choosing colorblind-friendly options
    # seaborn-colorblind / tableau-colorblind1O
# If you think that someone will want to print your figure, use less ink
# If it will be printed in black-and-white, use "grayscale" style