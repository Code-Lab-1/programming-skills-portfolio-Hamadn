# Creating a dictionary and assigning it a variable(glossary)
glossary = {
    "String": "A series of characters.",
    "Variable": "A variable is a location that stores temporary data within a program which can be modified, store and display whenever need.",
    "Boolean": "A Boolean expression or Boolean logic is an expression used for creating statements that are either TRUE or FALSE.",
    "List": "Lists are used to store multiple items in a single variable.",
    "Dictionary": "Dictionaries are used to store data values in key:value pairs.",
    "Iterable": "Any object that can return its members one at a time is an iterable. Examples include lists, strings, tuples, dicts, and file objects.",
    "Break": "Used to exit a python for loop or a while loop.",
    "Function": "A parameterized sequence of statements.",
    "Slice": "Sub parts of sequences.",
    "Module": "The basic unit of code reusability in Python. A block of code imported by some other code."
    }

# Loop for key:value pair in items in the dictionary
for var, meaning in glossary.items():
# For every key:value pair print it in this format
    print(var + " : " + meaning + "\n")