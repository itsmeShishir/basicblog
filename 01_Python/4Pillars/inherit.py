# class Parent:
#     def __init__(self, lastname, fatherName):
#         self.lastname = lastname
#         self.fatherName = fatherName

# class child(Parent):
#     def __init__(self, firstname, lastname, fatherName):
#         self.firstname = firstname
#         super().__init__(lastname, fatherName)

# chid1 = child("shishir", "bhandari", "someone")
# print(chid1.lastname)
# print(chid1.fatherName)
# print(chid1.firstname)

class Parent:
    age = 27
    def __init__(self, lastname, fatherName):
        self.lastname = lastname
        self.fatherName = fatherName

class child(Parent):
    pass

chid1 = child("shishir", "bhandari")
print(chid1.lastname)
print(chid1.fatherName)
print(chid1.age)

# wap to create a class name teacher with the properties of teachername, subject and 
# make another child class that print the details using inheritance like 
# teachername, subject, firstname, lastname and age


