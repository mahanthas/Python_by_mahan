word = "MAHANTHA SWAMY"
#       01234567891234

# string[start : stop : step]

length = len(word)
print(f"the lenght of string word is : {length}")

print(word[0:length]) # provide the full string

print(word[0:6]) # provides the string till 5th index

print(word[4:]) # provides the string from index 4 to end of index

print(word[:10]) # provides the string till index 9

print(word[::-1]) # provides the reverse of string

print(word[-7::-1]) # here it doesnt consider the -7 and -1 index 
#here it starts from 7 and goes backward till beginning 

print(word[3:9:1]) # ANTHA 

print(word[3:9:2]) # ATA 

print(word[8:][::-1])