name = input("What is your name?")
marks = float(input("Type your total marks:"))


if marks > 80 and marks <= 90 or marks > 90:
    print('''You have passed the subject,
             and you got an A+ grade''')
elif marks > 70 and marks <= 80:
    print('''You have passed the subject,
             and you got an A grade''')
elif marks > 60 and marks <= 70:
    print('''You have passed the subject,
             and you got an B grade''')
elif marks > 50 and marks <= 60:
    print('''You have passed the subject,
             and you got an C grade''')
elif marks >= 40 and marks <= 50:
    print('''You have passed the subject,
             and you got an A grade''')
else:
    print("You have failed the subject")