# swap two numbers 

def swap_nums_temp(a,b):
    temp = a
    a = b
    b = temp

    print(f"{a} and {b}")

def swap_num_wo_temp(a,b):
    a,b = b,a
    print(f"{a} and {b}")

swap_nums_temp(5,6)
swap_num_wo_temp(5,6)