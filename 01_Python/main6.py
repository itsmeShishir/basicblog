list1 = [1,2,3,4,5,"7"]
# list1 -> objects -> [1,2,3,4,5,"7"]
list2 = [0,1,2,3,4,5, 0, 0]


list3 = list2+list1
print(list3)
print(list1[0:3])
print(list1[-1])
list1[0] = "shishir"
print(list1)

# methods in list -> append, insert, remove, pop , clear, count, index, extend, copy, sort, reverse
print(type(list1)) #list
list1.append("bhandari") # append always add the element at the end of the list
print(list1)


#insert
list1.insert(0, "hi") # -> in the given index it will provide the value
print(list1)

# remove
list1.remove("hi") # removes the given value
print(list1)

# pop -> remove last element
list1.pop()
print(list1)

#clear -> create or remove all the list from the elements
list1.clear()
print(list1)

#cout -> count the number of given value in the list
print(list2.count(0))
print(list2.count(1))


# index -> return the index of the given value
print(list2.index(4))

#copy -> list1
list4 = list2.copy()
print(list4)

#extends -> list2
list4.extend(list1)
print(list4)

#sort -> list2
list2.sort()
print(list2)

#reverse -> list2
list2.reverse()
print(list2)

list5 = [1,2,3,4,5,6]

if 2 in list5:
    print("yes")
else:
    print("not")

# Tuple in python
tup1 = (1,2,3,4,5)
print(tup1)
print(type(tup1))

print(tup1[0])

# tup1[0] = 10
# print(tup1)

# methods in tuple -> count index
print(tup1.count(1))
print(tup1.index(3))

# type conversion in python tuple -> list  and again list -> tuple
list6 = list(tup1)
print(list6)
list6.append("shishir")
print(list6)
tup2 = tuple(list6)
print(tup2)




