# Classes 
class Person:
    # Properties  -> attributes -> variables
    name = "shsihir"
    age = 27
    # Methods -> functions
    def getDetails(self):
        print(f"my name is {self.name} and age is {self.age}")
    @classmethod
    def abcd(cls):
        return cls.name
    @staticmethod
    def add(a,b):
        return a+b

print(Person.abcd())

p1 = Person()
p1.getDetails()
print(Person.add(1,2))