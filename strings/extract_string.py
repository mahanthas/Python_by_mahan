# write a program to extract domain name form an email 
# test@example.com --> 'example.com'

str = "test@example.com"

def extract_domain(str):
    print(str.split('@')[-1])

extract_domain(str)
extract_domain("mahan@yahhoo.com")