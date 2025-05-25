"""
Reverse the sentence and check for the palindrome
example: "A man, a plan, a canal: Panama"
"""
import re
sentence = "A man, a plan, a canal: Panama"

def is_palindrome(sentence):
    cleaned = re.sub("[^a-zA-Z0-9]","",sentence).lower()
    print(cleaned)
    if (cleaned == cleaned[::-1]):
        return True
    return False

#print(is_palindrome(sentence))

"""
Find the single number in a list where every other number appears twice.
"""
num_list = [10,20,30,20,30,40,50,50,40]

def get_single_number(num):
    result_sum = sum(num)
    result_set = sum(set(num))
    print(f"result_sum : {result_sum}, result_set: {result_set} ")
    return 2 * sum(set(num)) - sum(num)
        
print(get_single_number(num_list))