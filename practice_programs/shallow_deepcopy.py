import copy

a = [1,2,3,4]

shalow_copy = copy.copy(a)
shalow_copy.append(5)
shalow_copy.remove(1)
print(a)
print(shalow_copy)

b = [1,2,3,4]
deep_copy = copy.deepcopy(b)
deep_copy.append(5)
deep_copy.remove(1)
print(b)
print(deep_copy)