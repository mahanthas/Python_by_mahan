"""
Exercise 3: Replace all whitespace with -
Input: "regex is powerful" → Output: "regex-is-powerful"
"""

import re

text = input("provide the text : ")

pattern = r"\s"

print(re.sub(pattern,"-",text))