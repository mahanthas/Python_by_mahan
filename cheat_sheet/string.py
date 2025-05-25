str = " MAHANTHA SWAMY "

#1 -> .strip()  --> removes whitespaces at start and end
print(f"strip --> {str.strip()}") 

#2-> .split()  --> splits string into list with provide string 
print(f"split --> {str.split(" ")}")

#3 -> .join()  ->joins elememnts of an iterable
str1 = "is cool"
print(str.join(["one","two","three"]))

#4 -> replace() ->replace letter with other character
print(str.replace('A','a'))

#5 -> upper()  -> capitalizes all the letters in string
print(str.upper())

#6 -> lower() -> makes entire string into lower case
print(str.lower())

#7 -> startswith() -> checks whether strings starts with provided string or character
print(str.startswith(' M'))

#8 -> endswith() -> checks whether string endswith rpovided string or character
print(str.endswith('Y '))

#9 -> find()  -> checks for the character or string in the provided string
print(str.find('A')) #-> returns the first index of the character

#10 -> isdigit() -> checks if all the character in string are digit or not
print(str.isdigit())

#11 -> isalpha() -> checks if all the character in string are alphabet or not
print(str.isalpha())