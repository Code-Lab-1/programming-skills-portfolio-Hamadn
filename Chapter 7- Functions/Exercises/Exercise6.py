# Creating a function called calculate
# This function adds and subtracts the values of a and b
# Then returns the value of both variables
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
# Assigning the calling out of the function with the arguments to a variable(res)
res = calculate(40, 10)

# Printing the value of the variable(res)
print(res)