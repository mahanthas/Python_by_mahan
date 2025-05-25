# write a program to reverse word in a sentence

str = "mahantha swamy is a legend"

def reverse_words(str):
    print(' '.join(str.split()[::-1]))

reverse_words(str)