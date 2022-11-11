# Lambda Function 

import collections

area = lambda b, h: 0.5 * b * h

print(area(5, 4))

# Creating Keys in Dictionaries

minus_one_dict = collections.defaultdict(lambda: -1)
point_zero_dict = collections.defaultdict(lambda: (0,0))
message_dict = collections.defaultdict(lambda: "No Message")

print(minus_one_dict)
print(point_zero_dict)
print(message_dict)