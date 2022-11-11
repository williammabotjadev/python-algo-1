# An Implementation of an Animal Shelter based on a Queue 

class Node(object):
    def __init__(self, animalName=None, animalKind=None, pointer=None):
        self.animalName = animalName 
        self.animalKind = animalKind 
        self.pointer = pointer 
        self.timestamp = 0 
