# Poisson processes - events appear to happen at a certain rate, but completely random
# Examples:
# Number of animals adopted from an animal shelter per week
# Number of people arriving at a restaurant per hour
# Number of earthquakes in California per year

# Poisson distribution
# - probability of some number of events occurring over a fixed period of time
# - subset of discrete probability distribution
# - time is irrelevant
# Examples:
# Probability of greater than or equal to 5 animals adopted from an animal shelter per week
# Probability of 12 people arriving at a restaurant per hour
# Probability of less than 20 earthquakes in California per year

# Lambda - average number of events per time interval

from scipy.stats import poisson
import pandas as pd
import matplotlib.pyplot as plt
# pmf = probability mass function, good for getting exact success
# If the average number of adoptions per week is 8, what is P(# adoptions in a week = 5)?
# k = number of occurrences of the event at a certain rate, mu = expected number of occurrences / mean / average / lambda
five_adoptions_in_a_week = poisson.pmf(k=5, mu=8) # 0.09 chance / few chance of adopting exactly 5 animals per week
print(five_adoptions_in_a_week)

# cdf = cumulative distribution function, good for getting less than or equal to a certain value (uses the concept of Z-score)
# to get values greater than just subtract to 1
# If the average number of adoptions per week is 8, what is P(# adoptions in a week less than or equal to 5)?
less_than_or_equal_to_five_adoptions_per_week = poisson.cdf(k=5, mu=8)
print(less_than_or_equal_to_five_adoptions_per_week) # 0.19 chance of adopting less than or equal to 5 animals per week
# If the average number of adoptions per week is 8, what is P(# adoptions in a week greater than 5)?
greater_than_five_adoptions_per_week = 1 - poisson.cdf(k=5, mu=8)
print(greater_than_five_adoptions_per_week) # 0.81 (higher chance, as the probability is greater than the average) of adopting greater than 5 animals per week
# If the average number of adoptions per week is 10, what is P(# adoptions in a week > 5)?
greater_than_five_adoptions_per_week = 1 - poisson.cdf(k=5, mu=10)
print(greater_than_five_adoptions_per_week) # 0.93 (higher chance, as the probability is greater than the average) of adopting greater than 5 animals per week

# rvs = random variates (good for simulation)
# generate 10 random numbers of adoptions in a week with an average adoption rate of 8
print(poisson.rvs(mu=8, size=10))

# The higher the sample size, the closer it approaches to normal distribution graph
pd.Series(poisson.rvs(mu=8, size=100)).plot(kind="hist", bins=10)
plt.show()