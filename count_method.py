# The Count method for string occurences

phrase = "Buffy is Buffy is Buffy"

res = phrase.count("Buffy", 0, -1)

print(res)

res_one = phrase.count("Buffy")

print(res_one)

# Replace Method

res_two = phrase.replace("Buffy", "who", 2)

print(res_two)