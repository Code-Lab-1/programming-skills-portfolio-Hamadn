# Creating a dictionary and assigning it a variable(glossary)
glossary = {
    "String": "A series of characters.",
    "Variable": "A variable is a location that stores temporary data within a program which can be modified, store and display whenever need.",
    "Boolean": "A Boolean expression or Boolean logic is an expression used for creating statements that are either TRUE or FALSE.",
    "List": "Lists are used to store multiple items in a single variable.",
    "Dictionary": "Dictionaries are used to store data values in key:value pairs."
    }


# Declaring the same variable and changing its value for every key:value pair in the dictionary
# Printing the key and value using concatenation between key,value and string
word = "String"
print(word + " : " + glossary[word] + "\n")

word = "Variable"
print(word + " : " + glossary[word] + "\n")

word = "Boolean"
print(word + " : " + glossary[word] + "\n")

word = "List"
print(word + " : " + glossary[word] + "\n")

word = "Dictionary"
print(word + " : " + glossary[word] + "\n")
