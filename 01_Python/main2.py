# Data types in python
# always in camelCase
# String
abc = "hel\nlo's"
cde = 'hi'
tripleQuotation= """
    hello 
    world 
    by 
    shishir bhandari
"""
print(abc)
print(cde)
print(tripleQuotation)
print(type(abc))
# int
abc = 10
print(abc) #10
print(type(abc)) #int
# Float
abc = 10.50
print(abc) #10.50
print(type(abc)) #float
# Complex
abc = 1+3j
print(abc) #1+3j
print(type(abc)) #complex
# Boolean
abc = True
print(abc) # True
print(type(abc)) #boolean
#none
abc = None
print(abc) #None
print(type(abc)) #none

# List
list1 = [1,23,4,5,"shishir", 10.5, True]
print(list1)
print(type(list1))
# Tuple
tup = (1,23,4,5,6,7,4,2,3,1)
print(list1)
print(type(list1))
# Set
set = {1,23,4,5,6,7,4,2,3,1}
print(list1)
print(type(list1))
# Dictionary -> key and value pairs
dict = {
    "name": "shishir",
    "age": 27
}
print(dict)
print(type(dict))