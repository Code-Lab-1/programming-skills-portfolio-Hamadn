# Importing date class from datetime module
from datetime import date

# Assigning a variable(f_date) to the class(date) with values
f_date = date(2013, 7, 2)

# Assigning a variable(l_date) to the class(date) with values
l_date = date(2022, 7, 11)

# Assigning a variable(dif) to the formula(calculates the difference between the dates)
dif = l_date - f_date

# Printing the value of dif with the property of .days
# .days tells the difference between the dates in days
print(dif.days)