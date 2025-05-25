import yaml

yml_file = "C:\\MAHAN\\Python_by_mahan\\yml_file_handling\\example.yml"

def read_yml():
    with open(yml_file, 'r') as file:
        data = yaml.safe_load(file)
        print(data['name'])
        print(data['age'])
        print(data['skills'])
        print(data['details'])

read_yml()