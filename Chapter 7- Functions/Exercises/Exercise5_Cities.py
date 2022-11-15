# Creating a function called describe_city with two arguments
# First argument is 'city' and second argument is 'country with its default value set to 'France'
def describe_city(city, country='France'):
# Printing a statement using concatenation of variable and string
    print(city + " is in " + country + ".")
# Calling out the function with the value for country changed to 'Paris'
describe_city('Paris')
# Calling out the function with the values changed for both arguments
# For city it changed to 'Sindh' and country changed to 'Pakistan'
describe_city('Sindh', 'Pakistan')
# Calling out the function with the value for city changed to 'Lyon'
describe_city('Lyon')