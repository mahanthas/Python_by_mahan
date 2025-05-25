# list are mutable , so the original list will be modified 

lst1 = [1,2,3]
lst1.append(4) # appens the provided element to end of list
print(lst1)
lst1.extend([5,6]) # concatenates the list with other list 
print(lst1)
lst1.insert(3,90) # inserts the element at provided index
print(lst1)
lst1.remove(90) # removes the specifeid element 
print(lst1)
lst1.pop() # removes the last elemnt from list
print(lst1)
lst1.clear() # empties the list
print(lst1)

lst2 = [3,4,7,5,2,1,5,9,8]
print(lst2.index(4)) # returns the index of provided element
print(lst2.count(5)) # returns the total count of the elements
print(lst2.count(1)) # returns 0 if the element is not present
lst2.sort() # sorts list into ascending order but doesnt remove duplicates
print(lst2)
lst2.sort(reverse=True) # sorts the list into descending order
print(lst2)
lst2.reverse() # reverses the list from begin to end into end to begin
print(lst2)

lst3 = [1,4,7,3]
lst4 = lst3.copy() # here its shallow copy
print(lst4)
lst5 = lst3[:] # normal copy
print(lst5)
print(lst5[1:6]) # slices the list from 1 to 5 , 6 index will be not considered 