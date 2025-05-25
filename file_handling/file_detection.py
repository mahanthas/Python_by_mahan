# python file detection

import os

file_path = "file_handling\\files\\test.txt"

if os.path.exists(file_path):
    print(f"the location {file_path} exists")
else:
    print(f"{file_path} doesnt exists")

