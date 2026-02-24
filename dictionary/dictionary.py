dict = {
    "name" : "Siddharth",
    "key"  : "value",
    "math" :  95
}

print(dict.items())
print(dict.get("key"))  # to get the value

dict.update({"city" : "bangloure"})  #update
print(dict)

new_dict = {"Science" : "100", "age" : 17}  #update the dict
dict.update(new_dict)  #for the new dict

print(dict)
