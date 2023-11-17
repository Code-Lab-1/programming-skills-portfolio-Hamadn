# Assigning a variavle(string) to the prompt
string = str(input("Enter the string you want to sort: "))

# Assigning a variable(sort) to the property(.join) and function(sorted)
# This sorts the string and joins '' which is nothing, between every character
sort = ''.join(sorted(string))

# Printing value of variable(sort)
print(sort)