from pathlib import Path

readfile = Path("C:\MAHAN\Python_by_mahan\README.md")

def read_file(readfile : Path):
    with open(readfile, 'r') as rf:
        string_list = []
        string_list.extend(rf.readlines())

        print(string_list)

def write_file(readfile : Path):
    with open(readfile, 'a') as wf:
        wf.write("Hello this is mahantha")

    

write_file(readfile)
read_file(readfile)
