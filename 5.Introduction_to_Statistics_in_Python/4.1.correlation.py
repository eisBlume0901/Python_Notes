# Correlation - determine and measure the relationship between two variables (uses a sample not a population)
# Analyzing correlation requires two methods: magnitude and direction

# Correlation coefficient
# Number between -1 and 1
# Magnitude corresponds to the strength of the relationship
# Sign (+ / -) corresponds to the direction of the relationship (positive or negative - inverse propertional)
# Types: Pearson (r), Spearman (r_s), Kendall's tau, Point-Biserial (r_pb)

# 0.8 <= r <= 1.0 (very strong relationship) - the data points are closely clustered along the line
# 0.6 <= r <= 0.79 (strong relationship)
# 0.4 <= r <= 0.59 (moderate relationship)
# 0.2 <= r <= 0.39 (weak relationship)
# 0 <= r <= 0.19 (little to very weak relationship)

# Regression vs Correlation
# Regression - measures how two variables affect each other using an EQUATION
# Correlation - measures the STRENGTH of a LINEAR RELATIONSHIP between two variables

# Correlation does not imply causation (x is correlated with y does not mean x causes y)
# Confounding - this phenomenon could lead to spurious correlation. Thus, it is important to consider
# potential confounding variables and account them in research design to ensure results are valid. Left
# unchecked can introduce many research biases and misinterpret results.

# Transformations (to make the data more linear by improving a fit between X and Y): Log (log(x)), Square root (sqrt(x)), reciprocal (1/x), or combinations: [log(x) and log(y), sqrt(x) and 1/y]
# When to use transformations:
# 1. Skewed data
# 2. Heteroscedasticity
# 3. Non-linearity
# 4. Outliers

import seaborn as sns # higher level library that is built on top of Matplotlib as you can use jointplot, pairplot, heatmap
import matplotlib.pyplot as plt # can create almost any kind of plot but require more code
import pandas as pd
import numpy as np

data = pd.read_csv("WHR2023.csv")
world_happiness_2023 = pd.DataFrame(data)
print(world_happiness_2023.head())

# Does having high GDP per capita increases Healthy life expectancy
# scatterplot - plots a scatter plot
# lmplot - plots a linear model plot (create a scatter plot with a linear fit on the top of it)
sns.lmplot(x="Logged GDP per capita", y="Healthy life expectancy", data=world_happiness_2023, ci=None)
plt.show()

print(world_happiness_2023["Logged GDP per capita"].corr(world_happiness_2023["Healthy life expectancy"])) # 0.8375 has a positive correlation

