# Assigning a variable(num1) to the prompt
num1  = int(input("Enter the number: "))

# Prints the first message if the remainder of dividing the number by 2 and 3 is 0
if num1%2 == 0 and num1%3 == 0:
    print("Number is divisible by 2 and 3 both")
# If it is not divisible by 2 and 3 then it prints the second message
else:
    print("Number is not divisible by both.")