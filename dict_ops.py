# Basic Dictionary Operations

woody = {}
woody['name'] = "Woody Allen"
woody['job'] = "Director"

print(woody)

litchfield = dict({
    "name": "Piper",
    "age": 29,
    "hobby": "Being Awesome"
})

print(litchfield)

litchfield = dict(
    name="Gaia",
    age=23,
    hobby="Drawing"
)

print(litchfield)

litchfield = dict([
    ("Name", "Red"),
    ("Age", 54),
    ("Hobbies", "Cooking")
])