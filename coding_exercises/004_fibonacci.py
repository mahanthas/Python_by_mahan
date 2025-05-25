"""
WAP for fibonacci series of given number and fibonacci sum of it 
"""

def fibonacci_series(i):
    if i <= 1:
        return i
    else:
        return fibonacci_series(i-1) + fibonacci_series(i-2)

#print(fibonacci_series(5))
for i in range(6):
    print(fibonacci_series(i))