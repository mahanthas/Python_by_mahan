"""
Questions: 
        1. Create a new file “practice.txt” using python. Add the following data in it:
                    Hi everyone
                    we are learning File I/O
                    using Java.
                    I like programming in Java.
        2. WAF that replace all occurrences of “java” with “python” in above file.
        3. Search if the word “learning” exists in the file or not.
        4. WAF to find in which line of the file does the word “learning”occur first.
            Print -1 if word not found.
        5. From a file containing numbers separated by comma, print the count of even numbers.
"""
#Question 1
# with open("practice.txt","w+") as pt:
#     pt.write("Hi everyone\n\
#     we are learning File I/O\n\
#     using Java.\n\
#     I like programming in Java.")
#     data = pt.read()
#     print(data)

#Question 2
# def replace_words(old,new):
#     with open("practice.txt","r") as rw:
#         data = rw.read()
#         replaced_data = data.replace(old,new)
#         print(replaced_data)

# replace_words("Java","Python")

#Question 3
# def find_match(word):
#     with open("practice.txt","r") as fm:
#         data = fm.read()
#         if(data.find(word) != -1):
#             print("Match Found") #if match is present it throw some values 
#         else:
#             print("Match NOT Found") #if match is not found it throw -1

# find_match("learning")

#Question 4
# def match_found_return(word):
#     with open("practice.txt","r") as mfr:
#         data = mfr.readlines()
#         length = len(data)
#         for i in range(length):
#             if(word in data[i]):
#                 print(f"{word} present in line : {i}")
#                 found = True
#         if not found:
#             print("-1")
# match_found_return("Java")

#Question 5
def count_even_numbers():
    count = 0
    with open("numbers.txt","r") as cen:
        data = cen.read()
        nums = data.split(",")
        print(nums)
        for val in nums:
            if(int(val) %2 == 0):
                count+= 1
    print(count)
count_even_numbers()