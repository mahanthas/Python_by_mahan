# sets are mutable and unordered , so original set can be altered 

s1 = {0,1,2,4,3,1,5,7,2,6}
print(s1)
s1.add(10) # appends the value at the end of set 
print(s1)
s1.remove(10) # removes the element 10 from the set 
print(s1)
#s1.remove(20) # raises error if element is not present in set
#print(s1)
s1.discard(20) # if element is present removes it , if not doesnt throw any error
print(s1)
s1.pop() # removes any random element from the set
print(s1)
s1.clear() # empties the set 
print(s1)

s2 = {1,2,3} 
s3 = {3,4,5}
print(s2 | s3) # returns the union of set2 and set3
print(s2&s3) # returns the intersection of set2 and set3
print(s2-s3) # returns the s2 but removes the intersection elements
print(s3-s2) # returns the s3 but removes the intersection elements
print(s2^s3) # returns s2 and s3 but removes the intersections elements
s2.update(s3) # updates s2 with s3 
print(s2)

s4 = {1,2} 
s5 = {1,2,3}
print(s4.issubset(s5)) 
print(s5.issuperset(s4))
print(s4.isdisjoint(s5)) # returns true if there are no common elements