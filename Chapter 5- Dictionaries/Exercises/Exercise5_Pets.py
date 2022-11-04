pets = []

animal = {
    "Animal": "cat",
    "Name": "Jack",
    "Owner": "Sara",
    "Weight": 10,
    "Eats": "chicken",
}
pets.append(animal)

animal = {
    'Animal': 'lion',
    'Name': 'Rocky',
    'Owner': 'Clare',
    'Weight': 150,
    'Eats': 'meat',
}
pets.append(animal)

animal = {
    'Animal': 'parrot',
    'Name': 'Bruno',
    'Owner': 'Lisa',
    'Weight': 1,
    'Eats': 'seeds',
}
pets.append(animal)

for animal in pets:
    print("What I know about " + animal["Name"] + ":")
    for key, value in animal.items():
        print(f"\t{key}: {value}")