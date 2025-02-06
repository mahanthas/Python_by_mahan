set_collection = {1,2,2,4,5,3,6,6,7,2,6}

print(set_collection)

print(type(set_collection))

null_set = set() #syntax to create empty set

print(type(null_set))

def add_ele_set():
    print("enter the number of elements to be added into set: ")
    n = int(input())
    set_elements = set()
    for i in range(n):
        set_elements.add(input())

    print(set_elements)
    print(len(set_elements))

#add_ele_set()

set1 = {1,2,2,4,5,6}
set2 = {2,6,3,8,9}

print(set1.union(set2))

print(set1.intersection(set2))