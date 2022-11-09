# NamedTuple Collection 
from collections import namedtuple

MonsterTuple = namedtuple("Monsters", "name age power")

example_tuple = MonsterTuple("Vampire", 35, "immortal")

print(example_tuple)