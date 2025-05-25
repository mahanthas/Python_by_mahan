import csv

csv_path = "file_handling\\files\\email-password-recovery-code.csv"

with open(csv_path, "r") as csv_file:
    content = csv.DictReader(csv_file, delimiter=";")
    for row in content:
        # print(row)
        if "Login email" in row:
            if "mary" in (row["Login email"]):
                print(row["Login email"])