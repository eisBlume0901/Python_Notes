# Lists
# [] - lists use square brackets and its elements is separated by comma
# It can contain combination of different data types (unlike in Java, only one data type is required)
# myList[index] - accepts integers or slices only, returns the value of an element
# negative indexing - starts at the last element (-1, -2, ...)
# positive indexing - starts at the first element (0, 1, ...)
# slicing - [inclusive_start:exclusive_end] - returns specified range of elements,
#           [:] - returns all elements,
#           [:exclusive_end] - starts at 0 and ends at specified end,
#           [inclusive_start:] - starts at a specified start until the last element
mySubjectGrades = ["Science", 95, "Math", 94, "English", 90, "History", 91, "Arts", 97, "Physical Education", 89, "Social Studies", 93]
print(type(mySubjectGrades))
print(mySubjectGrades)
# positive indexing
print(mySubjectGrades[0])
print(mySubjectGrades[1])
# negative indexing
print(mySubjectGrades[-2])
print(mySubjectGrades[-1])
# slicing
print(mySubjectGrades[2:6])
print(mySubjectGrades[:])

print(mySubjectGrades[:6]) # ['Science', 95, 'Math', 94, 'English', 90]
print(mySubjectGrades[6:]) # ['History', 91, 'Arts', 97, 'Physical Education', 89, 'Social Studies', 93]

print(mySubjectGrades[-4:]) # ['Physical Education', 89, 'Social Studies', 93]
print(mySubjectGrades[:-8]) # ['Science', 95, 'Math', 94, 'English', 90]

# [row][col] - fetch row and then col (list specifically and can do slicing)
mySubjectGrades1 = [
    ["Science", 95],
    ["Math", 94],
    ["English", 90],
    ["History", 91],
    ["Arts", 97],
    ["Physical Education", 89],
    ["Social Studies", 93]
]
print(type(mySubjectGrades1))
print(mySubjectGrades1)
print(mySubjectGrades1[4][:]) # ['Arts', 97]
print(mySubjectGrades1[1][1]) # 94
print(mySubjectGrades1[-3][0]) # Arts

# manipulating lists (+, del(), )
fruits = ["apple", "banana", "orange", "mango", "grapes", "watermelon", "pineapple"]
print(fruits)
# adding elements using +
more_fruits = fruits + ["strawberry", "kiwi", "cherry"]
print(more_fruits)
# deleting elements using del()
del(fruits[-2])
print(fruits)
del(more_fruits[-4])
print(more_fruits)

colors1 = ["red", "orange", "yellow", "green", "blue", "violet"]
# Be careful when copying the same array and manipulating it in a newly stored
# variable because it also overrides the original one
colors2 = colors1
colors2[1] = "pink"
print(colors1)
print(colors2)

# Use list() or [:] to override and properly copy the list
# colors2 = list(colors1) # version 1 using list()
colors2 = colors1[:] # version 2 using originalArr[:]
colors2[-1] = "lavender"
colors1[1] = "orange"
print(colors1)
print(colors2)


