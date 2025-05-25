import re

pattern1 = r"[bc]"
print(re.findall(pattern1,"aabbcc"))

pattern2 = r'\*[ab]'  
print(re.findall(pattern2,"**animal"))

pattern3 = r'.'
print(re.findall(pattern3,"hello"))

pattern4 = r'^H'
print(re.findall(pattern4,"Hello world"))

pattern5 = r'world$'
print(re.findall(pattern5,"Hello world"))

pattern6 = r'he*o'
print(re.findall(pattern6,"heo"))

pattern7 = r'hel+o'
print(re.findall(pattern7,"hello"))