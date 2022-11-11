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
    
    def dequeue_dog(self):
        if self.headDog:
            newAnimal = self.headDog 
            self.headDog = self.headDog.pointer 
            return (newAnimal.animalName)
        else:
            print("No Dogs in this Shelter")

    def dequeue_cat(self):
        if self.headCat:
            newAnimal = self.headCat
            self.headCat = self.headCat.pointer 
            return (newAnimal.animalName)
        else:
            print("No Cats in this Shelter")

    def dequeue_any(self):
        if self.headCat and not self.headDog:
            self.dequeue_cat()
        elif self.headDog and not self.headCat:
            self.dequeue_dog()
        elif self.headCat and self.headDog:
            if self.headDog.timestamp < self.headCat.timestamp:
                self.dequeue_dog()
            else:
                self.dequeue_cat()
        else:
            print("No Animals in this Shelter")