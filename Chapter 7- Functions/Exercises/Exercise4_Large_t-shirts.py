# Creating a function called make_shirt with default arguments
# For size it is 'large' and for message it is 'I love Python
def make_shirt(size='large', message='"I love Python!"'):
# Printing a statement using concatenation of variable and string
    print("\nI'm making a " + size + " " + "t-shirt.")
    print("It says, " + message)
# Calling out the function as it is
make_shirt()
# Calling out the function and changing the default value of size to 'medium'
make_shirt(size='medium')
# Calling out the function and changing the default values
# From 'large' to 'small' and from 'I love Python' to 'Keep calm and program' 
make_shirt(size='small', message='"Keep calm and program."')