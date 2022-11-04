toppings = "What topping would you like on your pizza?"
toppings += "\nEnter 'quit' when done: "

while True:
    topping = input(toppings)
    if topping != 'quit':
        print("  I will add " + topping + " to the pizza.")
    else:
        break