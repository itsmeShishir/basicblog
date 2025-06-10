# set and dict 
set1 = {1,2,3,4,5}
print(set1)

#type
print(type(set1))

set2 = {1,2,3,4,5,1,2,3,4,5,0}
print(set2)

# Set Methods in python -> add, remove, pop, clear, discard, union, 
# intersection, difference

set1.add(9)
print(set1)

#remove 
set1.remove(9)
print(set1)

#pop
set1.pop()
print(set1)

# clear
set1.clear()
print(set1)

#union
set3 = {1,2,3,4,5,6,7,8,9}
print(set3.union(set2))

#intersection
set3 = {2,3,4,5,6,7,8,9}
print(set3.intersection(set2))

#difference
set3 = {1,2,3,4,5,6,7,8,9}
print(set3.difference(set2))

#copy
set3 = {1,2,3,4,5,6,7,8,9}
set4 = set3.copy()
print(set4)

#discard
set3 = {1,2,3,4,5,6,7,8,9}
set3.discard(4)
print(set3)

#DICT
dict1 = {
    "name": "hari", 
    "age": 23, 
    "gender": "Male", 
    "isAbove18": True, 
    1: 27
}

print(dict1)
print(type(dict1))
print(dict1["name"])
print(dict1[1])
print(dict1.keys())
print(dict1.values())
#methods in dict -> clear, copy, fromkeys, get, items, keys, pop, popitem, 
#update, values

dict2 = {
    2:44
}
print(dict2)

dict2 = dict1.copy()
print(dict2)

#clear dict1
dict1.clear()
print(dict1)

# fromKeys
dict3 = dict2.fromkeys([1,2,3,4,"age"])
print(dict3)

#get
print(dict2.get("age"))

#keys
print(dict2.keys())

#pop
dict2.pop("age")
print(dict2)

#popitem
dict2.popitem()
print(dict2)


# update
dict2.update(dict3)
print(dict2)

#Loops in python -> for, while, break, continue, pass

# for loops 
for i in range(1,101):
    print(i)

set1 = {1,2,3,4,5,6,7,8}
for i in set1:
    print(i)

for key, value in dict2.items():
    print(key,"=",  value)


list1 = [1,2,3,4,5,6,7,8, 9, 10]
tuple1 = (1,2,3,4,5,6,7,8, 9, 10)
          
