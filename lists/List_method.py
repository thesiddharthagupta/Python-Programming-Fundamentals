list = [2, 4, 9, "bob", 25.25, "alish"]

list.append(9)  #appending the value at last
print(list)

list.sort() #assending order 
print(list)

list.sort(reverse=True)     #reverse order
print(list)

list.reverse()   # reverse whole list without order
print(list)

list.insert(1,5)    #inserting (indx, value)
print(list)

list.remove(16)  #remove the value from list from 1st
print(list)

list.pop(3)     #remove the value from the spacific indx
print(list)