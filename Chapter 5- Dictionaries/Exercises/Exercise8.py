# Creating a dictionary and assigning it a variable(test_dict)
test_dict = {
    "name": "Zoraiz",
    "age": 18,
    "salary": 6000,
    "city": "India"
}
# Printing the dictionary
print(test_dict)

# Changing the key named 'location' to 'city'
test_dict['location'] = test_dict.pop('city')
# Printing the dictionary after changing
print(test_dict)