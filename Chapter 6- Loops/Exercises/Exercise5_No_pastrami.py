# Assigning the variable(sandwich_orders) to a list
sandwich_orders = ['fries', 'chicken', "pastrami", 'falafel', 'roast beef', "pastrami", "grilled chicken", "pastrami"]
# Assigning the variable(finished_sandwiches) to an empty list
finished_sandwiches = []

# Loop to check until the word'pastrami' is in the list(sandwich_orders)
while 'pastrami' in sandwich_orders:
# Remove the word pastrami
    sandwich_orders.remove('pastrami')
# Print a new line
print("\n")

# Loop for the list
while sandwich_orders:
# Moving the values of sandwich_orders to current_sandwich by using .pop
    current_sandwich = sandwich_orders.pop()
# Printing the statement using concatenation of variable and string
    print(current_sandwich + " sandwich coming up!")
# Append the values of finished_sandwiches to current_sandwiches
    finished_sandwiches.append(current_sandwich)

# Print new line
print("\n")  
# Print the string
print("I'm sorry, we're out of pastrami.")
# Print new line
print("\n")

# Loop for every item in the list(finished_sandwiches)
for x in finished_sandwiches:
# Print this statement using cancatenation of string and variable
    print("I made a " + x + " sandwich.")