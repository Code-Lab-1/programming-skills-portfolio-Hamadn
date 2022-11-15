# Creating a dictionary and assigning it a variable(rivers)
rivers = {
    "Tana": "Kenya",
    "Bafing": "Mali",
    "Kura": "Georgia"
    }

# Loop for every key:value pair in the dictionary
for river, country in rivers.items():
# Print a statement using concatenation and in this format
    print("The " + river + " flows through " + country + ".")

# Printing a string
print("\nThe following rivers are included in the dictionary:")
# Loop for all the keys in the dictionary
for river in rivers.keys():
# Print the keys
    print(river)
# Print a string
print("\nThe following countries are included in the dictionary:")
# Loop for all the values in the dictionary
for country in rivers.values():
# Print the values
    print(country)