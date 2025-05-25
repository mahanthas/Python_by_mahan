# Writing in the files in python
import json, csv

text = "i am legend"

employees = ["MAHAN", "SWAMY", "SHIVU", "PRAVEEN"]

# file_path = "file_handling\\files\\file.txt"
file_path = "file_handling\\files\\file_lists.txt"
json_path = "file_handling\\files\\file_lists.json"
csv_path = "file_handling\\files\\file_lists.csv"

try :
    with open(file_path, "w") as file:
        for m in employees:
            file.write(f"{m}\n")
        print(f"txt file created at {file_path}")
except FileExistsError:
    print(f"the file already exists at {file_path}")
except FileNotFoundError:
    print(f"the file not found at {file_path}")
# with open(file_path, "a") as file:
#     file.write(f"\n {text}")

employee_dict = {
    "name": "mahan",
    "company": "bosch",
    "salary": 70000,
    "role": "engineer"
}
try :
    with open(json_path, "w") as file:
        json.dump(employee_dict, file, indent=5)
        print(f"json file created at {json_path}")
except FileExistsError:
    print(f"the file already exists at {json_path}")
except FileNotFoundError:
    print(f"the file not found at {json_path}")

employees_csv = [["name","role","salary"],
                 ["mahan","engineer",5000],
                 ["kevin","cook",2000],
                 ["raj","mechanic",10000]
]

try :
    with open(csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        for p in employees_csv:
            writer.writerow(p)
        print(f"csv file created at {csv_path}")
except FileExistsError:
    print(f"the file already exists at {csv_path}")
except FileNotFoundError:
    print(f"the file not found at {csv_path}")