import numpy as np

# Comparison operators: how Python variables relate and returns a boolean
x = 2
y = 5
print(x < y)
print(x <= y)
print(x == y)
print(x > y)
print(x >= y)
print(x != y)
print()

a = "kate"
b = "kathrina"
print(a < b)
print(a <= b)
print(a == b)
print(a > b)
print(a >= b)
print(a != b)
print()

# print(a < x) # Returns TypeError meaning it cannot evaluate the condition of two different data types

# Boolean Operators
# and / logical_and() (If both are true, then it is true)
# or / logical_or() (If one is true and one if false, then it is still true)
# not / logical_not() (If not true, then it is false)
var1 = 9
var2 = 10

print(var1 < var2 and var1 != var2)
print(var1 < var2 and var1 == var2)
print(var1 > var2 and var1 == var2)
print(var1 > var2 and var1 != var2)
print()

print(var1 < var2 or var1 != var2)
print(var1 < var2 or var1 == var2)
print(var1 > var2 or var1 == var2)
print(var1 > var2 or var1 != var2)
print()

print(not(var1 < var2 and var1 == var2))

grades = [75, 74, 90, 89, 85, 89, 63, 95, 96, 97, 92, 91, 93, 72, 81, 83, 60]
# print(grades[grades > 75 or grades == 75]) # Throws a TypeError since two conditions cannot be carried out in an array

np_grades = np.array(grades)
passing_grades = np.logical_or(np_grades > 75, np_grades == 75)
print(passing_grades)
print(np_grades[passing_grades])
failing_grades = np.logical_and(np_grades >= 60, np_grades < 75)
print(failing_grades)
print(np_grades[failing_grades])


# Conditional statements (if elif else statements)
print("Input a number", "\n")
num = int(input())

# Logical circuiting / short circuit evaluation - will stop evaluating as soon it finds a condition that allows it to make a definitive conclusion
if num % 10 == 0:
    print(str(num), "is divisible by 10")
elif num % 2 == 0:
    print(str(num), "is an even number")
else:
    print(str(num), "is an odd number")
