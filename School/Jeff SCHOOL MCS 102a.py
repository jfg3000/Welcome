### MCS 102a JULY 15 2026
from itertools import count
from random import shuffle

num1 = 4324234
num2 = 2312312
total1 = print(f"Sum: {num1 + num2}")

# String = a set of characters in a line
# "c" = character
# "chat" = string

# TEST TEST TEST TEST "This is a comment"

message = ("jefferson test")
message = ("jefferson test 222")
print(message)

# Notice how python printed the most recent one, so if a variable has the same name, it will print the latest one.

message1 = ("I like this python thing")
message2 = (f"I like this python thingy\n")
print(message1)
print(message2)

############### ESCAPE CHARACTERS = It is used whenever there is more than one single(1) or double(2) apostrophe or quote being used in the string
# it is denoted as \ backslash

############### TITLE CASES ##############
message3 = "BuLacAn StaTe UnIveSsity"
print(message3.title()) # Title Case
print(message3.upper()) # All caps
print(message3.lower()) # All lower case

############### WHITE SPACES - vertically or horizontal spaces/spacebars ##############
# \n adds a vertical space, \t for horizontal space or indent
note1 = ("This is the first, \tthis is the second.\n")
print(note1)
note2 = ("This is the first,\nthis is the second\n")
print(note2)

############### Whitespaces: Strips  ##############
# .strips is a command that removes all unnecessary spaces in code, for example:
phrase1 = ("jefferson                   ")
print(phrase1)
phrase2 = ("Jefferson\n                  ")
print(phrase2.rstrip())
# .Lstrip = strips the left side of the string
# .Rstrip = strips the right side of the string
# .strip = strips the both sides of the string

#CONCATENATION = the process of joining separate items, such as text strings, lists, or events, end-to-end into a single continuous sequence

#### MCS 102a JULY 17 2026 (DEMO 1)

############## Removing Prefixes in Strings ##############
website_url = "https://www.youtube.com/jefferson"
print(website_url)

website_url.removeprefix("https://") # Removes the specified prefix of the string, SPELLING IS IMPORTANT,
# THE STRING MUST EXIST SO THE SPELLING IS IMPORTANT, IF ONE LETTER IS MISSING IT WONT WORK!
print(website_url.removeprefix("https://"))

website_url = website_url.removeprefix("https://") # UPDATE THE STRING SO IT IS EASIER TO PRINT!
print(website_url)

# METHOD = dinudugtong mismo sa variable
# FUNCTION = sa loob ng parenthesis nilalagay ang variable name

############## Numbers ##############
# Integers = Whole numbers
# Float number = Decimal numbers
1 + 2
3           -    5 # Python will read it as 3-5 and will disregard the whitespaces
5 / 2 # Division written in code like this will always give a Float number (Decimal)
4 / 2 # This too will also give a Float number

5 // 2 # INTEGER DIVISION OPERATOR, this will give a whole number as an answer
3 ** 2 # EXPONENTIATION OPERATOR, for exponents.
3 ^ 2 # XOR / exclusive or operator ( exactly one of the components must be true for it to be true)

### PEMDAS in Python will always follow the PEMDAS from left to right.

############## Multiple assignments ##############
x = 1
y = 2
z = 3
x, y ,z = 1, 2, 3
x + y + z

### In python math, whenever a variable is ALL CAPS, it is a CONSTANT
MAX_YEAR = 10000

## The import statement allows you to import math modules and use their funtions in your code.
import math
import this # The Zen of Python


### MCS 102a JULY 17, 2026 (DEMO 2, NEW LESSON)

########################### CREATING LISTS ##########################################
# Lists = are used to store multiple items
# They are created using square brackets [] while items being seperated by commas
# Called in C++ as "Arrays"

############## Creating a list ##############
colors = ["red", "blue", "green", "yellow"]
print(colors)

############## Accessing the elements or items in a list ##############
## Note that index positions or the first item will always start at 0, not 1
print(colors[0]) # Accessing the first item in the list
print(colors[3]) # Fourth Item in  the list
print(colors[-1]) # Accessing the last item in the list
print(colors[-2]) # Accessing the second to the last item in the list

