# Remove all special characters from a string

str = "mah@ant!ha sw%a&my"

def remove_special_char(str):
    result = ''
    for char in str:
        if char.isalnum() or char.isspace():
            result += char
    print(result)

remove_special_char(str)