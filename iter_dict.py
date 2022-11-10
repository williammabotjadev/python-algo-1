# Iterating over a Dictionary

foods = {
    "Yoghurt": 23,
    "Banana": 87,
    "Apple": 22,
    "Juice": 40,
    "Bread": 82
}

for i in sorted(foods.keys()):
    print(f"Key: {i}, Value: {foods[i]}")

for j in sorted(foods.items()):
    print(j)

# Using Generators to sort a Dictionary

def gen_dict_vals(dict_input):
    for i in sorted(dict_input.keys()):
        yield i, dict_input[i]

print(gen_dict_vals(foods))