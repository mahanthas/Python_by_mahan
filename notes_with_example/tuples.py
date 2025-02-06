print("enter the size of the tuple:")
n = int(input())
tup = ()
list = []

for i in range(n):
    list.append(input())

tup = tuple(list)
print(list)
print(tup)

#tuple slicing
print(tup[0:])

print(tup[:len(tup)])

print(tup[2:5])

#tuple methods
print(tup.count('15'))

print(tup.index('15'))
