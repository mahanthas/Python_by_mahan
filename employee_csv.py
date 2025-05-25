import csv

employee_csv = "C:\\MAHAN\\Python_by_mahan\\file_handling\\files\\employees.csv"

def func_reader():
    with open(employee_csv,'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        age_index = header.index("age")
        name_index = header.index("name")
        for row in reader:
            if int(row[age_index]) > 30:
                print(row[name_index])

def func_dictreader():
    with open(employee_csv,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['age']) > 30:
                print(row['name'])

func_dictreader()