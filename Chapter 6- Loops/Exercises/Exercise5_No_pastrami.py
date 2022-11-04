sandwich_orders = ['fries', 'chicken', "pastrami", 'falafel', 'roast beef', "pastrami", "grilled chicken", "pastrami"]
finished_sandwiches = []


while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
print("\n")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(current_sandwich + " sandwich coming up!")
    finished_sandwiches.append(current_sandwich)

print("\n")  
print("I'm sorry, we're out of pastrami.")
print("\n")
for x in finished_sandwiches:
    print("I made a " + x + " sandwich.")