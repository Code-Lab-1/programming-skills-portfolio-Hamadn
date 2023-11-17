# Creating dictionaries inside a dictionary and assigning it a variable(dict1)
dict1 = {
    'stu1': {'name': 'Hamad', 'subject': 'Ict'},
    'stu2': {'name': 'Raheem', 'subject': 'Maths'},
    'stu3': {'name': 'Zoraiz', 'subject': 'Physics'}
}
# Changing the value for the key(subject) in the value of the key(stu3) to 'English
dict1['stu3']['subject'] = 'English'
# Printing the dictionary after changing
print(dict1)