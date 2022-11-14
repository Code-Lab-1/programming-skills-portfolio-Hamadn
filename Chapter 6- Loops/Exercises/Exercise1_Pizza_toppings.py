# Assigning a variable(toppings) to the string
toppings = "What topping would you like on your pizza?"
# Changing the value of th variable(toppings) to toppings + "Enter 'quit' when done: "
toppings += "\nEnter 'quit' when done: "

# Loop to check the input of user
while True:
# Assigning a variable(topping) to the prompt
    topping = input(toppings)
# Checking if the user input is not quit
    if topping != 'quit':
# Print this statement(made using cocatenation of string and variable)
        print("  I will add " + topping + " to the pizza.")
# If the user input is 'quit' then break the loop
    else:
        break