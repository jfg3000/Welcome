#ahaaah




""""
2.  
    The song “99 Bottles of Beer” starts with this verse:
    99 bottles of beer on the wall,
    99 bottles of beer.
    Take one down, pass it around,
    98 bottles of beer on the wall.
    Then the second verse is the same, except that it starts with 98 bottles and ends with 97. The song continues, for a very long time, until there are 0 bottles of beer. Write a function called bottle_verse that takes a number as a parameter and displays the verse that starts with the given number of bottles.
""" 

def bottle_verse(number):
    for number in range(number, 0, -1):                 # Starting point= number, Ending point= 0, Decrement=-1
        print(f"{number} bottles of beer on the wall,\n"
            f"{number} bottles of beer.\n"
            "Take one down, pass it around,\n"
            f"{number - 1} bottles of beer on the wall.\n")
bottle_verse(99)

def message(n):
        for n in range(0, n, 1):
            print(f"i ate {n} times.")
message(26)