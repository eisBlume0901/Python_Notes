# Exponential distribution
# Variant of Poisson distribution (which governs HOW MANY EVENTS happen in a given period of time) by which
# governs HOW MUCH TIME elapses between consecutive events)
# Unlike Poisson distribution, it is continuous (time-dependent)
# Time = 1 (unit of time)/lambda (or rate of occurrences)
# Time until the next event occurs

# Student / t-distribution (t-statistic)
# Variant of normal probability distribution but has fatter tails (higher dispersion of variables since there are more uncertainty
# Making inferences of a small sample from unknown population (especially if the sample is too big, unlike normal distribution,
# the higher the sample size, the closer we are to the normal distribution = z-statistic)
# degrees of freedom
#   which determines the thickness of the tails
#   As the degrees of freedom increase, particularly when they reach 30 or more, the distribution becomes more similar to a normal distribution

# Log-normal distribution


from scipy.stats import expon

# cumulative distribution function = good for getting for less than or equal to a certain value
# What is the probability it takes Amir less than an hour to respond to a lead? Given that on average, he responds 1 request every 2.5 hours
# scale = mean time, before the parameter scale = given time
print(expon.cdf(1, scale=2.5))

# What is the probability it takes Amir more than 4 hours to respond to a lead? Given that on average, he responds 1 request every 2.5 hours
print(1 - expon.cdf(4, scale=2.5))

# What is the probability it takes Amir 3-4 hours to respond to a lead?
print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))