##  Demonstration of encapsulation using protected and private designators

##  Assignment:

##  Class should make use of private attribute or function
##
##  Class should make use of a protected attribute or function
##
##  Create object that makes use of protected and private



# the class myPets has one protected attribute, "_petName" and
#   one private attribute, "__petAge"

#'''
class myPets:
    def __init__(self):
        self._petName = "Jinx"
        self.__petAge = 4

    def getPrivate(self):
        print(self.__petAge)

catVar = myPets()
print(catVar._petName)
catVar.getPrivate()
#'''

#The above code should print with no errors, for the following reasons:
#   _petName is protected, which will remain accessible without additional code
#   __petAge is private, but the method getPrivate() allows us to access it.
#   This is because the print() method takes place within the class.
#   Using the print() method outside of the class will not access any private attributes.
#   Without calling the getPrivate() method, we would not be able to directly
#       print __petAge to the console.


#For an example of the error message we would get if we tried to directly
#   access a private attribute, comment out all of the code above, and uncomment
#   all the code below. The value for _petName should print, but the value for
#   __petAge will not be accessible.

'''
class myPets:
    def __init__(self):
        self._petName = "Jinx"
        self.__petAge = 4

    def getPrivate(self):
        print(self.__petAge)

catVar = myPets()
print(catVar._petName)
print(catVar.__petAge)
'''

