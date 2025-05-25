# tuple = () ordered and unchangeable. Duplicates OK. Faster

tup1 = (2,4,5,7,9,9,4,0,4)

print(tup1)
# print(dir(tup1))
# print(help(tup1))

print(tup1.count(9))
print(tup1.index(4))

"""
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
"""