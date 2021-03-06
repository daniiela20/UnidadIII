"""Daniela Alejandra Vargas Palomino"""
"""GITI9072-e"""
"""Example Creational Patterns"""

class Korean:
    """Korean speaker"""
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"

class British:
    """English speaker"""
    def __init__(self):
        self.name = "British"

    #Note the defferent method name here!
    def speak_english(self):
        return "Helllo!"

class Adapter:
    """This changes the generic method name to individualsed method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object

        #Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
        #For example, speak() will be translated to speack_korean()if the mapping say so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of attributes!"""
        return getattr(self._object, attr)

#List to store speaker objects
object = []

#Create a Korean object
korean = Korean()

#create a British object
british = British()

#Append the objects to the objects list
object.append(Adapter(korean, speak=korean.speak_korean))
object.append(Adapter(british, speak=british.speak_english))

for obj in object:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
