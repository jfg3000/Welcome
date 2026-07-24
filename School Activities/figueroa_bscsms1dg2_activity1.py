
""" Instructions:
1. Create a new Python file named lastname_pysg_activity1.py (replace "lastname" with your surname, and “pysg” with your complete program, year and section ).
2. Complete all three problems below in order. Label each problem clearly using comments (e.g., # Problem 1).
3. Test your code after writing each problem to make sure it runs without errors.
4. Add comments explaining what each block of code does.
5. Once finished, save your file (as a .py file) and submit it through the designated submission board in the
Microsoft Teams assignment tab or on a provided Google form on or before Tuesday, 28 April 2026, 10PM .
Late submissions will not be accepted. """

# Problem 1. Student Profile Card
""" Create variables to store a student's profile information: name (string), age (integer), gpa (float), and is_enrolled
(boolean). After that, it should be printed as a formatted profile card using these variables, like as presented below. """

print()                             # adds kind of link a space bar for the code to look better in run haha
print("Student Profile Card")       # Student Profile Card
name = "Jefferson Figueroa"
print(f"Name: {name}")              # prints "Name: Jefferson Figueroa", used f-strings to indicate the said variable (name)
age = 17                            # used f-strings to incorporate the math things and varibles inside of a text hahaha
print(f"Age: {age}")                # prints "Age: 17", same context for the f-strings as the print(f"Name: {name}") one. 
gpa = 3.50
print(f"GPA: {gpa}")                # prints "GPA: 3.5", same context for the f-strings as the print(f"Name: {name}") one. 
is_enrolled = True
print(f"Enrolled: {is_enrolled}")   # prints "Enrolled: True", same context for the f-strings as the print(f"Name: {name}") one. 
print()

# Problem 2. Simple Grade Calculator
""" Create a list called scores containing 5 numeric grades (integers or floats), e.g. [85, 90, 78, 92, 88]. After that, it should:
1. Calculate the total sum of scores using sum().
2. Calculate the average by dividing the sum by the number of scores (use len()).
3. Store the result in a variable called average.
4. Print the total and average with a descriptive message, e.g. "Average score: 86.6". """

scores = [75, 80, 85, 90, 95]      # stored the list of 5 integers inside of variable "scores"
sumofscores = sum(scores)          # labelled "sumofscores" to store it as a variable para goods lang po sorry sir hehe, the sum() function lets you add up values of integers or floats inside of a list 
print(sumofscores)                 # printed "425", printed the sum of the variable "scores", well since its integers yung nilalaman nung list directly computed the sum.

lengthofscores =  len(scores)      # labelled "lengthofscores" to store it as a variable para goods,  the len() function lets know how many items are inside of a list, in this instance 5 
print(lengthofscores)              # printed "5", printed the length of the variable "scores", same context as print(sumofscores), same context as print(sumofscores)

average = sumofscores / lengthofscores   # the formula for the average is sum of the "" DIVIDED and the length of the "", in this case "" is list. Just divided both of the variables and used DIVISION which is indicated as /
print(f"Average score: {average}")       # printed "Average score: 85.0", used f-strings to incorporate other values (in this case math values) and VARIABLES and merge it into one print inside of a text hahaha.
print()

# Problem 3. Grocery List Manager
""" Create a list called groceries with at least 5 items (strings) you'd buy at a store. After that, do the following tasks:
1. Print the first and last item using indexing.
2. Add a new item to the end of the list using .append().
3. Remove one item using .remove().
4. Print the total number of items using len().
5. Print the final list.# """

grocery = ["water", "milk", "food", "snacks", "canned goods"] # created a list called "grocery" which contained "water, milk, food, snacks, canned goods"
firstitem = grocery[0]     # labelled it as "firstitem" just for it to be cleaner sir arcel galvezzzz, accessed the FIRST in the list through grocery[0], which was "water"
print(firstitem)           # printed "water" 
lastitem = grocery[-1]     # labelled it as "lastitem", printed the LAST item in the list which was "canned goods", used grocery[-1] which counted backwards from the end of the sequence or list
print(lastitem)            # printed "canned goods", also as to why grocery[-1] is better, its because in using negative indexing, you can print the last item in the list WITHOUT KNOWING THE LENGTH OF THE LIST AND TO BE EFFICIENT

print(f"{grocery[0]}, {grocery[-1]}")   # can also use this, which prints the first and last item in the list in just one line of code, used f-strings to print more than one assigned variable and value

grocery.append("vegetables")                    # .append() lets you ADD an item or a value in a list, when you append, the item that you appended ALWAYS appears at the end of the list (unless you use like .insert), i used .append("vegetables"), in which added vegetables to the end of the list.
grocery.remove("snacks")                        # .remove() lets you REMOVE an item from the list, this is CASE SENSITIVE. i used .remove("snacks"), which removed snacks from the list
print(f"Total number of items: {len(grocery)}") # printed the length of the list "grocery" which is "5", just added an f-string just to make it more cleaner haha. .len() lets you know how many items are inside of a list
print(grocery)                                  # FINAL LIST: ['water', 'milk', 'food', 'canned goods', 'vegetables'] | LIST BEFORE: ["water", "milk", "food", "snacks", "canned goods"]
print()
