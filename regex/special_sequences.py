import re
txt = "The ainb rain in spain _ 20"

pattern1 = r'\AThe' # checks whether txt starts with pattern
print(re.findall(pattern1,txt))

pattern2 = r'\bain' # checks the boundary word whether words in txt starts with ain or not 
print(re.findall(pattern2,txt))

pattern3 = r'ain\b' # checks the boundary words whether words in txt ends with ain 
print(re.findall(pattern3,txt))

pattern4 = r'\Bain' # checks the pattern is present in words starting with some characters 
print(re.findall(pattern4,txt)) # considers only rain and spain because only those have characters with prefix

pattern5 = r'ain\B' # checks the pattern is present in words ending with some characters
print(re.findall(pattern5,txt)) # considers only ainb as its ending with a character

pattern6 = r'\d' # checks the numerical values in string 
print(re.findall(pattern6, txt)) # returns 2, 0

pattern7 = r'\D' # checks the non-numerical values in string 
print(re.findall(pattern7, txt)) 

pattern8 = r'\s' # returns all the whitespaces
print(re.findall(pattern8, txt))

pattern9 = r'\S' # returns all non - whitespaces
print(re.findall(pattern9, txt))

pattern10 = r'\w' # returns all the characters (a-z, 0-9, _)
print(re.findall(pattern10, txt))

pattern11 = r'\W' # returns all the non characters other than (a-z, 0-9, _)
print(re.findall(pattern11, txt))

pattern12 = r'20\Z'
print(re.findall(pattern12, txt))