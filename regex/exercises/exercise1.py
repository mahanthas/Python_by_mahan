"""
Exercise 1: Match all phone numbers in a text
Input: "Call me at 123-456-7890 or 987-654-3210" → Output: ['123-456-7890', '987-654-3210']
"""

import re

text = input("provide the phone number : ")

pattern = r"\d{3}-\d{3}-\d{4}"

matches = re.findall(pattern, text)

print(matches)