dict={1:"you",2:"me",3:"he"}
dict.update({4:"she",5:"him"})
print(dict)
dict["5"]="her"
print(dict)
dict.pop(4)
print(dict)
dict.popitem()
print(dict)
del dict[2]
print(dict)
dict.clear()
print(dict)
