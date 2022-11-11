# An Implementation of an Animal Shelter based on a Queue 

class Node(object):
    def __init__(self, animalName=None, animalKind=None, pointer=None):
        self.animalName = animalName 
        self.animalKind = animalKind 
        self.pointer = pointer 
        self.timestamp = 0 

class AnimalShelter(object):
    def __init__(self):
        self.headCat = None 
        self.headDog = None 
        self.tailCat = None 
        self.tailDog = None 
        self.animalNumber = 0 

    def enqueue(self, animalName, animalKind):
        self.animalNumber += 1 
        newAnimal = Node(animalName, animalKind)

        if animalKind.casefold() == "Cat".casefold():
            if not self.headCat:
                self.headCat = newAnimal 
            if self.tailCat:
                self.tailCat.pointer = newAnimal 
            self.tailCat = newAnimal 

        if animalKind.casefold() == "Dog".casefold():
            if not self.headDog:
                self.headDog = newAnimal
            if self.tailDog:
                self.tailDog.pointer = newAnimal
            self.tailDog = newAnimal
    
        