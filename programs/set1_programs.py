#convert integer to decimal 
import decimal
int = 100
print(decimal.Decimal(int))
print(type(decimal.Decimal(int)))

#converting an string of integers to decimal 
import decimal
str = '12345'
print(decimal.Decimal(str))
print(type(decimal.Decimal(str)))

#reversing the string using extended slicing technique
str = "Mahantha swamy"
print(str[::-1])

#counting vowels in a given word 
str1 = "mahantha swamy"
vowels = ['a','e','i','o','u']
vowel_count = 0 
for i in range(len(str1)):
    if (str[i] in vowels ):
        vowel_count += 1
print(vowel_count)

#fibonacci series
def fibonnaci(n):
    if n <= 1:
        return n
    return fibonnaci(n-1)+fibonnaci(n-2)
for i in range(6):
    print(f"{fibonnaci(i)}",end=" ")


#lambda function for addition 
sum = lambda a,b:a+b 
print(sum(5,6))

#Check if two strings are anagrams (in both strings all the characters are same)
str1 = "listen"
str2 = "slient"

str1.replace(" ","")
str2.replace(" ","")
print(sorted(str1) == sorted(str2))
print((str1 == str2))

#counting letters,digits,spaces in provided string
import re
str3 ="mahan born in 19 99"
digit_count = re.sub("[^0-9]", "",str3)
letter_count = re.sub("[^a-zA-Z]", "",str3)
space_count = re.findall("[ \s]",str3)

print(f"{len(letter_count)} , {len(digit_count)} , {len(space_count)}")

#creating instance member variables in python
class Test:
    def __init__(self):
        self.a =10
    def ifs(self):
        self.b = 14

t1 = Test()
t2 = Test()
t1.c = 45
print(t1.__dict__)
print(t2.__dict__)
