# Try; Moving Car
import time 

# Stations or toll gate entry/exit points:
toll_data = {
    "Mindanao Avenue": 85.00,
    "Valenzuela": 85.00,
    "Meycauayan": 85.00,
    "Marilao": 85.00,
    "Bocaue": 105.00,
    "Balagtas": 136.00,
    "Tabang": 157.00,
    "Pulilan": 202.00,
    "San Simon": 266.00,
    "Clark North": 467.00,
    "Tarlac": 670.00,
}
# MAIN MENU CHOICES
Overview = ("\nThis code was made for the fulfillment of the FINAL COURSE OUTPUT of the course MCS 102a\n"
    "\tMade by:\n"
    "Anonuevo, Leila Czamyr\n"
    "De Jesus, Junnel Apolo\n"
    "Figueroa, Jefferson\n"
    "Paloma, Cali\n"
    "Robles, Kimberly\n")


# MAIN MENU
MainMenu = ("\n===============================================================\n" 
        "\tGROUP 6 COMPUTER PROGRAMMING FINAL COURSE OUTPUT\n"
        "\t\t    TOLL GATE/RFID SYSTEM\n" 
    "===============================================================")
print(MainMenu)
Choices = ("MENU:"
           "\n1. Members"
           "\n2. Main Program"
           "\n===============================================================")
print(Choices)

def MainMenuGoBack():
    while True:
        answer = input("Type 1 to go back to the main menu!: ").strip()
        if answer == "1":
            print(MainMenu)
            print(Choices)
            break
        else:
            print("Invalid Answer!")


while True:
    choice = input("Choose an option from the numbers 1-2: ").strip()
     
    if choice == "1":
        print(Overview)
        MainMenuGoBack()
    elif choice == "2":
        menu1 = True
        menu2 = True
        break
    else:
        print("Invalid Answer!")


# Menu
if menu1 is True:
    print()
    print("PS. for the purpose of the project, we'll assume that the fees will be manually inputed instead of being automatic.")
    print("===============================================================\n" 
        "\t\t    TOLL GATE/RFID SYSTEM\n" 
    "===============================================================")
    
while menu2 is True:
    Choice2 = input("Type '1' to get the car moving or '0' to exit: ").strip()
    if Choice2 == '1':
        menu1 = False
        menu2 = False
        carmoving = True
        break
    elif Choice2 == '2':
        menu1 = False
        menu2 = False
        carmoving = False
        print("Exiting the program...")
    else:
        print("Invalid Input, try again!")


# Simulation
Road = "_______|_______________|_______"  
length = len(Road) 
counter = 0

while carmoving is True:
    for j in range(0, length):
        print("\r" + Road[0:j] + "🚘" + Road[j+1:], end="")  
        time.sleep(0.5)
        counter += 1
        if counter == 7:                     # == 7 kasi yung index ng toll gate ay 8 so magiistop yung kotse sa 7 which is before the gate.     
            carmoving = False
            CarDiagram = True
            print()
            break

# "\r" means carriage return, nanjan yan para maibalik yung parang line of code sa starting position so that it runs in a straight line parang ganon pre
# Road[0:j] = everything na nasa kaliwa nung kotse, or yung character, starts at 0, ends at j, which is len(Road), 
# "🚘" = char that moves
# Road[j+1:] = lahat ng nasa right ng kotse, j+1 kasi as j is at 0, j+1 = 1, hanggang may magstop na block of code sakanya.
# end="" = para hindi maging infinite yung pag travel ng kotse or kung wala to, magiging infinite loop
# counter = nagsisilbing parang stopping parameter ng kotse, nakabase sa index ng string, so as the car moves or j+1, the counter +=1 until a certain condition is met.

if CarDiagram is True:
    print("\n===========================================")
    print("\nCar has reached the toll gate!")
    print("""   
    [O]    <-- Red Light

    | |             
 ---+ +--- [TOLL]  
    | |           
  [ 🚗 ]""")

    print("\n===========================================\n")

