"""
WAP to find the maximum and minimum number from the list 
"""

def max_num(lst1):
    max = lst1[0]
    for i in range(len(lst1)):
        if max < lst1[i]:
            max = lst1[i]
    return max

def min_num(lst1):
    min = lst1[0]
    for i in range(len(lst1)):
        if min > lst1[i]:
            min = lst1[i]
    return min

lst1 = [10,50,4,60,80,2,5]
print(max_num(lst1))
print(min_num(lst1))