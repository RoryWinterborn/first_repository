""" 
Question 1
Create a function that will calculate the sum of two numbers
"""

def sum_two_nos(a,b):
    '''Returns the sum of two arguments.'''

    return a+b


"""
Question 2
Write a function that performs multiplication of two arguments. By default
the function should multiply the fist argument by 2.
"""

def multiply(a,b=2):
    '''The is function returns the product of two arguments. If only one 
    argumentis is given it will be multiplied by two.''' 

    return a*b


"""
Question 3
Write a function to calculate a to the power of b. If b is not given its 
default value should be 2.
"""

def power(a,b=2):
    '''This function can take up to two arguments. If two arguments are 
    provided the first argument will be raised to the power of the second
    argument. If only one argment is provided it will be raised to the 
    power of two.'''

    return a**b


"""
Question 4
Create a new file called capitals.txt; On a single line store the names of
the following five capital cities: London, Paris, Madrid, Lisbon, Rome.
"""
capital_cities = ["London", "Paris", "Madrid", "Lisbon", "Rome"]

with open("capitals.txt", 'w') as file:
    for item in capital_cities:
        file.write(item)
        if capital_cities.index(item) < len(capital_cities) - 1:
            file.write(", ")


"""
Question 5
Write code that requests the user to input another capital city; Add this 
to the list of cities in capitals.txt and print the file to the screen.
"""

new_capital = input("Please input a capital city:\n>>>")

with open("capitals.txt", "a") as file:
    file.write(", " + new_capital)
    
with open("capitals.txt", "r") as file:
    contents = file.read()
    
print(contents)

"""
Question 6
Write a finction that wiull copy the contents of one file into another file
"""

def copy_file(in_file,out_file):
    '''This function takes two arguments; an input file and an output file
    and copies the contents of the input file into the output file'''

    with open(in_file, "r") as old_file:
        with open(out_file, "w") as new_file:
            new_file.write(old_file.read())


