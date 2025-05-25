dict1 = {"name": ["mahan","dhanush","punith"],"age":[20,50,60],"fruits":["apple","mango","banana"]}

print(dict1)

#1 -> get() -> retrives value for the provided key 
print(dict1.get("age"))

#2 -> keys() -> returns dictionary keys
print(dict1.keys())

#3 -> values() -> retursn dictionary values
print(dict1.values())

#4 -> items() -> returns key-value pairs
print(dict1.items())

#5 -> update() -> updates dictionary 
dict1.update({"marks":[90,80,98]}) # update should be done with {}
print(dict1.items())

#6 -> pop() -> removes key and returns value
print(dict1.pop("marks"))

#7 -> popitem() -> removes last inserted key-value pair
print(dict1.popitem())

#8 -> clear() -> clears the dictionary 
dict1.clear()
print(dict1)