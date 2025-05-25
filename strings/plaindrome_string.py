#write a program to check if string is a palindrome

str = "MALAYALAM"
str1 = "MAHANTHA"

def check_plaindrome(str):
    if(str[::-1] == str):
        print(f"provided string is palindrome")
    else:
        print(f"provided string is not palindrome")

check_plaindrome(str)
check_plaindrome(str1)