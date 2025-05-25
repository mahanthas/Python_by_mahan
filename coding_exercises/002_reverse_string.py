"""
WAP to reverse the string using slicing and without using slicing
"""

def reverse_builtin(str):
    return str[::-1]

def reverse_without_builtin(str):
    str1 = ''
    print(len(str))
    for i in range(len(str)-1,-1,-1):
        str1 += str[i] 
    return str1

string1 = "Mahan"
print(reverse_builtin(string1))
print(reverse_without_builtin(string1))