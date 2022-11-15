# Assigning a value to a variable(age)
age = 18

# Prints the first message if the condition is fulfilled
if age < 2:
    print("The person is a baby.")
# Prints the second message if the condition before it is not fulfilled
elif age >= 2 and age < 4:
    print("The person is a toddler.")
# Prints the third message if any of the conditions before it are not fulfilled
elif age >= 4 and age < 13:
    print("The person is a kid.")
# Prints the fourth message if any of the conditions before it are not fulfilled
elif age >= 13 and age < 20:
    print("The person is a teenager.")
# Prints the fifth message if any of the conditions before it are not fulfilled
elif age >= 20 and age < 65:
    print("The person is an adult.")
# Prints the last message if any of the conditions before it are not fulfilled
else:
    print("The person is an elder.")