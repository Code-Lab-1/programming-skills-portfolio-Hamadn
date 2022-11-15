def table():
    num = int(input("Type any number: "))
    for x in range(1,11):
        tab = num*x
        print(num, "x", x, "=", tab)
table()