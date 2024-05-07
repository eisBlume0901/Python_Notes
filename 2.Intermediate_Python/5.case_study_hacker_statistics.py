import numpy as np
import matplotlib.pyplot as plt

print(np.random.rand()) # Generates pseudo-random numbers (still uses a mathematical formula)

np.random.seed(123) # This ensures reproducibility of the same generated pseudo-random number
print(np.random.rand()) # 0.6964691855978616 will always be the result because we set the .seed to 123

# Seed is an initial value that is used to generate a sequence of random numbers. When setting a seed,
# the random generator produces a sequence of numbers that appear random but starting at the same seed,
# will get the same sequence of numbers again.

np.random.seed(456)
coin = np.random.randint(0, 2) # Head(0) or Tail(1) (In this syntax, 2 is exclusive)
print(coin) # 1 will always be the result because we set the .seed to 456

if coin == 0:
    print("heads")
else:
    print("tails") # Since 1 is always the same result then it will be tails

# Random walk - stochastic or random process describing path consisting of a succession of random steps
# Real life applications:
# behavior of molecules in a gas or fluid (physics),
# network routing where packets are sent along random paths to avoid congestion (networking)

# 10 random outcomes of heads or tails in coin tossing
np.random.seed(7841)
outcomes = []
tails = [0]
for x in range(10): # for in range loops 10 times
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")
print("Outcomes", outcomes)
print("Tails", tails)
# Outcomes ['heads', 'tails', 'heads', 'heads', 'tails', 'tails', 'heads', 'heads', 'tails', 'tails']


# 10 random walk by monitoring how many tails were tossed
np.random.seed(123)
tails = [0] # Starts with 0 since no tails have been tossed before the first toss)
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin) # No need for if-else since tails is set to be 1
print("Tails", tails)
# Tails [0, 0, 1, 1, 1, 2, 3, 3, 3, 4, 5] # the last element means that there were 5 tails from 10 toin cosses
# Tails list has 10 elements disregard the first element since no one tosses tails first
# Outcomes counterpart ['head', 'head', 'tails', 'head', 'head', 'tails', 'tails', 'head', 'head', 'head', 'tails', tails]

# Getting the distribution of tossing coins, implementing random walk algorithm
np.random.seed(123)
final_tails = []
for x in range(10_000): # 10000 rounds of 10 coin tosses, the larger the size, the distribution gets normalized
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1]) # Records the final number of tails tossed in each round
    # (which consists of 10 tosses in 100 times!)
print("Final Tails in each 10 coin tosses 10,000 times")
print(final_tails)
# [3, 6, 4, ..., 7, 4, 4]
# Simple interpretation
# 3 tails out of 10 for first round
# 6 tails out of 10 for second round and so forth
plt.hist(final_tails, bins=10, edgecolor='white', color='blue') # Remember, histogram shows the frequency of the tails in a certain range
# Simple interpretation
plt.xlabel("Final Tails in each 10 coin tosses 10,000 times")
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.ylabel("Number of Final tosses")
plt.yticks([250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500])
plt.show()
# There are ~2400 times the coin was tossed 5 to 6 times out of 10


# Whole code for the Empire State Building bet
# Part 1
np.random.seed(134)
step = 50
dice = np.random.randint(1, 7)

if dice <= 2:
    step = step - 1
elif dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1, 7)

print("Dice", dice)
print("Step", step)

# Part 2
np.random.seed(134)
step = 50
random_walk = [0]

for x in range(100):
    step = random_walk[-1]

    dice = np.random.randint(1, 7)

    if dice <= 2:
        step = max(0, step - 1) # Ensures that we do not go below step 0, max function means we are NOT going BELOW 0
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    random_walk.append(step)

print("Random Walks", random_walk)

plt.plot(random_walk) # if y-axis is not depicted, the list/numpy uses the index of it as the y axis
plt.xlabel("Random Walk")
plt.ylabel("Number of Steps")
plt.show()

# Part 3 - Last and improved version
np.random.seed(123)
step = 50
all_walks = []

for i in range(500): # 500 rounds of 100 random walk bet
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        random_walk.append(step)
    all_walks.append(random_walk)
    # all_walks.append(random_walk[-1])
# print("All Walks", all_walks)
# Final random walk count
# All Walks [71, 101, 73, 81, 103] # applicable for 5 only not 500

np_all_walks = np.array(all_walks) # Contains 500 rows with 100 columns
plt.plot(np_all_walks)
plt.show() # It is expected to be messier since our all_walks merge 500 rounds of 100 step game

# NumPy's .transpose() use to permute the dimensions of an array.
# Permute - a 2D array's first dimension represents rows and the second dimension represents columns.
# Permutation change the order of these dimensions which means the first dimension is now columns and the second dimensions is now rows.
# In discrete math, this is called matrix transpose

np_all_walks_transposed = np.transpose(np_all_walks) # Now contains 100 rows with 500 columns
plt.plot(np_all_walks_transposed)
plt.xlabel("Random Walk in 100 times in 500 rounds")
plt.show() # It is expected to see a linear graph with 500 different color lines to represent 500 rounds

ends = np_all_walks_transposed[-1, :]
plt.hist(ends, edgecolor='white') # Default value of bins is 10
plt.xticks([20, 40, 60, 80, 100, 120])
plt.xlabel("Final (100th) Walk Count in 500 rounds")
plt.yticks([20, 40, 60, 80, 100, 120])
plt.ylabel("Frequency of the Final Walk Count")
plt.show()

# Calculating the odds of getting Final (100th) Walk Count in 500 simulations
print(len(ends[ends >= 60]) / 500 * 100)
