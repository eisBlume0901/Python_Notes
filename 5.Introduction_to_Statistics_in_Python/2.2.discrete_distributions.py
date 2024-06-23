import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the data
data = {
    'group_id': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'group_size': [2, 4, 6, 2, 2, 2, 3, 2, 4, 2]
}
restaurant_groups = pd.DataFrame(data)

# Histogram of restaurant groups (review 1.basic_plots_with_matplotlib.py under 2.Intermediate_Python
restaurant_groups["group_size"].plot(kind="hist", bins=[2, 3, 4, 5, 6], xlabel="Group Size")
plt.show()

# Discrete Probability Distribution in Tabular Form
size_distribution = restaurant_groups["group_size"].value_counts() / restaurant_groups.shape[0] # Getting the total number of group tables in terms of id (A-J is 10 tables)
print(size_distribution)
print(np.sum(size_distribution)) # Sum of probabilities is always 1 means that all possible outcomes will likely happen

# Expected Value / Mean Probability Distribution
# Purposes:
# Central tendency = average value of a random variable
# Long term expectation = average value you would expected over many repetitions of an experiment or random process
#   Individual outcomes can vary, but the average converges to the expected value
expected_value = np.sum(size_distribution.index * size_distribution.values) # 2.90
print(expected_value)

# Discrete Probability Distribution for 4 people or more
groups_4_or_more = size_distribution[size_distribution.index >= 4]
prob_4_or_more = np.sum(groups_4_or_more)
print(prob_4_or_more) # 0.30