# Entry point (BALINTAWAK ONLY)
print("PS. The only entry point is Balintawak to ensure better accuracy of the rate of the toll fees.")
print("Your entry point is: Balintawak")
while True:
    choice3 = input("Continue? Y/N: ").upper()
    if choice3 == "Y":
        break
    elif choice3 == "N":
        print("bawal")
        break
    else:
        print("Invalid input! Choose from the choices above.")

print("\n===========================================")
print("\nThank you!")
print("""   
    [O]    <-- Green Light
  [ 🚗 ]
    | |             
 ---+ +--- [TOLL]  
    | |           
            """)

print("\n===========================================\n")

# Car move
Road = "_______|_______________|_______"  
length = len(Road)
counter = 9
carmoving2 = True
while carmoving2:
    for j in range(8, length):
        print("\r" + Road[0:j] + "🚘" + Road[j+1:], end="")
        time.sleep(0.5)
        counter += 1
        if counter == 24:
            carmoving2 = False
            print()
            break

if CarDiagram is True:
    print("\n===========================================")
    print("\nCar has reached the toll gate!")
    print("""   
    [O]    <-- Red Light

    | |             
 ---+ +--- [TOLL]  
    | |           
  [ 🚗 ]""")

    print("\n===========================================\n")

tollgatechoices2 = ("\nChoices of Exit:\n"
    "    Mindanao Avenue, Valenzuela, Meycauayan, Marilao\n"
    "    Bocaue, Balagtas, Tabang, Pulilan,\n"
    "    San Simon, Clark North, Tarlac\n")
print(tollgatechoices2)

#Exit point 
exitpoint = True
vehicleclass = True
while exitpoint:
    exit = input("Where is your Exit point?: ").title()
    if exit in toll_data:
        print("Your Exit point is: " + exit)  
        exitpoint = False
        print()
    else:
        print("Invalid input! Choose from the choices above.")

print("\n==============================================================================================================================\n"
                                              "\t\t\t\t\tVEHICLE CLASS MENU\n" 
              "Vehicle Class 1: (Cars, Jeepneys, Pick-ups, Taxis, Vans, and vehicles with 2-axles and 7 ft. height)"
              "\nVehicle Class 2: (Buses, Trucks with 2-axles and 7 ft. above height, and light vehicles with more than 2-axles and 7 ft. height)"
              "\nVehicle Class 3: (Trucks with 3 or more axles and 7 ft. above height)"
              "\nFYI: 2-axles = 4 wheels, 3-axles = 6 wheels.\n"
        "\n==============================================================================================================================\n")

while vehicleclass:
    vehicle = input("What is your vehicle class?(1, 2, 3): ")
    if vehicle == "1":
        print("Your vehicle class is: " + vehicle)
        vehicle_class = 1
        break   
    elif vehicle == "2":
        print("Your vehicle class is: " + vehicle)
        vehicle_class = 2.5
        break
    elif vehicle == "3":
        print("Your vehicle class is: " + vehicle)
        vehicle_class = 3
        break
    else: 
        print("Invalid Input!") 

toll_fee = toll_data[exit]*vehicle_class
print(f"Your fee is: {round(toll_fee)}")

# Car move
print("\n===========================================")
print("\nThank you!")
print("""   
    [O]    <-- Green Light
  [ 🚗 ]
    | |             
 ---+ +--- [TOLL]  
    | |           
            """)

print("\n===========================================\n")

Road = "_______|_______________|_______"  


length = len(Road)
counter = 25
carmoving2 = True
while carmoving2:
    for j in range(25, length):
        print("\r" + Road[0:j] + "🚘" + Road[j+1:], end="")
        time.sleep(0.5)
        counter += 1
        if counter == 31:
            carmoving2 = False
            break

print("\nThank you for using the system!")

# BROKEN LOOP, DI KO ALAM KUNG PAANO ILOOP ULIT SA START AWIT
"""ending = True
while ending:
    end = input("\nThank you for using the system!, Wanna use it Again? (Y/N): ").upper()
    if end == "Y":
        print(MainMenu)
        print(Choices)
        ending = False
        break
    if end == "N":
        print("Exiting the program...")
        break
    else:
        print("Invalid Input! Please only type the letters Y or N.")"""
