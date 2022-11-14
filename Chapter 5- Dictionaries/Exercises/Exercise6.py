# Creating dictionaries inside a dictionary and assigning it a variable(Dict)
Dict = {
    "class": {
        "student": {
            "name": "Hamad",
            "marks": {
                "ICT": 70,
                "Maths": 80
            }
        }
    }
}

# Printing the value for the key maths inside the dictionaries
print(Dict['class']['student']['marks']['Maths'])