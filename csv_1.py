import csv 
from pathlib import Path

data = [
        ["name", "age", "place"],
        ["mahan",25,"banglore"],
        ["ajai",27,"chennai"],
]

csvfile = Path("C:\\MAHAN\\Python_by_mahan\\perfile.csv")

def write_csv(file,data):
    with open(file, 'w') as cf:
        writer = csv.writer(cf)
        writer.writerows(data)

def read_csv(file):
    with open(file, 'r') as cf:
        reader = csv.reader(cf)
        header = next(reader)
        if "age" in header:
         for row in reader:
            print(row)

write_csv(csvfile, data)

read_csv(csvfile)