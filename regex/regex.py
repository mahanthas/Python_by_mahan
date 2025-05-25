"""
regex ==> mean regular expression , which search for alpha, digits and special charaters

\d ==> refers to digits
\D ==> refers to others apart from digits

[A-Z] => check for capital letters 
[a-z] => check for small letters
[0-9] => check for digits/numbers 

usage is done by importing re 

example:  email verfication 
          verfiy whether the email is in same pattern example@gmail.com

"""

import re

pattern = r"[A-za-z0-9]+@[A-Za-z]+\.(com|net|org)"

email = input("enter the email id :")

if (re.search(pattern,email)):
    print(f"{email} is an valid email")
else:
    print(f"{email} is an invalid email")

