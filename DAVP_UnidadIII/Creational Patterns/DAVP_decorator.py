"""Daniela Alejandra Vargas Palomino"""
"""GITI9072-e"""
"""Example Creational Patterns"""

from functools import wraps

def make_blink(function):
    """Defines the decorator"""

    #This make the decorator transparent in term of its name and docstring
    @wraps(function)

    #Define the inner function
    def decorator():
        #Grab the return value of the function being decorated
        ret = function()

        #Add new functionality to the fuction being decorated
        return "<blink>" + ret + "</blink>"

    return decorator

#Apply the decorator here!
@make_blink
def hello_world():
    """Original function!"""

    return "Hello,World"

#Check the result of decorating
print(hello_world())
#Check if the function  name is  still the same name of the function being decorated
print(hello_world.__name__)
#check if the docstring is still the same as that of the function being decorated
print(hello_world.__doc_)