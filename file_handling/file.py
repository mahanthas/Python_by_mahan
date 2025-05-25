import csv

write_file_path = "file_handling\\file.txt"
write_csv_path = "file_handling\\file.csv"
data = [["Mahantha is legend", "Mahan is great"],
        ["12","30"],
        ["20000","50000"]]

def write_file(file_path):
    with open(file_path, 'w') as f:
        for st in data:
            f.write(f"{st}\n")

def read_file(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()
        for line in data:
            print(line,end='')

def write_csv(file_csv):
    with open(file_csv, 'w') as f:
        for st in data:
            writer = csv.writer(f,st)

def read_csv(file_csv):
    with open(file_csv, 'r') as f:
        reader = f.read()
        for rows in reader:
            print(rows)

write_file(write_file_path)
read_file(write_file_path)
write_csv(write_csv_path)
read_csv(write_csv_path)