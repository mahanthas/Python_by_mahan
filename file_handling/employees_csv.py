import csv 
import numpy as np 
from collections import defaultdict

csv_path = "file_handling\\files\\employees.csv"

# Task1 : Open and print each row from the CSV.

def task1(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

task1(csv_path)

# Task2 : Extract and print just the names of all employees.

def task2(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        index = header.index("name")
        for row in reader:
            print(row[index])

task2(csv_path)

# Task3 : Print all employees whose department is Engineering. 

def task3(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        index = header.index("name")
        print(f"Employees with department : engineering are :")
        for row in reader:
            if "Engineering" in row:
                print(f"{row[index]}")

task3(csv_path)

# Task4 : Print the name and salary of employees earning more than 70k.

def task4(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        sal_index = header.index("salary")
        name_index = header.index("name")
        for row in reader:
            if int(row[sal_index]) > 70000:
                print(f"employee {row[name_index]} is earning {row[sal_index]}")

task4(csv_path)

# Task5: Calculate and print the average salary of all employees.

def task5(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        sal_index = header.index("salary")
        avg_sal = []
        for row in reader:
            avg_sal.append(int(row[sal_index]))
        print(f"average salary is : {np.mean(avg_sal):.3f}")

task5(csv_path)

#Task6: Print names of employees who are under 30 years old.

def task6(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        age_index = header.index("age")
        name_index = header.index("name")
        print(f"the employees under age 30 : ")
        for row in reader:
            if int(row[age_index]) < 30:
                print(f"{row[name_index]}")

task6(csv_path)

# Task7: Group employees by department and print the total number in each.

def task7(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        dept_id = header.index("department")
        d = defaultdict(int)
        for row in reader:
            dept = row[dept_id]
            d[dept] += 1
        for dep, count in d.items():
            print(f"the {dep} department has {count} employees")

task7(csv_path)