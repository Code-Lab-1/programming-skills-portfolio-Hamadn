age = "What is your age?"
age += "\nEnter 'quit' when done. "

while True:
    a = input(age)
    if a == 'quit':
        break
    a = int(a)

    if a < 3:
        print("  Your ticket is free.")
    elif a < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")