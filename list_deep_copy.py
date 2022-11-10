# Making a Deep Copy of a List

myList = [1,2,3,4]
myList2 = [5,6,7,8]

newList = myList[:]
newList2 = list(myList2)

print(newList)
print(newList2)