# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

string = input()
groups = groupby(string)
result = []
for key, group in groups:
    count = len(list(group))
    result.append(f"({count}, {key})")
print(' '.join(result))
