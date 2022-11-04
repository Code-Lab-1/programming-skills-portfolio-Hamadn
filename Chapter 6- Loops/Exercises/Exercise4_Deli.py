sandwich_orders = ['fries', 'chicken', 'falafel', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(current_sandwich + " sandwich coming up!")
    finished_sandwiches.append(current_sandwich)

print("\n")
for x in finished_sandwiches:
    print("I made a " + x + " sandwich.")