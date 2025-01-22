"""
Questions: WAF--> write a function
        1. WAF to print the length of a list. ( list is the parameter)
        2. WAF to print the elements of a list in a single line. ( list is the parameter)
        3. WAF to find the factorial of n. (n is the parameter) (without recursion)
        4. WAF to convert USD to INR.
        5. Write a recursive function to calculate the sum of first n natural numbers.
        6. Write a recursive function to print all elements in a list. Hint : use list & index as parameters.
"""


#Question 1:
list = [10,20,80,90,10,20]

def length(list):
    print(len(list))

length(list)

#Question 2:
list1 = list.copy()

def print_elements(list):
    for item in list:
        print(item,end=" ")

print_elements(list1)

#Question 3
def factorial(n):
    if(n==0 or n==1):
        fact = 1
    fact = 1 
    for i in range(2,n+1):
        fact *= i
    print(fact)
factorial(9)

#Question4
def convert_USD_to_INR(n):
    usd_val = n
    inr_val = n * 85
    print(usd_val, "USD is equal to",inr_val,"INR")

convert_USD_to_INR(10)

#Question 5
def print_sum_natural(n):
    if(n < 0):
        return 0
    return print_sum_natural(n-1) + n

print(print_sum_natural(10))

#Question 6
marks = [10,20,30,40,50]
i = len(marks)
def print_elements_in_list(list,n=0):
    if(n == i):
        return
    print(marks[n])
    return print_elements_in_list(list,n+1)

print_elements_in_list(marks)