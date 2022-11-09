# Working with Casing in strings

captcha = "aKE32DNSD"

user_input = "AKe32dnsd"

print(captcha.casefold() == user_input.casefold())

jumbled_case = "The Brown Quick Fox Jumped over the Lazy Dog"

print(jumbled_case.swapcase())