# IF FROM START TO FINISH, WE CAN START FROM 0, 1, 2 ,3 ...
# IF FROM FINISH TO START, WE CAN START FROM -1, -2, -3 ....

# We can also access more than one item in the list,
print(colors[1:3]) # Accessing a range of items in the list, (from index 1 to index 2)

# NOTICE HOW IT DID NOT COUNT YELLOW, INSTEAD IT IS BLUE,
# THE  INDEX NUMBER COUNTS THE NUMBER BEFORE IT OR AFTER IT WHEN DOING THIS COMMAND, SO IF YOU TYPE THE 3, IT WILL ONLY COUNT TO THE 2
# SO IF YOU TYPE 1 (BLUE), IT WILL COUNT 2(GREEN) IN PRINTING A RANGE OF ITEMS IN A LIST
print(colors[:4]) # Accessing a range of items in the list (FROM THE BEGINNING to index 4)
print(colors[1:]) # Accessing a range of items in the list (index 1 to THE LAST INDEX)

############## Incorporating commands in a list in a string ##############
# print(colors.title()) # WILL NOT WORK
print(colors[3].title()) # CORRECT COMMAND

############## Incorporating lists in a string using f-strings ##############
note3 = f"I like the color {colors[1].title()}" # It should look like this
print(note3)

############## Modifying items in a list ##############
print(colors) # ['red', 'blue', 'green', 'yellow']
# To change items in a list, first input the index number of what you want to change and equal it to a variable that you want.
colors[2] = "violetblack"
print(colors)  # ['red', 'blue', 'green', 'yellow']
colors[3] = colors[3].upper() # Changing cases or title cases of items in lists.
print(colors) # ['red', 'blue', 'violet', 'YELLOW']
colors[0] = "Rainbow"
colors[0] = colors[0].title()
print(colors) # ['Rainbow', 'blue', 'violetblack', 'YELLOW']

############## Common Errors ##############
#colors = "color spectrum" # Replacing the list with a string variable.
#print(colors) # Changed the variable from a list to a string.

############## Adding items in a list ##############
## You can add items in a list using the:
# APPEND METHOD: .append() APPEND = ADDING SOMETHING IN A LIST
fruit_basket = ["apple", "banana", "cherry", "orange"]
print(fruit_basket) # ["apple", "banana", "cherry", "orange"]
fruit_basket.append("AVOCADO")
print(fruit_basket) # ['apple', 'banana', 'cherry', 'orange', 'AVOCADO'] # whenever you add in a list, it will add it at the end as a standard.

BULSUCS1D = []
print(BULSUCS1D) # []
BULSUCS1D.append("Jefferson Figueroa")
BULSUCS1D.append("Jefferson")
BULSUCS1D.append("Jeff")
print(BULSUCS1D) # ['Jefferson Figueroa', 'Jefferson', 'Jeff'] # The order of the list will always be the order that you inputed the data in string

BULSUCS1D[1] = "Estrada"
print(BULSUCS1D) # ['Jefferson Figueroa', 'Estrada', 'Jeff']

BULSUCS1D[1] = BULSUCS1D[2].upper()
print(BULSUCS1D) # ['Jefferson Figueroa', 'JEFF', 'Jeff']

############## Inserting items in to a list using the: ##############
# INSERT METHOD: .insert() requires to variables, the index number and variable name
BULSUCS1D.insert(1, "JFG")
print(BULSUCS1D) # ['Jefferson Figueroa', 'JFG', 'JEFF', 'Jeff'] # Notice how python added the variable the after the index number that you inputed it in.
# If you type in index1, it will show it up index2. or ISININGIT yung variable pagkatapos ng index1, or inbetween index1 and index3.

# If sobra yung index number from the list itself, it will work like just the .append() command as it will appear in the end
BULSUCS1D.insert(10, "JFG")
print(BULSUCS1D) # ['Jefferson Figueroa', 'JFG', 'JEFF', 'Jeff', 'JFG']

