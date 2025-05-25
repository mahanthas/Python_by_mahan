# dicts are mutable and unordered , so original form can be changed

dict1 = {'a':1,'b':2, 'c':3}
print(dict1)
print(dict1.keys()) # returns all the keys present in dictionary in form of list
print(dict1.values()) # returns all the values present in dictionary in form of list
print(dict1.items()) # returns all the key values pairs in list of tuples

for key , values in dict1.items():
    print(key,values)  # returns the key values in normal way

dict2 = {'name':'Mahan', 'age':25}
print(dict2['name']) # returns the value of provided key
#print(dict2['mahan']) # raises keyerror if you want to access values in this way
print(dict2.get('age')) # another way to get the value of provided key
dict2['job'] = 'engineer' # add the key value into dictionary
dict2['place'] = '' # we can add only key to dict without value
print(dict2)
dict2['name'] = 'Alice' # here name value will be replaced with Alice
print(dict2)
dict2.pop("place") # should always provide the key , if not raises typeerror
print(dict2)
dict2.clear() # empties the whole dictionary
print(dict2)

d3 = {'a':1} 
d4 = {'b': 2}
d3.update(d4) # concatenates the d3 and d4 into d3
print(d3)
d5 = d3.copy()
print(d5)