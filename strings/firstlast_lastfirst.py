# write a program to convert "first_name last_name" to "Last_name, First_name" format.

str = "first_name last_name"

def firstlast_lastfirst(full_name):
    names = full_name.split()
    if len(names) == 2:
        first, last = names
        print(f"{last.title()}, {first.title()}")
    else:
        return "Invalid format – please provide 'First Last'"

firstlast_lastfirst(str)