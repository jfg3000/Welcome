CONDITIONAL STATEMENTS IN PYTHON 

Conditional Statements allows us to execute certain blocks of code based on 
specific instructions and whether if a condition is TRUE or FALSE.

THREE TYPES OF CONDITIONAL STATEMENTS:
    1. if statement: executes a block of code if a specific condition is true
    2. if-else statement: executes two blocks of code, one for true, and one for false
    3. if-elif-else statement: allows to check MULTIPLE conditions based on a condition which is true.
# Note: the else statements can be removed only if we want to check for a single condition.

Lists: lists are collections of items that are MUTABLE(can be changed after creation)
In python, we can use conditional statements to manipulate lists based on certain conditions.
Conditional statements are often used with loops to iterate through a list to perform actions.STATEMENTS



EXAMPLE 1: Checking for special items in a list,
# Note that we use the keyword "in" to check if an item exists in a list.

colors = ["blue", "green", "red"]
if "blue" in colors:
    print("Blue is in colors")
else:
    print("Blue is not in fruits")



EXAMPLE 2: Checking that a list is not empty

items = []  # THIS IS AN EMPTY LIST
if items:                                       # THIS LINE CHECKS IF THERE IS ITEMS IN THE LIST.
    print("The list of items is not empty")
else:                                           # THIS CHECKS IF THERE ARE NO ITEMS IN THE LIST
    print("The list is empty")



EXAMPLE 3: Number Filtering
Lets say that we have a list, and we want to filter out the EVEN NUMBERS in the list
for this we will use loops along with an if statement

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []

for number in numbers:                # THIS LINE SHOULD INCLUDE A COUNTER VARIABLE (in this case 'number')
    if number % 2 == 0:               # THIS LINE SHOULD ALWAYS INVOLVE THE COUNTER VARIABLE FROM THE FOR LOOP
        even_numbers.append(number)
print("Even numbers: ", even_numbers) # NOTICE THAT WE DID NOT PUT AN "else" statement, ITS BECAUSE IT IS NOT NEEDED BECAUSE EVEN NUMBERS WERE THE ONLY 



EXAMPLE 4: List Comprehension with Conditional Statements
# List comprehension is basically shortening of code for optimization.
#  for example, we can create a list of squares of even numbers from the original list of numbers.
# Syntax : list_name: [<code block> for <counter*> in <list> if <condition]

numbers = [1, 2, 3, 4, 5, 6] 
squared_even_numbers = [number ** 2 for number in numbers if number % 2 == 0]
print("Squared Even Numbers: ", squared_even_numbers)
# number ** 2 = what needs to be done
# for number in number = 
# if number % 2 == 0 = the condition



EXAMPLE 5: Filtering strings based on length
# We can determine the length of a string using len()
# Lets say we have a list of words and we want to filter out words that have 5 characters or longer

words = ["wowwers", "bsmcs", "stem", "philippines", "lmdk", "feddde", "dada"]
long_words = []                       # This is were all words longer with 5 characters go

for word in words:                  # COUNTER: "word", LIST: "words"
    if len(word) > 5:
        long_words.append(word)
print("Long words: ", long_words)



EXAMPLE 6: List Comprehension of FILTERING STRINGS based on length
# Syntax : list_name: [<code block> for <counter*> in <list> if <condition]
words = ["wowwers", "bsmcs", "stem", "philippines", "lmdk", "feddde", "dada"]
long_words_comprehension = [word for word in words if len(word) > 5]   
print("Words longer than 5 characters (using list comprehension): ", long_words_comprehension)



########################################
USING MULTIPLE LISTS WITH CONDITIONAL STATEMENTS
# We can also use multiple lists and conditional statements at the same time.
# When finding common elements like this, its better to seperate it between one list( that goes inthe loop), and the other list( that is the condition)
EXAMPLE 7: Finding common elements between 2 lists
list1 = [1, 2, 3, 4, 5, 6, 7]        # Yung paiikutin or nasa loop.
list2 = [6 ,7 ,8 ,9, 10, 11 ,12]     # Basehan or condition
common_elements: []

for num in list1:
    if num in list2:
        common_elements.append(num)
print(common_elements)

# List comprehension (Not done)
li

EXAMPLE 8: Using multiple lists with conditional statements
# Lets say we have a list of toppings and a customer orders specific toppings, we want to know
# if the requested toppings are available

available_toppings = ["sprinkle", "pepper", "pineapple", "cheese", "barbeqcue", "olives"]   # IF
requested_toppings = ["pater", "water", "cheese"]   # FOR

for requested_topping in requested_toppings:
    if requested_toppings in available_toppings:
        print(f"Adding {requested_topping}".)
    else:
        print(f"{requested_topping} is not available.")
print("Finished making your order!")



################################################
KEYBOARD INPUT AND CONDITIONAL STATEMENTS
# We can also use user input and conditional statements

EXAMPLE 9: Asking a user to input a number and checking if its positive, negative, or zero
user_input = input("Enter a number bro: ")

if user_input > 0:
    print("The number si positive")
elif user_input < 0:
    print("The number is negative:")
else:
    print("The number is zero")