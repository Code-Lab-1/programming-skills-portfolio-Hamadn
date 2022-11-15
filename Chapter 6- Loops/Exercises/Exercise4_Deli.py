# Assigning a variable(sandwich_orders) to a list
sandwich_orders = ['fries', 'chicken', 'falafel', 'roast beef']
# Creating an empty list
finished_sandwiches = []

# Loop for the list
while sandwich_orders:
# Moving the sandwich_orders to current_sandwich by using .pop
    current_sandwich = sandwich_orders.pop()
# Printing the statement using concatenation of variable and string
    print(current_sandwich + " sandwich coming up!")
# Append the values of finished_sandwiches to the values in current_sandwiches
    finished_sandwiches.append(current_sandwich)
# Print a new line
print("\n")

# Loop for every item in list(finished_sandwiches)
for x in finished_sandwiches:
# Printing the statement using concatenation between variable and string
    print("I made a " + x + " sandwich.")