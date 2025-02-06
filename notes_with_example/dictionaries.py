dict = {
    "name": "mahan",
    "age": 45,
    "marks" : [90,86,78,98,99],
    "hobby" : "playing cricket",
}

print(type(dict))
print(dict)

print(dict["marks"])

dict["name"] = "Swamy" #here overwrite happens 
print(dict)

student = {
    "name":"Swamy",
    "marks":{
        "phy":98,
        "chem":97,
        "maths":95,
    },
}

print(student["marks"]["phy"])

#Dict Methods
print(dict.keys()) #returns all the keys

print(dict.values()) #returns all the values

print(dict.items()) #returns all the key,value pair in tuple form

print(dict.get("name")) # returns in normal print form 

print(dict.popitem()) #returns the last pair in tuple form

dict2 = {
    "hello":"world",
    "mane" : {
        "hello",
        "world",
    }
}

dict.update(dict2)
print(dict)

print(len(dict)) #returns the length of dict