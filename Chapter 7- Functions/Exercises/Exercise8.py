#Creating a funtion called add with one argument(num)
def add(num):
    if num:
# Return this result
        return num + add(num - 1)
# If the value for num is 0, then return 0
    else:
        return 0
# Assigning a variable(prod) to the function with the argument for num as 10
prod = add(10)

# Printing the result
print(prod)