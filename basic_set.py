# Basic Set operations

people = { "Buffy", "Angel", "Giles" }

print(people.add("Willow"))

more_people = { "Xander", "Willow", "Giles"}

vampires = {"Drusilia", "Angel", "Spike"}

print(people.intersection(more_people))

print(people.union(more_people))

print(people.difference(vampires))

print(people)

people.clear()

print(people)