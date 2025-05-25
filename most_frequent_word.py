import re 
from collections import Counter

def most_frequent_word(string):
    input_string = string.lower()

    pattern = r"\b\w+\b"

    words = re.findall(pattern, input_string)
    word_counts = Counter(words)
    common_word, count = word_counts.most_common(1)[0]

    print(f"the most common word in provided string is {common_word} and count is {count}")

most_frequent_word("hello sir , hello!, how are you sir , hello#")