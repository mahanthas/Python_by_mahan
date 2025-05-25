""" 
WAP to check the palindrome of string and number as input
"""

def palindrome_string(str1):
    str2 = str1[::-1]
    if str2.lower() == str1.lower():
        print(f"{str1} is a palindrome")
    else:
        print(f"{str1} is not a palindrome")

palindrome_string("Maham")

def palindrome_number(n):
    temp = n
    num = 0
    while(temp>0):
        divisor = temp%10
        num = num * 10 + divisor 
        temp //= 10
    return num
print(palindrome_number(1221))