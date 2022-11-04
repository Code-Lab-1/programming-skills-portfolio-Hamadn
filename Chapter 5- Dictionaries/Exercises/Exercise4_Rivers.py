rivers = {
    "Tana": "Kenya",
    "Bafing": "Mali",
    "Kura": "Georgia"
    }

for river, country in rivers.items():
    print("The " + river + " flows through " + country + ".")

print("\nThe following rivers are included in the dictionary:")
for river in rivers.keys():
    print(river)

print("\nThe following countries are included in the dictionary:")
for country in rivers.values():
    print(country)