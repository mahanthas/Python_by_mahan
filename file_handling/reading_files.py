# reading files using python (.txt, json, csv)
import json, csv
file_path = "file_handling\\files\\file.txt"
file_lists_path = "file_handling\\files\\file_lists.txt"
json_path = "file_handling\\files\\file_lists.json"
csv_path = "file_handling\\files\\file_lists.csv"

def read_txt(path):
    with open(path,"r") as txt:
        content = txt.read()
    print(content)

def read_csv(path):
    with open(path, "r") as csv_file:
        content = csv.reader(csv_file)
        for line in content:
            print(line[1])

read_txt(file_path)
read_csv(csv_path)