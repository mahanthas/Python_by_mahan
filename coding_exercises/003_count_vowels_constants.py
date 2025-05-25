"""
WAP to count vowles and constants from the string 
"""

def count_vowel_constant(str):
    count_vowel = 0
    count_constant = 0
    vowels = ['a','e','i','o','u']
    for char in str:
        if char.lower() in vowels:
            count_vowel += 1
        elif char.lower() not in vowels:
            count_constant += 1
    print(f"the constants and vowels in {str} are {count_constant} and {count_vowel}")

count_vowel_constant('Mahan')
