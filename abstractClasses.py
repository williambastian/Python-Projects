# importing ABC will allow us to create custom abstract classes and methods
# abstraction helps prevent messy, inefficient code


from abc import ABC, abstractmethod

# myTasks will be the abstract class, with taskDetails() as the abstract method
# printEncouragement() is a conventional method, which can coexist with abstract methods in an abstract class

class myTasks(ABC):
    @abstractmethod
    def taskDetails(self, name, priorityLevel, daysTilDue): #these parameters will be strictly required each subclass of myTasks
        pass #no implementation is specified for taskDetails() in the abstract class
    def printEncouragement(self):
        print("Making a list is the first step to success!")

# the myChores class defines the implementation of taskDetails()
class myChores(myTasks):
    def taskDetails(self, name, priorityLevel, daysTilDue, assignedTo): #while the parent parameters are required, we can also add unique parameters in subclasses
        print("{} Priority: {} will complete the {} task in {} days.".format(priorityLevel, assignedTo, name, daysTilDue))
    def choreMessage(self): # choreMessage() is a method unique to the myChores class
        print("Chores aren't fun, but they keep life organized!")

#taskDetails() can be defined differently for each subclass of myTasks, as long as it maintains the parent parameters
class myStudies(myTasks):
    def taskDetails(self, name, priorityLevel, daysTilDue, courseName):
        print("{} Priority: I will complete the {} in {} days for my {} course.".format(priorityLevel, name, daysTilDue, courseName))
    def studyMessage(self):
        print("Education is a lifelong pursuit!")


takeTrash = myChores() #we instantiate takeTrash as an object of the myChores subclass
takeTrash.taskDetails("(taking the trash out)","Medium",3,"William") #calling taskDetails with values for each parameter, specifically the parameters specified in the subclass definition
takeTrash.choreMessage() #takeTrash can also call its own methods
takeTrash.printEncouragement() #takeTrash can also call conventional, non-abstracted methods inherited from myTasks
    
