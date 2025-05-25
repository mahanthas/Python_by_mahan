import os

file1 = "C:\\MAHAN\\Python_by_mahan\\file1.txt"
file2 = "C:\\MAHAN\\Python_by_mahan\\file2.txt"

if os.path.exists(file1):
    with open(file1,'r') as file1:
        file1_data = file1.readlines()

if os.path.exists(file2):
    with open(file2, 'r') as file2:
        file2_data = file2.readlines()

with open("file3.txt", 'w') as file3:
    for line in file1_data:
        for line in file2_data:
            file3.write(line)
