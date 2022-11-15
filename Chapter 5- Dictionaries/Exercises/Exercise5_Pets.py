# Creating an empty list and assigning it a variable(pets)
pets = []

# Creating and redeclaring the same variable with a different dictionary each
animal = {
    "Animal": "cat",
    "Name": "Jack",
    "Owner": "Sara",
    "Weight": 10,
    "Eats": "chicken",
}
# Adding the dictionary to the list
pets.append(animal)

animal = {
    'Animal': 'lion',
    'Name': 'Rocky',
    'Owner': 'Clare',
    'Weight': 150,
    'Eats': 'meat',
}
# Adding the dictionary to the list
pets.append(animal)

animal = {
    'Animal': 'parrot',
    'Name': 'Bruno',
    'Owner': 'Lisa',
    'Weight': 1,
    'Eats': 'seeds',
}
# Adding the dictionary to the list
pets.append(animal)

# Loop for every item in the list
for animal in pets:
# Print a statement in this format using concatenation
    print("What I know about " + animal["Name"] + ":")
# Loop for all the key:value pairs in the dictionaries
    for key, value in animal.items():
# Print the key and the value in this format
        print(f"\t{key}: {value}")