# Creating a function called max with three arguments
def max(a, b, c):
# Prints the first message if a is greater than b and a is greater than c
    if a > b and a > c:
        print(f"{a} is maximum among all")
# Prints the second message if the condition before it is not fulfilled
    elif b > a and b > c:
        print(f"{b} is maximum among all")
# Prints the last message if all of the conditions before it are not fulfilled
    else:
        print(f"{c} is maximum among all")
# Calling out the function with arguments
max(57,67,10)