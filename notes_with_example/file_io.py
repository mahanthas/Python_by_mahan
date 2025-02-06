from pathlib import Path
import os

file_name = Path.joinpath(Path(__file__).resolve().parent,"python_notes","python.txt")
print(file_name)

f = open(file_name,"r")
# data = f.read()
# print(data)
# print(type(data))

line2 = f.readline() # will print the line
print(line2)
line1 = f.readlines() # will store the lines in list
print(line1)
f.close()

new_file_name = Path.joinpath(Path(__file__).resolve().parent,"python_notes","python_new.txt")
print(new_file_name)
nd = open(new_file_name,"x")
new_data = nd.write("Hello Mahantha\n \
        How are you ? \n \
        Hope you are doing well\n ")
print(new_data)

os.remove(new_file_name)