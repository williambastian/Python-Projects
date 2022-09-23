#This script is meant to illustrate polymorphism in the heroDesc() function, which is implemented differently in the two child classes



# Parent class, from which child classes will inherit properties and values unless overwritten

class superHeroes:
    name = "Superman"
    classification = "superhuman"
    powers = "super-strength, super-speed, invulnerability, \nflight, heat-vision, x-ray vision, super-enhanced-senses\n"
    origin = "Kryptonian"
    publisher = "DC Comics"

    def heroDesc(self):
        print("Name: {}\nClassification: {}\nAbilities: {}\nOrigin: {}\nPublisher: {}\n".format(self.name, self.classification, self.powers, self.origin, self.publisher))
        
# Child class, which inherits value of the publisher property and the value of the classification property.
# The patron and weapon properties are unique to this class.
# The heroDesc() method uses both inherited and unique property values within this class. 
class Amazons(superHeroes):
    name = "Wonder Woman"
    powers = "Amazonian strength, speed, endurance, and durability"
    origin = "Warrior Princess of Themiscyra"
    patron = "Athena"
    weapon = "golden lasso of truth"

    def heroDesc(self):
        print("The {} Amazon {}, scion of {}, wields a mighty {}. \nShe possesses {}.\nPublisher: {}\n".format(self.classification, self.name, self.patron, self.weapon, self.powers, self.publisher))

# This child class inherits the value of the classification property, overwrites the values for other properties shared with superHeroes(),
#   and has unique properties team and negatives.
# The heroDesc() method uses both inherited and unique property values, similar to the Amazons() class.
class Mutants(superHeroes):
    name = "Cyclops"
    powers = "the ability to shoot force beams from his eyes"
    team = "The X-Men"
    negatives = "an inability to stop these beams without special eye equipment"
    origin = "Mutant"
    publisher = "Marvel Comics"

    def heroDesc(self):
        print("The {} mutant {} is a member of {}. \nHis mutation gives him {}, \nbut also {}. \nPublisher: {}".format(self.classification, self.name, self.team, self.powers, self.negatives, self.publisher))
 



if __name__ == "__main__":
    #instances of each class are created here
    #invoking heroDesc() gives a different result each time, due to the polymorphism of the function
    superMan = superHeroes()
    superMan.heroDesc()
    wonderWoman = Amazons()
    wonderWoman.heroDesc()
    cyclops = Mutants()
    cyclops.heroDesc()
    
