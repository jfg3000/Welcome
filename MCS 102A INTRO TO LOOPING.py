## DEMO 3 - WORKING WITH LISTS JULY 22 2026

## Data types and structures
## Simple data types: Strings, Integers, Float numbers, Boolean (OR TRUE OR FALSE)
## Compound data types: Lists, Dictionaries, Tuples, Sets

## Recall: Lists
# Lists - data structure used to store multiple items

fruits = ["apple", "date", "cherry", "banana", "grape"]
print(fruits)
# print(fruits.title()) # AttributeError: 'list' object has no attribute 'title'
print(fruits[0].title())

### INTRODUCTORY TO LOOPING ###
# Looping is the most common way to automate tasks in a computer
fruits = ["apple", "banana", "cherry", "date", "grape", "fig"]
print(fruits)

# FOR LOOP
for fruit in fruits:
    print(fruit) # This will only work for the text above if its INDENTED and if its TRUE,
                 # this wil not work if its for fruit in fruits = false or something
                 # fruit = string, fruits = strings
                # IF fruits is a string variable, and fruit is a string, then you can apply str methods and functions

# MORE WORK FOR LOOPS
for fruit in fruits:
    print(fruit.title())
    print(f"My favorite fruit is {fruit.upper()}")
print("dih")

# Making a Numerical List: range(start(inc)), end(exc), step)
for value in range(1, 10):
    print(value) # For python, the first index number will always be included, but the last index is EXCLUDED
                 # So if its 1 TO 10, it will only run to 1 TO 9.
                 # (range(start(included), end(excluded) IF AND ONLY IF TWO ARGUMENTS

for value in range(6):
    print(value) # This is technically only giving a range END Value,
                 # If only 1 argument, it will count as the END variable
                 # The start number will always be 0 so ( THIS PRINT WILL COUNT FROM 0 TO 5 )

# SKIP COUNTING
for value in range(1, 100, 8):
    print(value) # range(start(included), end(excluded), step(increments/decrement)

# Creating Lists from range()
num_count = []

numbers = list(range(5, 51, 5)) # FOR INCREASING ORDER
print(numbers) # Creating a list from 5 to 50, in multiples of 5 (inc of 50)
type(numbers)

num_seq = list(range(50, 4,-5)) # FOR DECREASING ORDER
print(num_seq) # Creating a list from 50 - 5, in reverse, in multiples of 5

numbers.reverse()
print(numbers)

num_count1 = []
for value in range(2, 21, 2):
    num_count1.append(value)
print(num_count1) # ONLY PRINTED ONCE


num_count2 = []
for value in range(2, 21, 2):
    num_count2.append(value)
    print(num_count2) # PRINTED 10 NUMBERS

num_count3 = []
for value in range(2, 21, 2):
    squares = value ** 2
    num_count3.append(squares)
    print(num_count3) # PRINTED 10 NUMBERS


print(num_count1)
print(num_count2)

######## SIMPLE STATISTICS WITH A LIST OF NUMBERS ###############
print(num_seq)
print(num_count1)

min(num_seq)
min(num_count1)
max(num_seq)
max(num_count1)


##### LIST COMPREHENSIONS ####
# List Comprehensions allows you to generate lists using one line of code.
num_cnt = [value ** 2 for value in range(2, 21, 2)] # REFERENCE FOR line num_count3
print(num_cnt)      #[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
print(num_count3)   #[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
                    # Both codes have the same output, BUT PRINT num_cnt IS MORE EFFICIENT BECAUSE IT IS SHORTER.

### Working with part of a list ###
# Slicing = Accessing part of a list
colors = ["red", "blue", "green", "yellow"]
print(colors[1:3]) # Accessing a range of items in the list, (from index 1 to index 2)
print(colors[:4]) # Accessing a range of items in the list (FROM THE BEGINNING to index 4)
print(colors[1:]) # Accessing a range of items in the list (index 1 to THE LAST INDEX)
print(colors[-3:]) # If you want to print the last 3 vars

## LOOPING WITH A SLICE ##
for fruit in fruits[-3:]:
    print(fruit.title())

for fruit in fruits[-3:]:
    print(f"herehrehrehrherhe: {fruit.title()}")

## COPYING A LIST ##
fav_foods = ["samgyup", "chicken_wings", "adobo", "bulalo"]
pinoy_foods = fav_foods[:]

fav_foods.append("ramen")
pinoy_foods.append("sisig")

print(fav_foods) # ['samgyup', 'chicken_wings', 'adobo', 'bulalo', 'ramen']
print(pinoy_foods) # ['samgyup', 'chicken_wings', 'adobo', 'bulalo', 'sisig']

#### TUPLES #####
# A tuple just looks like a list, except you are using PARENTHESIS INSTEAD OF SQUARE BRACKETS. Once you define
# A tuple, you can access individual elements by using each item's index. just as you would for a list.
# A tuple is immutable (UNCHANGEABLE) list. the elements inside CANNOT be changed.

tpl_week = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(tpl_week)
print(tpl_week[0])
print(tpl_week[0].upper())

## WRITING OVER A TUPLE ##
tpl_week[-3] = "Thursday" # TypeError: 'tuple' object does not support item assignment
tpl_week = ("Mon", "Tue", "Wed", "Thursday", "Fri", "Sat", "Sun")
print(tpl_week[-3:])


#ts too hard
