# tuple are immutable and ordered , so the original form cant be changed 

t1 = (1,2,3,4,2)
print(t1.count(2)) # returns the number of occurances of provided element
print(t1.index(2)) # returns the index of first occurance

t2 = (1,2)
t3 = (3,4)
t4 = t2+t3 # concatenates both tuples into one tuples
print(t4)
t5 = t4[2:5] # slices the tuples and return new tuple from 2 to 4 indexes
print(t5)