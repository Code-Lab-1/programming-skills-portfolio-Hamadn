# Assigning a variable(a) to an integer
a = 0
# Assigning a variable(n) to the prompt
n = int(input("Enter number "))
# Loop for values in the given range
for x in range(1, n + 1, 1):
# Change the a value to a + x
    a += x
# Print new line
print("\n")
# Print the string and the value of a
print("Sum is: ", a)