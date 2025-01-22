"""
Questions:
    1.Store following word meanings in a python dictionary :
        table : “a piece of furniture”, “list of facts & figures”
        cat : “a small animal”

    2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. 
        How many classrooms are needed by all students.

        ”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”

    3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
        an empty dictionary & add one by one. Use subject name as key & marks as value.

    4. Figure out a way to store 9 & 9.0 as separate values in the set.
        (You can take help of built-in data types)
"""

def question1():
    dict = {}
    dict["cat"] = "a small animal"
    dict["table"] = ["a piece of furniture","list of facts & figures"]

    print(dict)

question1()

def question2():
    classroom = {"python","java","C++","python","javascript","java","python","java","C++","C"}

    print(type(classroom))
    print(classroom)
    print("number of classroom need for all subject is :",len(classroom))

question2()

def question3():
    subjects_dict = {}
    print("enter the number of subjects : ")
    n = int(input())
    for i in range(n):
        subject = input()
        marks = input()
        subjects_dict[subject] = marks

    print(subjects_dict)
    print(subjects_dict.keys())
    print(subjects_dict.values())

question3()

def question4():
    number_set = set()
    number_set.add('9')
    number_set.add('9.0')

    print(number_set)

question4()