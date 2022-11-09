# Making a deep copy on other collection types

import copy

# Deep Copy on a Set
people = {
    "Buffy",
    "Giles",
    "Blade"
}

slayers = people.copy()

slayers.discard("Blade")

slayers.remove("Giles")

print(slayers)

print(people)

# Make a Deep copy on a Dict

dict_eg = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

newDict = dict_eg.copy()

# Make a Deep copy on an Object

class Student(Object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age 


student = Student("William", 35)

newObj = copy.copy(student)
newDeepObj = copy.deepcopy(student)

print(newObj)
print(newDeepObj)

