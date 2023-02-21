## The parent class in this example is "animals."
## This class is initialized with def __init__ followed by its properties.
## A test method is also defined, which prints the values for these properties.

class animals:
    def __init__(self, mass, species, habitat):
        self.mass = mass
        self.species = species
        self.habitat = habitat
    def printDesc(self):
        print(self.mass, self.species, self.habitat)
        
## The animals object fido demonstrates the class's functionality
fido = animals("25 lbs", "Dog", "Back-yards")
fido.printDesc()

## Fish is the first child class. We define it in relation to animals.
## We define and initialize additional properties, color and waterType.
## We use super() to inherit the printDesc() method from the parent / superclass, animals
## There is no need to define mass, species, or habitat for fish, because these
##  definitions are inherited.
## A new method, fishDesc() is also included, which is unique to the fish class

class fish(animals):
    def __init__(self, mass, species, habitat, color, waterType):
        super().__init__(mass, species, habitat)
        self.color = color
        self.waterType = waterType

    def fishDesc(self):
        print(self.mass, self.species, self.habitat, self.color, self.waterType)


## We create a fish object to demonstrate inheritance of mass, species, and habitat,
##  inheritance of printDesc(), and functionality of fishDesc()
        
nemo = fish("2 oz.", "Clownfish", "Coral Reefs", "Orange", "Salt Water")
nemo.printDesc()
nemo.fishDesc()


## We repeat the process of creating a child class for the new birds class.
## Instead of color and waterType, birds uses wingspan and nestType.
## Note again that there is no need to re-define mass, species, or habitat.
## The class birds inherits the properties and methods of animals, similar to the child class fish.

class birds(animals):
    def __init__(self, mass, species, habitat, wingspan, nestType):
        super().__init__(mass, species, habitat)
        self.wingspan = wingspan
        self.nestType = nestType

    def birdDesc(self):
        print(self.mass, self.species, self.habitat, self.wingspan, self.nestType)

gull = birds("15 oz.", "Common Gull", "Coastal Wetlands", "125cm", "Ground Nests")
gull.printDesc()
gull.birdDesc()
