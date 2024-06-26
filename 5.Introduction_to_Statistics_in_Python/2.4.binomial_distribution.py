# Binomial distributions https://youtu.be/rvg9oUHtX50

# BINS
# Binary Outcomes - only deals with success or fail
# Independent Trials - the success and failure of the event is not dependent on previous experiment
# Number of Trials - how many times the experiment will be done
# Same probability per trial - probability is unchanging (50-50)

# Examples:
# Rolling a die 4 times. What is the probability of rolling a 1 twice?

# Properties
# Mean / Expected value = n * p, where n = number of trials, p = probability of success
#   expected value is what you would expect the outcome of an event to be on average
# Standard Deviation = sqrt(n * p * (1 - p))
# Check Binomial Distribution Formula png image for the P(X = x)

from scipy.stats import binom

# rvs = random variates from a binomial distribution, good for simulation

# 8 coin flips, n=1 means 1 coin to flip, p=0.5 there is a 50 percent chance to get heads, size=8 there is 8 times to flip a coin
random_8_coin_flips_results = binom.rvs(n=1, p=0.5, size=8)
print(random_8_coin_flips_results) # returns to an array of results, 0 corresponds to tails, 1 corresponds to heads

# flipping 8 coins one time, n=8 means 8 coins to flip, size=1 with 8 coins being flip one time at the same time
random_flipping_8_coins_at_the_same_time = binom.rvs(n=8, p=0.5, size=1)
print(random_flipping_8_coins_at_the_same_time) # returns an array of results, ranges from 1 to 8 (1 means 1 head out of 8, 8 means 8 out of 8)

# flipping 3 coins 10 times, n=3 means 3 coins to flip, size=10 with 3 coins being flip 10 times at the same time
random_flipping_3_coins_10_times = binom.rvs(n=3, p=0.5, size=10)
print(random_flipping_3_coins_10_times) # returns an array of results, ranges from 1 to 3 (1 means 1 head out of 3, 3 means 3 heads out of 3)

# rolling a die 4 times getting 1 twice, n=1 means 1 die, size=4 means rolling the die 4 times, p=1/6 means 1 out of 6 die faces we can get a number of 1
random_rolling_a_die_4_times = binom.rvs(n=1, p=1/6, size=4)
print(random_rolling_a_die_4_times)




# pmf = probability mass function, good for getting exact success

# Getting P(heads = 7) or probability of getting exactly 7 heads out of 10 coin flips at the same time
# k - resulting value, n - number of trials, p - probability of success
probability_of_getting_7_heads = binom.pmf(k=7, n=10, p=0.5)
print(round(probability_of_getting_7_heads, 4)) # 0.1172



# cdf = cumulative distribution function, good for getting value less than or equal to a certain value

# Getting P(heads <= 7) or probability of getting values 1, 2, 3, 4, 5, 6, 7 heads out of 10 coin flips at the same time
probability_of_getting_less_than_or_equal_to_7_heads = binom.cdf(k=7, n=10, p=0.5)
print(round(probability_of_getting_less_than_or_equal_to_7_heads, 4)) # 0.9453, higher chance since we can get those values

# Getting P(heads > 7) or probability of getting values 8, 9, 10 heads out of 10 coin flips
probability_of_getting_greater_than_7_heads = 1 - binom.cdf(k=7, n=10, p=0.5)
print(round(probability_of_getting_greater_than_7_heads, 2)) # 0.05, lower chance since it is nearly impossible to 8 to perfect heads at the same time


# mean / expected value = n * p
expected_value_of_heads_out_of_10_flips = 10 * 0.5
print(expected_value_of_heads_out_of_10_flips) # 0.05