str1 = "Mahantha"
str2 = " Swamy"

str3 = str1+str2
print(str3) #concatenate string

length = len(str3)
print(length) #length of the string str3

#slicing
print(str3[0]) 

print(str3[0:5])

print(str3[0:]) #is same as str[0:len(str3)]

print(str3[:5]) #is same as str[0:5]

print(str3[-8:-1]) #print the string with negative index

print(str3[-(length) : -1])

print(str3.replace("Swamy","Stark"))

print(str3.find('h'))

print(str3.casefold()) #make case according to highest one as lower case is highest in str

print(str3.capitalize()) #captalize only the 1st character

print(str3.count('a')) #counts the character in str

print(str3.swapcase()) #swaps the lower to higher vice -versa

print(str3.lower()) #lowers all the chars

print(str3.upper()) #uppers all the chars 
