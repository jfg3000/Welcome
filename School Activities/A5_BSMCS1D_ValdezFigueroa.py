# Activity on Python Data Structures Lists, Tuples, Dictionaries and Sets
print()
# Question No. 1.)   
dog = {
    "name": "John Paul",
    "kind": "Bulldog", 
    "owner": "Jeff"
}
cat = {
    "name": "Cali",
    "kind": "Persian", 
    "owner": "Prince"
}
bird = {
    "name": "Jerry",
    "kind": "Parrot", 
    "owner": "Sir Arcel"
}

pets = [dog, cat, bird]

for pet in pets:
    print(f"The owner of the {pet['name']}, a {pet['kind']}, is {pet['owner']}.")


# Question No. 2.)
print()
favorite_places = {
    "Prince": ["Manila", "Baguio", "Boracay"],
    "jeff": ["Cebu", "Palawan", "Davao"],
    "marcuis": ["Baguio", "Tagaytay", "Manila"]
}

for person, places in favorite_places.items():
    print(person + "' favorite places are:")
    for place in places:
        print("-", place)


# Question No. 3.)  
print()
cities = {
    "Manila": {"country": "Philippines", 
               "population": 1902520, 
               "fact": "Manila is the capital of the Philippines"},
    "San Jose Del Monte": {"country": "Philippines", 
                "population": 685688, 
                "fact": "San Jose Del Monte is a city in the province of Bulacan"},
    "Quezon City": {"country": "Philippines", 
                    "population": 3000000, "fact": 
                    "Quezon City was founded by Manuel L. Quezon"}
} 
for city, facts in cities.items():
        print(f"{city} is a city in the {facts['country']} that has a population of {facts['population']}. \nFACT: {facts['fact']}." + "\n")

