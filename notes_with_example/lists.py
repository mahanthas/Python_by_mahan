print("Enter the len of the list to be created :")
n = int(input())
list = []

for i in range(n):
    list.append(input())

print(list)
list1 = list.copy() 

list1.append("87")
print(list)
print(list1) # list1 both will be changed here 

list.reverse()
print(list) #prints the list in reverse order

list.sort()
print(list) #sorts list in ascending order

list.sort(reverse=True)
print(list) #sorts list in descending order

print(list.count('15')) #provides the count of value in 

list.insert(3,"mahan")
print(list) #adds the element in given index

list.pop()
print(list) #removes last element

list.remove('15')
print(list) #removes the first occurance of given  value