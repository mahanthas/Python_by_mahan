# generators 

def gen():
    for i in range(5):
        yield i
    
for i in gen():
    print(f"{i}")
