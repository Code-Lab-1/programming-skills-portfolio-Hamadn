# Assigning a value 0f 0 to a variable(tax)
tax = 0

# Assigning a variable(pr) to the prompt
pr = int(input("Enter the price of the bike: "))

# Executes the first condition if it the condition is fulfilled
if pr > 100000:
# Assigning the formula to calculate 15% of pr as tax to a variable(tax)
    tax = 15/100*pr
# Executes the second condition if the condition before it is not fulfilled
elif pr > 50000 and pr <= 100000:
# Assigning the formula to calculate 10% of the pr as tax to a variable(tax)
    tax = 10/100*pr
# Executes the last condition if all of the conditions before it are not fulfilled
else:
# Assigning the formula to calsulate 5% of the pr as tax to a variable(tax)
    tax = 5/100*pr
    
# Printing the result
print("Tax to be paid",tax)