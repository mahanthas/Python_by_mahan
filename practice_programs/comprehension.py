"""
[expression for item in iterable if condition]
"""


a = [x*x for x in range(6) if x%2 == 0]
print(a)