############## Removing items from a list ##############
# We can remove items from a list using the:
# DELETE STATEMENT: del [RESERVED WORD NI PYTHON]
# REMOVE STATEMENT: .remove()
# POP STATEMENT: .pop() # If we use pop, matatanggal agad yung nasa DULO

### DEL METHOD ###
del BULSUCS1D[2]
print(BULSUCS1D) # ['Jefferson Figueroa', 'JFG', 'Jeff', 'JFG'], we removed 'JEFF' from the list.

### POP METHOD (TINATANGGAL AGAD YUNG DULO, DEFAULT VALUE OF -1,) ###
BULSUCS1D.pop(-1)               # Returns, then removes the last item in the list.
print(BULSUCS1D)                # ['Jefferson Figueroa', 'JFG', 'Jeff'] removed 'JFG' from the list
cs1d_student = BULSUCS1D.pop()  # The last item in the list is already removed, but saved in another variable.
print(BULSUCS1D)                # ['Jefferson Figueroa', 'JFG'] removed 'Jeff' from the list

### REMOVE METHOD ###
class_mayor = "JFG"
BULSUCS1D.remove(class_mayor)
print(BULSUCS1D)              # ['Jefferson Figueroa'] removed "JFG"
BULSUCS1D.append("JFG")
BULSUCS1D.append("Jeff")
BULSUCS1D.insert(4, "JFG")
print(BULSUCS1D)              # ['Jefferson Figueroa', 'JFG', 'Jeff', 'JFG']
BULSUCS1D.remove(class_mayor) # The first OCCURRENCE of the contents of class_mayor will be removed.
print(BULSUCS1D)              # ['Jefferson Figueroa', 'Jeff', 'JFG'] removed the first JFG from the list.

############## Organization of items in a list ##############

### Sorting ###
# There are two ways to sort items in python:
### .sort() method: changing the order of the list PERMANENTLY. ###
print(BULSUCS1D)             # ['Jefferson Figueroa', 'Jeff', 'JFG']
BULSUCS1D.append("Mom")
BULSUCS1D.append("Estrada")
print(BULSUCS1D)             # ['Jefferson Figueroa', 'Jeff', 'JFG', 'John', 'Estrada']
BULSUCS1D.sort()             # Using this, we will arrange the list in ASCENDING ORDER. Be it ALPHABETICAL or NUMERICAL
print(BULSUCS1D)             # ['Estrada', 'JFG', 'Jeff', 'Jefferson Figueroa', 'Mom'] Notice how E was first, and M was last.
BULSUCS1D.sort(reverse=True) # Using this, we will arrange the list in DESCENDING ORDER.
print(BULSUCS1D)             #['Mom', 'Jefferson Figueroa', 'Jeff', 'JFG', 'Estrada'] Notice how M was first, and E was last.

### sorted() function: lets you display the order of the list in a particular order, but doesnt actually affect the order of the list. ###
fruit_basket = ["orange", "cherry", "banana","apple"]
print(fruit_basket)                       # ["orange", "cherry", "banana","apple"]
print(sorted(fruit_basket))               # ['apple', 'banana', 'cherry', 'orange'] Arranged now in ALPHABETICAL ORDER.
print(sorted(fruit_basket, reverse=True)) # ['orange', 'cherry', 'banana', 'apple'] Arranged now in REVERSE ALPHABETICAL ORDER.
print(fruit_basket)                       # ['orange', 'cherry', 'banana', 'apple'] ACTUAL LIST.

### reverse() method: printing the order of the list in REVERSE ORDER. ###
print(fruit_basket)           # ['orange', 'cherry', 'banana', 'apple']
fruit_basket.reverse()        # reversing the position in the list, PERMANENTLY
print(fruit_basket)           # ['apple', 'banana', 'cherry', 'orange']
fruit_basket.reverse()        # undoes the reserve of positions in the list, PERMANENTLY since only positions were reversed.
print(fruit_basket)           # ['orange', 'cherry', 'banana', 'apple']

# Knowing the number of elemetns in the list >> Finding the length of the list.
### len() function = to determine the length of the list ###
fruit_basket.index("orange")
print(fruit_basket)