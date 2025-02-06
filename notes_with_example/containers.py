"""
Containers in python :
        *List
        *Tuple
        *Set
        *Dictionary
"""

#List : this is an sequenece container where we provide different data , which can be modified
list_var =[]
print("Provide no. of elements in list: ")
n = int(input())

for i in range(n):
    list_var.append(input())

print(list_var)

#Tuple : this is an sequence container where we provide simliar data , which cannot be modified
tuple_var = ()

print("enter the no. of elements: ")
m = int(input())

for i in range(m):
    tuple_var = tuple_var + (input(),)

print(tuple_var)
