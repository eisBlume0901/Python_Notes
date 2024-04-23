# Article explaining why NumPys are better than lists
# https://datascience.blog.wzb.eu/2018/02/02/vectorization-and-parallelization-in-python-with-numpy-and-pandas/

# NumPys
# Can only hold one data type so that it could perform mathematical operations

import numpy as np

weight_kg = [50, 54, 56, 57, 49, 60, 48]
print(weight_kg)

weight_lb = np.array(weight_kg) * 2.20462
print(weight_lb)

# NumPy vs List
# + is considered concatenation in lists
# + is considered as mathematical operation for numpys

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]

print(arr1 + arr2)
print(np.array(arr1) + np.array(arr2))

# NumPy can subset with conditions
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
np_nums = np.array(nums)
even = np_nums % 2 == 0
print(np_nums[even])
print(np_nums[np_nums != 0])

# NumPy can subset the same with lists
# [inclusive_start:exclusive_end]
print(np_nums[1:11])
# [:exclusive_end]
print(np_nums[:6])
print(np_nums[:-5])
# [inclusive_start:]
print(np_nums[6:])
print(np_nums[-5:])

# 2D NumPy Arrays
# .shape - returns number of rows and columns, attribute of 2D numpy arrays

np_2d = np.array([
    [57.6, 48.1, 55.3, 60.7, 65.1],
    [1.60, 1.59, 1.58, 1.72, 1.81]
])
print(np_2d.shape) # 2 rows, 5 columns

# subsetting numpys can subset the same with lists or using comma to separate row and column index
print(np_2d[0])
print(np_2d[1])

print(np_2d[1][1:2]) # Version 1
print(np_2d[1, 1:2]) # Version 2

print(np_2d[0][:]) # Version 1
print(np_2d[0, :]) # Version 2

print(np_2d[0][0]) # Version 1
print(np_2d[0, 0]) # Version 2

print(np_2d[1][-1]) # Version 1
print(np_2d[1, -1]) # Version 2

# 2D Arithmetic
# Note remember the rules of matrix operations
np_mat = np.array([
    [3, 6, 9],
    [12, 15, 18],
    [21, 24, 27]
])

print(np_mat * 0.1)
print(np_mat * 0.3)
print(np_mat + np.array([10, 20, 30])) # must have the same column length

# NumPy Basic Statistics
# .mean(), .median(), .std(), .var(), .corrcoef(), .random.normal()

grades = [75, 80, 95, 84, 93, 91, 82, 90]
np_grades = np.array(grades)

print(np.mean(np_grades))
print(np.median(np_grades))

study_time_per_hour_in_a_day = [1, 1.5, 5, 1.5, 3.5, 3, 1.5, 2.5]
np_study_time_per_hour_in_a_day = np.array(study_time_per_hour_in_a_day)
print(np.std(np_study_time_per_hour_in_a_day))
print(np.var(np_study_time_per_hour_in_a_day))

np_2d_grades_study_time = np.array([grades, study_time_per_hour_in_a_day])
print(np.corrcoef(np_2d_grades_study_time[0], np_2d_grades_study_time[1])) # means that grades and study hours is correlated

# Generating random normal distribution
intelligent_quotient = np.round(np.random.normal(99, 10, 100), 0)
print(intelligent_quotient)

