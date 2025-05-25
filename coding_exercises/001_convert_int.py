"""
WAP to convert integer into decimal, hexadecimal, octal, binary
"""
import decimal
num1 = 1234
print(f"Decimal of {num1} is {decimal.Decimal(num1)}")
print(hex(num1)[2:])
print(oct(num1)[2:])
print(bin(num1)[2:])