# Assigning a variable(values) to the prompt
values = input("Input some comma seprated numbers : ")

# Assigning a variable(l) to the split property and spliting them with commas
l = values.split(",")

# Assigning a variable(t) to changing the format of list to tuple
t = tuple(l)

# Printing the list and tuple with items seperated by commas
print('List : ',l)
print('Tuple : ',t)