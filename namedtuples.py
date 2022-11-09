# NamedTuple Collection 
from collections import namedtuple

MonsterTuple = namedtuple("Monsters", "name age power")

MonsterTuple = ("Vampire", 35, "immortal")

print(MonsterTuple)