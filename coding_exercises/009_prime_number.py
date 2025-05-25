"""
WAP to check prime number and create list of prime numbers

4
2 -> 4%2
3 -> 3%3
4 -> 4%4

5
2-> 5%2
3-> 5%3
4-> 5%4


"""

def is_prime(num):
    for i in range(2,num):
        if num%i == 0 :
            return False
    return True

print(is_prime(4))

def prime_num_list(num):
    lst = []
    for i in range(2,num+1):
        if is_prime(i):
            lst.append(i)
    return lst

print(prime_num_list(12))