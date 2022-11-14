# Assigning the value of 6 to a variable(price)
price = 6

# Assigning the value of 50 to a variable(money)
money = 50

# Assigning the formula of how many usb can she get with the money to a variable(amount)
amount = money//price

# Assigning the formula of how much money would she be left with to a variable(money_left)
money_left = money%price

# Printing the statement using concatenation of variable and string
# And changing the int values to string
print("She can buy" + " " + str(amount) + " " + "usb sticks.")
print("She would have" + " " + str(money_left) + " " + "pounds left.")