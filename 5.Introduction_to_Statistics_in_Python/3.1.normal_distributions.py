# Normal probability distribution - a subset of continuous probability distribution

# Properties of normal probability distribution

# Its bell shaped curve is always symmetrical
# The mean, median, and mode are exactly the same
# The distribution can be described by two values: mean (having the highest probability)
#   and standard deviation (as it goes further away from mean, its probability decreases)
# The area under the curve is always 1 (note that its curve is asymptotic to 0 because
#   the curve equalling to 1 represents the total probability of all possible outcomes, 0 means it would not likely happen)

# Empirical rule (68-95-99.7)
# Around 68% of values are within 1 standard deviation from the mean
# Around 95% of values are within 2 standard deviation from the mean
# Around 99.7% of values are within 3 standard deviation from the mean

# Standardizing the normal probability distribution with Z-score helps how many blocks away from the mean (ranging -3 to +3)
# so that we can easily make conclusions out of it (note that z-score charts get the area under the curve from the left / right
# so always try to subtract it by 1 if applicable)

# Getting the certain probability of an outcome or value (not exact), we use z-score charts

from scipy.stats import norm
import matplotlib.pyplot as plt

# cdf = cumulative distribution function (uses the concept of Z-scores) https://youtu.be/xI9ZHGOSaCg
# x=154 point of interest (finding the area under that certain curve point), loc=161 is the mean of the normal distribution, scale=7 is the standard deviation
# Finding percent of women shorter than 154 cm
shorter_than_154_cm = norm.cdf(x=154, loc=161, scale=7) # implicitly uses the concept of Z-scores
print(shorter_than_154_cm) # 0.1587 meaning there are few short women in NHANES
# Finding the percent of women taller than 154 cm
taller_than_154_cm = 1 - norm.cdf(x=154, loc=161, scale=7)
print(taller_than_154_cm) # 0.8413 meaning there are many more tall women in NHANES
# Finding the percent of women under the range of 154-157 cm
women_between_154_and_157_cm = norm.cdf(x=157, loc=161, scale=7) - norm.cdf(x=154, loc=161, scale=7)
print(women_between_154_and_157_cm) # 0.1252 meaning there are few women at that range in NHANES


# ppf = percent point function / inverse Cumulative Distribution Function (commonly use in finding values on the x-axis)
# What height are 90% of women shorter than? (What height falls below 90% of individual heights)
height_at_90_percent_shorter_than = norm.ppf(q=0.9, loc=161, scale=7)
print(height_at_90_percent_shorter_than) # 90% of women are shorter than 169.97 cm
# What height are
height_at_15_percent_shorter_than = norm.ppf(q=0.1587, loc=161, scale=7)
print(height_at_15_percent_shorter_than) # 154.00 (refer to the question "Finding the percent of women shorter than 154 cm"), it took the value back


# rvs = random variates (good for simulation / experiment of random values)
# Generate 10 random heights with a mean of 161 and standard deviation of 7
# loc = mean, scale = standard deviation, size = number of heights
ten_random_heights = norm.rvs(loc=161, scale=7, size=10)
print(ten_random_heights) # returns an array of random heights

plt.hist(ten_random_heights, bins=10, edgecolor="white")
plt.show()

one_thousand_random_heights = norm.rvs(loc=161, scale=7, size=1000)

plt.hist(one_thousand_random_heights, bins=10, edgecolor="white")
plt.show()