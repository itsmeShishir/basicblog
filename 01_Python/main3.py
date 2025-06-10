# String Methods and concatination
# String -> A collection of set of characters 
# -> 3 ways to write string in Python '', "", """ """
# String Concatination (+) 
firstName = "Shishir"
lastName = "Bhandari"
fullName = firstName +" "+ lastName
print(fullName)
print(firstName, lastName)

num = 20
# print(firstName+num) # type error -> 
# modern apraoch
# f-> string f"{}"
print(f"my first name is {fullName} and num is {num}")
# Methods 
one = "hello world"
print(one.upper()) # wcapital]
print(one.lower()) # lower
print(one.title()) # 
one = "HELLO WORLD"
print(one.capitalize())

# check if the given method consists or not 
print(one.islower()) #False
print(one.isupper()) #True
print(one.isdecimal()) #False
one = "hello22"
print(one.isalnum()) #true

# indexing and funding and slicing in the sting 
two = "abcdefghij klmnopqr stukwxyz"
print(len(two))
three = two.rindex("r")
print(three)
#slicing
print(two[0])
print(two[3:18])
print(two[0:27:2])
# replace
print(two.replace("b", "0"))

#int and float 
four = 4 #int
five = 5.0 #decimal number

print(four + five)
print(type(four)) #  int
print(type(five)) # float

#complex number
six = 6+3j

print(six)
print(type(six)) # complex number

# how to ask input form the user
firstName = input("enter your firstname")
lastName = input("enter your last name ")
fullName = firstName +" "+ lastName
print(fullName)

# wap to ask 2 input frmo the user and multiply that number


