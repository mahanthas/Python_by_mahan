# sets = {} unordered and immutable, but add/remove ok. NO duplicates allowed

set1 = {2,3,7,8,7,9,2,9,0}
set2 = {4,5,6,13,2,9,7}

print(set1)
# print(dir(set1))
# print(help(set1))

set1.add(12)
print(set1)
print(set1.difference(set2))
#print(set1.difference_update(set2)) # it will remove the numbers from ste1 common in set2
print(set1.intersection(set2))
print(set1.union(set2))



"""
add(self, object, /)
 |      Add an element to a set.
 |
 |      This has no effect if the element is already present.
 |
 |  clear(self, /)
 |      Remove all elements from this set.
 |
 |  copy(self, /)
 |      Return a shallow copy of a set.
 |
 |  difference(self, /, *others)
 |      Return a new set with elements in the set that are not in the others.
 |
 |  difference_update(self, /, *others)
 |      Update the set, removing elements found in others.
 |
 |  discard(self, object, /)
 |      Remove an element from a set if it is a member.
 |
 |      Unlike set.remove(), the discard() method does not raise
 |      an exception when an element is missing from the set.
 |
 |  intersection(self, /, *others)
 |      Return a new set with elements common to the set and all others.     
 |
 |  intersection_update(self, /, *others)
 |      Update the set, keeping only elements found in it and all others.    
 |
 |  isdisjoint(self, other, /)
 |      Return True if two sets have a null intersection.
 |
 |  issubset(self, other, /)
 |      Report whether another set contains this set.
 |
 |  issuperset(self, other, /)
 |      Report whether this set contains another set.
 |
 |  pop(self, /)
 |      Remove and return an arbitrary set element.
 |
 |      Raises KeyError if the set is empty.
 |
 |  remove(self, object, /)
 |      Remove an element from a set; it must be a member.
 |
 |      If the element is not a member, raise a KeyError.
 |
 |  symmetric_difference(self, other, /)
 |      Return a new set with elements in either the set or other but not both.
 |
 |  symmetric_difference_update(self, other, /)
 |      Update the set, keeping only elements found in either set, but not in both.
 |
 |  union(self, /, *others)
 |      Return a new set with elements from the set and all others.
 |
 |  update(self, /, *others)
 |      Update the set, adding elements from all others.
"""