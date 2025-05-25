def add1(*args):
    return sum(args)

print(add1(1,2,3))
print(add1(1,2,3,4,5))
print(add1(3,6,8,3))

def userdetails(**kwargs):
    print(kwargs)

userdetails(Name='mahan',age=25,id=2024,pincode=583132)
