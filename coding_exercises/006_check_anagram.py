"""
WAP to find the whether the two strings are anagrams or not
"""

str1 = "Mahan"
str2 = 'Ahanm'

def check_anagram(str1,str2):
    if sorted(str1.lower()) == sorted(str2.lower()):
        return True
    else:
        return False
    
print(check_anagram(str1,str2))
