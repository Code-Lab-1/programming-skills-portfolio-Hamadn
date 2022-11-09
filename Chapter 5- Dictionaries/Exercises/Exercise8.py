test_dict = {
    "name": "Zoraiz",
    "age": 18,
    "salary": 6000,
    "city": "India"
}
print(test_dict)

test_dict['location'] = test_dict.pop('city')
print(test_dict)