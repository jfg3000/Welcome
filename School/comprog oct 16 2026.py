# Functions in Python

##   This will be divided into 4 parts:   ## 
# 01: Build / define and call functions
# 02: Pass / parameters and arguments
# 03: Return / produce reusable values
# 04: Reuse / lists, modules, flexible inputs

# IMPORTANT NOTE: parameters = arguments, or parameters > arguments if there is a default value.

## Functions can be defined using the def keyword, followed by the function name and parentheses.
## def function_name():
    # "Block of Code":

def greet_user(name):     # greet_user is the function name, and name is the parameter
    message = f"Hello my friend called {name}!"   # Block of code that will be executed when the function is called
    print(message)

userinput = input("Enter your name: ")
greet_user(userinput)

## Positional Arguments ORDER MATTERS

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

animal_type = input("Enter the type of animal: ")
pet_name = input("Enter the name of the pet: ")
describe_pet(animal_type, pet_name)  # Positional arguments are passed in the order they are defined in the function

## Keyword Arguments ORDER MATTERS

describe_pet(
    animal_type="hamster", 
    pet_name="harry"
)  # Keyword arguments are passed in the order they are defined in the function

## Default Values you can put default values inside of the parameters of functions, 
# It should always be placed in the last place of the parameters

# Keyword argument in this is anime_name="JJK" in the parameter
def describe_anime(anime_type, anime_name="JJK"):
    """Display information about an anime."""
    print(f"\nI like {anime_type} type of animes.")
    print(f"The GOAT of {anime_type} type animes is {anime_name.title()}.")

user_anime_type = input("Enter the type of anime: ")
describe_anime(user_anime_type)  

# Practice:
def make_shirt(size, message="I love ComSci"):
    """Display information about a shirt."""
    print(f"\nThe size of the shirt is {size}.")
    print(f"The message on the shirt is '{message}'.")

make_shirt("L")  # Default message will be used
make_shirt("M", "I love Python")  # Custom message will be used
make_shirt(size="S", message="I love Coding")  # Keyword arguments can be used to specify the parameters in any order
make_shirt(message="I love Coding", size="XL")  
print("\nor")
## sizers = input("Enter the size of the shirt: ")
## make_shirt(sizers)

## Difference between print() and return in functions
# Key takeaways
# print() = displays a message to the screen, it returns to the user
# return = same as print(), but returns a value to the program, which can be saved into an variable or object
# datatypes that can be returned: (int, str, float, boolean, lists, collections of data, etc.)
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

areasq = calculate_area(5, 10)  # The return value is saved into the variable areasq
print(f"The area of the rectangle is: {areasq}")

# If else statements in functions
def full_name(first, last, middle=""):   # middle="" is treated as false in default, if it is not provided, it will be treated as an empty string
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

fullname = full_name("jefferson", "figueroa")
print(fullname)
fullname2 = full_name("jefferson", "figueroa", "dela")
print(fullname2)

# Looping in functions
# While loops
while True:
    first_name = input("Enter your first name: ")
    if first_name == "quit":
        break

    last_name = input("Enter your last name: ")
    if last_name == "quit":
        break

    print(f"Hello, {full_name(first_name, last_name)}!")  # Calling the full_name function inside the print statement

# For loops (PASSING A LIST)
def greet_students(names):
    """Greet each student in the list."""
    for name in names:
        print(f"Hello, {name.title()}!")

students = ["alice", "bob", "charlie"]
greet_students(students)  # Passing the list of students to the function
students = ["jeff"] 
greet_students(students)  # Welcome, Jeff!
