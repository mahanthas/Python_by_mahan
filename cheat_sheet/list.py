list1 = [10,20,50,10,20,30]

#1 -> append()  -> adds new value or element to end of the list
list1.append(40)
print(list1) 

#2 -> extend()  -> adds one or more elements to the list 
list1.extend([50,70,80])  #-> argument should always be in list
print(list1)

#3 -> insert() -> adds an element at specified index
list1.insert(3,40)
print(list1)

#4 -> remove() -> removes first occurance of element
list1.remove(10)
print(list1)

#5 -> pop() -> removes and returns last element
print(list1.pop())

#6 -> index() -> returns first index of the element
print(list1.index(10))

#7 -> count() -> counts the occurances of element
print(list1.count(20))

#8 -> sort() -> sorts the list 
list1.sort()
print(list1) # only supports one datatype 

#9 -> reverse() -> reverse the list 
list1.reverse()
print(list1)
