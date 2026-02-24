student = {"name": "Siddhartha", "age": 20, "marks": 90}

print(student.get("name"))  #safely get value

print(student.keys())   #get all keys

print(student.values()) #get all values

print(student.items())  #get key-value pairs


student.update({"age": 18}) #add/update
student.update({"grade": "A"})
print(student)

new_student = student.copy()
print(new_student)      #to create new student


student.pop("marks")      #remove specific key
print(student)

print(student.popitem())   #remove last item automatically

print(student.clear())  #to clear the whole  dict



