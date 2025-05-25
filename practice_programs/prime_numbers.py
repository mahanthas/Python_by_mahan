# print all the numbers provided till number given 

def primenumber(num):
    prime_numbers = []
    for i in range(2,num):
        if i > 1:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                prime_numbers.append(i)

    print(f"{prime_numbers}")

primenumber(10)