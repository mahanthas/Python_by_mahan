# strings are immutable

s1 = "hello! My name is Mahan"
print(s1.capitalize()) # Only captializes the first word

print(s1.title()) # captializes every word in sentence

print(s1.upper()) # Captilizes every alphabets in the sentence

print(s1.lower()) # lowers every alphabet in sentence

print(s1.swapcase()) # swaps the upper to lower and vice-versa

s2 = "  My name mahan from  "
print(s2.strip()) # here it will remove spaces from beginning and at end , not in the middle 
print(s2.split()) # returns list of words from sentence
print(s2.lstrip()) # removes space to the left of sentence
print(s2.rstrip()) # removes spaces to the right of sentence

s3 = "Hello World "
print(s3.find("ello")) # returns the given word staring index 
print(s3.index('o')) # returns the index of the given char
print(s3.count('l')) # return total number of count of element
print(s3.replace("Hello" , "Hi")) # replaces and return new string doesnt modify the original string 

s4 = "Hello"
s5 = "12345"
s6 = "Hello123"
print(s4.isalpha()) # checks for the all the elements are alphabets or not
print(s5.isdigit()) # checks for all the elements are numbers or not
print(s6.isalnum()) # checks for the combinations of alpha and num 
