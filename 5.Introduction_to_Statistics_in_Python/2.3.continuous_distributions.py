from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt

# cdf = cumulative distribution function

# Problem from DataCamp
# The sales software used at your company is set to automatically back itself up,
# but no one knows exactly what time the back-ups happen. It is known, however,
# that back-ups happen exactly every 30 minutes. Amir comes back from sales meetings
# at random times to update the data on the client he just met with. He wants to know
# how long he'll have to wait for his newly-entered data to get backed up. Use your
# new knowledge of continuous uniform distributions to model this situation and answer
# Amir's questions.

min_time = 0
max_time = 30

print("Probability of waiting less than 5 mins")
print(uniform.cdf(5, min_time, max_time))

print("Probability of waiting more than 5 mins")
print(1 - uniform.cdf(5, min_time, max_time))

print("Probability of waiting 10-20 mins")
print(uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time))

# Generating random numbers according to uniform distribution
np.random.seed(334)
# Generating 1000 wait times between 0 and 30
waiting_times = uniform.rvs(min_time, max_time, size=1000)
plt.hist(waiting_times)
plt.show()