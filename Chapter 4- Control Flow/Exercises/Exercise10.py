# Assigning a variable(per) to the prompt
per = int(input("Enter marks: "))

# Prints first message if value of per is greater than 90
if per > 90:
    print("Grade is A")
# Prints second message if value of per is greater than 80 and less than is equal to 90
if per > 80 and per <= 90:
    print("Grade is B")
# Prints third message if the per value is greater than is equla to 60 and less than is equal to 80
if per >= 60 and per <= 80:
    print("Grade is C")
# Prints fourth message if the per value is less than 60
if per < 60:
    print("Grade is D") 
