# Sampling distributions
#   - choosing large / many number of samples (n, derived from a population)
#   - obtain by taking repeated samples of the same size from a population
#   - For each sample, we can calculate mean (this is the most commonly used), variance, standard deviation
#       which is then organized for plotting a sampling distribution graph. If we calculate the mean of every
#       sample we will get the "sample means" (average of all samples - samples that also took the average)

# Central Limit Theorem
#   - The mean of the sample means is equal to the mean of the population (independent of sample size)
#       useful for drawing conclusions/inference from the sample with respect to the population
#   - The standard deviation of the sample means (standard error) is equal to the standard deviation of the population divided by the square root of the sample size.
#   - If the population is normal, then the sample means will have a normal distribution (independent of sample size, even it is less than 30 samples)
#   - If the population is not normal, but the sample size is greater than 30 (n > 30),
#       then sampling distribution of sample means approximates a normal distribution for any population distribution shape

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Problem is to determine the average customers (how many users) per deal for Amir's company products
np.random.seed(104)
data = pd.read_csv('amir_deals.csv')
amir_deals = pd.DataFrame(data)

sample_means = [] # Storing all means of each sample

# 100 sample means
for i in range(100):
    sampl_20 = amir_deals["num_users"].sample(20, replace=True) # getting 20 independent samples out of all amir_deals's num_users
    sampl_20_mean = np.mean(sampl_20)
    sample_means.append(sampl_20_mean)

sample_means_series = pd.Series(sample_means) # Convert to series to plot the histogram
sample_means_series.hist()
plt.show()