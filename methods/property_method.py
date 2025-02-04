 
def factorial(num):
    if(num==0 or num==1):
        fact = 1
        return fact
    fact = num * factorial(num -1)
    return fact
    
fact_value = factorial(5)
print(fact_value)