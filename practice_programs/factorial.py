# print the factorial of provided number
# 0,1,2,3,4,5

def factorial(num):
    if num == 1:
        return num
    while(num > 1):
        return num * factorial(num - 1)

print(f"{factorial(10)}")