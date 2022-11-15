# Importing date class from datetime module
from datetime import date

# Assigning a variable(date_1) to the class(date) with values
date_1 = date(2013, 7, 2)

# Assigning a variable(date_2) to the class(date) with values
date_2 = date(2022, 7, 11)

# Assigning a variable(dif) to the formula(calculates the difference between the dates)
dif = date_2 - date_1

# Printing the value of dif with the property of .days
# .days tells the difference between the dates in days
print(dif.days)