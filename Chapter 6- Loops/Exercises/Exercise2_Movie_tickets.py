# Assigning a variable(age) to a string
age = "What is your age?"
# Changing the value of age to age + "\nEnter 'quit' when done. "
age += "\nEnter 'quit' when done. "

# Loop to check the input of user
while True:
# Assigning a variable(a) to the prompt
    a = input(age)
# Checking if the input of the user is not 'quit'
    if a == 'quit':
# If it is 'quit' then break the loop
        break
# Redeclaring the variable(a) and assigning it the int format of input
    a = int(a)
# Checking if the user input is less than 3
    if a < 3:
# If less than 3 then print this statement
        print("  Your ticket is free.")
# Checking if the user input is less than 13(the first condition is not fulfilled)
    elif a < 13:
# If less than 13 then print this statement
        print("  Your ticket is $10.")
# If none of the condition before is fulfilled then print this statement
    else:
        print("  Your ticket is $15.")