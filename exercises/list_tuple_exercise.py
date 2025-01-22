""" 
    Questions:
    1. Ask the user to enter the number of there favorite movies and stores names in list
    2. check it list contains a palindrome elements or not 
    3. WAP to count the number of students with the "A" grade in the following tuple
        ["C","D","A","A","B","B","A"]
"""

def movies():
    print("Enter the number of favorite Movies")
    n = int(input())
    movies_list = []
    for i in range(n):
        movies_list.append(input())
    print(movies_list)

def check_list_palindrome():
    list = [1,2,3,3,1]
    list1 = list.copy()

    list1.reverse()
    if(list == list1):
        print("Provide List is a palindrome list")
        print(list)
        print(list1)
    else:
        print("Provided List is not a palindrome list")
        print(list)
        print(list1)

def count_students_with_grade(grade):
    list = ["C","D","A","A","B","B","A"]
    tup = tuple(list)
    print(f"students with Grade {grade} in provided tuple is : {tup.count(grade)}")


def sort_list():
    list = ["C","D","A","A","B","B","A"]
    list.sort()
    print(list)
    list.sort(reverse=True)
    print(list)

#uncomment below functions to execute
#movies()
#check_list_palindrome()
#count_students_with_grade("B")
sort_list()