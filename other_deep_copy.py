# Making a deep copy on other collection types

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
