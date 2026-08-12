Lesson 5 Conditional Statements

Algorithms: step-by-step procedures for solving problems
Flowcharts: visualization of algorithms using symbols and arrows
Pseudocode: imitation of code using plain English to describe the logic of a program

Integer Divisions and Modulus Operators
    Integer Division (//): returns the (INTEGER VALUE WITHOUT DECIMAL) quotient of a division operation, discarding any remainder
    Modulus Division (%): returns the remainder of a division operation
    Usual Division (/): returns the (FLOAT VALUE WITH DECIMAL) quotient of a division operation

minutes = 105 
minutes // 60   # 1
minutes / 60    # 1.75
minutes % 60    # 45, remainder

Computing for remainder without using the MODULO (%) operator
hours = minutes // 60
remainder = minutes - (hours * 60) # 45

Boolean Values | Boolean values are either true or false values
type(True)  # <class 'bool'>, which is a reserved word. 
type(False) # <class 'bool'>, which is a reserved word.

Comparison Operators | Comparison operators are used to compare values and return a boolean result (True or False).

x = 6
y= 7
a, b = 5, 5 # a = 5, b = 5 
a == b      # USE THIS TO TEST, ERROR AS OF RIGHT NOW BUT IT SHOULD RETURN TRUE.

To check for boolean values, we can use comparison operators such as:
    == (equal to)           # IF ONLY SINGLE EQUAL, you are doing ASSIGNMENTS, if DOUBLE EQUAL, you are doing comparisons
    != (not equal to)       # Can use NOT instead of !
    > (greater than)
    < (less than)
    >= (greater than or equal to)
    <= (less than or equal to)

Logical Operators | Logical operators are used to combine multiple boolean expressions and return a boolean result (True or False).

Logical Operators:
AND (and) - returns True if both expressions are True, otherwise returns False         # XAND
    # Example: x > y and a == b # False and True = Returns False
    ### Note: In math, 1 is on switch, 0 is off switch, 0 ^ 1 = 0 (^ = caret) [DISJUNCTION] ###
    # CONJUNCTION, both statements need to be true for the result to be true, if one is false, the result is false
    # XAND (xand) - returns True if both expressions are True, otherwise returns False

OR (or) - returns True if at least one expression is True, otherwise returns False    
    # Example: x > y and a == b # False and True = Returns True
    ### Note: In math 0 v 1 = 1 (v = vee/wedge) [DISJUNCTION] ###
    # DISJUNCTION, if one statement is true, the result is true, if both statements are false, the result is false
    # XOR (xor) - returns True if exactly one expression is True, otherwise returns False      # XNOR

NOT (not) - returns the opposite boolean value of the expression # If the condition is TRUE, then the value is FALSE.
    # Lets say we do not x > y, which means not False, which means TRUE. If we do not a == b, which means not True, which means FALSE.
    ### Note: In math ~0 = 1 (~ = tilde) ###




###########################################################################

CONDITIONAL STATEMENTS | allows you to execute code based on specific conditions
# if statement: executes a block of code if a condition is True [in pseudocodes, it is denoted as "IF, THEN"]
# elif statement: stands for "else if" and allows you to check multiple conditions
# else statement: executes a block of code if all previous conditions are False

IF STATEMENTS SYNTAX: 
Example:
x = 10                                  
if x > 0:                      # line 1
    print("x is positive")     # line 2

# if x < 0, it prints nothing since the condition is false, it skipped it.
# Common errors and Possible errors:

x = 10
if x > 0                     # SyntaxError: expected ':", Error in the structure
    print("x is positive")   # IndentationError: unexpected indent, since line 75 has an error, line 76 will run independently.

# SyntaxError, missing colon (:) on line 74.
# IndentationError, unexpected indentation.

x = 10
if x > 0                    
print("x is positive") # IndentationError: expected indented block.


###########################################################################

ELSE STATEMENT SYNTAX: [if-else statements]
if <condition>: 
    # Input code to execute if condition is TRUE.
else:
    # Code to execute if condition is FALSE.

# Note: ELSE statements are OPTIONAL, AND CAN BE USED TO PROVIDE AN ALTERNATIVE BLOCK OF CODE WHEN THE IF CONDITION IS NOT MET.
x = -9
if x > 0:
    print("x is positive")
if x < 0:  
    print("x is negative") 
# This line of code is valid and printed "x is negative"!

# Possible Errors in Else Statements:
x = -9
if x > 0:                       
    print("x is positive")      # line 1
else x < 0:                     # line 2, ERROR, SyntaxError: expected ':', the correct code is just "else:""
    print("x is negative")      # line 3, ERROR, IndentationError: unexpected indent, since line 106 has an error, line 107 will run independently.


###########################################################################

ELIF STATEMENT SYNTAX: [CHAINED CONDITIONALS] [if-else, if-else statements] 
# if <condition1>: 
    # Input code to execute if condition is TRUE.
# elif <condition2>:
    # Code to execute if condition2 is TRUE.
# else:
    # Code to execute if condition is FALSE.
the elif statement allows you to check multiple conditions in a SEQUENTIAL MANNER, if the first condition is false, it will check the next condition until it reaches the else statement.

# Note: in an if-elif-else statement, you can remove the else, but it is generally recommended to include it to handle cases where none of the conditions are met.
# It is better to have code CLOSE BOUNDED (every code is closed), to prevent unexpected behaviour in the code.
Example:
x = 0
if x > 0:
    print("x is positive")
else:  
    print("x is negative") 
# There is an error here, although it runs, it has an logic error, where it prints that x(which is 0) is negative, which is entirely false.
# This is called an SEMANTIC ERROR, an error in the code through logic but runs.

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative") 
else:  
    print("x is neither negative nor positive") 
