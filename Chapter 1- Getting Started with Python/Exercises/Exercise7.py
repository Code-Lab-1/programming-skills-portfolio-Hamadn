# Assigning a variable(name) to the prompt
name = input("What is your name: ")

# Assigning a variable(age) to the prompt(accept only integers)
age = int(input("How old are you: "))

# Assigning a variable(current_year) to the prompt(accept only integers)
current_year = int(input("What is the current year: "))

# Assigning a variable(year) to the formula
year = current_year - age + 100

# Assigning a variable(yr) to the concatenatinon of the string and variable
yr = name + ", you will be 100 years old in the year " + str(year)

# Printing the string and concatenation of string and variable
print(yr)