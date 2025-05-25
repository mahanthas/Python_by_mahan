# write a program to count the vowel s in string
str = "mahAntha swAmy"

def vowel_count(str):
    count = 0
    for char in str:
        if(char.lower() in 'aeiou'):
            count += 1
    print(f"the vowel count in str {str} is {count}")

def vowel_count_lambda(str):
    return sum(1 for char in str if char.lower() in 'aeiou')

count_lambda = vowel_count_lambda(str)
print(f"the vowel count in str {str} is {count_lambda}")
vowel_count(str)