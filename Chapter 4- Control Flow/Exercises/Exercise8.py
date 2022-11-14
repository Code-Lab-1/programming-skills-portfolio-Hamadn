# Assinging a variable(year) to the prompt(integer only)
year = int(input("Enter the year: "))
# Check if the value of year is divisible by 100 and 400 or 4
if year%100 == 0:
    if year%400 == 0:
        print("Entered year is leap year.")
    else:
        print("Entered year is not a leap year.")
else:
    if year%4 == 0:
        print("Entered year is leap year.")
    else:
        print("Entered year is not a leap year.")

    